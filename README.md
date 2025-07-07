# 📊 CSV-Query 

A lightweight command-line SQL-like query engine for CSV files.

Inspired by MySQL's interactive shell, `csv-query` lets you load large CSV files and perform SQL-style queries like `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, and even `STATS` and `EXPORT`. It's perfect for ML engineers, data analysts, and developers who want a blazing-fast way to inspect and slice datasets directly from the terminal.

---

## 🚀 Features

- Interactive CLI: Run multiple queries in a MySQL-style REPL.
- SQL-like query support: `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`
- Dataset inspection: `DESC`, `STATS`, and `HELP` commands
- ML-focused features: Profiling, schema view, export results
- Output formatting: Pretty tables, JSON, and raw CSV
- Modular codebase for easy extension

---

## 📂 Folder Structure

```plaintext
csv query/
├── .gitignore
├── README.md
├── src/
│   ├── filter.py
│   ├── loader.py
│   ├── main.py
│   ├── parser.py
│   ├── tabulate.py
│   ├── utils.py
```


---

## 🛠 Installation

```bash
git clone https://github.com/AndyFerns/csv-query.git
cd csv-query
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py
csv-query> SELECT * FROM data.csv WHERE age > 30 ORDER BY name LIMIT 5;
csv-query> DESC;
csv-query> STATS;
csv-query> EXPORT output.csv;
csv-query> HELP;
csv-query> EXIT;
```

## Supported Commands

### SELECT Query

SQL-like query to filter and view data.

```sql
SELECT column1, column2 FROM file.csv WHERE condition ORDER BY column DESC LIMIT 10;
```

### WHERE Query

Supports logical and comparison operators

- `=`, `!=`, `<`, `>`, `<=`, `>=`

- `AND`, `OR`, `NOT`

### ORDER BY Query

Ascending (default) or DESC

### LIMIT modifier

Restrict number of output rows

## Example

```sql
SELECT name, salary FROM employees.csv WHERE salary > 50000 ORDER BY salary DESC LIMIT 10;
```

## 📦 Output Formats

Output defaults to a pretty table, but can be configured (future support) for:

- Table (default)

- JSON

- CSV string

## 💡 Features for ML/Data Engineers

- 📌 STATS command for quick profiling

- 🧹 DISTINCT to check cardinality and deduplication

- 🧮 Export filtered datasets for preprocessing

- 🧭 Interactive CLI for ad-hoc data exploration

- 🗂 DESC + HELP for quick schema and command reference

## 🤝 Contributing

Pull requests are welcome! Please document your code and follow the folder structure.

## 📄 License

MIT License. Feel free to fork, extend, and modify.

## 👨‍💻 Author

Made by AndyFerns
