
# Pizza Runner Case Study

## Database Creation

```sql
CREATE DATABASE pizza_runner;
USE pizza_runner;
```

## Loading Dataset

### Runners Table
```sql
DROP TABLE IF EXISTS runners;
CREATE TABLE runners (
  runner_id INTEGER,
  registration_date DATE
);

INSERT INTO runners
  (runner_id, registration_date)
VALUES
  (1, '2021-01-01'),
  (2, '2021-01-03'),
  (3, '2021-01-08'),
  (4, '2021-01-15');
```

### Customer Orders Table
```sql
DROP TABLE IF EXISTS customer_orders;
CREATE TABLE customer_orders (
  order_id INTEGER,
  customer_id INTEGER,
  pizza_id INTEGER,
  exclusions VARCHAR(4),
  extras VARCHAR(4),
  order_time TIMESTAMP
);

INSERT INTO customer_orders
  (order_id, customer_id, pizza_id, exclusions, extras, order_time)
VALUES
  (1, 101, 1, '', '', '2020-01-01 18:05:02'),
  (2, 101, 1, '', '', '2020-01-01 19:00:52'),
  (3, 102, 1, '', '', '2020-01-02 23:51:23'),
  (3, 102, 2, '', NULL, '2020-01-02 23:51:23'),
  (4, 103, 1, '4', '', '2020-01-04 13:23:46'),
  (4, 103, 1, '4', '', '2020-01-04 13:23:46'),
  (4, 103, 2, '4', '', '2020-01-04 13:23:46'),
  (5, 104, 1, 'null', '1', '2020-01-08 21:00:29'),
  (6, 101, 2, 'null', 'null', '2020-01-08 21:03:13'),
  (7, 105, 2, 'null', '1', '2020-01-08 21:20:29'),
  (8, 102, 1, 'null', 'null', '2020-01-09 23:54:33'),
  (9, 103, 1, '4', '1, 5', '2020-01-10 11:22:59'),
  (10, 104, 1, 'null', 'null', '2020-01-11 18:34:49'),
  (10, 104, 1, '2, 6', '1, 4', '2020-01-11 18:34:49');
```

### Runner Orders Table
```sql
DROP TABLE IF EXISTS runner_orders;
CREATE TABLE runner_orders (
  order_id INTEGER,
  runner_id INTEGER,
  pickup_time VARCHAR(19),
  distance VARCHAR(7),
  duration VARCHAR(10),
  cancellation VARCHAR(23)
);

INSERT INTO runner_orders
  (order_id, runner_id, pickup_time, distance, duration, cancellation)
VALUES
  (1, 1, '2020-01-01 18:15:34', '20km', '32 minutes', ''),
  (2, 1, '2020-01-01 19:10:54', '20km', '27 minutes', ''),
  (3, 1, '2020-01-03 00:12:37', '13.4km', '20 mins', NULL),
  (4, 2, '2020-01-04 13:53:03', '23.4', '40', NULL),
  (5, 3, '2020-01-08 21:10:57', '10', '15', NULL),
  (6, 3, 'null', 'null', 'null', 'Restaurant Cancellation'),
  (7, 2, '2020-01-08 21:30:45', '25km', '25mins', 'null'),
  (8, 2, '2020-01-10 00:15:02', '23.4 km', '15 minute', 'null'),
  (9, 2, 'null', 'null', 'null', 'Customer Cancellation'),
  (10, 1, '2020-01-11 18:50:20', '10km', '10minutes', 'null');
```

### Pizza Names Table
```sql
DROP TABLE IF EXISTS pizza_names;
CREATE TABLE pizza_names (
  pizza_id INTEGER,
  pizza_name TEXT
);

INSERT INTO pizza_names
  (pizza_id, pizza_name)
VALUES
  (1, 'Meatlovers'),
  (2, 'Vegetarian');
```

### Pizza Recipes Table
```sql
DROP TABLE IF EXISTS pizza_recipes;
CREATE TABLE pizza_recipes (
  pizza_id INTEGER,
  toppings TEXT
);
INSERT INTO pizza_recipes
  (pizza_id, toppings)
VALUES
  (1, '1, 2, 3, 4, 5, 6, 8, 10'),
  (2, '4, 6, 7, 9, 11, 12');
```

### Pizza Toppings Table
```sql
DROP TABLE IF EXISTS pizza_toppings;
CREATE TABLE pizza_toppings (
  topping_id INTEGER,
  topping_name TEXT
);

INSERT INTO pizza_toppings
  (topping_id, topping_name)
VALUES
  (1, 'Bacon'),
  (2, 'BBQ Sauce'),
  (3, 'Beef'),
  (4, 'Cheese'),
  (5, 'Chicken'),
  (6, 'Mushrooms'),
  (7, 'Onions'),
  (8, 'Pepperoni'),
  (9, 'Peppers'),
  (10, 'Salami'),
  (11, 'Tomatoes'),
  (12, 'Tomato Sauce');
```

## Data Cleaning

### Customer Orders Table
```sql
-- setting sql_safe_updates = 0 to perform updates 
SET sql_safe_updates = 0;

-- updating 'null' or '' text with NULL values in exclusions column  
UPDATE customer_orders
SET exclusions = NULL 
WHERE exclusions = 'null' OR exclusions = '';

-- updating 'null' or '' text with NULL values in extras column
UPDATE customer_orders
SET extras = NULL 
WHERE extras = 'null' OR extras = '';
```

### Runner Orders Table
```sql
-- replacing 'null' text with NULL in pickup_time column 
UPDATE runner_orders 
SET pickup_time = NULL 
WHERE pickup_time = 'null';

-- replacing 'null' text with NULL in distance column 
UPDATE runner_orders 
SET distance = NULL 
WHERE distance = 'null';

-- replacing 'km' and ' km' with '' in distance column 
UPDATE runner_orders
SET distance =  REPLACE(distance , ' km' , '');

UPDATE runner_orders
SET distance =  REPLACE(distance , 'km' , '');

-- changing data type varchar(7) to float in distance column 
DESC runner_orders;

ALTER TABLE runner_orders 
MODIFY distance FLOAT; 

-- modification on duration column 

-- replacing 'null' text with NULL
UPDATE runner_orders
SET duration = NULL 
WHERE duration = 'null';

-- splitting at 'm' character
UPDATE runner_orders 
SET duration = SUBSTRING_INDEX(duration , 'm',1);

-- replacing ' ' with '' 
UPDATE runner_orders 
SET duration = REPLACE(duration , ' ' ,'');

-- changing data type from varchar(7) to int 
DESC runner_orders;

ALTER TABLE runner_orders 
MODIFY duration INT;

-- cancellation column 
UPDATE runner_orders 
SET cancellation = NULL 
WHERE cancellation = 'null' OR cancellation = '';

-- setting sql_safe_updates back to 1
SET sql_safe_updates = 1;
```

### Pizza Toppings (Optional)
Here is a Python code snippet to convert row values into a column for better understanding and easy use case purposes in pandas:

```python
import pandas as pd

df = pd.read_csv('/content/pizza_recipes.csv')
df['toppings'] = df.toppings.str.split(',') 
newdf = df.explode('toppings') 
newdf.to_csv('pizza_recipes_cleaned.csv')
```

## A. Pizza Metrics

### 1. How many pizzas were ordered?
```sql
SELECT COUNT(*) pizza_order_count FROM customer_orders;
```

### 2. How many unique customer orders were made?
```sql
SELECT COUNT(DISTINCT order_id) AS unique_orders FROM customer_orders;
```

### 3. How many successful orders were delivered by each runner?
```sql
SELECT runner_id, COUNT(DISTINCT t1.order_id) AS order_count 
FROM customer_orders t1
INNER JOIN runner_orders t2 
ON t1.order_id = t2.order_id
WHERE t2.cancellation IS NULL
GROUP BY runner_id;
```

### 4. How many of each type of pizza was delivered?
```sql
SELECT pizza_name, COUNT(*) AS pizza_count
FROM customer_orders t1
INNER JOIN runner_orders t2 
ON t1.order_id = t2.order_id
INNER JOIN pizza_names t3 
ON t1.pizza_id = t3.pizza_id
WHERE cancellation IS NULL
GROUP BY pizza_name;
```

### 5. How many Vegetarian and Meatlovers were ordered by each customer?
```sql
SELECT t1.customer_id, pizza

_name, COUNT(*) AS pizza_count
FROM customer_orders t1
INNER JOIN pizza_names t2 
ON t1.pizza_id = t2.pizza_id
GROUP BY t1.customer_id, t2.pizza_name;
```

### 6. What was the maximum number of pizzas delivered in a single order?
```sql
SELECT MAX(counts) as max_pizzas_ordered
FROM
  (SELECT order_id, COUNT(*) as counts
   FROM customer_orders 
   GROUP BY order_id) t;
```

### 7. For each customer, how many delivered pizzas had at least 1 change and how many had no changes?
```sql
SELECT customer_id,
SUM(
  CASE 
    WHEN (exclusions IS NOT NULL OR extras IS NOT NULL)
    THEN 1 ELSE 0 END) AS pizzas_with_changes,
SUM(
  CASE 
    WHEN (exclusions IS NULL AND extras IS NULL)
    THEN 1 ELSE 0 END) AS pizzas_without_changes
FROM customer_orders t1
INNER JOIN runner_orders t2 
ON t1.order_id = t2.order_id
WHERE t2.cancellation IS NULL
GROUP BY customer_id;
```

### 8. How many pizzas were delivered that had both exclusions and extras?
```sql
SELECT COUNT(*) AS pizzas_with_exclusions_and_extras
FROM customer_orders t1
INNER JOIN runner_orders t2 
ON t1.order_id = t2.order_id
WHERE exclusions IS NOT NULL 
AND extras IS NOT NULL
AND cancellation IS NULL;
```

## B. Runner and Customer Experience

### 1. How many runners signed up for each 1 week period? (i.e. how many runners signed up every week)
```sql
SELECT DATE_FORMAT(registration_date, '%Y-%v') AS week, 
COUNT(runner_id) AS runners 
FROM runners
GROUP BY week
ORDER BY week;
```

### 2. What was the average time in minutes it took for each runner to arrive at the Pizza Runner HQ to pick up the order?
```sql
SELECT runner_id, ROUND(AVG(duration)) AS avg_duration
FROM runner_orders
WHERE duration IS NOT NULL
GROUP BY runner_id;
```

### 3. Is there any relationship between the number of pizzas and how long the order takes to prepare?
```sql
SELECT COUNT(order_id) as pizza_count, ROUND(AVG(duration)) as avg_duration
FROM customer_orders t1
JOIN runner_orders t2
ON t1.order_id = t2.order_id
WHERE duration IS NOT NULL
GROUP BY pizza_count
ORDER BY pizza_count;
```

### 4. What was the average distance traveled for each customer?
```sql
SELECT t1.customer_id, ROUND(AVG(distance),2) AS avg_distance
FROM customer_orders t1
INNER JOIN runner_orders t2 
ON t1.order_id = t2.order_id
WHERE distance IS NOT NULL
GROUP BY customer_id;
```

### 5. What was the difference between the longest and shortest delivery times for all orders?
```sql
SELECT (MAX(duration) - MIN(duration)) AS time_difference
FROM runner_orders
WHERE duration IS NOT NULL;
```

### 6. What was the average speed for each runner for each delivery and do you notice any trend for these values?
```sql
SELECT runner_id, 
ROUND(AVG(distance / duration), 2) AS avg_speed
FROM runner_orders
WHERE distance IS NOT NULL AND duration IS NOT NULL
GROUP BY runner_id;
```

### 7. What is the successful delivery percentage for each runner?
```sql
SELECT runner_id, 
CONCAT(ROUND((SUM(
  CASE WHEN cancellation IS NULL
  THEN 1 ELSE 0 END) / COUNT(*)) * 100, 2), '%') AS success_rate
FROM runner_orders
GROUP BY runner_id;
```

# Pizza Runner Case Study

## C. Ingredient Optimisation

### 1. What are the standard ingredients for each pizza?

```sql
WITH cte AS (
  SELECT pizza_name, topping_name 
  FROM pizza_recipes_cleaned t1 
  INNER JOIN pizza_toppings t2 ON t1.toppings = t2.topping_id
  INNER JOIN pizza_names t3 ON t1.pizza_id = t3.pizza_id
) 
SELECT pizza_name, GROUP_CONCAT(topping_name) AS standard_ingredients 
FROM cte
GROUP BY pizza_name;
```

### 2. What was the most commonly added extra?

```sql
WITH cte AS (
  SELECT pizza_id, extras, COUNT(extras) AS cnt, 
  DENSE_RANK() OVER (PARTITION BY pizza_id ORDER BY COUNT(extras) DESC) AS rank_no
  FROM customer_orders_exploded 
  WHERE extras IS NOT NULL
  GROUP BY pizza_id, extras
) 
SELECT pizza_name, extras, topping_name AS commonly_added_extras 
FROM cte AS t1
INNER JOIN pizza_names t2 ON t1.pizza_id = t2.pizza_id 
INNER JOIN pizza_toppings t3 ON t1.extras = t3.topping_id
WHERE rank_no = 1;
```

### 3. What was the most common exclusion?

```sql
WITH cte AS (
  SELECT exclusions, COUNT(exclusions) AS cnt, 
  DENSE_RANK() OVER (ORDER BY COUNT(exclusions) DESC) AS rank_no
  FROM customer_orders_exploded 
  WHERE exclusions IS NOT NULL
  GROUP BY exclusions
) 
SELECT exclusions, topping_name AS commonly_removed_toppings  
FROM cte AS t1
INNER JOIN pizza_toppings t3 ON t1.exclusions = t3.topping_id
ORDER BY cnt DESC;
```

### 4. Generate an order item for each record in the customer_orders table in the format of one of the following:

#### MEAT LOVERS

```sql
SELECT DISTINCT order_id
FROM customer_orders t1 
INNER JOIN pizza_names t2 ON t1.pizza_id = t2.pizza_id
WHERE t2.pizza_name = 'Meatlovers';
```

#### Meat Lovers - Exclude Beef

```sql
SELECT DISTINCT order_id
FROM customer_orders_exploded t1 
INNER JOIN pizza_names t2 ON t1.pizza_id = t2.pizza_id
WHERE t2.pizza_name = 'Meatlovers' AND exclusions = 3;
```

#### Meat Lovers - Extra Bacon

```sql
SELECT DISTINCT order_id
FROM customer_orders_exploded t1 
INNER JOIN pizza_names t2 ON t1.pizza_id = t2.pizza_id
WHERE t2.pizza_name = 'Meatlovers' AND (extras = 1 OR extras LIKE '%1%');
```

#### Meat Lovers - Exclude Cheese, Bacon - Extra Mushroom, Peppers

```sql
SELECT DISTINCT order_id
FROM customer_orders_exploded t1 
INNER JOIN pizza_names t2 ON t1.pizza_id = t2.pizza_id
WHERE t2.pizza_name = 'Meatlovers' AND exclusions IN (1, 4) AND extras IN (6, 9);
```

### 5. Generate an alphabetically ordered comma-separated ingredient list for each pizza order from the customer_orders table and add a 2x in front of any relevant ingredients

```sql
SELECT pizza_name, GROUP_CONCAT(topping_name ORDER BY topping_name) AS ingredients
FROM pizza_names t1 
INNER JOIN pizza_recipes_cleaned t2 ON t1.pizza_id = t2.pizza_id 
INNER JOIN pizza_toppings t3 ON t2.toppings = t3.topping_id 
GROUP BY pizza_name;
```

## D. Pricing and Ratings

### 1. If a Meat Lovers pizza costs $12 and Vegetarian costs $10 and there were no charges for changes - how much money has Pizza Runner made so far if there are no delivery fees?

```sql
SELECT SUM(total_earning) AS money_made 
FROM (
  SELECT runner_id, 
    SUM(CASE 
      WHEN pizza_id = 1 THEN 12 
      ELSE 10
    END) AS total_earning
  FROM customer_orders t1 
  INNER JOIN runner_orders t2 ON t1.order_id = t2.order_id
  WHERE cancellation IS NULL
  GROUP BY runner_id
) t;
```

### 2. What if there was an additional $1 charge for any pizza extras?

```sql
WITH cte AS (
  SELECT *, 
    SUBSTRING_INDEX(extras, ',', 1) AS extras1,
    CASE 
      WHEN extras IS NOT NULL AND extras LIKE '%,%' THEN SUBSTRING_INDEX(extras, ',', -1)
    END AS extras2,
    CASE 
      WHEN pizza_id = 1 THEN 12
      ELSE 10
    END AS base_pizza_cost
)
SELECT SUM(total_cost) AS total 
FROM (
  SELECT *, 
    CASE 
      WHEN (extras1 IS NOT NULL) AND (extras2 IS NOT NULL) THEN base_pizza_cost + 2 
      WHEN (extras1 IS NOT NULL) AND (extras2 IS NULL) THEN base_pizza_cost + 1
      WHEN (extras1 IS NULL) AND (extras2 IS NOT NULL) THEN base_pizza_cost + 1
      ELSE base_pizza_cost
    END AS total_cost
  FROM cte
) t;
```

### 5. If a Meat Lovers pizza was $12 and Vegetarian $10 fixed prices with no cost for extras and each runner is paid $0.30 per kilometre traveled - how much money does Pizza Runner have left over after these deliveries?

```sql
WITH cte AS (
  SELECT runner_id, 
    CASE 
      WHEN pizza_id = 1 THEN 12 
      ELSE 10 
    END AS pizza_base_price,
    ROUND(distance * 0.3) AS km_cost
  FROM customer_orders t1 
  INNER JOIN runner_orders t2 ON t1.order_id = t2.order_id
  WHERE cancellation IS NULL
) 
SELECT SUM(pizza_base_price) - SUM(km_cost) AS profit 
FROM cte;
```
