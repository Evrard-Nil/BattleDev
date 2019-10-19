# Objective
A very famous international industrial pastry manufacturing firm has decided to
organize a contest game. The winning ticket is slid inside a chocolate bar.
Chocolate bars are time-stamped. Each package indicates its precise expiration
date using a number representing the number of microseconds that have passed
since January 1, 1900 (that's precise, they are serious on chocolote bars). You have an insider information, and you know for sure that the ticket is in a package whose iterated sum of the numbers of the time stamp is equal to 42. To obtain the iterated sum of the figures of an integer strictly greater than 99, for example 10412412, we sum up his figures: 1-0-4-1-4-1-2-15, then take the sum of his figures and so on until we have a number of up to two digits , in this case: 15 has only two digits, so the sum of the iterated figures of 10412412 is 15. If the integer is smaller than 99, the iterated sum is the integer number itself. A 3-week internship in the company, renewable, will be offered to the lucky winner, so you decide to put all the chances on your side by buying all the
chocolate bars respecting this constraint!
# Data format
## Input
Row 1: a integer N between 1 and 1000 representing the number of bars
purchased.
Rows 2 to N +1: the timestamp of the expiry date as displayed on the packaging of
the bar, in the form of an integer of 2^32 or less.
## Output
The number of bars that have a chance to contain the winning ticket.
# Examples
## Input
6

1571220869

1571320869

1570424270

1570220869

1570420870

1570420869

## Output
2
## Input
1
42
## Output
1