from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "level_lounge/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    # Only display top-level comments (parent is none)
    comments = post.comments.filter(parent__isnull=True).order_by("-created_at")
    comment_count = post.comments.count()

    # Pass form to the template for new comments
    form = CommentForm()

    return render(
        request,
        "level_lounge/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "forms": form,
        }
    )


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            # Check if this is a reply to an existing comment
            parent_id = request.POST.get('parent_id')
            parent_comment = None
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
            
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Assuming the user is logged in
            comment.parent = parent_comment  # Set parent comment if it's a reply
            comment.save()
            
            return redirect('post_detail', slug=post.slug)
    
    return redirect('post_detail', slug=post.slug)