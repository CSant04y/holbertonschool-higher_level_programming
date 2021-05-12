// This toggles the class of an HTML header tag
// When the user touches the header it toggles the color from green to red
$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('green')) {
    $('header').toggleClass('red');
  } else {
    $('header').toggleClass('green');
  }
});
