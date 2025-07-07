def format_output(rows, columns):
    if not rows:
        print("No results found.")
        return

    headers = rows[0].keys() if columns == ['*'] else columns
    col_widths = {col: max(len(str(col)), max(len(str(row.get(col, ''))) for row in rows)) for col in headers}

    # Header
    header_line = ' | '.join(f"{col:<{col_widths[col]}}" for col in headers)
    separator = '-+-'.join('-' * col_widths[col] for col in headers)
    print(header_line)
    print(separator)

    # Rows
    for row in rows:
        print(' | '.join(f"{str(row.get(col, '')):<{col_widths[col]}}" for col in headers))
