import random
from math import floor
from statistics import mean, median, mode, pvariance, StatisticsError
import numpy as np
import pylab as pl


class Dado:
    def __init__(self, facce):
        self.facce = facce

    def lancia(self):
        return random.randint(1, self.facce)

class Dado_truccato (Dado):
    def __init__(self, facce, numero_truccato, percentuale_successo):
        super().__init__(facce)
        self.numero_truccato = numero_truccato
        self.percentuale_successo = percentuale_successo
        self.numero_lancio = 0
        self.lista_numeri = []

    def lancia(self):
        if self.numero_lancio == 100 or not self.lista_numeri : self.trucca()
        self.numero_lancio += 1
        return self.lista_numeri[self.numero_lancio-1]
    
    def trucca(self):
        self.lista_numeri.clear()
        numeri = [x for x in range(1, self.facce) if x != self.numero_truccato]
        for x in range(100-self.percentuale_successo):
            self.lista_numeri.append(random.choice(numeri))
        self.lista_numeri.extend(
            self.percentuale_successo*[self.numero_truccato])
        random.shuffle(self.lista_numeri)
        self.numero_lancio = 0

    def aggiorna_dado(self, risultato):

        if risultato == self.numero_truccato:
            self.successi += 1
        if self.numero_lancio == 100:
            self.numero_lancio = 0
            self.successi = 0

class Dado_custom (Dado):
    def __init__(self, lista_facce: list):
        super().__init__(len(lista_facce))
        self.lista_facce = lista_facce

    def lancia(self):
        alfa = random.choice(self.lista_facce)
        return alfa

class Giocata:
    def __init__(self, numero_dadi, facce_dado, numero_lanci):
        self.dadi = []
        self.risultati = []
        self.numero_lanci = numero_lanci
        self.numero_dadi = numero_dadi
        self.facce_dado = facce_dado
        self.esegui_lanci()

    def inizializza_dadi(self):
        self.dadi.clear()
        for dado in range(self.numero_dadi):
            self.dadi.append(Dado(self.facce_dado))

    def esegui_lanci(self):
        self.risultati.clear()
        if not self.dadi:
            self.inizializza_dadi()
        for lancio in range(self.numero_lanci):
            somma_parziale = 0
            for dado in self.dadi:
                #alfa = dado.lancia()
                somma_parziale += dado.lancia()
            self.risultati.append(somma_parziale)

class Giocata_truccata(Giocata):
    def __init__(self, numero_dadi, facce_dado, numero_lanci, numero_truccato, percentuale_successo):
        self.numero_truccato = numero_truccato
        self.percentuale_successo = percentuale_successo
        super().__init__(numero_dadi, facce_dado, numero_lanci)

    def inizializza_dadi(self):
        self.dadi.clear()
        for dado in range(self.numero_dadi):
                self.dadi.append(Dado_truccato(
                self.facce_dado, self.numero_truccato, self.percentuale_successo))

class Giocata_dado_custom(Giocata):
    def __init__(self, numero_dadi, numero_lanci, lista_facce: list):
        self.lista_facce = lista_facce
        super().__init__(numero_dadi, len(lista_facce), numero_lanci)
        

    def inizializza_dadi(self):
        self.dadi.clear()
        for dado in range(self.numero_dadi):
            self.dadi.append(Dado_custom(self.lista_facce))

class Gruppo_giocate:
    def __init__(self, numero_statistiche, numero_dadi, facce_dado, numero_lanci):
        self.risultati = []
        self.numero_statistiche = numero_statistiche
        self.numero_lanci = numero_lanci
        self.numero_dadi = numero_dadi
        self.facce_dado = facce_dado
        for statistica in range(numero_statistiche):
            giocata = Giocata(numero_dadi, facce_dado, numero_lanci)
            self.risultati.append(giocata.risultati)

    def risultati_somma(self):
        return list([Statistica.somma(x) for x in self.risultati])

    def risultati_media(self):
        return list([Statistica.media(x) for x in self.risultati])

    def risultati_mediano(self):
        return list([Statistica.mediano(x) for x in self.risultati])

class Statistica:
    @staticmethod
    def stampa_grafico(risultati, label = "", labelx=""):
        bins = 100
        # Creazione dell'istogramma
        pl.title("Istogramma " + label)
        pl.hist(risultati, bins, histtype='stepfilled')
        pl.ylabel("Numero risultati")
        pl.xlabel(labelx) # Nome asse x
        pl.grid(b=True, axis='y')
        pl.show()

    @staticmethod
    def media(risultati):
        return mean(risultati)

    @staticmethod
    def valore_minimo(risultati):
        return min(risultati)

    @staticmethod
    def valore_massimo(risultati):
        return max(risultati)

    @staticmethod
    def range(risultati):  # intervallo valori da min a max
        return max(risultati)-min(risultati)

    @staticmethod
    def mediano(risultati):  # Median (middle value) of data.
        return median(risultati)

    @staticmethod
    def pvariance(risultati):  # Population variance of data.
        return pvariance(risultati)

    @staticmethod
    def moda(risultati):  # Mode (most common value) of data.
        try:
            return mode(risultati)
        except StatisticsError:
            return None

    @staticmethod
    def somma(risultati):  # Somma dei risultati
        return sum(risultati)

    @staticmethod
    def riepilogo(risultati):
        return "\n"\
            f"\tNumero di prove: {len(risultati)}"\
            f"\n\tValore minimo: {Statistica.valore_minimo(risultati)}"\
            f"\n\tValore massimo: {Statistica.valore_massimo(risultati)}"\
            f"\n\tRange: {Statistica.range(risultati)}"\
            f"\n\tMedia: {Statistica.media(risultati)}"\
            f"\n\tMediano: {Statistica.mediano(risultati)}"\
            f"\n\tModa: {Statistica.moda(risultati)}"\
            f"\n\tVariazione: {Statistica.pvariance(risultati)}"\
            "\n"

    @staticmethod
    def riepilogo_custom(risultati):
        return "\n"\
            f"\tNumero di prove: {len(risultati)}"\
            f"\n\tModa: {Statistica.moda(risultati)}"\
            "\n"

if __name__ == "__main__":
    alfa = Gruppo_giocate(500, 1, 6, 1000)
    print(f"Risultati di {alfa.numero_statistiche} prove,")
    print(f"con n°{alfa.numero_dadi} dadi normali con {alfa.facce_dado} facce, {alfa.numero_lanci} lanci")
    print("Somma")
    print(Statistica.riepilogo(alfa.risultati_somma()))
    print("Media")
    print(Statistica.riepilogo(alfa.risultati_media()))
    print("Mediano")
    print(Statistica.riepilogo(alfa.risultati_mediano()))
    Statistica.stampa_grafico(alfa.risultati_somma(), "Giocate multiple", "Somma")

    Lucia = Giocata(1, 10, 100)
    #Lucia.esegui_lanci()
    print(
        f"Risultati di n°{Lucia.numero_dadi} dadi normali con {Lucia.facce_dado} facce, {Lucia.numero_lanci} lanci")
    print(Statistica.riepilogo(Lucia.risultati))
    #Statistica.stampa_grafico(Lucia.risultati, "Lucia")
    #print(Lucia.risultati)

    Arturo = Giocata_dado_custom(1, 100, ["Rosso", "Verde", "Giallo"])
    #Arturo.esegui_lanci()
    print(
        f"Risultati di n°{Arturo.numero_dadi} dadi custom con {Arturo.facce_dado} facce ({Arturo.lista_facce}), {Arturo.numero_lanci} lanci")
    #print(Statistica.riepilogo_custom(Arturo.risultati))
    #Statistica.stampa_grafico(Arturo.risultati, "Arturo")

    Alberto = Giocata_truccata(1, 6, 110, 6, 60)
    #Alberto.esegui_lanci()
    print(
        f"Risultati di n°{Alberto.numero_dadi} dadi truccati con {Alberto.facce_dado} facce, {Alberto.numero_lanci} lanci,")
    print(
        f"numero truccato {Alberto.numero_truccato}, percentuale di successo {Alberto.percentuale_successo}%")
    print(Statistica.riepilogo(Alberto.risultati))
    Statistica.stampa_grafico(Alberto.risultati, "Alberto")
    print(Alberto.risultati)
