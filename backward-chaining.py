# Known facts
facts = {'A', 'B'}

# Rule base: each rule is a tuple (conditions, conclusion)
rules = [
    (['A', 'B'], 'C'),
    (['C'], 'D'),
]

# Create a mapping from conclusion to conditions for fast lookup
rule_dict = {conclusion: conditions for conditions, conclusion in rules}

def backward_chaining(goal, facts, rule_dict, depth=0):
    indent = "  " * depth
    print(f"{indent}Trying to prove: {goal}")
    
    if goal in facts:
        print(f"{indent}{goal} is already a known fact.")
        return True
    
    if goal not in rule_dict:
        print(f"{indent}No rule to derive {goal}.")
        return False
    
    conditions = rule_dict[goal]
    print(f"{indent}To prove {goal}, need: {conditions}")
    
    for condition in conditions:
        if not backward_chaining(condition, facts, rule_dict, depth + 1):
            print(f"{indent}Failed to prove {goal} because {condition} could not be proven.")
            return False
    
    # If all conditions are proven, goal is now a fact
    print(f"{indent}Successfully proved {goal}.")
    facts.add(goal)
    return True

# Example: Try to prove goal 'D'
goal = 'D'
result = backward_chaining(goal, facts.copy(), rule_dict)

print(f"\nCan we prove '{goal}'? {'Yes' if result else 'No'}")
