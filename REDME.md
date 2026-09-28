# Python Quiz Game
![Static Badge](https://img.shields.io/badge/python-3%20.12-blue)

A simple quiz game built with python
## Table of contents
- [Features](#features)
- [Project Struture](#project-struture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Envoirment Setup](#envoirment-setup)
- [Usage](#usage)
- [Example Output](#example-output)
- [Screeanshot](#screenshot)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Licence](#licence)
- [Author](#author)


## Features
- Quiz System
  - Asks the player multiple qustion
  - Cheks the ansewrs automaticlly
  - Calculates the final score
- Resulte Storage
  - Saves quiz results in `results.txt`
- Admin Mode
  - askss for the admin password
  - checks if the password is correct
  - keeps the private information outside the main python file
  - Loads the password from `.env`


## Project Struture

```txt
python_quiz_game/
│   .env.example
│   .gitignore
│   main.py
│   qustion.py
│   REDME.md
│   requirments.txt
│
├───gifs
│       dome.gif
│
├───pectures
│       1.jpg
│       2.jpg
│       3.jpg
└───
```
### File Description
| file | description |
| --- |---|
| `main.py` | main file used to run quiz game
| `qustion.py` | stores questions and answers
| `requirements.txt` | lists the python packages neeeded for the project|
| `.env.exmple` | shows the envoirment variables needed by the project|
| `.gitignore` | tells git which files and folders shold not be tracked|
| `pectures/` | stores project screenshot|
| `pectures/1.jpg` | screentshot of the game start|
| `pectures/2.jpg` | screentshot of the quiz section|
| `pectures/3.jpg` | screentshot of the final result|
| `gifs/` | stores demo GIF files|
| `gifs/demo.gif` | shows the project demo|

## Requirements
Before running the project, make sure you have:
- `python 3`
- `python-dotenv`

## Installation
1. open a terminal in the project folder.
2. check that python is installed:
```bash
python --version
```
3. install the python packages:
```bash
pip install -r requirements.txt
```

## Envoirment Setup
1. create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```
2. open the new `.env` file
3. replace the example value with your own password
```text
QUIZ_ADMIN_PASSWORDsyour_password_here
```
4. save the file.

> Do not commit your `.env` file because it may contain private information

## Usage
1. open a terminal in the project folder
2. run the quiz game
```bash
python main.py
```
3. choose `yes` or `no` for admin mode
4. if you choose `yes`, enter the password from your `.env` file
enter the password from your
5. enter your name
6. answer the questions
7. see your final score and message
8. your result is saved in `results.txt`

## Example Output
do u want to open admin mode? yes/no: no

what is your name ?alex
welcome alex

Product List
milk : 30 $
apple : 20 $
chocolate : 50 $

Enter the product name: milk

how many do you want? 3
total price: 150

## Screenshot

### start game
![start game](pectures\1.jpg)

### quiz
![quiz](pectures\2.jpg)

### final score
![final score](pectures\3.jpg)

## Demo
![quiz_game_demo](gifs\dome.gif)

## Roadmap
- [x] add multiple quiz qustions
- [x] calculate the final score 
- [x] save results to file
- [x] add admin mode
- [ ] add more quiz questions
- [ ] add difiiculty levels
- [ ] add a timer

## Contributing

## Licence

## Author
create by [Elsa](https://github.com/elsa-momeni)