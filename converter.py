"""
Reads raw data provided by https://github.com/hdtx/countdown
into a lookup dictionary containing solutions for each number.
"""
import os
import ast
import json
import rpn_to_pn
from collections import defaultdict

RAW_DATA_FOLDER = 'countdown-raw-data'
TARGET_FILE = 'math_lookup.json'

lookup_dict = defaultdict(list)

for file in os.listdir(RAW_DATA_FOLDER):
    with open(os.path.join(RAW_DATA_FOLDER, file)) as f:
        print(file)
        first_line = f.readline()
        for line in f:
            solutions = ast.literal_eval(line.split('#')[-1].strip())
            if solutions:
                for solution in solutions:
                    target = int(solution[0])
                    numbers = [x for x in solution[1] if x not in ["+", "-", "*", "/"]]
                    rpn_repr = ' '.join([str(x) for x in solution[1]])
                    pn_repr = rpn_to_pn.rpn_to_infix(rpn_repr)
                    try:
                        calculated_target = eval(pn_repr)
                        if calculated_target == target:
                            lookup_dict[target].append([numbers, pn_repr])
                    except ZeroDivisionError:
                        print(f"Encountered division by Zero for the following polish notation, skipping: {pn_repr}")

with open(TARGET_FILE, 'w') as f:
    f.write(json.dumps(lookup_dict))


