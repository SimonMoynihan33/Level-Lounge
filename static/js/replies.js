function toggleReplyForm(commentId) {
    let form = document.getElementById('reply-form-' + commentId);
    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block';  // Show the reply form
    } else {
        form.style.display = 'none';  // Hide the reply form
    }
}