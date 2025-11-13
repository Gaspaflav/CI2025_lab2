
## Delivery Review for TSP Genetic Algorithm

## Fixes

Only the most significant, logic-changing fixes that were actually applied are listed here.


1. Fix insertion mutation index computation
   - Location: `mutate_insertion` in `tsp.ipynb`.
   - Problem: Insert index was computed using a length value that became invalid after removing an element; this could produce incorrect insertions.
   - Action taken: Compute `insert_index` after popping the city using the current list length (allowed range starts at 1). This changes mutation behavior to be correct and deterministic with respect to list state.


## Nits

1. Add seed parameter (minor, already added)
   - Note: a `seed` parameter was added to `genetic_algorithm` and passed through `tuning_parameters` to improve reproducibility; this is primarily an operational convenience rather than a core logic change.

2. Explicit reversed-slice conversion
   - Note: `mutate_inversion` now uses `list(reversed(...))` for clarity. This is a readability/robustness improvement.


3. Guard initial population size calculation
   - Note: `BuildInitialPopulation` was modified to compute `num_random = max(0, population_size - greedy_population - 1)` before adding random permutations. This is a defensive fix to avoid negative-range loops when `population_size` is small.

4. Correct tuning function invocation
   - Action taken: Replaced the positional call with a keyword-argument call (population_size, offspring_size, generations, mutation_rate, mutation_prob, invert_prob, greedy_population, no_better). This fixes broken tuning experiments.

## Comments

1. Positive design choices
   - Greedy seeds help the GA find reasonable baselines quickly.
   - Tournament selection with increasing size is a sensible adaptive pressure strategy.

2. Performance considerations
   - Fitness evaluation is O(n) per tour and becomes the main bottleneck for large instances; consider incremental updates or vectorized operations.

3. Reproducibility
   - Document used seeds and store them with outputs; the added `seed` parameter helps with reproducible experiments.