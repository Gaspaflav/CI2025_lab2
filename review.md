# Review & Commented Rewrite of `tsp.ipynb`

- Performance & speed  
- Genetic operators  
- Local search  
- Population management  
- Reproducibility  

---


```markdown

## Performance and Speed

- You currently recompute distances many times inside loops.
- **Improvement:** Precompute a full distance matrix once per problem and reuse it in all fitness evaluations.
- Avoid unnecessary Python-level loops when possible and keep operations on arrays.

---

## Genetic Operators

- You use simple swap mutation. This is OK, but for TSP, operators that preserve adjacency (like inversion) often work better.
- **Improvements:**
  - Keep swap mutation, but **add inversion mutation**.
  - Allow different probabilities for each mutation type.

---

## Local Search

- Your GA does not use any local improvement (e.g. 2-opt).
- Pure GAs often converge slowly or get stuck in plateaus.
- **Improvement:** Add a light **2-opt local search** on some of the best individuals in each generation (memetic algorithm idea).

---

## Population Management

- Selection and elitism are not clearly described.
- **Improvements:**
  - Use **tournament selection** to pick parents.
  - Use **elitism**: always carry the best individual to the next generation.
  - Keep population size and number of generations configurable, and scale them with the problem size.

---

## Reproducibility

- Results change every run because the random seed is not fixed.
- **Improvement:** Set a seed at the beginning using `random.seed()` and `np.random.seed()`, at least for experiments in the report.

---

## Overall

The structure of your solution is good and works as a GA for TSP.  
The attached revised code focuses on:

- Precomputing distance matrices (performance)
- Better genetic operators (swap + inversion)
- Simple 2-opt local search
- Explicit tournament selection and elitism
- Reproducible experiments with fixed seeds
