# Pizza Sales Case Study

## Creating Database for this Case Study
```sql
CREATE DATABASE pizza_sales;
USE pizza_sales;
```

## Changing Data Type of Date and Time
```sql
ALTER TABLE orders 
MODIFY date DATE;

ALTER TABLE orders 
MODIFY time TIME;
```

## Basic Queries

1. Retrieve the total number of orders placed.
    ```sql
    SELECT COUNT(*) AS order_placed FROM orders;
    ```

2. Calculate the total revenue generated from pizza sales.
    ```sql
    SELECT SUM(sales) AS total_revenue FROM (
        SELECT ROUND((t1.quantity * t2.price)) AS sales  
        FROM order_details t1 
        INNER JOIN pizzas t2 ON t1.pizza_id = t2.pizza_id
    ) t;
    ```

3. Identify the highest-priced pizza.
    ```sql
    SELECT pizza_id AS highest_priced_pizza, price 
    FROM pizzas 
    WHERE price = (SELECT MAX(price) FROM pizzas);
    ```

4. Identify the most common pizza size ordered.
    ```sql
    SELECT size, COUNT(*) AS order_frequency 
    FROM order_details t1
    INNER JOIN pizzas t2 ON t1.pizza_id = t2.pizza_id
    GROUP BY size 
    ORDER BY order_frequency DESC 
    LIMIT 1;
    ```

5. List the top 5 most ordered pizza types along with their quantities.
    ```sql
    SELECT t3.pizza_type_id, SUM(t1.quantity) AS total_quantity
    FROM order_details t1
    INNER JOIN pizzas t2 ON t1.pizza_id = t2.pizza_id 
    INNER JOIN pizza_types t3 ON t2.pizza_type_id = t3.pizza_type_id 
    GROUP BY t3.pizza_type_id
    ORDER BY total_quantity DESC
    LIMIT 5;
    ```

## Intermediate Queries

6. Join the necessary tables to find the total quantity of each pizza category ordered.
    ```sql
    SELECT t3.category, SUM(t1.quantity) AS total_quantity
    FROM order_details t1
    INNER JOIN pizzas t2 ON t1.pizza_id = t2.pizza_id 
    INNER JOIN pizza_types t3 ON t2.pizza_type_id = t3.pizza_type_id 
    GROUP BY t3.category;
    ```

7. Determine the distribution of orders by hour of the day.
    ```sql
    SELECT HOUR(time) AS hour_of_the_day, COUNT(*) AS order_count, 
    ROUND((COUNT(*) / (SELECT COUNT(*) FROM orders)) * 100) AS order_percent
    FROM orders 
    GROUP BY HOUR(time) 
    ORDER BY order_percent DESC;
    ```

8. Join relevant tables to find the category-wise distribution of pizzas.
    ```sql
    SELECT category, COUNT(*) AS no_of_diff_pizzas 
    FROM pizza_types t1
    INNER JOIN pizzas t2 ON t1.pizza_type_id = t2.pizza_type_id
    GROUP BY category;
    ```

9. Group the orders by date and calculate the average number of pizzas ordered per day.
    ```sql
    SELECT ROUND(AVG(order_count)) AS order_per_day 
    FROM (
        SELECT date, COUNT(*) AS order_count  
        FROM orders 
        GROUP BY date 
    ) t;
    ```

10. Determine the top 3 most ordered pizza types based on revenue.
    ```sql
    SELECT pizza_type_id, SUM(sales) AS revenue  
    FROM (
        SELECT pizza_type_id, ROUND(quantity * price) AS sales 
        FROM order_details t1 
        INNER JOIN pizzas t2 ON t1.pizza_id = t2.pizza_id 
    ) t
    GROUP BY pizza_type_id
    ORDER BY revenue DESC 
    LIMIT 3;
    ```

## Advanced Queries

11. Calculate the percentage contribution of each pizza type to total revenue.
    ```sql
    WITH cte AS (
        SELECT pizza_type_id, SUM(sales) AS revenue   
        FROM (
            SELECT pizza_type_id, ROUND(quantity * price) AS sales 
            FROM order_details t1 
            INNER JOIN pizzas t2 ON t1.pizza_id = t2.pizza_id 
        ) t
        GROUP BY pizza_type_id
    ) 
    SELECT pizza_type_id, 
    ROUND((revenue / (SELECT SUM(revenue) FROM cte)) * 100, 2) AS percent_sales 
    FROM cte;
    ```

12. Analyze the cumulative revenue generated over time.
    ```sql
    WITH cte AS (
        SELECT date, time, quantity * price AS sales
        FROM order_details t1 
        INNER JOIN orders t2 ON t1.order_id = t2.order_id
        INNER JOIN pizzas t3 ON t1.pizza_id = t3.pizza_id 
    ) 
    SELECT *, 
    ROUND(SUM(sales) OVER(ORDER BY date, time ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW), 2) AS cumulative_revenue
    FROM cte;
    ```

13. Determine the top 3 most ordered pizza types based on revenue for each pizza category.
    ```sql
    WITH cte AS (
        SELECT category, pizza_type_id, SUM(sales) AS revenue 
        FROM (
            SELECT category, t2.pizza_type_id, ROUND(quantity * price) AS sales 
            FROM order_details t1 
            INNER JOIN pizzas t2 ON t1.pizza_id = t2.pizza_id
            INNER JOIN pizza_types t3 ON t2.pizza_type_id = t3.pizza_type_id 
        ) t
        GROUP BY category, pizza_type_id 
    ) 
    SELECT * 
    FROM (
        SELECT *, DENSE_RANK() OVER(PARTITION BY category ORDER BY revenue DESC) AS rank_no 
        FROM cte 
    ) t1
    WHERE rank_no <= 3;
    ```

Let me know if you any error! 