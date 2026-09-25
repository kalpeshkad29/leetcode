# Write your MySQL query statement below
SELECT
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(
        MIN(n.test_date),
        pos.first_positive
    ) AS recovery_time
FROM patients p
JOIN
(
    SELECT
        patient_id,
        MIN(test_date) AS first_positive
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
) pos
ON p.patient_id = pos.patient_id
JOIN covid_tests n
ON pos.patient_id = n.patient_id
AND n.result = 'Negative'
AND n.test_date > pos.first_positive
GROUP BY
    p.patient_id,
    p.patient_name,
    p.age,
    pos.first_positive
ORDER BY
    recovery_time,
    p.patient_name;