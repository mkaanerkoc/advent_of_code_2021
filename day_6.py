generators = {}

with open('day_6_input.txt', 'r') as day_input:
  generator_offsets = list(map(int, day_input.read().split(',')))


def step(generators):
  new_generators = {}
  for offset, count in generators.items():
    if offset == 0:
      new_generators[6] = new_generators.get(6, 0) + count
      new_generators[8] = count
    else:
      new_generators[offset-1] = new_generators.get(offset-1, 0) + count
  return new_generators

# Part 1
generators = {offset:generator_offsets.count(offset) for offset in generator_offsets}
for x in range(80):
  generators = step(generators)

print(sum(generators.values()))

# Part 2
generators = {offset:generator_offsets.count(offset) for offset in generator_offsets}
for x in range(256):
  generators = step(generators)

print(sum(generators.values()))
