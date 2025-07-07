import argparse
from parser import parse_query
from loader import load_csv, get_columns
from filter import row_matches
from tabulate import format_output
from utils import export_to_csv

import os

def interactive_mode(filename, output_format):
    print(f"Loaded '{filename}'. Enter your SQL-like queries. Type 'DESC' to inspect columns. Type 'EXIT' to quit.")
    data = load_csv(filename)

    while True:
        try:
            query = input("csvsql> ").strip()
            if query.upper() in ('EXIT', 'QUIT'):
                break
            if query.upper() == 'DESC':
                print("Columns:", get_columns(filename))
                print(f"Total Rows: {len(data)}")
                continue

            parsed = parse_query(query)
            columns = parsed['columns']
            condition = parsed['condition']
            order_by = parsed['order_by']
            limit = parsed['limit']

            filtered = [row for row in data if row_matches(row, condition)]

            if order_by:
                key, direction = order_by
                filtered.sort(key=lambda r: r.get(key), reverse=(direction == 'DESC')) #type: ignore

            if limit:
                filtered = filtered[:limit]

            if columns != ['*']:
                filtered = [{col: row.get(col, '') for col in columns} for row in filtered]
            else:
                columns = list(filtered[0].keys()) if filtered else []

            format_output(filtered, columns, output_format)

        except Exception as e:
            print(f"[Error] {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Query CSV files using SQL-like syntax.")
    parser.add_argument('file', help="CSV file to load")
    parser.add_argument('--format', choices=['table', 'json', 'csv'], default='table', help="Output format")
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"File '{args.file}' not found.")
    else:
        interactive_mode(args.file, args.format)
