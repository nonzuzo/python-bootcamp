#question1
def compareStrings(garland,flower):
    common_letters=0
    for i in range(len(flower)):
        if flower[i] in garland:
            common_letters+=1
    print(common_letters)
         
compareStrings(" a","aAaee")
#question2
def calculate_Grade(score): 
    if score <=100 and score>= 85:
        return "A+","grade point = 4.0/4.0"
    
    elif score <=84 and score>=80:
        return "A","grade point = 4.0/4.0"
    
    elif score <=79 and score>=75:
        return  "B+","grade point = 3.5/4.0"
    
    elif score <=74 and score>=70:
        return  "B","grade point = 3.0/4.0"
    
    elif score <=69 and score>=65:
        return  "C+","grade point = 2.5/4.0"
    
    elif score <=64 and score>=60:
        return( "C","grade point = 2.0/4.0")
    
    elif score <=59 and score>=55:
        return  "D+","grade point = 1.5/4.0"
    
    elif score <=54 and score>=50:
        return  "D","grade point = 1.0/4.0"
    
    else:
        return  "E","grade point = 0.0/4.0"
#print(calculate_Grade(64))

def honour(cumulative_GPA):
    if cumulative_GPA >=3.85 and cumulative_GPA<=4.0:
        return "Summa Cum Laude"
    elif cumulative_GPA >=3.70 and cumulative_GPA<=3.84:
        return "Magna Cum Laude"
    elif cumulative_GPA >=3.5 and cumulative_GPA<=3.69:
        return "Cum Laude"
    else:
        None
# print(honour( 3.65))

def grades_Report():
    courses= int(input("Enter the number of courses: "))
    for i in range (courses):
        grade= int(input("enter grade: "))
        print(calculate_Grade(grade))
print(grades_Report()) 








#question3
number = int(input("Enter number: "))
addition=0
for i in range(number+1):
    addition+=i
print(f"the total is {addition}")

#question4
def customLen(name):
    length=0
    for i in name:
        length= length+1
    print(length)
customLen("nzu")

# question5
number=int(input("Enter number: "))
for i in range(1, 13):
    multiple= i*number
    print(i,"*",number, "=",multiple)

#question6
magic_number=int(input("enter a number between 1-100: "))
if magic_number>50:
    print("That number is too high!")
elif magic_number<50:
    print("That number is too low!")
else:
    print("Hooray! You got it correct")

#question7
def is_vowel(name):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    if name in vowels:
        return True
     return False
print(is_vowel("s"))

 






