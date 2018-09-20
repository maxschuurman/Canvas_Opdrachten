cijferICOR = 7.0
cijferPROG = 7.5
cijferCSN = 6.0

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3

beloning = (cijferICOR * 30) + (cijferPROG * 30) + (cijferCSN * 30)

overzicht = 'Mijn cijfers (gemiddeld een ' + str(round(gemiddelde,1)) + ') leveren een beloning van €' + str(beloning) + 'op!'

print(overzicht)