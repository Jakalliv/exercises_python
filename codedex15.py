import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
    return name.capitalize()

def create_fantasy_name(list_1, list_2, func):
  return random.choice(list_1) + ' ' + func(random.choice(list_2))


Suffixes = list(map(capitalize_suffix, suffixes))

fantasy_names = [create_fantasy_name(prefixes, suffixes, capitalize_suffix) for _ in range(10)]


def fire_in_name(name):
    return "Fire" in name
def concatenate_names(name1, name2):
    return name1 + " " + name2

def display_name_info(func1, func2, func3, pref, suff):
    names = [func1(pref, suff, capitalize_suffix) for _ in range(10)]
    filtered_names = list(filter(func2, names))
    concat_names = reduce(func3, filtered_names)

    return f"Generated Names: {names}\nFiltered Names: {filtered_names}\nConcatenated Name: {concat_names}"

print(display_name_info(create_fantasy_name, fire_in_name, concatenate_names, prefixes, suffixes))