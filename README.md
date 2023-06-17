# Hangman

![Title graphic](/assets/title.png)

The popular game of hangman, presented on a command line application format. The game is suitable to all persons, providing full user interaction to complete the game.

This game was created using the popular and powerful programming language called Python. It has been developed as project 3 of a 5 part series of repositories for Code Institute. Code institute offer a Diploma in Full Stack software development, that require the five projects to be submitted in order to succesfully pass the course.

I hope that you enjoy the game.

## Lucid Chart

![Flow Chart](/assets/flowchart.png)

Prior to initial implementation of the game, I constructed a flow chart to help me understand how I would be able to write the python code for the game. At the beginning of the game, I wanted to ask the user their name, and use it later on. Also I wanted to ask the user whether they were sure about their category decision. If not, I wanted to loop back to the question.

Finally, I needed to ensure that I could visually see how the code would work with regards to the guessing of letters. I was confused to begin with as I was asking myself whether the user found the correct letter in a word, which did not exist yet according to the flow chart. I rectified this to show that if the letter given was the correct word, and if not whether it was in the word before moving through the loop. 

I found the use of a flow chart incredibly useful when developing the application. It’s incredibly handy to have a visual representation of what I want my code to do, before writing it out. Although it is an early draft, I think adding to the chart as I was writing my code would have benefitted me further, as it was sometimes difficult to keep up with what I was coding.

## Design

![User interface](/assets/user-interface.png)
![Start of game](/assets/begin-game.png)

The design element does not feature too much in this project, as it is a command line interface project. Whilst not requiring any ‘glamorous’ design, the function of the app works well enough. I have previously seen some other apps developed by students that hold a little more style, but for the purposes of the game, everything is fine.

### ASCII Art

![Gallows art](/assets/gallows-art.png)
![ASCII Art](/assets/ASCII%20Hangman.png)

Looking at previous projects from other students, I really liked the idea of using ASCII (A graphical design technique using printable characters to create images) art. As a command line program, this game could easily have looked bland and boring to a user. I feel there could have been more use of the ASCII art, perhaps to display how many lives were remaining, as I don not feel this is highlighted quite as well as it should be.

## Testing

### Validation

![Snyk validator](/assets/snyk-validate.png)

For validation, I used Snyk. This allowed me to test the entire code and test it up to the PEP8 standards. PEP8 (Python Enhancement Proposal) dives into the readability and consistency of the Python code written. This test suggested I use a different method to exit the program, however there are no errors in what my current code does. Aside from my own personal readability issues (more below) my code conforms to PEP8.
