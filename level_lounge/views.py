from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator

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


