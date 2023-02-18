transormation = lambda x : x 
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transormation, values))
if values == transformed_values:
    print('ok')
else:
     print('fail')