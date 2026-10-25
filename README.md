# HR Attrition Analytics

An end-to-end data analytics portfolio project exploring employee attrition patterns and translating findings into practical, evidence-informed HR recommendations.

> **Dataset note:** This project uses a fictional IBM-style HR analytics sample dataset. It is for learning and portfolio demonstration; it does not describe a real company's workforce.

## Project Overview

Employee attrition can affect workforce stability, recruitment costs, productivity, and team continuity. This project explores how attrition varies across employee groups, identifies patterns worth investigating, and communicates findings through SQL analysis and an interactive Power BI dashboard.

**Workflow:** Data Cleaning → EDA → PostgreSQL Analysis → Power BI Dashboard → Key Insights & Recommendations

## Business Questions

- What is the overall employee attrition rate?
- How does attrition vary by department and job role?
- Is attrition different for employees who work overtime?
- Which age and tenure groups show higher observed attrition rates?
- How are job satisfaction and work-life balance ratings associated with attrition?
- How do business travel, marital status, job level, and monthly income compare across attrition groups?
- What actions could HR teams investigate to improve retention?

## Tools & Technologies

- **Excel / Power Query** — data cleaning and preparation
- **PostgreSQL / SQL** — validation, aggregations, segmentation, and business analysis
- **Power BI** — interactive dashboard, DAX measures, KPI cards, charts, and slicers
- **PowerPoint** — key insights and recommendations presentation

## Dataset & Preparation

- Original dataset: **1,470 rows × 35 columns**
- Analysis dataset: **1,470 rows × 32 columns**
- Removed three constant/non-informative columns: `EmployeeCount`, `Over18`, and `StandardHours`
- Validated `EmployeeNumber` as unique across all 1,470 records
- No duplicate rows or missing values were found in the cleaned dataset
- Attrition outcome:
  - **Attrition = Yes:** 237 employees
  - **Attrition = No:** 1,233 employees
  - **Overall attrition rate:** 16.12%

## Key Findings

### 1. Overtime
- Employees marked as working overtime had an attrition rate of **30.53%**.
- Employees not marked as working overtime had an attrition rate of **10.44%**.
- This observed gap of **20.09 percentage points** suggests workload and overtime deserve further investigation.

### 2. Tenure & Age
- Employees with **0–1 years at the company** had an attrition rate of **34.88%**.
- The **18–25 age group** had an attrition rate of **35.77%**.
- The 18–25 age group with 0–1 years of tenure had a rate of **62.22% (28 of 45 employees)**. Because this is a small subgroup, interpret it cautiously.

### 3. Department & Job Role
- **Sales** had the highest department-level attrition rate at **20.63%**.
- **Sales Representatives** had the highest job-role attrition rate at **39.76%**.
- **Laboratory Technicians** had an attrition rate of **23.94%**.
- Rates and counts provide different perspectives: a smaller group can have a high rate, while a larger department can account for more exits overall.

### 4. Job Satisfaction & Work-Life Balance
- Job Satisfaction rating **1** had an attrition rate of **22.84%**, compared with **11.33%** for rating **4**.
- Work-Life Balance rating **1** had an attrition rate of **31.25%**. The pattern across ratings 2–4 was not monotonic, so avoid oversimplifying the relationship.

### 5. Business Travel & Marital Status
- **Travel Frequently:** 24.91% attrition
- **Travel Rarely:** 14.96% attrition
- **Non-Travel:** 8.00% attrition
- **Single:** 25.53% attrition
- **Married:** 12.48% attrition
- **Divorced:** 10.09% attrition

These are descriptive group differences, not proof that travel frequency or marital status causes attrition. Marital status should not be used to profile individuals or make adverse employment decisions.

### 6. Monthly Income & Job Level
- Average monthly income among employees who stayed: **6,832.74**
- Average monthly income among employees who left: **4,787.09**
- Job Level 1 had an attrition rate of **26.34%** and accounted for **143 of 237 exits**.

The dataset does not explicitly establish a currency in this analysis. Treat income values as relative values rather than assigning a currency symbol. These differences do not prove that income alone caused employees to leave.

## Power BI Dashboard

The report is organized into two pages.

### Page 1 — HR Attrition Overview
- KPI cards: Total Employees, Employees Left, Attrition Rate, Average Monthly Income
- Attrition rate by department
- Attrition rate by overtime
- Attrition rate by job role
- Attrition rate by age group
- Attrition rate by job satisfaction rating
- Slicers for department, age group, job role, and overtime

### Page 2 — Attrition Drivers Investigation
- Attrition rate by tenure group
- Attrition rate by work-life balance rating
- Attrition rate by marital status
- Attrition rate by job level
- Average monthly income by attrition outcome
- Attrition rate by business travel
- Slicers for tenure group, work-life balance, job level, marital status, and business travel

## Recommendations

These are hypotheses to validate with employee feedback and current organizational data—not guaranteed fixes.

1. **Review overtime and workload:** examine overtime hours, staffing, peak periods, and recovery time, especially in roles showing larger overtime-related differences.
2. **Strengthen early-tenure support:** introduce structured onboarding and 30/60/90-day check-ins, clarify role expectations, and consider buddy or mentoring support.
3. **Investigate role-specific challenges:** use confidential stay interviews and manager discussions with Sales Representatives and Laboratory Technicians.
4. **Improve employee listening:** use pulse surveys and qualitative feedback to understand satisfaction and work-life balance concerns.
5. **Review career development:** investigate training access, internal mobility, and progression clarity for Job Level 1 employees.
6. **Monitor travel demands:** examine trip frequency, schedule predictability, and recovery time for frequently travelling employees.
7. **Monitor outcomes:** track attrition rates and counts by role, tenure, department, overtime, and hiring cohort over time.

## Suggested Success Metrics

- Overall attrition and voluntary attrition rates (if exit reason is available)
- 90-day retention and first-year attrition by hiring cohort
- Attrition rate and headcount by department and job role
- Attrition by tenure, overtime, and travel frequency
- Employee pulse-survey results and onboarding feedback
- Internal mobility and training participation by job level

Record a baseline before implementing changes. Where feasible, compare pilot teams with similar non-pilot teams and monitor unintended effects.

## Project Limitations

- The dataset is fictional and may not reflect real workforce conditions.
- The analysis is descriptive and does not establish causation.
- Some subgroups are small, so their rates may be unstable.
- The dataset does not include all potentially relevant factors, such as detailed exit reasons or qualitative employee feedback.
- Recommendations should be validated before being applied in a real organization.


## Conclusion

This project demonstrates an end-to-end analytics workflow—from data quality checks and SQL-based segmentation to interactive Power BI reporting and business-focused recommendations. The central lesson is to use attrition patterns to guide better questions, validate potential explanations, and evaluate retention actions with evidence.

**Project category:** HR Analytics · Exploratory Data Analysis · SQL · Power BI · Business Insights
## 📊 Power BI Dashboard

The Power BI dashboard provides an interactive view of employee attrition patterns across different workforce segments.

### Dashboard Preview

#### Dashboard 1

![HR Attrition Dashboard 1](Screenshots/Dashboard%201.png)

#### Dashboard 2

![HR Attrition Dashboard 2](Screenshots/Dashboard%202.png)

### Interactive Analysis

The dashboard helps explore employee attrition across dimensions such as:

* Department and job role
* Age and tenure
* Overtime
* Job satisfaction and work-life balance
* Business travel and other employee characteristics

**Note:** Download the Power BI `.pbix` file from the `Dashboard` folder to explore the report in Power BI Desktop.

