function toggleAll(source) {
  // Get all checkboxes with class 'checkbox'
  const checkboxes = document.querySelectorAll('.checkbox');
  
  // Loop through all checkboxes and set their checked property
  checkboxes.forEach(checkbox => {
      checkbox.checked = source.checked;
  });
}

function submitSingleDeleteModal(studentId) {
  const modal = document.querySelector("[data-modal-delete]");
  const studentLabel = document.querySelector("[student-number]");
  modal.showModal();

  studentLabel.innerText = studentId;
  studentLabel.style.fontWeight = "bold";
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

function editStudent(firstname, lastname, ID, year, gender) {
  const editfirstname = document.querySelector('#editFirstName');
  const editlastname = document.querySelector('#editLastName');
  const editID = document.querySelector('#editID');
  const edityear = document.querySelector('#editYear');
  const editgender = document.querySelector('#editGender');

  const modal = document.querySelector("[data-modal-edit]");
  modal.showModal();

  console.log(firstname);
  
  editfirstname.placeholder = firstname;
  editlastname.placeholder = lastname;
  editID.placeholder = ID;
  edityear.placeholder = year;
  editgender.placeholder = gender;
  document.getElementById('student_id-edit').value = ID;
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