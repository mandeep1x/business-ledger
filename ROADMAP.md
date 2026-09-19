# Dukkan Khata — Roadmap (Rings + Loops, Gated)

**Project:** a shop ledger. Customers + due/payment entries + balance.
**Method:** Rings = learning, Loops = building. A ring is passed only when its asserts are green AND its QUESTIONS are answered correctly. A loop moves only when its Definition of Done is ticked. Dates do not matter, gates do.

**Just-in-time rule (remember it):** learn only what the current ring/loop needs. Studying the full Python manual first is just-in-case — 3 months of theory, 0 projects. If the Khata needs `balance` today, learn `for` today. Decorators, generators, FastAPI stay in `IDEAS.md` until Loop 4.

**How to work (his procedure):**
1. Read the current ring/loop plus the next one's line. Do not reread the whole file; it is a reference.
2. Before code, plan 15 minutes: what to build, which file, which function.
3. Keep every step runnable. Never leave a broken tree overnight — end with a green run and a commit.
4. Tick the DoD literally. A half-ticked DoD means the loop repeats.
5. Answer the QUESTIONS out loud. Stuck means stay here, do not advance.
6. End with 3 lines in `docs/NOTES.md`: what was built, what broke, what is next. Then commit (`ring1: variables` / `loop0: cli`).

---

## RINGS (Python from zero — asserts green + QUESTIONS correct, or repeat)

### Ring 0 — Setup: prove Python runs (15 min)
**Goal:** run a file from the terminal with zero errors.
**Practice:** `rings/r00-setup.py`
**Gate:** file runs, asserts pass.
**QUESTIONS:** in the file. All correct = Ring 1.

### Ring 1 — Variables + print (30 min)
**Goal:** store a name and an amount, print one bill line.
**Practice:** `rings/r01-variables.py`
**Gate:** all asserts green.
**QUESTIONS:** in the file. All correct = Ring 2.

### Ring 2 — Conditions (45 min)
**Goal:** reject bad entries: amount <= 0 rejected, empty name rejected.
**Practice:** `rings/r02-conditions.py`
**Gate:** bad entries rejected, good entries pass.
**QUESTIONS:** in the file. All correct = Ring 3.

### Ring 3 — Loops (1 hr)
**Goal:** walk entries and compute a balance.
**Practice:** `rings/r03-loops.py`
**Gate:** loop balance equals the hand-computed balance.
**QUESTIONS:** in the file. All correct = Ring 4.

### Ring 4 — Functions (1 hr)
**Goal:** split code into pieces: `add_udhaar()`, `balance()`.
**Practice:** `rings/r04-functions.py`
**Gate:** function version and long-file version give the same output.
**QUESTIONS:** in the file. All correct = Ring 5.

### Ring 5 — Data structures (1.5 hr)
**Goal:** entries in a list, customers in a dict.
**Practice:** `rings/r05-data-structures.py`
**Gate:** dict finds a customer in one line; list needs a loop — difference visible.
**QUESTIONS:** in the file. All correct = Ring 6.

### Ring 6 — OOP + Khata (2 hr, most important)
**Goal:** write the `Customer` and `Khata` classes yourself.
**Practice:** `rings/r06-oop.py`, then compare with `app/customer.py` and `app/khata.py`.
**Gate:** 2 customers + 4 entries via classes, correct balance. Remove `self`, read the error, understand it.
**QUESTIONS:** in the file. All correct = Rings complete.

**Rings complete = ready to build the project.** Now Loops.

---

## LOOPS (Building — every loop is a running system)

### Loop 0 — CLI in memory (after Rings, 3-4 days)
The same 5 jobs: add customer, due entry, payment entry, balance, total pending. Storage is list/dict, no file.
**Done when:** 2 customers + 4 entries, correct balance; closing the program loses data (that pain is what Loop 1 fixes).

### Loop 1 — File storage (2 days)
Save/load `data.json`. Close and reopen, balance unchanged.
**Done when:** restart-proof. Note it down: two writers would corrupt the file — that pain is what PSQL fixes.

### Loop 2 — PSQL connect (real PSQL here, 3-4 days)
Two tables + JOIN-based balance. `migrations/01-init.sql`, connect with `psycopg`.
**Done when:** everything works with the JSON file deleted.

### Loop 3 — Cleanup + production glimpse
One-query balance with `GROUP BY`, `INDEX`, README + `docs/runbook.md`. A stranger can run it from the README = production-ready.

## NOT in scope (queued, not dropped)
- Web/API, auth — write them in `IDEAS.md`, they arrive in Loops 4-5.
