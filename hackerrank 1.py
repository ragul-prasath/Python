'''
🧩 Question: Second Lowest Grade Finder
You are given the names and scores of N students. Your task is to:

Store each student's name and score in a list.

Find the second lowest score among all the students.

Print the names of all students who have the second lowest score, in alphabetical order.

✅ Input Format:
The first line contains an integer N, the number of students.

The next 2N lines contain a student's name and their score, one pair per student.

✅ Constraints:
2 <= N <= 5

Student names are strings of lowercase/uppercase English letters.

Scores are floats between 0.0 and 100.0

There will always be at least two different scores.

✅ Output Format:
Print the names of the students who have the second lowest score.

Print each name on a new line.

The output should be in alphabetical order.
'''
# TO FIND SECOND LOWEST SCORE AMONG ALL STUDENT USING NESTED LIST EG: [[RAVI,89],[SAM,50],[HEMA,49]]
if __name__ == '__main__':
    l = []
    s = []
    x = []
    j=1
    for _ in range(int(input("Enter the no of  student: "))):

        name = input(f"enter the name of {j} student: ")
        score = float(input(f"Enter the score of {j} student: "))
        s.append(name)
        s.append(score)
        l.append(s)
        s = []
        j=j+1

    mx = float('inf')
    for i in range(len(l)):
        if l[i][1] < mx:
            mx = l[i][1]

    mx1 = float('inf')
    for i in range(len(l)):
        if l[i][1] < mx1 and l[i][1] != mx:
            mx1 = l[i][1]

    for i in range(len(l)):
        if l[i][1] == mx1:
            x.append(l[i][0])

    x.sort()
    for name in x:
        print(name)
