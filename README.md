# Dukkan Khata — Mandeep's first backend project

**In one line:** a small shop's credit ledger. Which customer, how much due, when given, when repaid.

**Why this project?**
- It uses exactly what the Rings teach, nothing extra
- PSQL plugs in later: customers + transactions = the real use of JOINs
- It is showable in production: a money domain, not a todo app

**What it does (only 5 jobs, nothing more):**
1. Add a customer (name + phone)
2. Due entry (customer, amount, date)
3. Repayment entry (payment)
4. Balance per customer (dues minus payments)
5. Total pending of the whole shop

**What it does NOT do (not now):**
- No login/auth, no web, no photos — those arrive in Loops 4-5
- It runs on the CLI, not in a browser
