setTimeout(function() {
    const messages = document.querySelectorAll('.messages .alert');
    messages.forEach(message => {
        message.style.transition = 'opacity 0.5s';
        message.style.opacity = '0';
        setTimeout(() => message.remove(), 500); // Remove from DOM after fade out
    });
}, 3000); // 3 seconds