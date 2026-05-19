const menuButton = document.querySelector(".menu-button");
const siteNav = document.querySelector(".site-nav");
const themeButtons = document.querySelectorAll(".theme-option");
const allowedThemes = ["light", "dark", "techy"];

function applyTheme(theme) {
    const selectedTheme = allowedThemes.includes(theme) ? theme : "light";
    document.body.dataset.theme = selectedTheme;

    themeButtons.forEach((button) => {
        const isActive = button.dataset.theme === selectedTheme;
        button.classList.toggle("active", isActive);
        button.setAttribute("aria-pressed", String(isActive));
    });
}

applyTheme(localStorage.getItem("projectXTheme") || "light");

themeButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const theme = button.dataset.theme;
        localStorage.setItem("projectXTheme", theme);
        applyTheme(theme);
    });
});

if (menuButton && siteNav) {
    menuButton.addEventListener("click", () => {
        const isOpen = siteNav.classList.toggle("open");
        menuButton.setAttribute("aria-expanded", String(isOpen));
    });

    siteNav.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            siteNav.classList.remove("open");
            menuButton.setAttribute("aria-expanded", "false");
        });
    });
}

const revealItems = document.querySelectorAll(".section, .project-card, .service-card, .process-card, .profile-panel, .auth-panel");

if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    revealObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.14 },
    );

    revealItems.forEach((item) => revealObserver.observe(item));
} else {
    revealItems.forEach((item) => item.classList.add("is-visible"));
}
