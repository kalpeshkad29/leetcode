# Write your MySQL query statement below
select 
l.book_id,l.title,l.author,l.genre,l.publication_year,
sum(case when b.return_date is null then 1 else 0 end ) as current_borrowers
from 
library_books l join borrowing_records b
on l.book_id=b.book_id
group by l.book_id,l.title,l.author,l.genre,l.publication_year,l.total_copies
having current_borrowers=l.total_copies
order by current_borrowers desc , l.title asc;