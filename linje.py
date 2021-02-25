class Linje:
    _linjeNr = 1
    def __init__(self):
        self._linjeNavn = str(Linje._linjeNr)
        self._stasjoner = []
        Linje._linjeNr += 1

    def __str__(self):
        return self._linjeNavn

    def hentlinjeNr(self):
        return self._linjeNavn

    def hentAlleStasjoner(self):
        return self._stasjoner

    def leggTilStasjon(self, stasjon):
        self._stasjoner.append(stasjon)

    def regnUtStasjonLinjer2(self): #legger til seg selv som stasjonen sin
        for j in self._stasjoner:
            j.leggTilLinje(self)


    def regnNabo(self):
        for i in range(len(self._stasjoner)):
            if i < len(self._stasjoner)-1:
                self._stasjoner[i].leggTilNaboStasjon(self._stasjoner[i+1])
            if i > 0:
                self._stasjoner[i].leggTilNaboStasjon(self._stasjoner[i-1])
