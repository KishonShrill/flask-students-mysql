document.addEventListener("DOMContentLoaded", function() {  
  // Modal Configuration
  // Modal Configuration
  // Modal Configuration
  const closeButtonDelete = document.querySelector("[data-close-modal-delete]");
  const closeButtonEdit = document.querySelector("[data-close-modal-edit]");
  const deleteModal = document.querySelector("[data-modal-delete]")
  const editModal = document.querySelector("[data-modal-edit]")


  closeButtonDelete.addEventListener("click", () => {deleteModal.close()})
  closeButtonEdit.addEventListener("click", () => {editModal.close()})


  // Delete Submission
  // Delete Submission
  // Delete Submission
  const studentLabel = document.querySelector("[student-number]");
  const deleteButton = document.querySelector("[delete-confirmation]");

  deleteButton.addEventListener("click", () => {
    console.log("I HAVE BEEN PRESSED");
    submitSingleDeleteForm(studentLabel.innerText);
  });
});
