# Swiggy Case Study

## 1. Find customers who have never ordered
```sql
SELECT u.user_id, u.name 
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE o.user_id IS NULL;
```

## 2. Average Price per Dish
```sql
SELECT f_name, AVG(price) AS avg_price_dish  
FROM menu 
INNER JOIN food ON menu.f_id = food.f_id
GROUP BY food.f_name;
```

## 3. Find the Top Restaurant in Terms of Number of Orders for a Given Month
```sql
SELECT r_id, 
       (SELECT r_name 
        FROM restaurants t2 
        WHERE t1.r_id = t2.r_id) AS restaurant_name,  
       COUNT(order_id) AS order_count 
FROM orders t1
WHERE MONTH(date) = 5
GROUP BY r_id 
ORDER BY order_count DESC
LIMIT 1;
```

## 4. Restaurants with Monthly Sales Greater Than x
```sql
SELECT r_name, 
       MONTHNAME(date) AS month_name, 
       SUM(amount) AS sales
FROM orders t1
INNER JOIN restaurants t2 ON t1.r_id = t2.r_id
GROUP BY r_name, MONTHNAME(date)
HAVING SUM(amount) > 1500;
```

## 5. Show All Orders with Order Details for a Particular Customer in a Particular Date Range
```sql
SELECT t1.order_id, 
       t1.amount, 
       t1.date, 
       t3.r_name, 
       t5.f_name, 
       t5.type
FROM orders t1 
INNER JOIN users t2 ON t1.user_id = t2.user_id
INNER JOIN restaurants t3 ON t1.r_id = t3.r_id
INNER JOIN order_details t4 ON t1.order_id = t4.order_id
INNER JOIN food t5 ON t4.f_id = t5.f_id
WHERE t2.name LIKE 'nitish' 
  AND (date BETWEEN '2022-05-10' AND '2022-06-29');
```

## 6. Find Restaurants with Max Repeated Customers
```sql
WITH cte AS (
  SELECT r_id, user_id, COUNT(order_id) AS order_count
  FROM orders 
  GROUP BY r_id, user_id
  HAVING COUNT(order_id) > 1
) 
SELECT rest.r_name, 
       COUNT(*) AS no_of_loyal_users 
FROM cte
INNER JOIN restaurants rest ON cte.r_id = rest.r_id
GROUP BY rest.r_name
ORDER BY no_of_loyal_users DESC
LIMIT 1;
```

## 7. Month Over Month Revenue Growth of Swiggy
```sql
SELECT month_name, 
       ((total_amount - LAG(total_amount) OVER (ORDER BY month_name DESC)) / total_amount) * 100 AS growth
FROM (
  SELECT MONTHNAME(date) AS month_name,
         SUM(amount) AS total_amount 
  FROM orders 
  GROUP BY MONTHNAME(date) 
  ORDER BY month_name DESC
) t;
```

## 8. Customer Favorite Food
```sql
WITH cte AS (
  SELECT t1.user_id, 
         t3.f_name, 
         COUNT(t3.f_name) AS food_order_frequency
  FROM orders t1 
  INNER JOIN order_details t2 ON t1.order_id = t2.order_id
  INNER JOIN food t3 ON t2.f_id = t3.f_id
  GROUP BY t1.user_id, t3.f_name
) 
SELECT name, 
       f_name,  
       food_order_frequency 
FROM (
  SELECT *, 
         DENSE_RANK() OVER (PARTITION BY user_id ORDER BY food_order_frequency DESC) AS rank_no
  FROM cte
) t
INNER JOIN users ON t.user_id = users.user_id
WHERE rank_no = 1;
```

## 9. Find the Most Loyal Customers for All Restaurants
```sql
WITH cte AS (
  SELECT r_id, 
         user_id, 
         COUNT(*) AS order_frequency 
  FROM orders 
  GROUP BY r_id, user_id
) 
SELECT t2.r_name, 
       t3.name, 
       t1.order_frequency 
FROM cte t1 
INNER JOIN restaurants t2 ON t1.r_id = t2.r_id 
INNER JOIN users t3 ON t1.user_id = t3.user_id
WHERE t1.order_frequency = (
  SELECT MAX(order_frequency) 
  FROM cte t2 
  WHERE t1.r_id = t2.r_id
);
```

## 10. Month Over Month Revenue Growth of a Restaurant
```sql
WITH cte AS (
  SELECT MONTHNAME(date) AS month_name,
         SUM(amount) AS total_amount 
  FROM orders 
  WHERE r_id = 1
  GROUP BY MONTHNAME(date)
) 
SELECT *, 
       ROUND(((total_amount - LAG(total_amount) OVER (ORDER BY month_name DESC)) / total_amount) * 100) AS sales_growth
FROM cte;
```

## 11. Most Paired Products
```sql
WITH cte AS ( 
  SELECT t1.order_id, 
         t2.f_id 
  FROM orders t1 
  INNER JOIN order_details t2 ON t1.order_id = t2.order_id
) 
SELECT (SELECT f_name 
        FROM food 
        WHERE f_id = SUBSTRING_INDEX(paired_food, ' ', 1)) AS f1,
       (SELECT f_name 
        FROM food 
        WHERE f_id = SUBSTRING_INDEX(paired_food, ' ', -1)) AS f2,
       paired_food, 
       COUNT(paired_food)
FROM (
  SELECT t1.order_id, 
         t1.f_id AS f1, 
         t2.f_id AS f2, 
         CONCAT(t1.f_id, ' ', t2.f_id) AS paired_food 
  FROM cte t1
  INNER JOIN cte t2 ON t1.order_id = t2.order_id AND t1.f_id < t2.f_id
) t
GROUP BY paired_food 
LIMIT 1;
```