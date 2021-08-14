function copyMessageDetailURL() {
  var textToCopy = document.getElementById('id_message-detail-url').value;
  window.prompt("Copy to clipboard: Ctrl+C, Enter", textToCopy);
}
