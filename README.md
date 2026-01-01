# SQL Beginner Challenge #15: Pattern Matching with LIKE

**Difficulty:** Beginner  
**Estimated time:** 10–15 minutes  
**Concepts:** `LIKE`, wildcard matching, text filtering  

This challenge introduces how to search and filter text in SQL using the `LIKE` operator—an essential technique for partial matches and search-style queries.

---

## 🧠 The Problem

A product manager asks:

> “Can we find all products whose names contain the word **USB**?”

Exact matches won’t work here.  
You need to filter text values based on a **pattern**, not the full value.

---

## 📊 Table Schema

### `products`

| Column Name | Type | Description |
|------------|------|-------------|
| product_id | INTEGER | Unique product ID |
| name | TEXT | Product name |
| category | TEXT | Product category |
| price | DECIMAL | Product price |

---

## 🧪 Sample Data

| product_id | name | category | price |
|-----------:|------|----------|------:|
| 101 | Wireless Mouse | Accessories | 24.99 |
| 102 | Mechanical Keyboard | Accessories | 89.00 |
| 103 | USB-C Hub | Accessories | 34.50 |
| 104 | USB Flash Drive | Accessories | 19.99 |
| 105 | Laptop Stand | Workspace | 39.99 |
| 106 | Webcam | Accessories | 59.99 |

---

## ✅ Requirements

Your query must:

- Return:
  - `name`
  - `price`
- Include only products whose name contains **USB**
- Use the `LIKE` operator
- Use wildcard characters (`%`)
- Not use `SELECT *`

---

## ✍️ Your Task

Write a SQL query that fulfills the requirements.

```sql
-- Write your query here

