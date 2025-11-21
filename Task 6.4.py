random_elements = [['toy', 'bee', 'cheese', 'ear'],
                   [False, 'word', '0110110', 10],
                   ['happiness', '(⅃ °ロ°)⅃ ', 'luck', None],
                   ['car', '<- code ->', 4.7, True]]

for row in random_elements:
    for index, element in enumerate(row):
        if (index % 2 == 0):
            print(element)
