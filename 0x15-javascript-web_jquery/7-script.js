// this gets a request from a url
const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.getJSON(url, function (data) {
    const name = data.name;
    $('DIV#character').text(name);
});
