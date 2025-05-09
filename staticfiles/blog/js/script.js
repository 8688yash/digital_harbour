// Wait until DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Smooth Scroll for anchor links
    const navLinks = document.querySelectorAll('nav ul li a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Only scroll if it's a # link (optional)
            if (this.hash !== "") {
                e.preventDefault();
                const target = document.querySelector(this.hash);

                if (target) {
                    window.scrollTo({
                        top: target.offsetTop - 100, // Adjust based on your header height
                        behavior: "smooth"
                    });
                }
            }
        });
    });

    // Mobile Menu Toggle (optional)
    const mobileMenu = document.querySelector('.mobile-menu');
    const nav = document.querySelector('nav');

    if (mobileMenu) {
        mobileMenu.addEventListener('click', function() {
            nav.classList.toggle('active');
        });
    }

    console.log("Digital Harbour script loaded successfully!");
});
