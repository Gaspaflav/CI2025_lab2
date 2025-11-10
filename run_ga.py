import json
import os

nb_path = os.path.join(os.path.dirname(__file__), 'tsp.ipynb')
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Build a globals dict and execute import/def cells only
G = {}

skip_markers = ['for prob in problems', 'problems=[', 'cont=0', "print(f\"Problem size"]

for cell in nb.get('cells', []):
    if cell.get('cell_type') != 'code':
        continue
    src = ''.join(cell.get('source', []))
    if any(marker in src for marker in skip_markers):
        continue
    # execute imports and function definitions and small helpers
    try:
        exec(src, G)
    except Exception as e:
        # Skip cells that might depend on runtime state
        print('Skipped cell due to error:', e)

# Now load a small problem and run genetic_algorithm
import numpy as np

prob_path = os.path.join(os.path.dirname(__file__), 'lab2', 'problem_g_10.npy')
if not os.path.exists(prob_path):
    print('Problem file not found:', prob_path)
else:
    problem = np.load(prob_path)
    # Call genetic_algorithm from globals
    ga = G.get('genetic_algorithm')
    if ga is None:
        print('genetic_algorithm not found in executed notebook code')
    else:
        print('Running genetic_algorithm on problem_g_10.npy (short run)')
        best = ga(problem, population_size=20, offspring_size=10, generations=30, mutation_rate=0.6, mutation_prob=0.7, invert_prob=0.5, greedy_population=5, no_better=10, seed=123)
        print('Best length returned:', best)
