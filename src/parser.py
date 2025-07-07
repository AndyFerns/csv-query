import re

def parse_query(query):
    pattern = r'SELECT (DISTINCT )?(.+?) FROM (\S+)(?: WHERE (.+?))?(?: ORDER BY (.+?))?(?: LIMIT (\d+))?$'
    match = re.match(pattern, query.strip(), re.IGNORECASE)
    if not match:
        raise ValueError("Invalid query format. Use: SELECT [DISTINCT] col1, col2 FROM file.csv WHERE col3 > 10 ORDER BY col4 DESC LIMIT 5")

    distinct_flag, columns, filename, condition, order_by, limit = match.groups()
    columns = [col.strip() for col in columns.split(',')] if columns.strip() != '*' else ['*']
    order = None

    if order_by:
        parts = order_by.strip().split()
        order = (parts[0], parts[1].upper() if len(parts) > 1 else 'ASC')

    return {
        'distinct': bool(distinct_flag),
        'columns': columns,
        'filename': filename,
        'condition': condition,
        'order_by': order,
        'limit': int(limit) if limit else None
    }
