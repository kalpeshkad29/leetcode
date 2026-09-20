# Write your MySQL query statement below
select d.driver_id,d.driver_name,
round(avg (case when month(t.trip_date) between 01 and 06 then t.distance_km/t.fuel_consumed end),2)
as first_half_avg,
round(avg (case when month(t.trip_date) between 07 and 12 then t.distance_km/t.fuel_consumed end),2)
as second_half_avg,
round(avg (case when month(t.trip_date) between 07 and 12 then t.distance_km/t.fuel_consumed end)
-
(avg (case when month(t.trip_date) between 01 and 06 then t.distance_km/t.fuel_consumed end)),2)
as efficiency_improvement
from drivers d join trips t
on d.driver_id=t.driver_id
group by d.driver_id,d.driver_name
HAVING
    COUNT(CASE WHEN MONTH(t.trip_date) BETWEEN 1 AND 6 THEN 1 END) > 0
    AND
    COUNT(CASE WHEN MONTH(t.trip_date) BETWEEN 7 AND 12 THEN 1 END) > 0
    AND
    AVG(CASE
            WHEN MONTH(t.trip_date) BETWEEN 7 AND 12
            THEN t.distance_km / t.fuel_consumed
        END)
    >
    AVG(CASE
            WHEN MONTH(t.trip_date) BETWEEN 1 AND 6
            THEN t.distance_km / t.fuel_consumed
        END)

ORDER BY efficiency_improvement DESC,d.driver_name ASC;
