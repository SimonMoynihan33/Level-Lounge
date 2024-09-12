from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "level_lounge/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    # Only display top-level comments (parent is none)
    comments = post.comments.filter(parent__isnull=True).order_by("-created_at")
    comment_count = post.comments.count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment successful'
    )

    # Pass form to the template for new comments
    comment_form = CommentForm()

    return render(
        request,
        "level_lounge/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )

# ------------------------------------- TO BE FIXED
# def add_comment(request, slug):
#     post = get_object_or_404(Post, slug=slug)
    
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
        
#         if form.is_valid():
#             # Check if this is a reply to an existing comment
#             parent_id = request.POST.get('parent_id')
#             parent_comment = None
#             if parent_id:
#                 try:
#                     parent_comment = Comment.objects.get(id=parent_id)
#                 except Comment.DoesNotExist:
#                     parent_comment = None  # In case the parent comment doesn't exist

#             comment = form.save(commit=False)
#             comment.post = post
#             comment.author = request.user  # Assuming the user is logged in
#             comment.parent = parent_comment  # Set parent comment if it's a reply
#             comment.save()
            
#             return redirect('post_detail', slug=post.slug)
    
#     return redirect('post_detail', slug=post.slug)