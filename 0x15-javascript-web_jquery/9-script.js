// script that fetches the value of hello from French API URL
// using jQuery API
const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.getJSON(URL, function (data) {
  const greeting = data.hello;
  $('DIV#hello').text(greeting);
});
