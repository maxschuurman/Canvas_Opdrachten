leeftijd = int(input('Geef je leeftijd: '))
paspoort = input('Heb je een Nederlandspaspoort: ')

if leeftijd >= 18 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Je mag niet stemmen')