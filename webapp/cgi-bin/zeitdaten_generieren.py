
import cgitb

import cgi
import sportlermodell
import yate

cgitb.enable()

alle_sportler = sportlermodell.konserve_lesen()

form_daten = cgi.FieldStorage()
sportler_name = form_daten['sportlerwahl'].value

l_elemente = ['1', '2', '3']

print(yate.antwort_anfang())
print(yate.seitenanfang('Zeitdaten'))
print(yate.header('Sportler: ' + sportler_name + ' Geb: ' + alle_sportler[sportler_name].geb + '.'))
print(yate.para('Die Bestzeiten sind:'))
print(yate.u_liste(l_elemente))
print(yate.seitenende({'Home': '/index.html', 'Anderen Sportler w&auml;hlen': 'liste_generieren.py'}))
