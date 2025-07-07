import json
import csv
import sys

def format_output(rows, columns, fmt='table'):
    if not rows:
        print("No results found.")
        return

    if fmt == 'json':
        print(json.dumps(rows, indent=2))
    elif fmt == 'csv':
        writer = csv.DictWriter(sys.stdout, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    else:
        col_widths = {col: max(len(col), max(len(str(row.get(col, ''))) for row in rows)) for col in columns}
        header = ' | '.join(f"{col:<{col_widths[col]}}" for col in columns)
        sep = '-+-'.join('-' * col_widths[col] for col in columns)
        print(header)
        print(sep)
        for row in rows:
            print(' | '.join(f"{str(row.get(col, '')):<{col_widths[col]}}" for col in columns))