/**
 * Function to toggle the visibility of the reply form associated with a specific comment.
 * @param {string} commentId - The ID of the comment for which the reply form needs to be toggled.
 */
function toggleReplyForm(commentId) {
    let form = document.getElementById('reply-form-' + commentId);
    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block'; // Show the reply form
    } else {
        form.style.display = 'none'; // Hide the reply form
    }
}
