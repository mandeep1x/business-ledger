# Ring 2 — Conditions (45 min)
# Run: python r02-conditions.py
# Gate: bad entries rejected, good entries pass. All green or repeat.

def is_valid_entry(name, amount, phone_number):
    if not name:
        return False
    if amount <= 0:
        return False
    if len(str(phone_number)) != 10:
        return False
    return True


# --- GATE: do not touch below, just run ---
assert is_valid_entry("Ramesh", 500, 8475451965) is True
assert is_valid_entry("", 500, 9501983027) is False, "empty name must be rejected"
assert is_valid_entry("Ramesh", 0, 78456542) is False, "zero due must be rejected"
assert is_valid_entry("Ramesh", -50, 4578564856) is False, "negative entry must be rejected"
assert is_valid_entry("Ramesh", -50, 95757846) is False, "negative entry must be rejected"
assert is_valid_entry("Ramesh", 500, 12345) is False, "5-digit phone must be rejected"
print("Ring 2 GATE: PASS")

# --- QUESTIONS (answer all correctly to enter Ring 3) ---
# Q1: When do you use elif instead of two separate if statements?
# Q2: What does `not name` catch that `name == ""` misses, if anything?
# Q3: Why return False early instead of one big condition at the end?
