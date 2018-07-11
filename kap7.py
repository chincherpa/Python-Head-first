import pickle


def saeubern(zeit_string):
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return(zeit_string)
    (mins, seks) = zeit_string.split(trenner)
    return(mins + '.' + seks)

class SportlerList(list):
    def __init__(self, name, geb=None, zeiten=[]):
        list.__init__([])
        self.name = name        
        self.geb = geb
        self.extend(zeiten)

    def top3(self):
        return(sorted(set([saeubern(t) for t in self]))[0:3])

def datei_lesen(txtdatei):
    try:
        with open(txtdatei) as out: daten = out.readline()
        templ = daten.strip().split(',')
        #print(templ[0], templ[1], templ)
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



konserve_machen(['james2.txt', 'julie2.txt', 'mikey2.txt', 'sarah2.txt'])
alle_sportler2 = konserve_lesen()
# print(alle_sportler2)

for x in alle_sportler2:
    print(x, alle_sportler2[x])


# james = datei_lesen('james2.txt')
# julie = datei_lesen('julie2.txt')
# mikey = datei_lesen('mikey2.txt')
# sarah = datei_lesen('sarah2.txt')

# print(james.name + ' \t Top3: ' + str(james.top3()))
# print(julie.name + ' \t Top3: ' + str(julie.top3()))
# print(mikey.name + ' \t Top3: ' + str(mikey.top3()))
# print(sarah.name + ' \t Top3: ' + str(sarah.top3()))
# sarah.append('1:24')
# print(sarah.name + ' - Top3: ' + str(sarah.top3()))
# sarah.extend(['1:22', '1,12'])
# print(sarah.name + ' - Top3: ' + str(sarah.top3()))
# james.append('1,09')
# james.append('1,89')
# print(james.top3())
# print(james.name + ' - Top3: ' + str(james.top3()))