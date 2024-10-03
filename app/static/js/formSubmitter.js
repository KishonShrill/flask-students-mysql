document.addEventListener('DOMContentLoaded', function() {
  const confirmButton = document.querySelector('.add[submit-confirmation]'); // The confirm button
  const editForm = document.getElementById('form'); // The form element
  const tooltip = document.getElementById('confirm-tooltip');
  let initialFormData = new FormData(editForm); // Get the initial form data

  // Disable the confirm button initially
  confirmButton.disabled = true;

  // Function to compare the current form data with the initial data
  function checkFormChanges() {
      const currentFormData = new FormData(editForm);
      for (let [key, value] of currentFormData.entries()) {
          if (initialFormData.get(key) !== value) {
              return true; // A change has been detected
          }
      }
      return false; // No changes
  }

  // Enable the confirm button if the form changes
  editForm.addEventListener('input', function() {
      if (checkFormChanges()) {
          confirmButton.disabled = false;
          confirmButton.classList.remove('disabled');
          tooltip.style.display = "none";
      } else {
          confirmButton.disabled = true;
          confirmButton.classList.add('disabled');
          tooltip.style.display = "block";
      }
  });
});
