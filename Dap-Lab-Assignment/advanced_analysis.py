import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("Cleaned_Data.csv")

# Clean column names by stripping whitespace
data.columns = data.columns.str.strip().str.replace('"', '').str.replace("'", '')

# 1. Remote Work Preference Distribution
plt.figure(figsize=(12, 6))

# Try to match the column name based on keywords
pref_col = [col for col in data.columns if "work" in col.lower() and "prefer" in col.lower()]

if pref_col:
    remote_pref = data[pref_col[0]].value_counts()
    remote_pref.plot(kind='bar', color='skyblue')
    plt.title("Preferred Remote Work Time Post-COVID")
    plt.xlabel("Remote Work Preference")
    plt.ylabel("Number of Employees")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    print("Remote work preference column not found.")


# 2. Productivity Comparison
plt.figure(figsize=(12, 6))
try:
    productivity_col = [col for col in data.columns if "productivity" in col.lower() and "remote" in col.lower()][0]
    productivity = data[productivity_col].value_counts()
    productivity.plot(kind='bar', color='lightgreen')
    plt.title("Self-Reported Productivity When Working Remotely")
    plt.xlabel("Productivity Level")
    plt.ylabel("Number of Employees")
    # plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
except IndexError:
    print("Could not find productivity column. Check your data.")

# 3. Employer Policy Impact
plt.figure(figsize=(10, 6))
try:
    policy_col = [col for col in data.columns if "employer" in col.lower() and "policy" in col.lower()][0]
    satisfaction_col = [col for col in data.columns if "satisfaction" in col.lower() or "feel better" in col.lower()][0]
    
    # Convert Likert scale to numerical if needed
    likert_map = {
        "Strongly disagree": 1,
        "Somewhat disagree": 2,
        "Neither agree nor disagree": 3,
        "Somewhat agree": 4,
        "Strongly agree": 5
    }
    data['Satisfaction_Score'] = data[satisfaction_col].map(likert_map)
    
    policy_groups = data.groupby(policy_col)['Satisfaction_Score'].mean()
    policy_groups.plot(kind='bar', color=['orange', 'blue'])
    plt.title("Impact of Employer Policy on Remote Work Satisfaction")
    plt.xlabel("Employer Requires Some Workplace Attendance")
    plt.ylabel("Average Satisfaction (1-5 Scale)")
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
except IndexError:
    print("Could not find required columns for policy analysis.")


# 4. Age Group Analysis
try: 
    plt.figure(figsize=(10, 6))
    age_col = [col for col in data.columns if "age" in col.lower()][0]
    sns.boxplot(data=data, x=age_col, y='Satisfaction_Score')
    plt.title("Remote Work Satisfaction by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Satisfaction Score")
    plt.tight_layout()
    plt.show()
except IndexError:
    print("Could not find age column or satisfaction score. Check your data.")

# 5. Remote Work Preference vs. Productivity
try:
    plt.figure(figsize=(10, 6))
    merged_data = data[[pref_col[0], productivity_col]].dropna()
    sns.countplot(data=merged_data, x=pref_col[0], hue=productivity_col)
    plt.xticks(rotation=90)
    plt.title("Remote Work Preference vs. Self-Reported Productivity")
    plt.xlabel("Remote Work Preference")
    plt.ylabel("Count")
    plt.legend(title="Productivity")
    plt.tight_layout()
    plt.show()
except IndexError:
    print("Could not find required columns for preference vs productivity analysis.")