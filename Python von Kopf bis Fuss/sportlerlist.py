
class SportlerList(list):

    def __init__(self, name, geb=None, zeiten=[]):
        list.__init__([])
        self.name = name        
        self.geb = geb
        self.extend(zeiten)

    def saeubern(zeit_string):
        if '-' in zeit_string:
            trenner = '-'
        elif ':' in zeit_string:
            trenner = ':'
        else:
            return(zeit_string)
        (mins, seks) = zeit_string.split(trenner)
        return(mins + '.' + seks)

    def top3(self):
        return(sorted(set([saeubern(t) for t in self]))[0:3])

    def clean_data(self):
        return(sorted(set([saeubern(t) for t in self])))
