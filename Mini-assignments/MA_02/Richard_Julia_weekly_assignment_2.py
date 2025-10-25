"""
Questionnaire: For what purposes did you use Generative AI / LLMs when completing your assignment?
[] Not at all
[x] Which ones did you use? (e.g., ChatGPT, Bard, etc.) ChatGPT
[x] Explaining programming concepts
[] Practicing coding exercises
[] Debugging code
[] Reviewing your Python code
[] Optimizing code
[] Writing or completing code
[] Other (please specify): _____________

"""  



"""
Imagine you are developing an interactive python program for managing the students of your class.
Your task is to create a Python program that interacts with the user to collect and analyze data.
The program should perform the following tasks:

  
    1. Create an empty dictionary called student_data. Add Information of 5 current ITECH/CompDesign students studdents. Each key will be the student's name. Each value will be another dictionary with "age" and "country".

    2.Collect student information manually. Ask the user to enter information for 2 additional students. For each student: Prompt for name, age, and country. Store the information in student_data using the student’s name as the key.
    Allow the user to skip a student by pressing Enter for the name.
    
    3. Calculate the average age of the students. Create a list of ages manually using the dictionary values. Use sum() and len() to calculate the average. Print the average age.
    
    4. Create a set called students_countries to store unique countries.

    5. Create a list called young_students that includes the names of students who are younger than the average age. Print the list of young students.

    6. Print out the list of young students and the set of unique countries.
    
    7. 
    Extra Challenges (Optional):
    Calculate and print the total number of students. Calculate and print the percentage of students under the average age.


Deliverables:

Submission on Github
Upload on ILIAS

"""


#1

student_data={}
student_data={
  "Sofia" : {
    "Age" : float(24),
    "Country" : "Mexico"
  },
  "Sophia" : {
    "Age" : float(23),
    "Country" : "Chile"
  },
  "Julia" : {
    "Age" : float(23),
    "Country" : "Canada"
  },
  "Tiago" : {
    "Age" : float(29),
    "Country" : "Brazil"
  },
  "Tuğçe" : {
    "Age" : float(25),
    "Country" : "Mexico"
  }}

print(student_data)


#2

student_1_name=input("Please enter student's name. ")
student_1_age_str=input("How old is " + student_1_name + " ? ")
student_1_age=float(student_1_age_str)
student_1_country=input("What country is " + student_1_name + " from? ")

student_1_data={
    "Age" : student_1_age,
    "Country" : student_1_country
}

student_2_name=input("Please enter student's name. ")
student_2_age_str=input("How old is " + student_2_name + " ? ")
student_2_age=float(student_2_age_str)
student_2_country=input("What country is " + student_2_name + " from? ")

student_2_data={
    "Age" : student_2_age,
    "Country" : student_2_country
}

#If student_1_name is empty/0, skip to student_2_name, and leave student_1_data out of student_data
#If student_2_name is empty/0, leave student_2_data out of the student_data

student_data[student_1_name]=student_1_data
student_data[student_2_name]=student_2_data

print(student_data)

#3

student_age = [info["Age"] for info in student_data.values()]

average_age=round(sum(student_age)/len(student_age), 1)
print("The average age of the students is", average_age, ".")

#4

student_countries = {info["Country"] for info in student_data.values()}

#5

young_student = []

for name, info in student_data.items():
    if info["Age"] < average_age:
        young_student.append(name)

print("These students are younger than the average age:", young_student)

#6

print("These students are younger than the average age:", young_student)
print("These are the countries where all of the students are from:", student_countries)

#7

total_students=student_data.items()

print("There are", len(total_students), "students.")

young_students_per=round(len(young_student)/len(total_students)*100, 1)

print(young_students_per, "% of the students are below the average age of", average_age, ".")