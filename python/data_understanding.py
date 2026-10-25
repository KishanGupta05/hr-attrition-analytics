## Dataset Understanding

import pandas as pd

df = pd.read_excel("Raw Data.xlsx")

print("Shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types and non-null counts:")
df.info()

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
print("Total Rows:", len(df))

print(
    "Unique Employee Numbers:",
    df["EmployeeNumber"].nunique()
)

print(
    "Duplicate Employee Numbers:",
    df["EmployeeNumber"].duplicated().sum()
)

print(
    "Missing Employee Numbers:",
    df["EmployeeNumber"].isna().sum()
)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
print("Attrition Counts:")
print(df["Attrition"].value_counts())

print("\nAttrition Percentages:")
print(
    df["Attrition"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
print("Column-wise Unique Values:\n")

for col in df.columns:
    print(
        f"{col}: "
        f"{df[col].nunique()} unique values"
    )

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

constant_columns = [
    "EmployeeCount",
    "Over18",
    "StandardHours"
]

for col in constant_columns:
    print(f"\n{col}")
    print(df[col].value_counts(dropna=False))



categorical_columns = [
    "Attrition",
    "BusinessTravel",
    "Department",
    "EducationField",
    "Gender",
    "JobRole",
    "MaritalStatus",
    "OverTime"
]

for col in categorical_columns:
    print(f"\n{col}:")
    print(df[col].value_counts(dropna=False))



#-------------------------------------------------------------------------------------------------------------------------------
##                                                              DATA CLEANING
#-------------------------------------------------------------------------------------------------------------------------------
# Check exact duplicate rows
duplicate_rows = df.duplicated().sum()

print("Exact Duplicate Rows:", duplicate_rows)
print(df.dtypes)


# Create a working copy
df_clean = df.copy()

# Identify constant columns
constant_columns = [
    "EmployeeCount",
    "Over18",
    "StandardHours"
]

# Remove constant columns from the working copy
df_clean = df_clean.drop(columns=constant_columns)

print("Original shape:", df.shape)
print("Cleaned shape:", df_clean.shape)

print("\nRemaining columns:")
print(df_clean.columns.tolist())


print("Missing values:", df_clean.isna().sum().sum())

print("Exact duplicate rows:", df_clean.duplicated().sum())

print(
    "Unique employee numbers:",
    df_clean["EmployeeNumber"].nunique()
)

print("Shape:", df_clean.shape)


##                          Numerical Data Validation

# Numerical Columns ka Statistical Summary
print(df_clean.describe().T)

## Business Logic Validate Karna
#A. Age Validation
print("Minimum Age:", df_clean["Age"].min())
print("Maximum Age:", df_clean["Age"].max())

print("\nAge below 18:")
print(df_clean[df_clean["Age"] < 18])

print("\nAge above 65:")
print(df_clean[df_clean["Age"] > 65])

#B. Income Validation
print("Minimum Monthly Income:", df_clean["MonthlyIncome"].min())

print(
    "Zero or Negative Income Records:",
    (df_clean["MonthlyIncome"] <= 0).sum()
)

#C. Tenure Consistency
invalid_tenure = df_clean[
    (df_clean["YearsInCurrentRole"] > df_clean["YearsAtCompany"]) |
    (df_clean["YearsAtCompany"] > df_clean["TotalWorkingYears"])
]

print("Potential Tenure Inconsistencies:", len(invalid_tenure))

print(
    invalid_tenure[
        [
            "EmployeeNumber",
            "TotalWorkingYears",
            "YearsAtCompany",
            "YearsInCurrentRole"
        ]
    ].head(10)
)

#D. Rating Range Validation
rating_columns = [
    "Education",
    "EnvironmentSatisfaction",
    "JobInvolvement",
    "JobLevel",
    "JobSatisfaction",
    "PerformanceRating",
    "RelationshipSatisfaction",
    "StockOptionLevel",
    "WorkLifeBalance"
]

for col in rating_columns:
    print(f"{col}: {sorted(df_clean[col].unique())}")


#-------------------------------------------------------------------------------------------------------------------------------
##                                      Outlier Investigation
#-------------------------------------------------------------------------------------------------------------------------------
# Columns to investigate
outlier_columns = [
    "MonthlyIncome",
    "Age",
    "YearsAtCompany"
]

for col in outlier_columns:
    Q1 = df_clean[col].quantile(0.25)
    Q3 = df_clean[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df_clean[
        (df_clean[col] < lower_bound) |
        (df_clean[col] > upper_bound)
    ]

    print(f"\nColumn: {col}")
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Potential Outliers:", len(outliers))



#-------------------------------------------------------------------------------------------------------------------------------
##                                     Kya High Income Senior Roles Se Related Hai?
#-------------------------------------------------------------------------------------------------------------------------------
#Step 1: High-income employees identify karo
# IQR upper bound for MonthlyIncome
Q1 = df_clean["MonthlyIncome"].quantile(0.25)
Q3 = df_clean["MonthlyIncome"].quantile(0.75)
IQR = Q3 - Q1

upper_bound = Q3 + 1.5 * IQR

high_income = df_clean[
    df_clean["MonthlyIncome"] > upper_bound
]

print("High-income employees:", len(high_income))

print("\nJob level distribution:")
print(high_income["JobLevel"].value_counts().sort_index())

print("\nJob role distribution:")
print(high_income["JobRole"].value_counts())

print("\nIncome summary:")
print(high_income["MonthlyIncome"].describe())


#Step 2: Tenure outliers investigate karo
# IQR upper bound for YearsAtCompany
Q1 = df_clean["YearsAtCompany"].quantile(0.25)
Q3 = df_clean["YearsAtCompany"].quantile(0.75)
IQR = Q3 - Q1

upper_bound = Q3 + 1.5 * IQR

long_tenure = df_clean[
    df_clean["YearsAtCompany"] > upper_bound
]

print("Long-tenure employees:", len(long_tenure))

print("\nJob level distribution:")
print(long_tenure["JobLevel"].value_counts().sort_index())

print("\nJob role distribution:")
print(long_tenure["JobRole"].value_counts())

print("\nTenure summary:")
print(long_tenure["YearsAtCompany"].describe())


#-------------------------------------------------------------------------------------------------------------------------------
##                                   Categorical Data Quality
#-------------------------------------------------------------------------------------------------------------------------------
categorical_columns = df_clean.select_dtypes(
    include=["str", "object", "category"]
).columns

for col in categorical_columns:
    print(f"\n{col}")
    print("Unique values:", df_clean[col].nunique())

    print("Leading/trailing spaces:",
          df_clean[col].astype("string").str.strip().ne(
              df_clean[col].astype("string")
          ).sum())


##
expected_categories = {
    "Attrition": {"Yes", "No"},
    "BusinessTravel": {
        "Travel_Rarely",
        "Travel_Frequently",
        "Non-Travel"
    },
    "Department": {
        "Sales",
        "Research & Development",
        "Human Resources"
    },
    "Gender": {"Male", "Female"},
    "OverTime": {"Yes", "No"},
    "MaritalStatus": {
        "Single",
        "Married",
        "Divorced"
    }
}

for col, expected in expected_categories.items():
    actual = set(df_clean[col].dropna().unique())

    unexpected = actual - expected
    missing_categories = expected - actual

    print(f"\nColumn: {col}")
    print("Unexpected categories:", unexpected)
    print("Expected categories not observed:", missing_categories)

print("Hello")
## 
remaining_categories = {
    "EducationField": {
        "Life Sciences",
        "Medical",
        "Marketing",
        "Technical Degree",
        "Other",
        "Human Resources"
    },
    "JobRole": {
        "Sales Executive",
        "Research Scientist",
        "Laboratory Technician",
        "Manufacturing Director",
        "Healthcare Representative",
        "Manager",
        "Sales Representative",
        "Research Director",
        "Human Resources"
    }
}

for col, expected in remaining_categories.items():
    actual = set(df_clean[col].dropna().unique())

    print(f"\nColumn: {col}")
    print("Unexpected categories:", actual - expected)
    print("Expected categories not observed:", expected - actual)

##
print("Final Shape:", df_clean.shape)

print("Total Missing Values:", df_clean.isna().sum().sum())

print("Exact Duplicate Rows:", df_clean.duplicated().sum())

print(
    "Unique Employee Numbers:",
    df_clean["EmployeeNumber"].nunique()
)

print(
    "Overall Attrition Rate:",
    round((df_clean["Attrition"] == "Yes").mean() * 100, 2),
    "%"
)

##
# Save cleaned dataset as CSV
df_clean.to_csv(
    "HR_Attrition_Cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully!")
print("Final shape:", df_clean.shape)
