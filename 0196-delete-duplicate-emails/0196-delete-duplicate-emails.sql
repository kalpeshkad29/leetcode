# Write your MySQL query statement below
delete e2 from Person e1,Person e2
where e1.email=e2.email
and e2.id>e1.id;
