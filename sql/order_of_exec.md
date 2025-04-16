| Step | Clause         | Description                                 |
|------|----------------|---------------------------------------------|
| 1️⃣   | `FROM`         | Get and join tables/data sources.           |
| 2️⃣   | `ON`           | Filter rows based on join condition (if applicable). |
| 3️⃣   | `JOIN`         | Combine rows from multiple tables.          |
| 4️⃣   | `WHERE`        | Filter rows (before grouping).              |
| 5️⃣   | `GROUP BY`     | Group rows based on one or more columns.    |
| 6️⃣   | `HAVING`       | Filter groups (after grouping).             |
| 7️⃣   | `SELECT`       | Return the selected columns/expressions.    |
| 8️⃣   | `DISTINCT`     | Remove duplicate rows.                      |
| 9️⃣   | `ORDER BY`     | Sort the result set.                        |
| 🔟   | `LIMIT / OFFSET` | Return a subset of the results.             |


### **Example:**

```
SELECT department, COUNT(*) as num_employees
FROM employees
WHERE active = true
GROUP BY department
HAVING COUNT(*) > 5
ORDER BY num_employees DESC
LIMIT 10;
```

Execution flow:

    Get data from employees → FROM

    Filter only active employees → WHERE

    Group by department → GROUP BY

    Filter groups with >5 employees → HAVING

    Count and select fields → SELECT

    Sort by employee count → ORDER BY

    Return top 10 → LIMIT


