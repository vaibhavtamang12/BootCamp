# GROUP BY, ORDER BY, HAVING BY
-- GROUP BY
-- In SQL, the GROUP BY clause is used to group rows that have the same values into summary rows.
use zomato;
desc orders;
-- A) GROUP BY using HAVING
SELECT age, COUNT(*) AS Number
FROM customers
GROUP BY age
HAVING age >= 0;

-- B) GROUP BY using CONCAT
-- Group Concat is used in MySQL to get concatenated values of expressions with more than one result per column.
SELECT OID, GROUP_CONCAT(DISTINCT status) AS Status
FROM orders
GROUP BY status;


-- ORDER BY
-- Ascending
SELECT *
FROM orders
ORDER BY cid ASC;

-- Descending
SELECT *
FROM orders
ORDER BY cid DESC;

-- HAVING BY
-- A) Find the products with amount greater than 200.
SELECT *
FROM payment
GROUP BY payment_mode
HAVING amount < 10;

