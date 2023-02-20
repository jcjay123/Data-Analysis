students = pd.read_csv('grades.txt',delimiter=',',header='infer')
students.head()
#Handling the missing values using isnull()
students.isnull()
#get the sum of missing values for each column like this:
students.isnull().sum()
students[students.isnull().any(axis=1)]
students.StudyHours = students.StudyHours.fillna(students.StudyHours.mean())
students
students = students.dropna(axis=0, how='any')
students
# Get the mean study hours using to column name as an index
mean_study = students['StudyHours'].mean()

# Get the mean grade using the column name as a property (just to make the point!)
mean_grade = students.Grade.mean()
# Print the mean study hours and mean grade
print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))
# Get students who studied for the mean or more hours
students[students.StudyHours > mean_study]
# What was their mean grade?
students[students.StudyHours > mean_study].Grade.mean()
passes  = pd.Series(students['Grade'] >= 60)
students = pd.concat([students, passes.rename("Pass")], axis=1)
students
print(students.groupby(students.Pass).Name.count())
print(students.groupby(students.Pass)['StudyHours', 'Grade'].mean())
# Create a DataFrame with the data sorted by Grade (descending)
students = students.sort_values('Grade', ascending=False)
# Show the DataFrame
students
