# Goal

It's always difficult to get motivated to go to the gym but for a few months, you've found a winning formula. You go after work with a colleague motivated and motivates you to miss any session.

Lack of luck, tonight he's sick. You thought you had a good excuse to dodge, but it's gone. Your colleague begs you to go there because he forgot his wallet in his locker the day before.

Lockers are protected by a numeric password. Your colleague, a little paranoid, does not want to write you the password by message but it gives you two indications:
- An interval [A, B] and a number D
- It guarantees that the password is the first number divisible by D in this interval

The interval is inclusive which means that the password can be the lower bound or the upper bound.

You must determine the password of the locker.

# Data format

## Entrance

Line 1: an integer A between 10 and 10,000 representing the lower bound of the interval.
Line 2: an integer between A + 1 and 10,001 representing the upper bound of the interval.
Line 3: an integer D between 1 and 1000 representing a divisor of the password.

## Exit

An integer corresponding to the password of the locker.