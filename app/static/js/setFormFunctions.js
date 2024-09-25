function setSearchForm(destination) {
  const searchForm = document.getElementById('searchForm');
  const query = document.getElementById('search').value;
  const option = document.getElementById('searchOption').value;
  
  if ('student' == destination) {
    const selection = document.getElementById('studentSelection').value;
    searchForm.action = "/students/search/sort=" + selection + "?q=" + query + "&course=" + option;
  } else if ('programs' == destination) {
    searchForm.action = "/programs/search?q=" + query + "&college=" + option;
  } else {
    searchForm.action = "/colleges/search?q=" + query + "&college=" + option;
  }
  searchForm.submit();
}

function setCreateSubmitForm() {
  const createForm = document.getElementById('editForm');

  createForm.action = window.location.pathname + "/submit";
  createForm.submit();
}

function setEditForm(chosen_id, type) {
  const editForm = document.getElementById('singleEditForm');

  editForm.action = `/${type}/edit/id=${chosen_id}`;
  editForm.submit();
}

function setEditSubmitForm() {
  const editForm = document.getElementById('editStudentForm');

  editForm.action = window.location.pathname + "/submit";
  editForm.submit();
}

function submitSingleDeleteForm() {
  // Set the hidden input's value to the student's ID
  document.getElementById('delete-chosen_id').value = document.querySelector("[chosen-id]").innerHTML;
  // Submit the single delete form
  document.getElementById('singleDeleteForm').submit();
}