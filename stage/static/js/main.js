function copyMessageDetailURL() {
  var textToCopy = document.getElementById('id_message-detail-url');

  textToCopy.select();
  textToCopy.setSelectionRange(0, 99999); /* For mobile devices */

  document.execCommand('copy');

  alert('Copied to clipboard!');
}
