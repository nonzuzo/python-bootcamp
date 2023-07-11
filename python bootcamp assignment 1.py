# question 1
hwWeight=0.4
examWeight=0.5
discussionWeight=0.1

homework_grade = float(input("please enter your homework grade: "))
exam_grade =float(input("please enter your exam grade: "))
discussion_grade =float(input("please enter discussion grade: "))

total_grade=(hwWeight*homework_grade)+(examWeight*exam_grade)+(discussionWeight*discussion_grade)
print(total_grade)

#question 2
#a fruitful function returns a value whilst a void function does not

#question 3
P=10000
n=12
r=0.08
t=int(input("please enter the number of years the money will be compounded for: "))
A=P*(1+(r/n))**(n*t)
print(A)

#question 4
def calculateGPA(score):
    if score>=84:
        return 4.0
    elif score>=75:
        return 3.5
    elif score>=70:
        return 3.0
    elif score>=65:
        return 2.50
    elif score>=60:
        return 2.00
    elif score>=55:
        return 1.50
    elif score>=50:
        return 1.00
    else:
        return 0.00
        
 
def getHonours(GPA):
    if GPA >=3.85:
        return "Summa Cum Laude"
    elif GPA >=3.70:
        return "Magna Cum Laude"
    elif GPA >=3.5:
        return "Cum Laude"
    else:
        None
        
GPA=calculateGPA(90)
honour=getHonours(GPA)

print(GPA)
print(honour)

#question 5
import math
radius= int(input("please enter the radius: "))
area= math.pi * radius**2
print(area)

#question 6
def is_triangle(sideA,sideB,sideC):
    if sideA+sideB==sideC or sideA+sideC==sideB or sideC+sideB==sideA:
        return True
    else:
        return False
    
#print(is_triangle(14,7,7))

 
a =int(input(" please enter length 1: "))
b =int(input(" please enter length 2: "))
c =int(input(" please enter length 3: ")) 
 
triangle = is_triangle( a,b,c)
print("can these lengths make a triangle?",triangle)































