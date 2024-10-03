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

  const modal = document.querySelector("[data-modal-delete]");
  const studentLabel = document.querySelector("[chosen-id]");
  modal.showModal();

  const confirmationButton = document.querySelector("button[delete-confirmation]");
  if (chosen_id == 'MULTIPLE') {
    // Modify the button's properties
    confirmationButton.setAttribute("onclick", "deleteAll()");  // Change onclick function
    console.log("olSGBDFUOBWSEVBFSDVB")
  }

  studentLabel.innerText = chosen_id;
  studentLabel.style.fontWeight = "bold";
  console.log(chosen_id)
}


function deleteAll() {
  const deleteSelectedForm = document.getElementById('deleteSelectedForm')
  
  let selectedIDs = [];
  const checkboxes = document.querySelectorAll('.checkbox');

  checkboxes.forEach(checkbox => {
    if (checkbox.checked) {
      selectedIDs.push(checkbox.value);
    }
  });
  
  deleteSelectedForm.submit();
}