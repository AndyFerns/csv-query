def row_matches(row, condition):
    if not condition:
        return True
    try:
        # Safe eval: Convert values to numeric if needed
        safe_row = {k: convert(v) for k, v in row.items()}
        return eval(condition, {}, safe_row)
    except Exception as e:
        raise ValueError(f"Error evaluating condition '{condition}' on row {row}:\n{e}")

def convert(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value.strip()
