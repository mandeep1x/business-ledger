# Ring 3 — Loops (1 hr)
# Run: python r03-loops.py
# entries = (customer_id, kind, amount). kind is "udhaar" or "payment".
# Gate: the loop balance must equal the hand-computed balance.

entries = [(1, "udhaar", 500), (1, "payment", 200), (1, "udhaar", 100), (1, "udhaar", 300)]

balance = 0
for cid, kind, amt in entries:
    # print(cid, kind, amt)
    if cid == 1:
        if kind == "udhaar":
            balance = balance + amt
        else:
            balance = balance - amt

print("balance:", balance)

# --- GATE: do not touch below, just run ---
assert balance == 700, "500 - 200 + 100 + 300 must equal 700"
print("Ring 3 GATE: PASS")

# --- QUESTIONS (answer all correctly to enter Ring 4) ---
# Q1: When do you use for, and when while?
# Q2: Why does a menu loop use `while True`?
# Q3: What does `for cid, kind, amt in entries` unpack on each round?
