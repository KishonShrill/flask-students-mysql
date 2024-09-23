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

  // Get all elements with class="closebtn"
  var close = document.getElementsByClassName("closebtn");
  var i;

  // Loop through all close buttons
  for (i = 0; i < close.length; i++) {
    // When someone clicks on a close button
    close[i].onclick = function(){

      // Get the parent of <span class="closebtn"> (<div class="alert">)
      var div = this.parentElement;

      // Set the opacity of div to 0 (transparent)
      div.style.opacity = "0";

      // Hide the div after 600ms (the same amount of milliseconds it takes to fade out)
      setTimeout(function(){ div.style.display = "none"; }, 600);
    }
  }
});
