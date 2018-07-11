import cgitb
import glob
import sportlermodell
import yate

cgitb.enable()

dateien = glob.glob('data/*.txt')
alle_sportler = sportlermodell.konserve_machen(dateien)

print(yate.antwort_anfang())
print(yate.seitenanfang('Herzlisch willkommen!'))
print(yate.para('Sportler ausw&auml;hlen:'))
print(yate.form_anfang('zeitdaten_generieren.py'))
for sportler in alle_sportler:
    print(yate.radio_button('sportlerwahl', alle_sportler[sportler].name))
print(yate.form_ende('Ausw&auml;hlen'))
print(yate.seitenende({'Home': '/index.html'}))
