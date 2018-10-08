treinrit = int(input('Vul hier de afstand van uw reis in: '))
tarief = treinrit * 0.80
leeftijd = int(input('Vul hier uw leeftijd in: '))
weekend = input('Vul hier in welke dag het is: ')

if treinrit > 50:
    tarief = 15 + (int(treinrit) * 0.60)

if treinrit <= 0:
    tarief = 0

if leeftijd < 12 or leeftijd >= 65 and weekend != ('Zaterdag', 'Zondag'):
    int(tarief) * 0.70
elif leeftijd < 12 or leeftijd >= 65 and weekend == ('Zaterdag', 'Zondag'):
    int(tarief) * 0.65

if weekend == 'Zaterdag' or 'Zondag'and leeftijd < 12 or leeftijd >= 65:
    float(tarief) * 0.65
    if leeftijd < 12 or leeftijd >= 65 and weekend !=('Zaterdag', 'Zondag'):
        float(tarief) * 0.70
print(tarief)