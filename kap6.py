def saeubern(zeit_string):
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return(zeit_string)
    (mins, seks) = zeit_string.split(trenner)
    return(mins + '.' + seks)

#class Sportler:
#    def __init__(self, ein_name, ein_geb=None, ein_zeiten=[]):
#        self.name = ein_name
#        self.geb = ein_geb
#        self.zeiten = ein_zeiten
#    
#    def top3(self):
#        return(sorted(set([saeubern(t) for t in self.zeiten]))[0:3])
#    
#    def neue_zeit(self, zeit):
#        self.zeiten.append(zeit)
#        
#    def neue_zeiten(self, zeiten):
#        self.zeiten.extend(zeiten)

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

        
james = datei_lesen('james2.txt')
julie = datei_lesen('julie2.txt')
mikey = datei_lesen('mikey2.txt')
sarah = datei_lesen('sarah2.txt')

print(james.name + ' \t Top3: ' + str(james.top3()))
print(julie.name + ' \t Top3: ' + str(julie.top3()))
print(mikey.name + ' \t Top3: ' + str(mikey.top3()))
print(sarah.name + ' \t Top3: ' + str(sarah.top3()))
# sarah.append('1:24')
# print(sarah.name + ' - Top3: ' + str(sarah.top3()))
# sarah.extend(['1:22', '1,12'])
# print(sarah.name + ' - Top3: ' + str(sarah.top3()))
# james.append('1,09')
# james.append('1,89')
# print(james.top3())
# print(james.name + ' - Top3: ' + str(james.top3()))