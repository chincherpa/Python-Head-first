import pickle
from sportlerlist import SportlerList


def datei_lesen(txtdatei):
    try:
        with open(txtdatei) as out:
            daten = out.readline()
        templ = daten.strip().split(',')
        # print(templ[0], templ[1], templ)
        return(SportlerList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('Datei nicht gefunden' + str(ioerr))
        return(None)


def konserve_machen(dateiliste):
    alle_sportler = {}
    for datei in dateiliste:
        sportler = datei_lesen(datei)
        alle_sportler[sportler.name] = sportler
    try:
        with open('sportler.pickle', 'wb') as sppd:
            pickle.dump(alle_sportler, sppd)
    except IOError as ioerr:
        print('Dateifehler (konserve_machen)' + str(ioerr))
    return(alle_sportler)


def konserve_lesen():
    alle_sportler = {}
    try:
        with open('sportler.pickle', 'rb') as sppl:
            alle_sportler_r = pickle.load(sppl)
    except IOError as ioerr:
        print('Dateifehler (konserve_lesen)' + str(ioerr))
    return(alle_sportler_r)
