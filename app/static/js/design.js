document.addEventListener("DOMContentLoaded", function() {
  // Get the current URL path
  const currentPath = window.location.pathname;
  console.log(window.location.pathname)

  // Find all nav links
  const navLinks = document.querySelectorAll('.aside__nav-links');

  // Iterate through each link and apply background color if the path matches
  navLinks.forEach(link => {
      if (link.getAttribute('href') === currentPath) {
          link.style.backgroundColor = "rgb(0, 154, 0)";
          link.style.color = "white";
      }
  });
});
