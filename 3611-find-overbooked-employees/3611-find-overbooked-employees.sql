# Write your MySQL query statement below
select e.employee_id,e.employee_name,e.department,count(*) as meeting_heavy_weeks
from employees e 
join
(select employee_id,YEARWEEK(meeting_date,1) as week_no from meetings group by employee_id,YEARWEEK(meeting_date,1) having sum(duration_hours)>20) t
on e.employee_id=t.employee_id
group by 
e.employee_id,
e.employee_name,
e.department
having count(*)>=2
order by meeting_heavy_weeks desc,e.employee_name asc;
