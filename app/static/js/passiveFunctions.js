document.addEventListener("DOMContentLoaded", function() {  
  // 
  setTimeout(async function() {
    $(".loader-wrapper").fadeOut("slow");
  }, 1000);
  
  // Modal Configuration
  // Modal Configuration
  // Modal Configuration
  const closeButtonDelete = document.querySelector("[data-close-modal-delete]");
  const deleteModal = document.querySelector("[data-modal-delete]")


  closeButtonDelete.addEventListener("click", () => {deleteModal.close()})


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
