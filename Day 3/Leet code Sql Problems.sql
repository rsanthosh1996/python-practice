--1193. Monthly Transactions I

SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY
    DATE_FORMAT(trans_date, '%Y-%m'),
    country;


--1174. Immediate Food Delivery II

SELECT
    ROUND(
        AVG(order_date = customer_pref_delivery_date) * 100,
        2
    ) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT
        customer_id,
        MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);


--550. Game Play Analysis IV

select
    round
    (count(distinct aa.player_id)/(select count(distinct player_id) from activity),2) as fraction
from Activity aa
join (select player_id,min(event_date) as first_date
from Activity
group by player_id)f
on f.player_id = aa.player_id
and aa.event_date = date_Add(f.first_date,interval 1 day)


--1934. Confirmation Rate

select 
e1.user_id,
round(avg(case when action = 'confirmed' then 1 else 0 end),2) as confirmation_rate
from Signups e1 
left join Confirmations e2 on e1.user_id = e2.user_id
group by e1.user_id


--570. Managers with at Least 5 Direct Reports
select e1.name  from Employee e1 
left join Employee e2 on e1.id = e2.managerId
group by e1.name having count(e2.name) >= 5 
