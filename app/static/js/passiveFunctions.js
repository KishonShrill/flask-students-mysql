document.addEventListener("DOMContentLoaded", function() {
  // Modal Configuration
  // Modal Configuration
  // Modal Configuration
  const closeButton = document.querySelector("[data-close-modal]");
  const modal = document.querySelector("[data-modal]")

  closeButton.addEventListener("click", () => {
    modal.close()
  })


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
