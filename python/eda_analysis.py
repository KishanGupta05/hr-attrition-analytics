#-------------------------------------------------------------------------------------------------------------------------------
#                                       Department-wise Attrition Analysis
#-------------------------------------------------------------------------------------------------------------------------------

import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("HR_Attrition_Cleaned.csv")

# Calculate department-wise employee count
department_analysis = df.groupby("Department").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

# Calculate attrition rate
department_analysis["Attrition_Rate_%"] = (
    department_analysis["Employees_Left"]
    / department_analysis["Total_Employees"]
    * 100
)

# Calculate the overall company attrition rate
overall_attrition_rate = (df["Attrition"] == "Yes").mean() * 100

# Calculate difference from company baseline
department_analysis["Difference_vs_Company_pp"] = (
    department_analysis["Attrition_Rate_%"]
    - overall_attrition_rate
)

# Sort departments by attrition rate
department_analysis = department_analysis.sort_values(
    "Attrition_Rate_%",
    ascending=False
)

print("Overall Company Attrition Rate:",
      round(overall_attrition_rate, 2), "%")

print("\nDepartment-wise Attrition Analysis:")

print(department_analysis.round(2))

#-------------------------------------------------------------------------------------------------------------------------------
#                                       Attrition by Overtime
#-------------------------------------------------------------------------------------------------------------------------------


# Employee count and attrition by overtime status
overtime_analysis = df.groupby("OverTime").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

# Calculate attrition rate
overtime_analysis["Attrition_Rate_%"] = (
    overtime_analysis["Employees_Left"]
    / overtime_analysis["Total_Employees"]
    * 100
)

# Sort for readability
overtime_analysis = overtime_analysis.sort_values(
    "Attrition_Rate_%",
    ascending=False
)

print("Attrition Analysis by Overtime:")
print(overtime_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                       Attrition by Job Satisfaction
#-------------------------------------------------------------------------------------------------------------------------------
# Attrition Analysis by Job Satisfaction

satisfaction_analysis = df.groupby("JobSatisfaction").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

satisfaction_analysis["Attrition_Rate_%"] = (
    satisfaction_analysis["Employees_Left"]
    / satisfaction_analysis["Total_Employees"] * 100
)

print("Attrition Analysis by Job Satisfaction:")
print(satisfaction_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                      Attrition by Work-Life Balance
#-------------------------------------------------------------------------------------------------------------------------------
# Attrition Analysis by Work-Life Balance

worklife_analysis = df.groupby("WorkLifeBalance").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

worklife_analysis["Attrition_Rate_%"] = (
    worklife_analysis["Employees_Left"]
    / worklife_analysis["Total_Employees"] * 100
)

print("Attrition Analysis by Work-Life Balance:")
print(worklife_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                      Attrition by Job Role
#-------------------------------------------------------------------------------------------------------------------------------
# Attrition Analysis by Job Role

jobrole_analysis = df.groupby("JobRole").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

jobrole_analysis["Attrition_Rate_%"] = (
    jobrole_analysis["Employees_Left"]
    / jobrole_analysis["Total_Employees"] * 100
)

jobrole_analysis = jobrole_analysis.sort_values(
    "Attrition_Rate_%",
    ascending=False
)

print("Attrition Analysis by Job Role:")
print(jobrole_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                      Attrition by Age Group
#-------------------------------------------------------------------------------------------------------------------------------
# Create age groups

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56-60"
    ]
)
age_analysis = df.groupby("AgeGroup", observed=False).agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

age_analysis["Attrition_Rate_%"] = (
    age_analysis["Employees_Left"]
    / age_analysis["Total_Employees"] * 100
)

print("Attrition Analysis by Age Group:")
print(age_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                      Attrition by Years at company
#-------------------------------------------------------------------------------------------------------------------------------
# Tenure groups create kar
df["TenureGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[-1, 1, 3, 5, 10, 20, float("inf")],
    labels=[
        "0-1 Years",
        "2-3 Years",
        "4-5 Years",
        "6-10 Years",
        "11-20 Years",
        "20+ Years"
    ]
)
#Attrition Rate calculate kar
tenure_analysis = df.groupby(
    "TenureGroup",
    observed=False
).agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

tenure_analysis["Attrition_Rate_%"] = (
    tenure_analysis["Employees_Left"]
    / tenure_analysis["Total_Employees"] * 100
)

print("Attrition Analysis by Years at Company:")
print(tenure_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                      Age Group X Tenure Group
#-------------------------------------------------------------------------------------------------------------------------------
# Attrition analysis by Age Group and Tenure Group

age_tenure_analysis = df.pivot_table(
    index="AgeGroup",
    columns="TenureGroup",
    values="Attrition",
    aggfunc=lambda x: (x == "Yes").mean() * 100,
    observed=False
)

print("Attrition Rate (%) by Age Group and Tenure Group:")
print(age_tenure_analysis.round(2))

# Employee counts by Age Group and Tenure Group

age_tenure_counts = df.pivot_table(
    index="AgeGroup",
    columns="TenureGroup",
    values="EmployeeNumber",
    aggfunc="count",
    observed=False,
    fill_value=0
)

print("Employee Count by Age Group and Tenure Group:")
print(age_tenure_counts)

# Employees who left by Age Group and Tenure Group

age_tenure_left = df[df["Attrition"] == "Yes"].pivot_table(
    index="AgeGroup",
    columns="TenureGroup",
    values="EmployeeNumber",
    aggfunc="count",
    observed=False,
    fill_value=0
)

print("Employees Left by Age Group and Tenure Group:")
print(age_tenure_left)


#-------------------------------------------------------------------------------------------------------------------------------
#                                      Monthly Income vs Attrition
#-------------------------------------------------------------------------------------------------------------------------------
# Monthly Income vs Attrition

income_analysis = df.groupby("Attrition")["MonthlyIncome"].agg(
    Employee_Count="count",
    Average_Income="mean",
    Median_Income="median",
    Minimum_Income="min",
    Maximum_Income="max"
)

print("Monthly Income Analysis by Attrition:")
print(income_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                     Job Level X Attrition
#-------------------------------------------------------------------------------------------------------------------------------
job_level_analysis = df.groupby("JobLevel").agg(
    Employee_Count=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum()),
    Average_Income=("MonthlyIncome", "mean")
)

job_level_analysis["Attrition_Rate"] = (
    job_level_analysis["Employees_Left"]
    / job_level_analysis["Employee_Count"]
    * 100
)

print(job_level_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                     Job Level X Attrition + Income
#-------------------------------------------------------------------------------------------------------------------------------
job_role_income = df.groupby(
    ["JobRole", "Attrition"]
).agg(
    Employee_Count=("EmployeeNumber", "count"),
    Average_Income=("MonthlyIncome", "mean")
).round(2)

print(job_role_income)


#-------------------------------------------------------------------------------------------------------------------------------
#                                   Job  Role Attrition Rate
#-------------------------------------------------------------------------------------------------------------------------------
job_role_attrition = df.groupby("JobRole").agg(
    Employee_Count=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

job_role_attrition["Attrition_Rate"] = (
    job_role_attrition["Employees_Left"]
    / job_role_attrition["Employee_Count"]
    * 100
)

job_role_attrition = job_role_attrition.sort_values(
    "Attrition_Rate",
    ascending=False
)

print(job_role_attrition.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                    Overtime X Job Role
#-------------------------------------------------------------------------------------------------------------------------------
overtime_role_analysis = df.pivot_table(
    index="JobRole",
    columns="OverTime",
    values="Attrition",
    aggfunc=lambda x: (x == "Yes").mean() * 100,
    observed=False
)

print("Attrition Rate by Job Role and Overtime:")
print(overtime_role_analysis.round(2))

##
overtime_role_counts = df.pivot_table(
    index="JobRole",
    columns="OverTime",
    values="EmployeeNumber",
    aggfunc="count",
    observed=False,
    fill_value=0
)

overtime_role_left = df[df["Attrition"] == "Yes"].pivot_table(
    index="JobRole",
    columns="OverTime",
    values="EmployeeNumber",
    aggfunc="count",
    observed=False,
    fill_value=0
)

print("Employee Count by Job Role and Overtime:")
print(overtime_role_counts)

print("\nEmployees Who Left by Job Role and Overtime:")
print(overtime_role_left)


#-------------------------------------------------------------------------------------------------------------------------------
#                                   Business Travel X Attrition
#-------------------------------------------------------------------------------------------------------------------------------
travel_analysis = df.groupby("BusinessTravel").agg(
    Employee_Count=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

travel_analysis["Attrition_Rate"] = (
    travel_analysis["Employees_Left"]
    / travel_analysis["Employee_Count"]
    * 100
)

print(travel_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                   Marital Status X Attrition
#-------------------------------------------------------------------------------------------------------------------------------

marital_analysis = df.groupby("MaritalStatus").agg(
    Employee_Count=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

marital_analysis["Attrition_Rate"] = (
    marital_analysis["Employees_Left"]
    / marital_analysis["Employee_Count"]
    * 100
)

print(marital_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                   PercentSalaryHike X Attrition
#-------------------------------------------------------------------------------------------------------------------------------
salary_hike_analysis = df.groupby("Attrition")["PercentSalaryHike"].agg(
    Employee_Count="count",
    Average_Hike="mean",
    Median_Hike="median"
)

print(salary_hike_analysis.round(2))


#-------------------------------------------------------------------------------------------------------------------------------
#                                  Year Since Last Promotion X Attrition
#-------------------------------------------------------------------------------------------------------------------------------
promotion_analysis = df.groupby("Attrition")[
    "YearsSinceLastPromotion"
].agg(
    Employee_Count="count",
    Average_Years="mean",
    Median_Years="median"
)

print(promotion_analysis.round(2))