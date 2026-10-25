CREATE TABLE hr_attrition (
    age INTEGER,
    attrition VARCHAR(3),
    businesstravel VARCHAR(30),
    dailyrate INTEGER,
    department VARCHAR(50),
    distancefromhome INTEGER,
    education INTEGER,
    educationfield VARCHAR(50),
    employeenumber INTEGER PRIMARY KEY,
    environmentsatisfaction INTEGER,
    gender VARCHAR(20),
    hourlyrate INTEGER,
    jobinvolvement INTEGER,
    joblevel INTEGER,
    jobrole VARCHAR(60),
    jobsatisfaction INTEGER,
    maritalstatus VARCHAR(30),
    monthlyincome NUMERIC(10,2),
    monthlyrate INTEGER,
    numcompaniesworked INTEGER,
    overtime VARCHAR(3),
    percentsalaryhike INTEGER,
    performancerating INTEGER,
    relationshipsatisfaction INTEGER,
    stockoptionlevel INTEGER,
    totalworkingyears INTEGER,
    trainingtimeslastyear INTEGER,
    worklifebalance INTEGER,
    yearsatcompany INTEGER,
    yearsincurrentrole INTEGER,
    yearssincelastpromotion INTEGER,
    yearswithcurrmanager INTEGER
);
SELECT * FROM hr_attrition;


SELECT
    COUNT(*) AS total_employees,
    COUNT(DISTINCT employeenumber) AS unique_employee_ids,
    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,
    COUNT(*) FILTER (
        WHERE attrition = 'No'
    ) AS employees_stayed,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS attrition_rate_pct
FROM hr_attrition;

--Department-wise Attrition Analysis
SELECT
    department,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    COUNT(*) FILTER (
        WHERE attrition = 'No'
    ) AS employees_stayed,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY department

ORDER BY attrition_rate_pct DESC;


--Overtime vs Attrition
SELECT
    overtime,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    COUNT(*) FILTER (
        WHERE attrition = 'No'
    ) AS employees_stayed,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY overtime

ORDER BY attrition_rate_pct DESC;


--Job Role Wise Attrition
SELECT
    jobrole,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    COUNT(*) FILTER (
        WHERE attrition = 'No'
    ) AS employees_stayed,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY jobrole

ORDER BY attrition_rate_pct DESC;


--Age Group Wise Attrition
SELECT
    CASE
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        WHEN age BETWEEN 56 AND 60 THEN '56-60'
        ELSE 'Other'
    END AS age_group,

    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    COUNT(*) FILTER (
        WHERE attrition = 'No'
    ) AS employees_stayed,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY
    CASE
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        WHEN age BETWEEN 56 AND 60 THEN '56-60'
        ELSE 'Other'
    END

ORDER BY
    MIN(age);


--Job Satisfaction VS Attrition
SELECT
    jobsatisfaction,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    COUNT(*) FILTER (
        WHERE attrition = 'No'
    ) AS employees_stayed,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY jobsatisfaction

ORDER BY jobsatisfaction;


--Work Life Balance Vs Attrion
SELECT
    worklifebalance,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    COUNT(*) FILTER (
        WHERE attrition = 'No'
    ) AS employees_stayed,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY worklifebalance

ORDER BY worklifebalance;


--Years at Company vs Attrition
SELECT
    CASE
        WHEN yearsatcompany BETWEEN 0 AND 1 THEN '0-1 Years'
        WHEN yearsatcompany BETWEEN 2 AND 3 THEN '2-3 Years'
        WHEN yearsatcompany BETWEEN 4 AND 5 THEN '4-5 Years'
        WHEN yearsatcompany BETWEEN 6 AND 10 THEN '6-10 Years'
        WHEN yearsatcompany BETWEEN 11 AND 20 THEN '11-20 Years'
        ELSE '20+ Years'
    END AS tenure_group,

    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    COUNT(*) FILTER (
        WHERE attrition = 'No'
    ) AS employees_stayed,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY
    CASE
        WHEN yearsatcompany BETWEEN 0 AND 1 THEN '0-1 Years'
        WHEN yearsatcompany BETWEEN 2 AND 3 THEN '2-3 Years'
        WHEN yearsatcompany BETWEEN 4 AND 5 THEN '4-5 Years'
        WHEN yearsatcompany BETWEEN 6 AND 10 THEN '6-10 Years'
        WHEN yearsatcompany BETWEEN 11 AND 20 THEN '11-20 Years'
        ELSE '20+ Years'
    END

ORDER BY
    MIN(yearsatcompany);


--Age Group × Tenure Group
SELECT
    CASE
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        WHEN age BETWEEN 56 AND 60 THEN '56-60'
        ELSE 'Other'
    END AS age_group,

    CASE
        WHEN yearsatcompany BETWEEN 0 AND 1 THEN '0-1 Years'
        WHEN yearsatcompany BETWEEN 2 AND 3 THEN '2-3 Years'
        WHEN yearsatcompany BETWEEN 4 AND 5 THEN '4-5 Years'
        WHEN yearsatcompany BETWEEN 6 AND 10 THEN '6-10 Years'
        WHEN yearsatcompany BETWEEN 11 AND 20 THEN '11-20 Years'
        ELSE '20+ Years'
    END AS tenure_group,

    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY
    CASE
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        WHEN age BETWEEN 56 AND 60 THEN '56-60'
        ELSE 'Other'
    END,

    CASE
        WHEN yearsatcompany BETWEEN 0 AND 1 THEN '0-1 Years'
        WHEN yearsatcompany BETWEEN 2 AND 3 THEN '2-3 Years'
        WHEN yearsatcompany BETWEEN 4 AND 5 THEN '4-5 Years'
        WHEN yearsatcompany BETWEEN 6 AND 10 THEN '6-10 Years'
        WHEN yearsatcompany BETWEEN 11 AND 20 THEN '11-20 Years'
        ELSE '20+ Years'
    END

ORDER BY
    MIN(age),
    MIN(yearsatcompany);


--Monthly Income vs Attrition
SELECT
    attrition,
    COUNT(*) AS total_employees,

    ROUND(AVG(monthlyincome), 2) AS avg_monthly_income,

    PERCENTILE_CONT(0.5)
        WITHIN GROUP (
            ORDER BY monthlyincome
        ) AS median_monthly_income,

    MIN(monthlyincome) AS min_monthly_income,

    MAX(monthlyincome) AS max_monthly_income

FROM hr_attrition

GROUP BY attrition

ORDER BY attrition;


--Job Level vs Attrition
SELECT
    joblevel,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct,

    ROUND(
        AVG(monthlyincome),
        2
    ) AS avg_monthly_income

FROM hr_attrition

GROUP BY joblevel

ORDER BY joblevel;


--Business Travel vs Attrition
SELECT
    businesstravel,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    COUNT(*) FILTER (
        WHERE attrition = 'No'
    ) AS employees_stayed,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY businesstravel

ORDER BY attrition_rate_pct DESC;


--Marital Status vs Attrition
SELECT
    maritalstatus,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    COUNT(*) FILTER (
        WHERE attrition = 'No'
    ) AS employees_stayed,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY maritalstatus

ORDER BY attrition_rate_pct DESC;


--Overtime × Job Role
SELECT
    jobrole,
    overtime,

    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct

FROM hr_attrition

GROUP BY
    jobrole,
    overtime

ORDER BY
    jobrole,
    overtime;


--Salary Hike vs Attrition
SELECT
    attrition,

    COUNT(*) AS total_employees,

    ROUND(
        AVG(percentsalaryhike),
        2
    ) AS avg_salary_hike_pct,

    PERCENTILE_CONT(0.5)
        WITHIN GROUP (
            ORDER BY percentsalaryhike
        ) AS median_salary_hike_pct,

    MIN(percentsalaryhike) AS min_salary_hike_pct,

    MAX(percentsalaryhike) AS max_salary_hike_pct

FROM hr_attrition

GROUP BY attrition

ORDER BY attrition;


--Years Since Last Promotion vs Attrition
SELECT
    attrition,

    COUNT(*) AS total_employees,

    ROUND(
        AVG(yearssincelastpromotion),
        2
    ) AS avg_years_since_promotion,

    PERCENTILE_CONT(0.5)
        WITHIN GROUP (
            ORDER BY yearssincelastpromotion
        ) AS median_years_since_promotion,

    MIN(yearssincelastpromotion) AS min_years_since_promotion,

    MAX(yearssincelastpromotion) AS max_years_since_promotion

FROM hr_attrition

GROUP BY attrition

ORDER BY attrition;


-------------------------------------------------------------------------------------------------------------------------
												--SQL Summary Query
-------------------------------------------------------------------------------------------------------------------------
WITH overall_summary AS (
    SELECT
        COUNT(*) AS total_employees,

        COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) AS employees_left,

        COUNT(*) FILTER (
            WHERE attrition = 'No'
        ) AS employees_stayed,

        ROUND(
            100.0 * COUNT(*) FILTER (
                WHERE attrition = 'Yes'
            ) / NULLIF(COUNT(*), 0),
            2
        ) AS overall_attrition_rate_pct

    FROM hr_attrition
),

overtime_summary AS (
    SELECT
        ROUND(
            100.0 * COUNT(*) FILTER (
                WHERE attrition = 'Yes'
            ) / NULLIF(COUNT(*), 0),
            2
        ) AS overtime_yes_attrition_rate_pct

    FROM hr_attrition
    WHERE overtime = 'Yes'
),

no_overtime_summary AS (
    SELECT
        ROUND(
            100.0 * COUNT(*) FILTER (
                WHERE attrition = 'Yes'
            ) / NULLIF(COUNT(*), 0),
            2
        ) AS overtime_no_attrition_rate_pct

    FROM hr_attrition
    WHERE overtime = 'No'
),

department_summary AS (
    SELECT
        department,
        COUNT(*) AS total_employees,

        COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) AS employees_left,

        ROUND(
            100.0 * COUNT(*) FILTER (
                WHERE attrition = 'Yes'
            ) / NULLIF(COUNT(*), 0),
            2
        ) AS attrition_rate_pct

    FROM hr_attrition
    GROUP BY department
),

jobrole_summary AS (
    SELECT
        jobrole,
        COUNT(*) AS total_employees,

        COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) AS employees_left,

        ROUND(
            100.0 * COUNT(*) FILTER (
                WHERE attrition = 'Yes'
            ) / NULLIF(COUNT(*), 0),
            2
        ) AS attrition_rate_pct

    FROM hr_attrition
    GROUP BY jobrole
)

SELECT
    o.total_employees,
    o.employees_left,
    o.employees_stayed,
    o.overall_attrition_rate_pct,

    ot.overtime_yes_attrition_rate_pct,
    no_ot.overtime_no_attrition_rate_pct,

    d.department AS highest_attrition_department,
    d.attrition_rate_pct AS department_attrition_rate_pct,

    j.jobrole AS highest_attrition_jobrole,
    j.attrition_rate_pct AS jobrole_attrition_rate_pct

FROM overall_summary o

CROSS JOIN overtime_summary ot

CROSS JOIN no_overtime_summary no_ot

CROSS JOIN (
    SELECT *
    FROM department_summary
    ORDER BY attrition_rate_pct DESC
    LIMIT 1
) d

CROSS JOIN (
    SELECT *
    FROM jobrole_summary
    ORDER BY attrition_rate_pct DESC
    LIMIT 1
) j;
