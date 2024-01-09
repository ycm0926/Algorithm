dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0,
         '6':0, '7':0, '8':0, '9':0, 'Set':1}

for i in input():
    if i == '6' and dict['6'] == dict['9'] == dict['Set']:
        dict['6'] += 1
        dict['Set'] += 1
    elif i == '9' and dict['6'] == dict['9'] == dict['Set']:
        dict['9'] += 1
        dict['Set'] += 1
    elif i == '6' and dict['6'] < dict['9']:
        dict['6'] += 1
    elif i == '6' and dict['6'] > dict['9']:
        dict['9'] += 1
    elif i == '9' and dict['6'] < dict['9']:
        dict['6'] += 1
    elif i == '9' and dict['6'] > dict['9']:
        dict['9'] += 1
    elif dict[i] < dict['Set']:
        dict[i] += 1
    elif dict[i] == dict['Set']:
        dict[i] += 1
        dict['Set'] += 1

print(dict['Set'])
