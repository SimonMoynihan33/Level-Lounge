// Fade out and remove messages after 3 seconds
setTimeout(function() {
    const messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        message.style.transition = 'opacity 0.5s'; // Smooth fade-out
        message.style.opacity = '0'; // Start fade-out
        setTimeout(() => message.remove(), 500); // Remove from DOM after fade-out completes
    });
}, 3000); // 3 seconds