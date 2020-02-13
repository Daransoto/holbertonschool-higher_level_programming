document.addEventListener('DOMContentLoaded', function () {
  $('DIV#add_item')[0].addEventListener('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item')[0].addEventListener('click', function () {
    $('UL.my_list')[0].lastElementChild.remove();
  });
  $('DIV#clear_list')[0].addEventListener('click', function () {
    $('UL.my_list').children().remove();
  });
});
