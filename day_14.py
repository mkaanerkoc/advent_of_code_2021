def solution():
    with open('data/day_14_input.txt', 'r') as day_input:
        template, formula_text = day_input.read().split('\n\n')
        formula_list = [formula.split(' -> ') for formula in formula_text.split('\n')]
        formulas_dict = {f[0]: f[1] for f in formula_list}

    # Part 1
    pairs_in_template, letters_count = initialize(template)
    for x in range(10):
        pairs_in_template, letters_count = step(pairs_in_template, letters_count, formulas_dict)
    letter_occurrences_sorted = sorted(letters_count.values())
    print(letter_occurrences_sorted[-1] - letter_occurrences_sorted[0])

    # Part 2
    pairs_in_template, letters_count = initialize(template)
    for x in range(40):
        pairs_in_template, letters_count = step(pairs_in_template, letters_count, formulas_dict)
    letter_occurrences_sorted = sorted(letters_count.values())
    print(letter_occurrences_sorted[-1] - letter_occurrences_sorted[0])


def step(template_dict, letter_count, formulas_dict):
    new_pairs_in_template = {}
    for pair, count in template_dict.items():
        new_letter = formulas_dict[pair]
        new_pairs_in_template[pair[0] + new_letter] = new_pairs_in_template.get(pair[0] + new_letter, 0) + count
        new_pairs_in_template[new_letter + pair[1]] = new_pairs_in_template.get(new_letter + pair[1], 0) + count
        letter_count[new_letter] = letter_count.get(new_letter, 0) + count
    return new_pairs_in_template, letter_count


def initialize(template):
    pairs_in_template = {}
    for curr_char, next_char in zip(template, template[1:]):
        pairs_in_template[curr_char + next_char] = pairs_in_template.get(curr_char + next_char, 0) + 1
    letters_count = {s: template.count(s) for s in template}
    return pairs_in_template, letters_count
