# Copilot Evidence — Step 03

## Refactor prompt

Refactor the file #file:exercise.py to remove duplicated discound logic
add a new helper "apply_discount" and reuse it, keep behaviour the same, keep the edge cases

## Why behavior is preserved

It was an requirement

## Before vs after summary

**Before:** The functions `checkout_total` and `invoice_total` contained identical discount calculation logic with 10 lines of duplicated code each (calculating subtotal, applying discount percentage, ensuring total doesn't go negative, and rounding).

**After:** Extracted the shared discount logic into a new helper function `apply_discount(subtotal, discount_percent)` that:

- Takes a subtotal and discount percentage as parameters
- Returns 0 or greater (handles negative totals by capping at 0)
- Rounds the final result to 2 decimal places
- Returns the subtotal unchanged if no discount is applied

Both `checkout_total` and `invoice_total` now simply compute their subtotal and delegate all discount calculation to the helper, eliminating duplication while preserving all original behavior including edge cases (empty lists, zero/negative discounts, negative resulting totals).
