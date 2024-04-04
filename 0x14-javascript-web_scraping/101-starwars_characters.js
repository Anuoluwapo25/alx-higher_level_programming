#!/usr/bin/node
const request = require('request');

function fetchMovieDetails(movieId, callback) {
	const url = "https://swapi-api.alx-tools.com/api/";
	request(url, (error, response, body) => {
        if (error) {
            callback(error, null);
            return;
        }
        if (response.statusCode !== 200) {
            callback(`Error: ${response.statusCode}`, null);
            return;
        }
        const movie = JSON.parse(body);
        callback(null, movie);
    });
}

function printCharacterNames(movie) {
    console.log(`Characters in "${movie.title}":`);
    movie.characters.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.error(error);
                return;
            }
            if (response.statusCode !== 200) {
                console.error(`Error: ${response.statusCode}`);
                return;
            }
            const character = JSON.parse(body);
            console.log(character.name);
        });
    });
}

function main() {
    const movieId = process.argv[2];
    if (!movieId) {
        console.error('Please provide the Movie ID as a command line argument.');
        return;
    }
    fetchMovieDetails(movieId, (error, movie) => {
        if (error) {
            console.error(error);
            return;
        }
        printCharacterNames(movie);
    });
}

maain();
