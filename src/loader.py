import csv

def load_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except Exception as e:
        raise RuntimeError(f"Error reading CSV: {e}")
