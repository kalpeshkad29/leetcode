# Write your MySQL query statement below
select customer.customer_id from Customer inner join Product 
on Customer.product_key=Product.product_key 
group by Customer.customer_id 
having count(distinct(Customer.product_key))= (select count(Product.product_key) from Product);