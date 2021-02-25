class Stasjon:
    def __init__(self, navn):
        self._navn = navn
        self._linjer = []
        self._naboStasjoner = set()

    def __str__(self):
        return self._navn

    def leggTilLinje(self, linje):
        self._linjer.append(linje)


    def leggTilNaboStasjon(self, nabo):
        self._naboStasjoner.add(nabo)


    def hentNavn(self):
        return self._navn


    def hentLinjer(self):
        return self._linjer


    def hentNaboStasjoner(self):
        return self._naboStasjoner
