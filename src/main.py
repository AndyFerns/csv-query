import sys
from parser import parse_query
from loader import load_csv
from filter import row_matches
from tabulate import format_output

def run_query(query):
    columns, filename, condition = parse_query(query)
    rows = load_csv(filename)
    filtered = [row for row in rows if row_matches(row, condition)]
    if columns != ['*']:
        filtered = [{col: row.get(col, '') for col in columns} for row in filtered]
    format_output(filtered, columns)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py \"SELECT col1 FROM file.csv WHERE col2 > 5\"")
        sys.exit(1)

    try:
        query = sys.argv[1]
        run_query(query)
    except Exception as e:
        print(f"[Error] {e}")
