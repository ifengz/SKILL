# Hazard Shapes

Small, language-neutral shapes that compile, pass a skim, and make a wrong call easy to write later. Treat each as a reason to inspect the hunk, not as a violation. Report only shapes this diff creates or worsens; a documented project convention, linter, or type checker wins over this list.

| Shape | Why it bites | Direction of the fix |
| --- | --- | --- |
| Adjacent parameters of the same primitive type (two ids, two amounts, two strings) | Swapping the arguments still compiles; the bug surfaces as wrong data far from the call | Distinct wrapper types, or one options object with named fields |
| A boolean flag parameter that switches behavior, or two interacting booleans | The call site reads `f(true, false)`, and combinations nobody intended become expressible | An enum or two named functions; make the invalid combination unrepresentable |
| A falsy-default expression (the language's `or`/default operator) where `0`, `false`, or `""` is legitimate | A real zero or empty value is silently replaced by the default | A nullish-only default, or an explicit presence check |
| A hidden default for currency, tenant, region, retry count, or timeout | The caller never chose it, so a wrong value ships unnoticed and the decision is invisible in review | Make the parameter required, or name the default as a constant with the reason |
| A destructive or bulk operation (delete, update, export) where an empty or missing filter means everything | An unset variable or empty list upstream turns a targeted call into a table-wide one | Reject an empty filter, require an explicit "all" argument, and cap the affected row count |
| Async work started and never awaited, or work fired and forgotten | Errors vanish, ordering is lost, and the process may exit before the work finishes | Await it, or hand it to a named background mechanism that logs failure |
| A focused or skipped test marker left in (`.only`, `.skip`, `fdescribe`, a reasonless conditional skip) | The suite goes green while most tests never ran | Remove the marker; if the skip is deliberate, give it a reason and a ticket |
