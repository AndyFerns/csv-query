import time
import csv
import hashlib

def export_to_csv(rows, filename, columns):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

def profile(stage_name):
    def decorator(fn):
        def wrapped(*args, **kwargs):
            start = time.time()
            result = fn(*args, **kwargs)
            print(f"[{stage_name}] Took {time.time() - start:.4f}s")
            return result
        return wrapped
    return decorator

def hash_row(row):
    return hashlib.md5(str(sorted(row.items())).encode()).hexdigest()

def deduplicate_rows(rows):
    seen = set()
    unique = []
    for row in rows:
        h = hash_row(row)
        if h not in seen:
            seen.add(h)
            unique.append(row)
    return unique

def display_help():
    """
    Prints the supported commands and usage in a styled ASCII box.
    """
    print("\n\033[96m" + "╔" + "═" * 46 + "╗")
    print("║{:^46}║".format("CSV-QUERY COMMANDS"))
    print("╚" + "═" * 46 + "╝\033[0m\n")

    print("\033[92m🟢 QUERY COMMANDS\033[0m")
    print("  SELECT ... FROM file.csv WHERE ... ORDER BY ... LIMIT ...")
    print("  SELECT DISTINCT column FROM file.csv")
    print("  DESC                     → View CSV column names and row count")
    print("  STATS                   → Summary statistics (mean, std, etc.)")
    print("  EXPORT filename.csv     → Save last query result")
    print("  EXIT or QUIT            → Exit the CLI\n")

    print("\033[93m🟡 MISC\033[0m")
    print("  HELP                    → Show this help screen\n")