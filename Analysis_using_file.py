import pandas as pd
import numpy as np
students =pd.read_csv('Grades.txt')
#printing first 5 values from csv file using head()
print(students.head())
#checking null values
print(students.isnull())
#counting the sum of null values for each column
print(students.isnull().sum())
#getting only null value positions
print(students[students.isnull().any(axis=1)])
#result Nan means not a number
#now that we have sum of null values we fill those null values with mean using fillna() function
students.StudyHours= students.StudyHours.fillna(students.StudyHours.mean())
students.Grade=students.Grade.fillna(students.Grade.mean())
print(students)
#we can remove null values like this but we should do it before setting values with mean
students=students.dropna(axis=0,how='any')
#Getting the mean for studhours and grade column
studyhours_mean= students.StudyHours.mean()
grade_mean=students.Grade.mean()
print("studying hours mean is",round(studyhours_mean,2),"Grades mean is",round(grade_mean,2))
# Get students who studied for the mean or more hours
print(students[students.StudyHours>studyhours_mean])
print(students[students.Name=='Rosie'])
#calculating mean for those who studied more than mean hours
print(students[students.StudyHours>studyhours_mean].Grade.mean())
#assuming pass marks is 60 and creating a column pass to see which student passed
passed_student=pd.Series(students.Grade>=60.0)
students = pd.concat([students, passed_student.rename("Pass")], axis=1)
print(students)
#counting the number of students passed and failed
print(students.groupby(students.Pass).Name.count())
#calculating avg hours studied by failed and passed students and also avg grades for passed and failed students
print(students.groupby(students.Pass)["StudyHours","Grade"].mean())
#finally sorting data
students=students.sort_values('Grade',ascending=False)
print(students)
