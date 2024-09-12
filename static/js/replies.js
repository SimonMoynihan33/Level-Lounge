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

function hideReplies() {
    console.log('hideReplies is called')
    let allRepliesContainers = document.querySelectorAll('.replies');

    // Loop through each reply container
    allRepliesContainers.forEach(function(repliesContainer) {
        let replies = repliesContainer.querySelectorAll('.reply');
        console.log(replies.length + ' replies found');
                
        // Hide replies beyond the third one
        for (let i = 3; i < replies.length; i++) {
            console.log('Hiding replies..')
            replies[i].classList.add('hidden-reply'); // Apply the hidden class
        }

        // If there are more than 3 replies, show the "Show more replies" button
        let showMoreButton = repliesContainer.nextElementSibling;
        if (replies.length > 3) {
            showMoreButton.style.display = 'inline-block';
        }
    });
};

/**
 * Function to reveal more hidden replies in batches of 3 when the "Show more replies" button is clicked.
 * @param {HTMLElement} button - The button element that triggered the event.
 */
function showMoreReplies(button) {
    let repliesContainer = button.previousElementSibling;
    let hiddenReplies = repliesContainer.querySelectorAll('.hidden-reply');
    
    // Show the next 3 hidden replies
    for (let i = 0; i < Math.min(3, hiddenReplies.length); i++) {
        hiddenReplies[i].classList.remove('hidden-reply');
    }

    // If there are no more hidden replies, hide the "Show more replies" button
    if (hiddenReplies.length <= 3) {
        button.style.display = 'none';
    }

    // Show the collapse button
    let collapseButton = button.nextElementSibling;  // Collapse button comes after "Show more replies"
    collapseButton.style.display = 'inline-block';  // Show the "Collapse replies" button
}

/**
 * Function to collapse replies back to only showing the first 3.
 * @param {HTMLElement} button - The button element that triggered the event.
 */
function collapseReplies(button) {
    let repliesContainer = button.previousElementSibling.previousElementSibling;  // Replies container is two elements before the button
    let replies = repliesContainer.querySelectorAll('.reply');

    // Hide all replies beyond the first 3
    for (let i = 3; i < replies.length; i++) {
        replies[i].classList.add('hidden-reply');  // Reapply the hidden class
    }

    // Show the "Show more replies" button
    let showMoreButton = button.previousElementSibling;
    showMoreButton.style.display = 'inline-block';  // Show the "Show more replies" button

    // Hide the collapse button
    button.style.display = 'none';  // Hide the "Collapse replies" button
}