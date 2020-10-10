# Rock-Paper-Scissors--Statistics-Guessing
A simple rock-paper-scissors game in which the computer tries to learn the paterns of the player based on simple prababilities.
Using the player's responses to previous games, the program tries to adjust itself to predict what the player will play next.

For example, if in the previous game the Computer played Rock and in the next game the player played Scissors, the program
will know that there's a higher chance of the player playing Scissors after the computer played Rock and will thus increase the
chance of it playing Paper after playing Rock. The decision by the computer may be purposefully biased but it is never forced.
It always comes down to a random number generation.
