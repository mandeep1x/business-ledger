# Ring 4 — Functions (1 hr)
# Run: python r04-functions.py
# Gate: the function version must produce the same output as inline code.

def add_udhaar(entries, cid, amount):
    entries.append((cid, "udhaar", amount))
    return entries

def balance(entries, cid):
    bal = 0
    for c, kind, amt in entries:
        if c == cid:
            if kind == "udhaar":
                bal = bal + amt
            else:
                bal = bal - amt
            # bal += amt if kind == "udhaar" else -amt
    return bal

entries = []
add_udhaar(entries, 1, 500)
add_udhaar(entries, 1, 100)
# add_udhaar(entries, 2, 750)

# x= balance(entries, 1)
# print(x)

# --- GATE: do not touch below, just run ---
assert balance(entries, 1) == 600
assert isinstance(entries, list)
print("Ring 4 GATE: PASS")

# --- QUESTIONS (answer all correctly to enter Ring 5) ---
# Q1: Why return a value instead of printing it inside the function?
# Q2: What is an argument, and what is a return value?
# Q3: What happens to `bal` after balance() finishes? Why?
