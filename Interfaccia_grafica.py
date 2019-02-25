
from tkinter import*
import Statistica_tiri_dadi as STD
window = Tk() 
window.geometry("400x500")
window.title("Statistiche Dadi")

def show_entry_fields():
    T1.delete('1.0', END)
    T1.insert(INSERT,f"Risultati di n°{E1.get()} dadi \ncon {E2.get()} facce, {E3.get()} lanci\n")
    if C2var.get() == 0 and C3var.get() == 0:
        alberto = STD.Giocata(int(E1.get()), int(E2.get()), int(E3.get()))
        risultati_da_stampare = alberto.risultati
    if C2var.get() == 1:
        T1.insert(INSERT,f"numero truccato {E5.get()}, percentuale di successo {E6.get()}%")
        alberto = STD.Giocata_truccata(int(E1.get()), int(E2.get()), int(E3.get()), int(E5.get()), int(E6.get()))
        risultati_da_stampare = alberto.risultati
    if C3var.get() == 1:
        alberto = STD.Gruppo_giocate(int(E8.get()), int(E1.get()), int(E2.get()), int(E3.get()))
        T1.insert(
            INSERT, f"Risultati di {E8.get()} prove")
        risultati_da_stampare = alberto.risultati_somma()

    T1.insert(INSERT, STD.Statistica.riepilogo(risultati_da_stampare))

    if C1var.get() == 1:
        STD.Statistica.stampa_grafico(risultati_da_stampare, "Risultati")


def show_dado_truccato():
    hide_giocate_multiple()

    if C2var.get() == 1:
        L5.grid(row=0, column=2, sticky="W")
        E5.grid(row=0, column=3, sticky="W")
        L6.grid(row=1, column=2, sticky="W")
        E6.grid(row=1, column=3, sticky="W")
    if C2var.get() == 0:
        hide_dado_truccato()

def hide_dado_truccato():
    C2var.set(0)
    L5.grid_remove()
    E5.grid_remove()
    L6.grid_remove()
    E6.grid_remove()

def show_giocate_multiple():
    hide_dado_truccato()
    if C3var.get() == 1:
        L8.grid(row=2, column=2, sticky="W")
        E8.grid(row=2, column=3, sticky="W")
    if C3var.get() == 0:
        hide_giocate_multiple()

def hide_giocate_multiple():
    C3var.set(0)
    L8.grid_remove()
    E8.grid_remove()

L1 = Label(window, text="Numero di Dadi")
L1.grid(row=0, column=0, sticky="W")
E1 = Entry(window, bd =2, width= 5)
E1.insert(0, '1')
E1.grid(row=0, column=1, sticky="W")
L2 = Label(window, text="Facce Dadi")
L2.grid(row=1, column=0, sticky="W")
E2 = Entry(window, bd =2, width= 5)
E2.insert(0, '6')
E2.grid(row=1, column=1, sticky="W")
L3 = Label(window, text="Numero di lanci")
L3.grid(row=2, column=0, sticky="W")
E3 = Entry(window, bd =2, width= 5)
E3.insert(0, '1000')
E3.grid(row=2, column=1, sticky="W")
L3 = Label(window, text="Grafico")
L3.grid(row=3, column=0, sticky="W")
C1var = IntVar()
C1 = Checkbutton(window, variable=C1var)
C1.grid(row=3, column=1, sticky="W")
L4 = Label(window, text="Truccato")
L4.grid(row=4, column=0, sticky="W")
C2var = IntVar()
C2 = Checkbutton(window, variable=C2var, command=show_dado_truccato)
C2.grid(row=4, column=1, sticky="W")
L7 = Label(window, text="Giocate_multiple")
L7.grid(row=5, column=0, sticky="W")
C3var = IntVar()
C3 = Checkbutton(window, variable=C3var, command=show_giocate_multiple)
C3.grid(row=5, column=1, sticky="W")

B1 = Button(window, text='Calcola', background= "salmon", command=show_entry_fields)
B1.grid(row=99, column=1, sticky="W", pady = 20,  columnspan=2)

T1 = Text(window, width = 50, height = 15)
#text.insert(END, text)
#text.insert(END, "Bye Bye.....")
T1.grid(row=100,column=0, sticky="W", columnspan=4 )

# text.tag_add("here", "1.0", "1.4")
# text.tag_add("start", "1.8", "1.13")
# text.tag_config("here", background="yellow", foreground="blue")
# text.tag_config("start", background="black", foreground="green")

L5 = Label(window, text="Numero Truccato")
E5 = Entry(window, bd =2, width= 5)
E5.insert(0, '6')
L6 = Label(window, text="Percentuale sussessi")
E6 = Entry(window, bd =2, width= 5)
E6.insert(0, '50')
L8 = Label(window, text="Numero giocate multiple")
E8 = Entry(window, bd=2, width=5)
E8.insert(0, '1000')

window.mainloop()
