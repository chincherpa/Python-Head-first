mann = []
anderer = []


try:
    daten = open('sketch.txt')

    for zeile in daten:
        try:
            (rolle, aussage) = zeile.split(':', 1)
            aussage = aussage.strip()
            if rolle == 'Man':
                mann.append(aussage)
            elif rolle == 'Other Man':
                anderer.append(aussage)
        except ValueError:
            pass

    daten.close()
except IOError:
    print('Datei nicht auffindbar!')

print(mann)
print(anderer)

