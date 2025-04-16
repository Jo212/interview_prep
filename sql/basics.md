# Difference Between `WHERE` and `HAVING` in SQL

## 📋 Comparison Table

| Feature              | `WHERE`                                 | `HAVING`                                 |
|----------------------|------------------------------------------|-------------------------------------------|
| **Purpose**          | Filters rows before grouping             | Filters groups after aggregation          |
| **Used With**        | `SELECT`, `UPDATE`, `DELETE`             | Typically used with `GROUP BY`            |
| **Applies To**       | Individual rows                          | Groups of rows                            |
| **Can Use Aggregates?** | ❌ No (e.g., `COUNT()`, `SUM()` not allowed) | ✅ Yes (e.g., `COUNT()`, `SUM()` allowed) |
| **Execution Order**  | Before grouping (`GROUP BY`)             | After grouping (`GROUP BY`)               |

---

## 🔄 SQL Query Execution Order

```text
1. FROM           -- Choose tables to query
2. JOIN           -- Apply joins
3. WHERE          -- Filter individual rows (no aggregates)
4. GROUP BY       -- Group remaining rows
5. HAVING         -- Filter groups (aggregates allowed)
6. SELECT         -- Select output columns
7. ORDER BY       -- Sort results
8. LIMIT/OFFSET   -- Return specific subset of results
---
```

## Example Using HAVING
```
SELECT department, COUNT(*) as total
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
```

# 🔔 Triggers in SQL

## ✅ What Is a Trigger?

A **trigger** in SQL is a set of instructions that automatically executes (or "fires") when a specific **event** occurs on a table or view.

---

## 🛠️ Use Cases for Triggers

- Auto-updating audit fields (e.g., `created_at`, `updated_at`)
- Logging changes to an audit table
- Enforcing complex business logic
- Validating or restricting changes
- Syncing data across tables

---

## 🧠 Types of Triggers

| **Trigger Timing** | **Event Type** | **Description**                          |
|--------------------|----------------|------------------------------------------|
| `BEFORE INSERT`    | Insert         | Runs before a new row is inserted        |
| `BEFORE UPDATE`    | Update         | Runs before a row is updated             |
| `BEFORE DELETE`    | Delete         | Runs before a row is deleted             |
| `AFTER INSERT`     | Insert         | Runs after a new row is inserted         |
| `AFTER UPDATE`     | Update         | Runs after a row is updated              |
| `AFTER DELETE`     | Delete         | Runs after a row is deleted              |

---

## 🧾 Basic Syntax (MySQL-style)

```sql
CREATE TRIGGER trigger_name
BEFORE INSERT ON table_name
FOR EACH ROW
BEGIN
  -- trigger logic here
END;

