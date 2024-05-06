# My Game List
*My Game List* is a web app that aims to make tracking your video game collection easier. MGL lets you keep track of the games you've finished, games you're currently playing, or even ones you haven't started yet. With each game entry, you're able to create notes, rate the game, and even upload screenshots of your gameplay. MGL uses the [IGDB API](https://api-docs.igdb.com/#getting-started) to pull video game data, which allows users to search for a specific game.

![](https://github.com/jtnguyen45/my-game-list/blob/main/main_app/static/images/screenshots/All%20Games.png)

## Technology Used
- Django
- Python
- PostgreSQL
- Amazon S3
- Materialize CSS

## Getting Started
Access My Game List [here](https://my-game-list-jtnguyen45-7c12e6e9c889.herokuapp.com/).

You can search for video games by title in the "Search Games" tab, and it will populate the results below.
![](https://github.com/jtnguyen45/my-game-list/blob/main/main_app/static/images/screenshots/Search%20Games.png)


To add a game to your collection, click on the "Add Game" tab in the navbar and fill out the form as seen below. For the cover, I recommend searching for the cover in google images. Including "imdb" in your search will return good results for game covers to use.
![](https://github.com/jtnguyen45/my-game-list/blob/main/main_app/static/images/screenshots/Add%20Game.png)


Once you add your game, you'll be redirected to the games info, as seen below! You will be able to edit the game entry, delete it, and even add notes and screenshots.
![](https://github.com/jtnguyen45/my-game-list/blob/main/main_app/static/images/screenshots/Features%201.png)


To add a note, you can expand the "Add a note" tab and put whatever informtion or update on the game you want.
![](https://github.com/jtnguyen45/my-game-list/blob/main/main_app/static/images/screenshots/Features%202.png)


To add screenshots of your gameplay, scroll to the bottom and add your images with the "Choose File" button. Click "Upload Photo", and that's it!
![](https://github.com/jtnguyen45/my-game-list/blob/main/main_app/static/images/screenshots/Features%203.png)
![](https://github.com/jtnguyen45/my-game-list/blob/main/main_app/static/images/screenshots/Features%204.png)

Enjoy your video game adventure!

## Next Steps
- Let user toggle between grid or list view when viewing their game collection
- Add platform and genre to models, and create corresponding functions to pull from the platform and genre endpoints in the IGDB API
- Add a "related games" section when viewing a game
- Create user profile and let them display top 5 favorite games
- Add forums type page for users to discuss video games
