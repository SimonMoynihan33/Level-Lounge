function toggleMsAuto() {
    const navItem = document.querySelector('.nav-item.ms-auto'); // Select the element with the ms-auto class
    if (window.matchMedia("(max-width: 768px)").matches) {
        // Remove ms-auto if screen is 768px or smaller
        navItem.classList.remove('ms-auto');
    } else {
        // Add ms-auto if screen is larger than 768px
        navItem.classList.add('ms-auto');
    }
}

// Run on page load
toggleMsAuto();

// Run every time the screen is resized
window.addEventListener('resize', toggleMsAuto);