# Write your MySQL query statement below
select u.name as name , sum(t.amount) as balance from Users u inner join Transactions t
on u.account=t.account
group by u.name
having balance>10000;