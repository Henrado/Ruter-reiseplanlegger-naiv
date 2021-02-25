
class Reise:
    def __init__(self):
        self._rute = []
        self._fremme = False
        self._harDuplikat = False
        self._maalStasjon = None

    def hentFremme(self):
        return self._fremme

    def hentDuplikat(self):
        return self._harDuplikat

    def settMaal(self, maal):
        self._maalStasjon = maal

    def hentMaal(self):
        return self._maalStasjon

    def hentSisteStasjon(self):
        return self._rute[-1]

    def leggTilRute(self, nyRute):
        self._rute.append(nyRute)

    def gjorTilTekst(self):
        test = []
        for i in self._rute:
            test.append(str(i))
        return test

    def sjekkOmFremme(self):
        if str(self._maalStasjon) in self.gjorTilTekst():
            self._fremme = True
            return True
            #return self._fremme

    def sjekkOmDuplikat(self):
        liste = self.gjorTilTekst()
        if len(liste) == len(set(liste)):
            return False
        else:
            self._harDuplikat = True
            return True

    def hentRute(self):
        return self._rute

    def __str__(self):
        tekst = ""
        for i in self._rute:
            tekst = tekst + " " + str(i)
        return  tekst

    def __lt__(self, other):
        return len(self._rute) > other
