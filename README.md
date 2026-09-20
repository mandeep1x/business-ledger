# Business Ledger CLI – Core Backend Build

A simple command-line tool for small shop owners to track customer debts and payments. 

---

## 🎯 The Main Purpose
The main purpose of this project is to replace an old-school **paper notebook** used by shopkeepers with a clean digital ledger. It answers three simple questions for the shop owner:
1. Who owes money?
2. How much do they owe?
3. When did they pay it back?

---

## 📊 How the Data Flows

```text
[Shop Owner CLI]
       │
       ▼
 ┌───────────┐         ┌────────────────┐
 │ CUSTOMERS │ ──────> │  TRANSACTIONS  │
 ├───────────┤         ├────────────────┤
 │ * Name    │         │ * Due Entry    │
 │ * Phone   │         │ * Repayment    │
 └───────────┘         │ * Date         │
                       └────────────────┘
```

## 🛠️ What it Does (Only 5 Features)
The system only does these 5 basic tasks:

* **Add a Customer:** Save a customer's name and phone number.
* **Record a Debt:** Log how much money a customer borrowed and the date.
* **Record a Payment:** Log when a customer pays back their debt.
* **Check Customer Balance:** Show exactly how much an individual customer still owes (Total Debt minus Total Payments).
* **Check Shop Total:** Show the total amount of pending money owed by all customers combined.

---

## 🚫 What it Does NOT Do (Out of Scope)
To keep the backend simple and clean, these features are omitted for now:
* **No Login System:** No usernames or passwords required.
* **No Web Interface:** It runs entirely inside your terminal screen, not in a browser.
* **No Photos:** You cannot upload receipts or profile pictures.
