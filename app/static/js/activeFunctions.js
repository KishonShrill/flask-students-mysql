function toggleAll(source) {
  // Get all checkboxes with class 'checkbox'
  const checkboxes = document.querySelectorAll('.checkbox');
  
  // Loop through all checkboxes and set their checked property
  checkboxes.forEach(checkbox => {
    checkbox.checked = source.checked;
  });
  toggleButton()
}

function toggleButton() {
  const checkboxes = document.querySelectorAll('.checkbox');
  const editButtons = document.querySelectorAll('.edit');
  const deleteButtons = document.querySelectorAll('.delete');
  const isAnyChecked = Array.from(checkboxes).some(checkbox => checkbox.checked);

  editButtons.forEach(button => {
    button.disabled = isAnyChecked;
    if (isAnyChecked) {
      button.classList.add('disabled');
    } else {
        button.classList.remove('disabled');
    }
  });
  deleteButtons.forEach(button => {
    button.disabled = isAnyChecked;
    if (isAnyChecked) {
      button.classList.add('disabled');
    } else {
        button.classList.remove('disabled');
    }
  });
}

function confirmationModal(studentId, category) {
  console.log(studentId + ":" + category);
  if (category == "singleDelete") {
    const modal = document.querySelector("[data-modal-delete]");
    const studentLabel = document.querySelector("[student-number]");
    modal.showModal();

    studentLabel.innerText = studentId;
    studentLabel.style.fontWeight = "bold";
  }
}


function deleteAll() {
  e.preventDefault();
  let selectedIDs = [];
  const checkboxes = document.querySelectorAll('.checkbox');

  checkboxes.forEach(checkbox => {
    if (checkbox.checked) {
      selectedIDs.push(checkbox.value);
    }
  });
}

function submitSingleDeleteForm(studentId) {
  // Set the hidden input's value to the student's ID
  document.getElementById('student_id').value = studentId;

  // Submit the single delete form
  document.getElementById('singleDeleteForm').submit();
}

function validateID() {
  const idInput = document.getElementById('editID');
  const regex = /^\d{4}-\d{4}$/;

  if (!regex.test(idInput.value)) {
      // idError.style.display = 'inline'; // Show the error message
      idInput.setCustomValidity("Invalid format. Must be 4 digits, a hyphen, and 4 digits.");
      return false; // Prevent form submission
  } else {
      // idError.style.display = 'none'; // Hide the error message
      idInput.setCustomValidity("")
      document.getElementById('singleEditForm').submit();
      return true; // Allow form submission
  }
}