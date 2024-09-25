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
  const actionButtons = document.querySelectorAll('.action');
  const deleteAllBtn = document.querySelector('#deleteAll');
  const isAnyChecked = Array.from(checkboxes).some(checkbox => checkbox.checked);

  actionButtons.forEach(button => {
    button.disabled = isAnyChecked;
    if (isAnyChecked) {
      button.classList.add('disabled');
    } else {
      button.classList.remove('disabled');
    }
  });

  if (isAnyChecked) {
    deleteAllBtn.removeAttribute("hidden");
  } else {
    deleteAllBtn.setAttribute("hidden", "hidden");
  }
}

function confirmationModal(chosen_id, category) {
  console.log(chosen_id + ":" + category);

  if (category == "singleDelete") {
    const modal = document.querySelector("[data-modal-delete]");
    const studentLabel = document.querySelector("[chosen-id]");
    modal.showModal();

    studentLabel.innerText = chosen_id;
    studentLabel.style.fontWeight = "bold";
  }

  if (category == "singleEdit") {
    const modal = document.querySelector("[data-modal-delete]");
    const studentLabel = document.querySelector("[chosen-id]");
    modal.showModal();

    studentLabel.innerText = chosen_id;
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

function validateStudent() {
  const fnInput = document.getElementById('studentFirstName');
  const lnInput = document.getElementById('studentLastName');
  const idInput = document.getElementById('studentID');
  const regexName = /^[A-Za-z\s]+$/;
  const regexID = /^\d{4}-\d{4}$/;

  if (!regexName.test(fnInput.value)) {
      alert("Invalid First Name: Only letters and spaces are allowed and must NOT be empty.");
      return false; // Prevent form submission
  }
  if (!regexName.test(lnInput.value)) {
    alert("Invalid Last Name: Only letters and spaces are allowed and must NOT be empty.");
    return false; // Prevent form submission
  }
  if (!regexID.test(idInput.value)) {
    alert("Invalid format for Student ID. Must be in the format 1234-5678.");
    return false; // Prevent form submission
  }
  
  return true;
}