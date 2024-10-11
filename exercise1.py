import itertools
import pandas as pd

# Define the variables of the proposition
variables = ['P', 'Q', 'R', 'S', 'T', 'D']

# Generate all possible combinations (64 combinations)
combinations = list(itertools.product([False, True], repeat=len(variables)))

# Funciones para cada proposición lógica
def not_p_then_s(p, s):
    return (not p) or s

def p_then_q_or_r(p, q, r):
    return (not p) or (q or r)

def q_and_r_then_t(q, r, t):
    return (not (q and r)) or t

def t_iff_d(t, d):
    return t == d

# Calculate values ​​for logical expressions
results = []
for comb in combinations:
    P, Q, R, S, T, D = comb
    expr1 = not_p_then_s(P, S)
    expr2 = p_then_q_or_r(P, Q, R)
    expr3 = q_and_r_then_t(Q, R, T)
    expr4 = t_iff_d(T, D)
    full_expr = expr1 and expr2 and expr3 and expr4
    results.append((P, Q, R, S, T, D, expr1, expr2, expr3, expr4, full_expr))

# Create a DataFrame to show the truth table
df = pd.DataFrame(results, columns=variables + ["P'→S", 'P→(Q∨R)', '(Q∧R)→T', 'T↔D', 'Expr. Completa'])
df = df.astype(int)
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)     # Show all rows (optional)
df.to_csv('tabla_verdad.csv', index=False) # Import for a CSV file