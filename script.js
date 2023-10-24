document.addEventListener("DOMContentLoaded", function () {
    const menuButton = document.getElementById("menu-button");
    const sidebar = document.querySelector(".sidebar");
    const content = document.querySelector(".content"); // Select the content element

    let isSidebarVisible = false;

    menuButton.addEventListener("click", function () {
        if (isSidebarVisible) {
            sidebar.style.display = "none"; // Hide the sidebar
            content.style.display = "block"; // Show the content
        } else {
            sidebar.style.display = "block"; // Show the sidebar
            sidebar.style.width = "100%"; // Expand the sidebar to 100% width
            content.style.display = "none"; // Hide the content
        }
        isSidebarVisible = !isSidebarVisible;
    });
});
