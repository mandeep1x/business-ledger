# Ring 6 — OOP + Khata (2 hr, most important)
# Run: python r06-oop.py
# Gate: 2 customers + 4 entries through classes, correct balances.
# Then remove `self`, read the error, understand it.
# These same classes live in app/customer.py and app/khata.py.

class Customer:
    def __init__(self, cid, name, phone):
        self.id = cid
        self.name = name
        self.phone = phone


class Khata:
    def __init__(self):
        self.entries = []

    def add_udhaar(self, cid, amount):
        self.entries.append((cid, "udhaar", amount))

    def add_payment(self, cid, amount):
        self.entries.append((cid, "payment", amount))

    def balance(self, cid):
        bal = 0
        for c, kind, amt in self.entries:
            if c == cid:
                if kind == "udhaar":
                    bal= bal + amt
                else:
                    bal= bal - amt
            

                # bal += amt if kind == "udhaar" else -amt
        return bal

c1 = Customer(1, "Ramesh", "9999999999")
c2 = Customer(2, "Suresh", "8888888888")

k = Khata()
k.add_udhaar(1, 500)
k.add_udhaar(1, 100)
k.add_payment(1, 200)
k.add_udhaar(2, 400)
k.add_payment(2, 100)

# print(f"Ramesh's Balance (ID 1): {k.balance(1)}")
# print(f"Suresh's Balance (ID 2): {k.balance(2)}")

# # --- GATE: do not touch below, just run ---
assert c1.name == "Ramesh"
assert k.balance(1) == 400, "500 + 100 - 200 must equal 400"
assert k.balance(2) == 300, "400 - 100 must equal 300"
print("Ring 6 GATE: PASS")

# --- QUESTIONS (answer all correctly to finish Rings) ---
# Q1: Why a class — why is a dict not enough for a customer?
# Q2: What is `self`?
# Q3: Where does the balance logic belong — inside Khata or outside? Why?
