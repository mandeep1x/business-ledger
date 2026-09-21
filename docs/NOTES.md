# NOTES.md — 3 lines at the end of every ring/loop.

## Ring 0 — Setup (date: 2026-09-19)
- Built: first Python run from VS Code terminal, `print("khata ready")`.
- Broke: nothing; gate green on first run.
- Next: Ring 1 variables.

## Ring 1 — Variables (date: 2026-09-19)
- Built: bill_line with f-string, `Ramesh owes: Rs 500`.
- Broke: deleted the assignment to see NameError, then restored it.
- Next: Ring 2. Status: PASSED (file green + Q1/Q2/Q3 correct).

## Ring 2 — Conditions (date: 2026-09-19)
- Built: phone rule added as third early-return block by Mandeep himself.
- Broke: `and` vs `or` dead check, then number-vs-digits confusion. Fixed with `len(str(phone)) != 10`.
- Next: Ring 3. Status: PASSED (file green + Q1/Q2/Q3 done).

## Ring 3 — Loops (date: 2026-09-19)
- Built: 4-entry balance pattern, filter `cid == 1` understood via experiment.
- Broke: edited gate data + stale assert message; fixed message to match 700.
- Next: Ring 3 QUESTIONS, then Ring 4. Status: PASSED (file green + Q1/Q2/Q3 done, debug print removed).

## Session 2026-09-19 (night halt)
- Rings passed: R0, R1, R2, R3. Ring 4 opened, file not run yet.
- Commits due: init docs + rings r00-r03 with NOTES.
- Resume tomorrow: run r04-functions.py, then Ring 4 QUESTIONS.

## Ring 4 — Functions (date: 2026-09-20)
- Built: full line-by-line understanding; broke and restored file twice by own experiments.
- Broke: passed `3` instead of list (argument order); print-vs-return confusion solved via None experiment; stale gate message fixed.
- Next: Ring 5. Status: PASSED (file green + Q1/Q2/Q3 done).

## Ring 5 — Data structures (date: 2026-09-20)
- Built: dict one-step lookup vs list loop search, duplicate-key insight from own project.
- Broke: nothing; file untouched, gate green first run. `[]` vs `.get()` learned via KeyError vs None.
- Next: Ring 6 (OOP). Status: PASSED (file green + Q1/Q2/Q3 done).

## Ring 6 — OOP (date: 2026-09-21)
- Built: Customer + Khata classes; blueprint, self, encapsulation via own examples.
- Broke: claimed PASS with gate commented (silent run); fixed data honestly to 400-100=300.
- Next: Loop 0 (project build). Status: PASSED (file green + Q1/Q2/Q3 done).

## RINGS COMPLETE — 2026-09-21
- R0 setup, R1 variables, R2 conditions, R3 loops, R4 functions, R5 data structures, R6 OOP. All green + questioned.
