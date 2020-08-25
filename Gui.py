#import os

from tkinter import messagebox
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Menu
from tkinter import Button
from Control import Control


Control = Control()



#Variablen (müssen noch über self. aufgerufen werden damit lokal und nicht mehr global)  
pCount = 0

#Funktionen des Dropdown Menues
        
def button_getmail():
        global mailentry
        mailentry = mail_eingabefeld.get()
        if (Control.aEMail.getMailrdy()):
            messagebox.showinfo(message= "Invalid Entry!\nAn email has already been created!", title = "Status")
        elif (mailentry == ""):
            messagebox.showinfo(message= "Invalid Entry!\nPlease fill in the input field correctly!", title = "Status")
        else:
            Control.aEMail.setAdresseEmpf(mailentry)
            messagebox.showinfo(message= "The email was added successfully!", title = "Status")
                
    

def button_cngmail():
        global mailentry
        mailentry = mail_eingabefeld.get()
        if (mailentry == ""):
            messagebox.showinfo(message= "invalid Entry!\nPlease fill in the input field correctly!", title = "Status")
        elif (mailentry == Control.aEMail.getAdresseEmpf()):
            messagebox.showinfo(message= "invalid Entry!\nNew mail identical to old one!", title = "Status")
        else:
            Control.aEMail.setAdresseEmpf(mailentry)
            messagebox.showinfo(message= "The mail was changed successfully!", title = "Status")

def button_plant():
    #Prüfe nach freien MAC-Adressen der Sensoren
    if (pCount == 3):
        messagebox.showinfo(message= "All sensors are already in use!\nPlease delete an existing plant first!", title = "Status")
    else:
        #Liste
        #-----------------------------------------------------------------------------------------------------------
        def increase():
            value = int(lbl_value["text"])
            if (int(lbl_value["text"]) == 3):
                lbl_value["text"] = f"{0}"
                try:
                    Control.getName(0)
                except IndexError:
                    lbl_plant["text"] = "empty"
                else:
                    lbl_plant["text"] = f"{Control.getName(0)}"
            else:
                lbl_value["text"] = f"{value + 1}"
                try:
                    Control.getName(value + 1)
                except IndexError:
                    lbl_plant["text"] = "empty"
                else:
                    lbl_plant["text"] = f"{Control.getName(value + 1)}"
                

        def decrease():
            value = int(lbl_value["text"])
            if (int(lbl_value["text"]) == 0):
                lbl_value["text"] = f"{3}"
                try:
                    Control.getName(3)
                except IndexError:
                    lbl_plant["text"] = "empty"
                else:
                    lbl_plant["text"] = f"{Control.getName(3)}"
            else:
                lbl_value["text"] = f"{value - 1}"
                try:
                    Control.getName(value - 1)
                except IndexError:
                    lbl_plant["text"] = "empty"
                else:
                    lbl_plant["text"] = f"{Control.getName(value - 1)}"
        #-----------------------------------------------------------------------------------------------------------

        #Delete Plant    
        #-----------------------------------------------------------------------------------------------------------
        def delete():
            global pCount
            value = int(lbl_value["text"])
            if (Control.getName(value) == ""):
                messagebox.showinfo(message= "There is no plant for deleting!", title = "Status")    
            else:
                Control.clear_Plant(value)
                lbl_plant["text"] = "empty"
                pCount = pCount - 1
        #-----------------------------------------------------------------------------------------------------------

        #Add Plant
        #-----------------------------------------------------------------------------------------------------------
        def addplant():
            global pCount
            value = int(lbl_value["text"])
            if (pCount < 4):
                #Anlegen
                if (hasattr(Control, "__alistPlant") and Control.getName(value) != ""):
                    messagebox.showinfo(message= "There is already a plant using this MAC!", title = "Status")
                else:
                #Eingabe und Anlegen in Control
                #-------------------------------------------------------------------------------
                    def enter():
                        global pCount
                        value = int(lbl_value["text"])
                        text = ""
                        text = e1.get()
                        wat = ""
                        wat = e2.get()
                        tim = ""
                        tim = e3.get()
                        if (text == ""):
                            messagebox.showinfo(message= "Please enter the name before saving!", title = "Status")
                        elif (wat == ""):
                            messagebox.showinfo(message= "Please enter the amout of water before saving!", title = "Status")
                        elif (tim == ""):
                            messagebox.showinfo(message= "Please enter the time for growing in weeks!", title = "Status")
                        else:
                            #NEU
                            mac = ""
                            mac = Control.aLearn.getMACSensor(value)
                            Control.new_Plant(text, tim, wat, value)
                            messagebox.showinfo(message= Control.getName(value), title = "Status")
                            lbl_plant["text"] = f"{Control.getName(value)}"
                            pCount = pCount + 1
                            pfnew.destroy()
                #-------------------------------------------------------------------------------

                #Darstellung Eingabefenster
                #-------------------------------------------------------------------------------
                pfnew = Tk()
                pfnew.title("Create plant")

                delfenster.rowconfigure([0, 1], minsize=50, weight=1)
                delfenster.columnconfigure([0, 1], minsize=50, weight=1)

                Label(pfnew, text="Name xx: ").grid(row=0)

                e1 = Entry(pfnew)
                e1.grid(row=0, column=1)

                Label(pfnew, text="Water xxl: ").grid(row=1)

                e2 = Entry(pfnew)
                e2.grid(row=1, column=1)

                Label(pfnew, text="Time xxh: ").grid(row=2)

                e3 = Entry(pfnew)
                e3.grid(row=2, column=1)

                btn_enter = Button(master=pfnew, text="Enter", command=enter)
                btn_enter.grid(row=3, columnspan=2, sticky="nsew")

                pfnew.mainloop()
                #-------------------------------------------------------------------------------
            else:
                messagebox.showinfo(message= "The max Number of Plants has been added!", title = "Status")
            
        #-----------------------------------------------------------------------------------------------------------

        #Darstellung Pflanzenedit
        #-----------------------------------------------------------------------------------------------------------
        delfenster = Tk()
        delfenster.title("Edit the plant")

        delfenster.rowconfigure([0, 1, 2], minsize=50, weight=1)
        delfenster.columnconfigure([0, 1, 2], minsize=50, weight=1)

        btn_decrease = Button(master=delfenster, text="-", command=decrease)
        btn_decrease.grid(row=0, column=0, sticky="nsew")

        lbl_value = Label(master=delfenster, text= "0")
        lbl_value.grid(row=0, column=1)

        btn_increase = Button(master=delfenster, text="+", command=increase)
        btn_increase.grid(row=0, column=2, sticky="nsew")

        #value = int(lbl_value["text"])

        lbl_plant = Label(master=delfenster, text= "Start", font = "Helvetica 16 bold italic")
        lbl_plant.grid(row = 1, columnspan = 4)

        #if (pCount == 0):
        #    lbl_plant = Label(master=delfenster, text= "empty", font = "Helvetica 16 bold italic")
        #    lbl_plant.grid(row = 1, columnspan = 4)
        #else:
        #    lbl_plant = Label(master=delfenster, text= Control.getName(value), font = "Helvetica 16 bold italic")
        #    lbl_plant.grid(row = 1, columnspan = 4)

        btn_delete = Button(master=delfenster, text="Delete", command=delete)
        btn_delete.grid(row=2, column=0, sticky="nsew")

        btn_add = Button(master=delfenster, text="Add", command=addplant)
        btn_add.grid(row=2, column=2, sticky="nsew")

        delfenster.mainloop()
        #-----------------------------------------------------------------------------------------------------------




#Infos für Benutzer falls Probleme auftreten sollten        
def action_get_info_dialog():
    m_text = "\
************************\n\
Iot Pflanzenbewaesserung\n\
Version 1.0\n\
Ruben Rath\n\
Nico Woessner\n\
************************"
    messagebox.showinfo(message=m_text, title = "Infos")



#Anzeigefenster erstellen        
fenster = Tk()
fenster.title("Plant irrigation")

fenster.rowconfigure([0, 1, 2], minsize=50, weight=1)

#Texte und Eingabefelder hinzufügen
info_text1 = Label(fenster, text = "Welcome to the IoT Plant Irrigation user interface", font = "arial 14")
info_text2 = Label(fenster, text = "Enter email and select the required functions from the dropdown menu!\n", font = "arial 10")
mail_label = Label(fenster, text = 'Email:', font = "arial 10")
mail_eingabefeld = Entry(fenster, bd = 5, width = 70)

#Grafische Anordnung der Texte und Eingabefelder im Anzeigefenster
info_text1.grid(row = 0, column = 0, columnspan = 2)
info_text2.grid(row = 1, column = 0, columnspan = 2)
mail_label.grid(row = 2, column = 0)
mail_eingabefeld.grid(row = 2, column = 1)

# Menüleiste 
menuleiste = Menu(fenster)

# Menü Datei und Help
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

# Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen
# Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
datei_menu.add_command(label="Add new email", command=button_getmail)
datei_menu.add_command(label="Change email", command=button_cngmail)
datei_menu.add_command(label="Plant editing", command=button_plant)
datei_menu.add_separator() # Fügt eine Trennlinie hinzu
datei_menu.add_command(label="Exit", command=fenster.quit)

help_menu.add_command(label="Info!", command=action_get_info_dialog)

# Menüs (Datei und Help) der Menüleiste als "Drop-Down-Menü"  
menuleiste.add_cascade(label="Functions", menu=datei_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

# Die Menüleiste mit den Menüeinrägen dem Fenster übergeben
fenster.config(menu=menuleiste)

Basics = False

if (Basics == False):
    Control.addBasics()
    Basics = True

while True:
    fenster.update_idletasks()
    fenster.update()
    Control.doRefresh()




#fenster.mainloop()
