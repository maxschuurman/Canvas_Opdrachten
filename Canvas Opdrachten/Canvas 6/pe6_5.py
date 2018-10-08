def kwadraten_som(grondgetallen):
    for negatief in grondgetallen:
        res = sum(int(negatief) for negatief in grondgetallen)
        return res

kwadraten_som([ 4, 5, 3, -81 ])