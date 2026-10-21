import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

df = pd.read_csv(
   "c:/Users/Muneer/Downloads/student_performance_100.csv"
)


print("Data shape:",df.shape)
print("Columns:",df.columns.tolist())
print(df.head())


average_marks = df["Average_Marks"].mean()
print("Class average marks", round(average_marks,2))


top_students = df.sort_values(
    by = "Total_Marks",
    ascending = False
).head(10)
print(top_students[["Name","Total_Marks","Average_Marks"]])


higher_attendance = df[df["Attendance_Percent"]>80]

higher_attendance = higher_attendance.sort_values(
    by ="Attendance_Percent",ascending =False
).head(10)

print(higher_attendance[["Name","Attendance_Percent","Average_Marks"]
                        ]
      )


subjects = [
    "Math_Marks",
    "Science_Marks",
    "English_Marks"
]

for subject in subjects:
    average = df[subject].mean()
    
    print(subject,"Average:",round(average,2))
    
    


subjects = [
    "Math_Marks",
    "Science_Marks",
    "English_Marks"
]
subject_averages = {}

for subject in subjects:
    
    average = df[subject].mean()
    subject_averages[subject] = average
print("Subject averages:",subject_averages)
highest_subject = max(subject_averages,key=subject_averages.get)

lowest_subject = min(subject_averages,key=subject_averages.get)

print("Highest average subject:",highest_subject)
print("Highest average marks:",round(subject_averages[highest_subject],2))
print("Lowest average subject:",lowest_subject)
print("lowest average subject:",round(subject_averages[lowest_subject],2))



subjects = list(subject_averages.keys())
averages = list(subject_averages.values())
plt.bar(subjects, averages)

for i, marks in enumerate(averages):
    plt.text(i, float(marks) + 1, f"{float(marks):.2f}", ha="center")

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

math_top_students = df[df["Math_Marks"]>80]

math_to_students =math_top_students.sort_values(
    by = "Math_Marks",ascending = False
)

print(math_top_students[["Name","Math_Marks"]])



top_attendance_wale = df[(df["Attendance_Percent"]>=80) & (df["Average_Marks"]>75)]
                         
                         
top_attendance_wale = top_attendance_wale.sort_values(
    by ="Average_Marks",ascending = False
)

print(top_attendance_wale[["Name","Attendance_Percent","Average_Marks"]])



correlation =  df["Study_Hours_Per_Day"].corr(df["Average_Marks"])

print("Study hours per day-Average marks",correlation)

plt.scatter(
    df["Study_Hours_Per_Day"],
    df["Average_Marks"]
)

plt.xlabel("Study Hours Per Day")
plt.ylabel("Average Makrs")
plt.title("Study Hours vs Average Marks")



x = df["Study_Hours_Per_Day"]
y = df["Average_Marks"]

m,b = np.polyfit(x,y,1)

plt.plot(x,m * x + b,label="Trend line")
plt.legend()
plt.show()


study_hours = 3

predicted_marks = m * study_hours + b

print("Pedicted average marks:",round(predicted_marks,2))


predicted_all = m * x + b

mae = np.mean(np.abs(y-predicted_all))

print("Mean Absolute Error:",round(mae,2))


correlation = df["Attendance_Percent"].corr(df["Average_Marks"])

print("Attendance vs Marks Correlation:",correlation)




plt.scatter(
    df["Attendance_Percent"],df["Average_Marks"]
)
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.title("Students average marks analysis based on attendance ")
plt.legend()
plt.show()



low_attendance = df[df["Attendance_Percent"]<75]
high_attendance =df[df["Attendance_Percent"]>=75]


group = ["Attedance <75%", "Attedance >=75%"]

average_marks =[
    low_attendance["Average_Marks"].mean(),
    
    high_attendance["Average_Marks"].mean()
]


plt.bar(group,average_marks)

plt.title("Attendace vs Average Marks")
plt.xlabel("Attendance  Group")
plt.ylabel("Average Marks")

for i, marks in enumerate(average_marks):
    plt.text(i,marks +1 ,f"{marks:.2f}",ha = "center")
    
plt.ylim(0,100)
plt.tight_layout()


plt.show()


differance = high_attendance["Average_Marks"].mean()-low_attendance["Average_Marks"].mean()
                                                                                                                                 

print("Differance in Average marks:",round(differance,2))



high_attendance_study = df[
    (df["Attendance_Percent"]>=75) &
    (df["Study_Hours_Per_Day"]>=3)
]  


print(high_attendance_study[["Name", "Attendance_Percent", "Study_Hours_Per_Day", "Average_Marks"]])



print("Total Students:",len(high_attendance_study))

print("Average Marks:",round(high_attendance_study["Average_Marks"].mean(),2))



low_attendance = df[df["Attendance_Percent"]<75]

high_att_low_study = df[
    (df["Attendance_Percent"]>=75) &
    (df["Study_Hours_Per_Day"]<3)
    
    
]


high_attendance_study = df[
    (df["Attendance_Percent"]>=75) &
    (df["Study_Hours_Per_Day"]>3)
]


groups = [
    "Attendance <75%",
    "high_attendance,\nStudy<3h",
    "High attendance,\nStudy >=3h"
]


averages = [
    low_attendance["Average_Marks"].mean(),
    high_att_low_study["Average_Marks"].mean(),
    high_attendance_study["Average_Marks"].mean()
    
    
]

plt.bar(groups,averages)
for i ,marks in enumerate(averages):
    plt.text(i,marks +1 ,f"{marks:.2f}",ha = "center")
    
    
plt.title("Attendance,Study hours vs Average Marks")
plt.ylabel("Average Marks")

plt.ylim(0,100)

plt.tight_layout()
plt.show()


duplicate_count = df.duplicated().sum()

print("Total duplicate rows :",duplicate_count)
missing_values =df.isnull().sum()

print("Missig values in each column:")
print(missing_values)