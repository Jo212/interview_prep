## 🔄 When to Use CTEs

- When you have complex logic and need to make your queries more readable.
- When you need to reuse the result of the query multiple times within the same query.
- When you are working with recursive queries (e.g., hierarchical data).

---

## 🔄 When to Use Subqueries

- For simple, one-off queries where you don’t need to reference the same result set multiple times.
- When you don’t need the overhead of a `WITH` clause and want the query to be more concise.

---

## 🏎️ Performance Considerations

- Subqueries are typically faster when they are optimized well by the database engine because they are often executed only once for each row or value.
- CTEs can sometimes be slower, especially in large datasets, because some database engines materialize CTEs — meaning the temporary result is stored in memory before being used. This can add overhead.
- However, modern database engines often optimize CTEs and in some cases treat them like subqueries, inlining them for performance.

---

## 📈 Example of Performance Difference

### 1. CTE Example

```sql
WITH DeptStats AS (
  SELECT department, COUNT(*) AS total_employees
  FROM employees
  GROUP BY department
)
SELECT e.name, e.department
FROM employees e
JOIN DeptStats ds ON e.department = ds.department
WHERE ds.total_employees > 50;
```
### 2. Subquery Example

```sql
SELECT e.name, e.department
FROM employees e
WHERE (
  SELECT COUNT(*) 
  FROM employees 
  WHERE department = e.department
) > 50;
