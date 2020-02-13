document.addEventListener('DOMContentLoaded', function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, stat) {
    $('DIV#hello').text(data.hello);
  });
});
