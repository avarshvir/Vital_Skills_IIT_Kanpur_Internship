import pandas as pd

# Sample data
data = {
    'Student': ['Alice', 'Bob', 'Alice', 'Bob', 'Alice', 'Bob'],
    'Subject': ['Math', 'Math', 'English', 'English', 'History', 'History'],
    'Score': [85, 90, 78, 88, 92, 84]
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)
print('----------------------------')
# Group by 'Subject'
grouped = df.groupby('Subject')

# Calculate the mean score for each subject
average_scores = grouped['Score'].mean()
print(average_scores)


#merging
print('------------------------------------------')

# DataFrame with student details
student_details = pd.DataFrame({
    'StudentID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [20, 21, 19, 22]
})

# DataFrame with student scores
student_scores = pd.DataFrame({
    'StudentID': [1, 2, 3, 4],
    'Subject': ['Math', 'English', 'Math', 'History'],
    'Score': [85, 90, 78, 88]
})

print("Student Details DataFrame:")
print(student_details)
print("\nStudent Scores DataFrame:")
print(student_scores)

# Merge the DataFrames on 'StudentID'
merged_df = pd.merge(student_details, student_scores, on='StudentID')

print("Merged DataFrame:")
print(merged_df)

