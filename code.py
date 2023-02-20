import numpy as np
import pandas as pd
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
print(data)
grades = np.array(data)
print(grades)
print (type(data),'x 2:', data * 2)
print('---')
print (type(grades),'x 2:', grades * 2)
#to view the shape of the array i.e., the length of the array or total number of grades
print(grades.shape)
#Calculating the average of the student marks by using mean() function
print(grades.mean())
# Defining an array of study hours per week
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]
# Creating a  2D array (an array of arrays)
student_data = np.array([study_hours, grades])
# displaying the array
print(student_data)
#showing shape of student data i.e., 2d array
print(student_data.shape)
avg_study = student_data[0].mean()
avg_grades= student_data[1].mean()
print("average study is",round(avg_study,2))
print("average grades is", round(avg_grades,2))
#using pandas to work with multi dimensional arrays he Pandas package offers a more convenient structure to work with the DataFrame.
students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie',
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

print(students)
# Get the data for index value 5
print(students.loc[5])
# Get the rows with index values from 0 to 5
print(students.loc[0:5])
# Get data in the first five rows without considering index by using iloc() method
print(students.iloc[0:5])
#iloc identifies data values in a DataFrame by position,
# which extends beyond rows to columns. So, for example,
#we can use it to find the values for the columns in positions 1 and 2 in row 1 like this:
print(students.iloc[1,[1,2]])
print(students.loc[2,'Grade'])
print(students.loc[students['Name']=='Aisha'])
print(students[students['Name']=='Aisha'])
#we can achieve the same results by using the DataFrame's query method
print(students.query('Name=="Pedro"'))
print(students[students.StudyHours==11.5])

