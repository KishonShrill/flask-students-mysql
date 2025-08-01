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
});