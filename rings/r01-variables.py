# Ring 1 — Variables + print (30 min)
# Run: python r01-variables.py
# Gate: all three asserts green. One red = repeat Ring 1, do not advance.

# --- Your code goes here ---
customer_name = "Ramesh"
udhaar_amount = 500

bill_line = f"{customer_name} owes: Rs {udhaar_amount}"

print(bill_line)

# --- GATE: do not touch below, just run ---
assert customer_name == "Ramesh", "store the name in a variable"
assert udhaar_amount == 500, "store the amount in a variable"
assert bill_line == "Ramesh owes: Rs 500", "build bill_line with an f-string"
print("Ring 1 GATE: PASS")

# --- QUESTIONS (answer all correctly to enter Ring 2) ---
# Q1: What is a variable — a box or a label? Why?
# Q2: Why are curly braces {} needed inside an f-string?
# Q3: What happens if you use customer_name before assigning it?
