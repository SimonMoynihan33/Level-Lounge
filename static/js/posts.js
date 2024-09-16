const editButtons = document.getElementsByClassName("btn-edit");
const postText = document.getElementById("id_body");  // Make sure this targets the correct post content field
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated post's ID upon click.
* - Fetches the content of the corresponding post.
* - Populates the `postText` input/textarea with the post's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_post/{postId}` endpoint.
*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let postId = e.target.getAttribute("post_id");
        let postContent = document.getElementById(`post${postId}`).innerText;
        postText.value = postContent;  // Populate the post content for editing
        submitButton.innerText = "Update";  // Change button text to "Update"
        postForm.setAttribute("action", `/edit_post/${postId}`);
    });
}