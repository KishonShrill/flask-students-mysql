function setSearchForm(destination) {
  const searchForm = document.getElementById('searchForm');
  const query = document.getElementById('search').value;
  
  if ('students' == destination) {
    const option = document.getElementById('searchOption').value;
    const selection = document.getElementById('studentSelection').value;
    searchForm.action = "/students/search/sort=" + selection + "?q=" + query + "&course=" + option;
  } else if ('programs' == destination) {
    const option = document.getElementById('searchOption').value;
    searchForm.action = "/programs/search?q=" + query + "&college=" + option;
  } else {
    searchForm.action = "/colleges/search?q=" + query;
  }
  searchForm.submit();
}

function setEditForm(chosen_id, type) {
  const editForm = document.getElementById('singleEditForm');

  editForm.action = `/${type}/edit/id=${chosen_id}`;
  editForm.submit();
}

function setSubmitForm() {
  const editForm = document.getElementById('form');

  editForm.action = window.location.pathname + "/submit";
  editForm.submit();
}

function submitSingleDeleteForm() {
  // Set the hidden input's value to the student's ID
  document.getElementById('delete-chosen_id').value = document.querySelector("[chosen-id]").innerHTML;
  // Submit the single delete form
  document.getElementById('singleDeleteForm').submit();
}