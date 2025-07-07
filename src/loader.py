import csv
import os

def load_csv(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def get_columns(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return next(reader)

def get_summary_stats(rows): #for distinct keyword
    import pandas as pd
    if not rows:
        return "No data."
    df = pd.DataFrame(rows)
    return df.describe(include='all').to_string()
