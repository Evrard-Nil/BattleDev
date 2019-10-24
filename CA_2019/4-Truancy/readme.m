# Objective
All the children want to become champion of the playground in the formidable
game of Magic Cards. It requires a lot of training, unfortunately your agenda is full
with hours of lessons. So you decide to develop a strategy to get the proper
training. Professor Harrison Jones doesn't have very good eyesight, not sure he
notices you're missing if you miss a few classes to practice Magic Cards.
He does however have a very good hearing, and is a little suspicious, if he does
not hear you arguing with your little classmates from the back of the class for more
than K consecutive courses, he will realize that something is wrong.
Knowing your weekly schedule, the goal of this challenge is to determine the best
combination of courses to miss, maximizing the number of hours you will spend
training without being discovered by the teacher. So you can choose to skip all the
courses you want, as long as you don't miss more than a certain number of
consecutive ones.

# Data format
### Input
Row 1: an integer N between 1 and 1000 representing the number of courses in
a week.
Row 2: an integer between 1 and N representing the number of consecutive
courses that you can skip without getting caught.
Rows 3 to N+1: an integer between 1 and 50 000 representing the duration of each
course.
## Output
The maximum number of hours you can skip without getting caught!
# Example
## Input
10
3
6
4
2
7
3
5
1
7
9
1
## Outside
42

In this example, you decide to attend only to the 3rd and 7th courses, so you never
miss more than 3 in a row. So you miss 6+4+7+3+5+7+9+1= 42 hours of class!