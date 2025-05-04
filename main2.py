import pandas as pd

# Sample data: Student scores
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 92, 88, 76],
    'Science': [90, 82, 85, 95, 80],
    'English': [78, 85, 88, 76, 90]
}

# Creating a DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Add a new column: Average Score
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

print("\nData with Average Score:")
print(df)

# Filter students with average score greater than 85
high_achievers = df[df['Average'] > 85]
print("\nStudents with Average Score > 85:")
print(high_achievers)

# Sort students by Average Score descending
sorted_df = df.sort_values(by='Average', ascending=False)
print("\nStudents Sorted by Average Score (Descending):")
print(sorted_df)

# Grouping (optional extension): Assume we have class sections
df['Section'] = ['A', 'B', 'A', 'B', 'A']
section_avg = df.groupby('Section')[['Math', 'Science', 'English', 'Average']].mean()
print("\nAverage Scores by Section:")
print(section_avg)