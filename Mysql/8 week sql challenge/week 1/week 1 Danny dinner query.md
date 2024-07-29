
# Danny's Dinner Database

## Creating Database

```sql
CREATE DATABASE dannys_dinner;

USE dannys_dinner;
```

## Loading Dataset

### Sales Table

```sql
CREATE TABLE sales (
  customer_id VARCHAR(1),
  order_date DATE,
  product_id INTEGER
);

INSERT INTO sales (customer_id, order_date, product_id)
VALUES
  ('A', '2021-01-01', '1'),
  ('A', '2021-01-01', '2'),
  ('A', '2021-01-07', '2'),
  ('A', '2021-01-10', '3'),
  ('A', '2021-01-11', '3'),
  ('A', '2021-01-11', '3'),
  ('B', '2021-01-01', '2'),
  ('B', '2021-01-02', '2'),
  ('B', '2021-01-04', '1'),
  ('B', '2021-01-11', '1'),
  ('B', '2021-01-16', '3'),
  ('B', '2021-02-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-07', '3');
```

### Menu Table

```sql
CREATE TABLE menu (
  product_id INTEGER,
  product_name VARCHAR(5),
  price INTEGER
);

INSERT INTO menu (product_id, product_name, price)
VALUES
  ('1', 'sushi', '10'),
  ('2', 'curry', '15'),
  ('3', 'ramen', '12');
```

### Members Table

```sql
CREATE TABLE members (
  customer_id VARCHAR(1),
  join_date DATE
);

INSERT INTO members (customer_id, join_date)
VALUES
  ('A', '2021-01-07'),
  ('B', '2021-01-09');
```

## Case Study Questions

Each of the following case study questions can be answered using a single SQL statement:

1. **What is the total amount each customer spent at the restaurant?**

    ```sql
    SELECT customer_id, SUM(price) AS sales
    FROM sales t1
    INNER JOIN menu t2 ON t1.product_id = t2.product_id
    GROUP BY customer_id;
    ```

2. **How many days has each customer visited the restaurant?**

    ```sql
    SELECT customer_id, COUNT(DISTINCT order_date) AS day_visited
    FROM sales
    GROUP BY customer_id;
    ```

3. **What was the first item from the menu purchased by each customer?**

    ```sql
    SELECT customer_id, product_name
    FROM (
        SELECT customer_id, order_date,
        FIRST_VALUE(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS first_order_date,
        product_name
        FROM sales t1
        INNER JOIN menu t2 ON t1.product_id = t2.product_id
    ) t
    WHERE order_date = first_order_date;
    ```

4. **What is the most purchased item on the menu and how many times was it purchased by all customers?**

    ```sql
    SELECT product_name, COUNT(*) AS order_count
    FROM sales t1
    INNER JOIN menu t2 ON t1.product_id = t2.product_id
    GROUP BY product_name
    ORDER BY order_count DESC
    LIMIT 1;
    ```

5. **Which item was the most popular for each customer?**

    ```sql
    WITH cte AS (
        SELECT customer_id, product_name, COUNT(product_name) AS order_count
        FROM sales t1
        INNER JOIN menu t2 ON t1.product_id = t2.product_id
        GROUP BY customer_id, product_name
    ) 
    SELECT customer_id, product_name, order_count
    FROM (
        SELECT *, DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY order_count DESC) rank_no
        FROM cte
    ) t
    WHERE rank_no = 1;
    ```

6. **Which item was purchased first by the customer after they became a member?**

    ```sql
    WITH cte AS (
        SELECT t1.customer_id, product_name, order_date,
        DENSE_RANK() OVER (PARTITION BY t1.customer_id ORDER BY order_date) AS rank_no
        FROM sales t1
        INNER JOIN members t2 ON t1.customer_id = t2.customer_id AND t1.order_date >= t2.join_date
        INNER JOIN menu t3 ON t1.product_id = t3.product_id
    )
    SELECT customer_id, order_date, product_name
    FROM cte
    WHERE rank_no = 1;
    ```

7. **Which item was purchased just before the customer became a member?**

    ```sql
    WITH cte AS (
        SELECT t1.customer_id, product_name, order_date,
        DENSE_RANK() OVER (PARTITION BY t1.customer_id ORDER BY order_date DESC) AS rank_no
        FROM sales t1
        INNER JOIN members t2 ON t1.customer_id = t2.customer_id AND t1.order_date < t2.join_date
        INNER JOIN menu t3 ON t1.product_id = t3.product_id
    )
    SELECT customer_id, order_date, product_name
    FROM cte
    WHERE rank_no = 1;
    ```

8. **What is the total items and amount spent for each member before they became a member?**

    ```sql
    SELECT t1.customer_id, COUNT(t1.product_id) AS total_items, SUM(price) AS amount_spent
    FROM sales t1
    INNER JOIN members t2 ON t1.customer_id = t2.customer_id AND t1.order_date < t2.join_date
    INNER JOIN menu t3 ON t1.product_id = t3.product_id
    GROUP BY t1.customer_id;
    ```

9. **If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?**

    ```sql
    SELECT customer_id, SUM(points) AS total_points
    FROM (
        SELECT customer_id,
        (CASE
            WHEN product_name = 'sushi' THEN price * 20
            ELSE price * 10
        END) AS points
        FROM sales t1
        INNER JOIN menu t2 ON t1.product_id = t2.product_id
    ) t
    GROUP BY customer_id;
    ```

10. **In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?**

    ```sql
    SELECT customer_id, SUM(points) AS total_points
    FROM (
        SELECT t1.customer_id, order_date,
        CASE
            WHEN order_date - join_date BETWEEN 0 AND 6 THEN price * 20
            ELSE price * 10
        END AS points
        FROM sales t1
        INNER JOIN members t2 ON t1.customer_id = t2.customer_id
        INNER JOIN menu t3 ON t1.product_id = t3.product_id
        WHERE order_date < '2021-01-31'
    ) t
    GROUP BY customer_id;
    ```
