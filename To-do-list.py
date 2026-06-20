

Tasks = ['Coding','Deutsch']

def show_tasks() : 
    for index,task in enumerate(Tasks) : 
        print(f"{index+1} -  {task}")

def add_tasks() :
    new_task = input("Neue Aufgabe hinzufügen: ")
    Tasks.append(new_task)

def delete_tasks() :
    show_tasks()
    del_nummer = int(input("Geben Sie die Nummer der Aufgabe ein,die Sie löschen möchten : "))
    if del_nummer <= len(Tasks) and del_nummer >=1 : 
     Tasks.pop(del_nummer-1)
     print("Die Aufgabe wurde erfolgreich gelöscht")
    else : 
     print("Diese Aufgabe existiert nicht !!")
    
      

while True : 
    print("________________________")
    print('1- Aufgaben Anzeigen')
    print('2- Aufgabe hinzufügen')
    print('3- Aufgabe löschen')
    print('4- Beenden')
    print('                 ')
    wahl = int(input("Wählen Sie die gewünschte Aktion aus : "))
    print("________________________")

    if wahl == 1 : 
        print("Deine Aufgabe : ")
        show_tasks()

    elif wahl == 2 : 
        add_tasks() 
        print("Die Aufgabe wurde erfolgreich hinzugefügt !")

    elif wahl == 3 : 
          delete_tasks()
          
    elif wahl == 4 : 
        print('Tschüss')
        break
    else : 
        print("Falsch Wahl !!!")