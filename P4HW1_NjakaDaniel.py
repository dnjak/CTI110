# Daniel Njaka
# 3/25/2025
# P4HW1
# Show scores and average based on user input


'''
Pseudocode

Create variable num_scores (int) -> user input number of score
Create an empty list -> scores_list
for each in range(num_scores)
    score = int(input(f"Enter score # {each+1}"))
    while score is invalid - less than 0 or score greater than 100
        output to user score is invalid
        output to user score must be 0-100
        score int(input(f"Enter score # {each+1}"))
    scores_list.append(score)
print scores_list to ensure it's correct

Get the lowest score in list -> assign to variable
Remove the lowest score from the list

get average of list after removing lowest score
use average to determine letter grade
'''

num_scores = int(input("Enter the number of scores: ")) 

scores_list = [] 
 
for each in range(num_scores): 
    score = int(input(f"Enter score #{each + 1}: ")) 
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.") 
        score = int(input(f"Enter score #{each + 1}: ")) 
    scores_list.append(score) 
print("\nScores entered:", scores_list) 
lowest_score = min(scores_list) 
scores_list.remove(lowest_score) 
average = sum(scores_list) / len(scores_list) 
print(f"Average after removing lowest score: {average:.2f}") 
if average >= 90: grade = 'A' 
elif average >= 80: grade = 'B' 
elif average >= 70: grade = 'C' 
elif average >= 60: grade = 'D' 
else: grade = 'F' 
print(f"Letter grade: {grade}")