"""q1_1.py"""

dict_a = {"k1": 10, "k2": 20, "k3": 30}
print('dict_a:', dict_a)

print(dict_a.keys())
for key in dict_a.keys():
    print(key)

print(dict_a.values())
for value in dict_a.values():
    print(value)

print(dict_a.items())
for key, value in dict_a.items():
    print(key, value)