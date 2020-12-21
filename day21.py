import collections
import re

def run(filename):
  ingredients = set()
  ingredient_count = collections.defaultdict(int)
  allergen_count = collections.defaultdict(int)
  allergens = {}
  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      m = re.match('([\w\s]+) \(contains ([\w, ]+)\)', line)
      g = m.groups()
      if m is None:
        print('ERROR')
      item_ingredients = set([i.strip() for i in g[0].split(' ')])
      for i in item_ingredients:
        ingredient_count[i] += 1
      ingredients |= item_ingredients
      item_allergens = [a.strip() for a in g[1].split(',')]
      # if 'peanuts' in item_allergens:
      # print(item_ingredients)
      # print(item_allergens)
      for a in item_allergens:
        allergen_count[a] += 1
      for allergen in item_allergens:
        if allergen in allergens:
          if allergen == 'soy':
            print(f'before {allergens[allergen]}')
          allergens[allergen] = allergens[allergen] & item_ingredients
          if allergen == 'soy':
            print(f'after {allergens[allergen]}')
        else:
          print(f'set {allergen} to {item_ingredients}')
          allergens[allergen] = item_ingredients

  print(allergens['soy'])
  # print(ingredients)
  print(allergens)
  print(allergen_count)

  allergen_ingredients = set()
  for a in allergens.values():
    allergen_ingredients |= a
  cnt = 0
  for i in ingredients - allergen_ingredients:
    cnt += ingredient_count[i]
  print(cnt)


run('day21_ex.txt')
# run('day21.txt')