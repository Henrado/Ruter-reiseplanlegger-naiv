from stasjon import Stasjon
from linje import Linje
from reise import Reise
import math
import copy

class Kart:
    def __init__(self):
        self._linjer = []
        self._alleStasjoner = {}
        self._reiser = []

    def lesFraFil(self, filnavn):
        for linje in open(filnavn):
            biter = linje.strip().split()
            nyLinje = Linje()
            for navn in biter:
                if navn not in self._alleStasjoner:
                    self._alleStasjoner[navn] = Stasjon(navn)
                    pass
                nyLinje.leggTilStasjon(self._alleStasjoner[navn])
            self._linjer.append(nyLinje)
        self._regnUtStasjonLinjer1()
        pass

    def _regnUtStasjonLinjer1(self):
        for i in self._linjer:
            i.regnNabo()
            i.regnUtStasjonLinjer2()
        pass

    def startReise(self, fraStasjon, tilStasjon):
        nyReise = Reise()
        nyReise.settMaal(self._alleStasjoner[tilStasjon])
        nyReise.leggTilRute(self._alleStasjoner[fraStasjon])
        self.reis(nyReise, 20)
        self._reiser.sort()
        for i in self._reiser:
            print(str(i))
        pass

    def reis(self, reise, antall):
        #print(antall)
        if antall > 0:
            if reise.sjekkOmFremme():
                print("Fremme!!")
                self._reiser.append(reise)
                return
            sisteStasjon = reise.hentSisteStasjon()
            for nabo in self._alleStasjoner[sisteStasjon.hentNavn()].hentNaboStasjoner():
                nyReise = copy.deepcopy(reise)
                nyReise.leggTilRute(nabo)
                if not nyReise.sjekkOmDuplikat():
                    self.reis(nyReise, antall-1)
            pass

    def hentLinje(self): #For å skrive ut
        for i in range(len(self._linjer)):
            print(i)
            liste = self._linjer[i].hentAlleStasjoner()
            for j in liste:
                print(j, end="")
            print()
        pass

    def skrivStasjon(self):
        stasjoner = self._alleStasjoner[input("Skriv")].hentNaboStasjoner()
        for i in stasjoner:
            print(i)


mittKart = Kart()
mittKart.lesFraFil("ruter.cvs")
#mittKart.hentLinje()
#mittKart.skrivStasjon()
mittKart.startReise(input("Fra: "), input("Til: "))
