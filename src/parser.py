import re

def parse_query(query):
    pattern = r'SELECT (.+) FROM (\S+)(?: WHERE (.+))?'
    match = re.match(pattern, query.strip(), re.IGNORECASE)
    if not match:
        raise ValueError("Invalid query format. Use: SELECT col1, col2 FROM file.csv WHERE condition")

    columns, filename, condition = match.groups()
    columns = [col.strip() for col in columns.split(',')] if columns.strip() != '*' else ['*']
    return columns, filename, condition
