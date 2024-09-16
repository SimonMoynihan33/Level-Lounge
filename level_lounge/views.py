from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "level_lounge/index.html"
    paginate_by = 6


def update_info(request):
    pass


def post_detail(request, slug):
    """
    View to display a single post and its comments, allowing users to add new comments.
    Handles both top-level comments and replies to other comments.
    
    - Retrieves the post using the slug.
    - Displays top-level comments (those with no parent).
    - Processes form submissions to add new comments.
    - Handles replies by attaching a 'parent' comment when applicable.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # Fetch only top-level comments (those without a parent)
    all_comments = post.comments.filter(parent__isnull=True).order_by("-created_at")
    
    # Paginate comments - Show 3 comments per page
    top_level_comments = post.comments.filter(parent__isnull=True).order_by("-created_at")
    paginator = Paginator(top_level_comments, 3)  # 3 comments per page
    page_number = request.GET.get('page')
    comments = paginator.get_page(page_number)  # Get the comments for that page
    comment_count = post.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user  # Assign the logged-in user as the comment author
            comment.post = post  # Attach the comment to the post
            comment.save()  # Save the comment to the database
            messages.success(request, 'Comment successfully posted.')
            return redirect('post_detail', slug=post.slug)  # Redirect to avoid duplicate form submission on refresh

    else:
        comment_form = CommentForm()

    return render(
        request,
        "level_lounge/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "top_level_comments": top_level_comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign the logged-in user as the post's author
            post.save()  # Save the post
            return redirect('post_detail', slug=post.slug)  # Redirect to the post detail page
    else:
        form = PostForm()

    return render(request, 'level_lounge/create_post.html', {'form': form})


@login_required
def edit_post(request, id):
    """
    Function to allow a user to edit their own posts
    """
    post = get_object_or_404(Post, id=id, author=request.user)  # Ensure only the author can edit the post
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'level_lounge/edit_post.html', {'form': form})


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    From CI walkthrough
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))