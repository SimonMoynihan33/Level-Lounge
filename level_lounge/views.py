from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, UserProfile
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
class PostList(generic.ListView):
    """
    View to display a paginated list of posts, showing the newest posts first.
    Posts are filtered to show only those with status = 1 (published).
    The list is paginated, showing 6 posts per page.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_at') 
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
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(parent__isnull=True).order_by("-created_at")  # Fetch top-level comments
    comment_form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
                new_comment.parent = parent_comment  # Set the parent comment
            new_comment.save()
            messages.success(request, 'Comment successfully posted.')
            return redirect('post_detail', slug=slug)

    return render(request, 'level_lounge/post_detail.html', {
        'post': post,
        'comments': comments,  # Top-level comments
        'comment_form': comment_form,
    })

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


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)  # Ensure only the author can delete the post
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')  # Redirect to home or post list after deletion

    return redirect('post_detail', id=post.id)  # Redirect back if not a POST request

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


def profile_view(request, username):
    """
    View to display the user's profile.
    """
    user_profile = get_object_or_404(UserProfile, user__username=username)  # Fetch the profile by username
    return render(request, 'level_lounge/profile.html', {'profile': user_profile})