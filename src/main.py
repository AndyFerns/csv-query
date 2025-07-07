import argparse
from parser import parse_query
from loader import load_csv, get_columns, get_summary_stats
from filter import row_matches
from tabulate import format_output
from utils import export_to_csv, display_help, deduplicate_rows

import os

def interactive_mode(filename, output_format):
    print(f"Loaded '{filename}'. Enter your SQL-like queries.")
    print("Commands: \n - DESC\n - STATS\n - EXPORT <filename>\n - HELP\n - QUIT")
    data = load_csv(filename)
    last_result = []

    while True: #main interactive mode loop
        try:
            query = input("csvsql> ").strip()
            if not query:
                continue
            if query.upper() in ('EXIT', 'QUIT'):
                break
            elif query.upper() == 'DESC':
                print("Columns:", get_columns(filename))
                print(f"Total Rows: {len(data)}")
                continue
            elif query.upper() == 'STATS':
                print(get_summary_stats(data))
                continue
            elif query.upper() == 'HELP':
                display_help()
                continue 
            elif query.upper().startswith('EXPORT '):
                out_file = query.split(' ', 1)[1]
                if last_result:
                    export_to_csv(last_result['rows'], out_file, last_result['columns']) #type:ignore
                    print(f"Exported to '{out_file}'")
                else:
                    print("No result to export.")
                continue

            parsed = parse_query(query)
            columns = parsed['columns']
            condition = parsed['condition']
            order_by = parsed['order_by']
            limit = parsed['limit']
            distinct = parsed['distinct']

            filtered = [row for row in data if row_matches(row, condition)]

            if order_by:
                key, direction = order_by
                filtered.sort(key=lambda r: r.get(key), reverse=(direction == 'DESC')) #type:ignore

            if limit:
                filtered = filtered[:limit]

            if distinct:
                filtered = deduplicate_rows(filtered)

            if columns != ['*']:
                filtered = [{col: row.get(col, '') for col in columns} for row in filtered]
            else:
                columns = list(filtered[0].keys()) if filtered else []

            format_output(filtered, columns, output_format)
            last_result = {'rows': filtered, 'columns': columns}

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
