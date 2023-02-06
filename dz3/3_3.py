points = {1: 'AEIOULNSTRАВЕИНОРСТ',
          2: 'DGДКЛМПУ',
          3: 'BCMPБГЁЬЯ',
          4: 'FHVWY',
          5: 'KЖЗХЦЧ',
          8: 'JZШЭЮ',
          10: 'QZФЩЪ'}
text = input().upper()
print(sum([k for i in text for k, v in points.items() if i in v]))
