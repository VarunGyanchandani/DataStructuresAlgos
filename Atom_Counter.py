def count_of_atoms(formula: str) -> str:
    from collections import defaultdict
    import re

    # Helper function to process the formula
    def parse_formula(formula):
        stack = []
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append('(')
                i += 1
            elif formula[i] == ')':
                temp_count = defaultdict(int)
                i += 1
                # Process the counts until we find the '('
                while stack and stack[-1] != '(':
                    element, count = stack.pop()
                    temp_count[element] += count
                stack.pop()  # Pop the '('

                # Check if there's a multiplier after the closing parenthesis
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i:j]) if i < j else 1
                i = j

                # Apply the multiplier to all elements in temp_count and push back to stack
                for element, count in temp_count.items():
                    stack.append((element, count * multiplier))
            else:
                # Parse the element
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                element = formula[i:j]
                i = j
                # Parse the count
                count_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[count_start:i]) if count_start < i else 1
                stack.append((element, count))

        # Combine results from the stack
        atom_count = defaultdict(int)
        while stack:
            element, count = stack.pop()
            atom_count[element] += count

        return atom_count

    # Main processing of the formula
    atom_count = parse_formula(formula)

    # Create sorted output
    sorted_atoms = sorted(atom_count.items())
    result = []

    for atom, count in sorted_atoms:
        result.append(atom)
        if count > 1:
            result.append(str(count))

    return ''.join(result)


# Example usage:
print(count_of_atoms("H2O"))  # Output: "H2O"
print(count_of_atoms("Mg(OH)2"))  # Output: "H2MgO2"
print(count_of_atoms("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"
