# Initial facts
facts = {'A', 'B'}

# Rule base: each rule is a tuple (conditions, conclusion)
rules = [
    (['A', 'B'], 'C'),
    (['C'], 'D'),
    (['D', 'E'], 'F'),  # Example of a more complex rule
]

# Inferred facts
inferred = set()

def forward_chaining(facts, rules):
    while True:
        applied = False
        for conditions, conclusion in rules:
            if all(cond in facts for cond in conditions) and conclusion not in facts:
                print(f"Applying rule: IF {conditions} THEN {conclusion}")
                facts.add(conclusion)
                inferred.add(conclusion)
                applied = True
        if not applied:
            break
    return facts

# Run inference
final_facts = forward_chaining(facts, rules)

print("\nFinal facts:")
print(final_facts)
