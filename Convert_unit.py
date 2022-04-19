from units import units
from units import unitsTypes
from units import unitsNames

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
