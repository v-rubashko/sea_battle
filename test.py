from random import choices
true_count = 0
false_count = 0
for _ in range(20):
    a = choices((True, False), weights=(12 * 0.05, 1 - 12 * 0.05))[0]
    if a:
        true_count += 1
    else:
        false_count += 1

print(true_count, false_count)