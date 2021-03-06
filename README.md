# Tic-Tac-Toe

## Overview

Tic-Tac-Toe is a simple game where two players compete to place three of their
"pieces" in a straight or diagonal line. 
([Read More](http://en.wikipedia.org/wiki/Tic-tac-toe))

This Project turns Tic-Tac-Toe in to a *fun*, web-based game where players can
try to defeat the Computer player. It is implemented using Django and HTML5.

## Usage

Here are the steps to quickly get this game up and running on your system:

1. Clone this repository
2. Create a [Virtual Environment](http://www.virtualenv.org/en/latest/) for this project.
3. Enter the Virtual Environment.
4. Install the dependencies: `pip install -r requirements.txt`
5. Create the database: `python manage.py syncdb`
6. Start Django's built-in HTTP Server: `python manage.py runserver`
7. Open the game on your web browser by browsing to 
    [localhost:8000](http://localhost:8000)

## Dependencies

* [Django](https://www.djangoproject.com/)
* [jQuery](http://jquery.com/)
* [Bootstrap](http://getbootstrap.com/)
* [Font Awesome](http://fontawesome.io/)

## Artificial Intelligence

The Artificial Intelligence is based upon the **Perfect Strategy** laid out in
the Wikipedia [article](http://en.wikipedia.org/wiki/Tic-tac-toe#Strategy). It 
currently implements most of the strategy with the exception of the *Fork* and 
*Block Forks* steps. While there is room for improvement to increase the 
opportunity for the Computer player to win, my manual testing has shown that the
game will always win in either a *Draw* or a *Computer Victory*.
