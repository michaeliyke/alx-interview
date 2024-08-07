#!/usr/bin/env node
// script that prints all characters of a Star Wars movie:

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    // Use Promise.all to process all characters with order preserved
    Promise.all(characters.map(processCharacter))
      .then((names) => names.forEach((name) => console.log(name)))
      .catch((error) => console.error('Error:', error));
  }

});

function processCharacter(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(response.statusCode);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}
