import time
import csv

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
