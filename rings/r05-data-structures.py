# Ring 5 — Data structures (1.5 hr)
# Run: python r05-data-structures.py
# Gate: one-line dict lookup works; list search needs a loop — difference visible.

customers = {1: "Ramesh", 2: "Suresh"}  # id -> name, one-line lookup
entries = [(1, "udhaar", 500), (2, "udhaar", 300)]  # ordered list

# Dict lookup: no loop needed
name = customers[1]

# List search: a loop is needed
count = 0
for c, kind, amt in entries:
    if c == 1:
        count = count + 1


# --- GATE: do not touch below, just run ---
assert name == "Ramesh"
assert count == 1, "customer 1 must have exactly 1 entry"
assert customers.get(99) is None, ".get() on a missing key must give None"
print("Ring 5 GATE: PASS")

# --- QUESTIONS (answer all correctly to enter Ring 6) ---
# Q1: To find a customer by id, list or dict? Why?
# Q2: When is a list the right choice over a dict?
# Q3: What is the difference between customers[99] and customers.get(99)?
