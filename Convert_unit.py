units = {1:
         {'km': {'m': 1000, 'cm': 100000, 'mm': 1000000, 'nm': 0.54},
          'm': {'km': 0.001, 'cm': 100, 'mm': 1000, 'nm': 0.0054}},
         2:
         {'kg': {'g': 1000, 'dkg': 100, 'oz': 35.27},
          'oz': {'kg': 0.03, 'g': 28.35}}}

unitsTypes = {1: 'Długośc',
              2: 'Waga'}

unitsNames = {'km': 'kilometry',
              'm': 'metry',
              'cm': 'centymetry',
              'mm': 'milimetry',
              'nm': 'mile morskie',
              'kg': 'kilogram',
              'g': 'gram',
              'dkg': 'dekagram',
              'oz': 'uncja'}

print('Wybierz cyfre odpowiadającą typowi jednostki do przeliczenia')
for i in unitsTypes:
    value = int(i)
    print(f'{value} : {unitsTypes[value]}')
mainUnitType = int(input('>>> '))


print('Wybierz jednostkę do przeliczenia')
for name in units[mainUnitType]:
    #print(f'{name} - {unitsNames[name]}')
    print("{:3s} - {} " .format(name, unitsNames[name]))
mainUnit = input('>>> ')

print(f'Wartość {mainUnit}')
mainUnitValue = float(input('>>> '))

print(f'Wybierz jednostkę na którą przeliczyć {mainUnit}')
for name in units[mainUnitType][mainUnit]:
    #print(f'{name} - {unitsNames[name]}')
    print("{:3s} - {} " .format(name, unitsNames[name]))
convertUnit = input('>>> ')

result = mainUnitValue * units[mainUnitType][mainUnit][convertUnit]
print(f'{mainUnitValue} {mainUnit} to {result:.2f} {convertUnit}')
