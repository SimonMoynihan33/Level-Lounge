/**
 * Function to toggle the visibility of the reply form associated with a specific comment.
 * @param {string} commentId - The ID of the comment for which the reply form needs to be toggled.
 */
function toggleReplyForm(commentId) {
    let form = document.getElementById('reply-form-' + commentId);
    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block';  // Show the reply form
    } else {
        form.style.display = 'none';  // Hide the reply form
    }
}

/**
 * Function to reveal more hidden replies in batches of 3.
 * @param {HTMLElement} button - The button element that triggered the event.
 */
function showMoreReplies(button) {
    let repliesContainer = button.previousElementSibling;
    let hiddenReplies = repliesContainer.querySelectorAll('.hidden-reply');
    
    console.log(hiddenReplies);  // Check if hidden replies are selected.querySelectorAll('.hidden-reply');

    // Show the next 3 hidden replies
    for (let i = 0; i < Math.min(3, hiddenReplies.length); i++) {
        hiddenReplies[i].classList.remove('hidden-reply');
    }

    // Hide the "Show more replies" button if there are no more hidden replies
    if (hiddenReplies.length <= 3) {
        button.style.display = 'none';
    }
}