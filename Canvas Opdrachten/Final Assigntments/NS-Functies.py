def standaardprijs(afstandKM):
    if afstandKM > 50:
        prijs = 15 + afstandKM * 0.60
    elif afstandKM <= 0:
        prijs = 0
    else:
        prijs = afstandKM * 0.80
    return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    stand_prijs = standaardprijs(afstandKM)

    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == 'ja':
            def_prijs = stand_prijs * 0.65
        else:
            def_prijs = stand_prijs * 0.70
    else:
        if weekendrit == 'ja':
            def_prijs = stand_prijs * 0.60
        else:
            def_prijs = stand_prijs

    return "Uw treinticket kost: €"+ str(def_prijs)
