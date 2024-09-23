function setSearchForm() {
  const searchForm = document.getElementById('searchForm');
  const query = document.getElementById('search').value;
  const college = document.getElementById('searchCollege').value;
  const selection = document.getElementById('studentSelection').value;

  searchForm.action = "/students/search/sort=" + selection + "?q=" + query + "&college=" + college;
  searchForm.submit();
}

function setEditForm(studentId) {
  const editForm = document.getElementById('singleEditForm');

  editForm.action = `/students/edit/id=${studentId}`;
  editForm.submit();
}

function setEditSubmitForm() {
  const editForm = document.getElementById('editStudentForm');

  editForm.action = window.location.pathname + "/submit";
  editForm.submit();
}

function submitSingleDeleteForm() {
  // Set the hidden input's value to the student's ID
  document.getElementById('student_id-delete').value = document.querySelector("[student-number]").innerHTML;
  // Submit the single delete form
  document.getElementById('singleDeleteForm').submit();
}