import re

with open('19.txt') as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    divide = data.index('')

rules = {}
for line in data[:divide]:
    rules[int(line.split(':')[0])] = line.split(': ')[1].strip('"')

messages = data[divide + 1: ]

# Part 1
filled_rules = rules.copy()
rule_num = 0
num_valid = 0

def fill_rule(rules, rule_num):
    rule = rules[rule_num]
    if re.search('[a-z]', rule):
        return rule
    for sub_rule in rule.split(' | '):
        for num in sub_rule.split():
            inner_rule = fill_rule(rules, int(num))
            if '|' in inner_rule:
                inner_rule = f'({inner_rule})'
            rule = rule.replace(num, inner_rule, 1)
    rule = rule.replace(' ', '')
    rules[rule_num] = rule
    return rule

def is_following_rule(message, rule):
    return bool(re.match(f'^({rule})$', message))

rule = fill_rule(rules, 0)
tot_part_1 = 0
for msg in messages:
    if is_following_rule(msg, rule):
        tot_part_1 += 1

print(f'Solution 1: {tot_part_1}')

# Part 2:
rule_42 = filled_rules[42]
rule_31 = filled_rules[31]

rules[8] = '42 | 42 8'
rules[11] = '42 31 | 42 11 31'

patter = (
    f"^({rule_42})+"
    "("
    
)