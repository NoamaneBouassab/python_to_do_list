import mysql.connector


class ToDoManager:
    
    def __init__(self):

        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'ilovemycatarmin',
            database = 'ToDo_DB'
        )
        self.cursor = self.db.cursor()

    def show_tasks(self) : 
       
        self.cursor.execute("Select task_name from tasks")
        tasks = self.cursor.fetchall()
        if len(tasks) == 0 :
            print("Deine To-Do-Liste ist leer!")
        else : 
            print("--- Deine Aufgaben ---")
            for index , task in enumerate(tasks,start=1) :
             print(f'{index}- {task[0]}')


    def add_tasks(self) :
        
        new_task = input("Schreiben Sie bitte die neue Aufgabe : ")

        if new_task.strip() : 
           sql = "insert into tasks (task_name) Values (%s)"
           val = (new_task,)
           self.cursor.execute(sql,val)
           self.db.commit()
           print(f'"{new_task}" wurde hinzugefügt ! ')
        else :
           
           print('Die Aufgabe darf nicht leer sein !!!')




    def delete_tasks(self) :

        self.cursor.execute("select id, task_name from tasks")
        tasks = self.cursor.fetchall()
        
        if len(tasks) == 0 :
            print("Deine To_Do_Liste ist leer !! Es gibt keine Aufgaben zum löschen !")
            return 
        
        print("-- Welche Aufgabe möchtest du löschen ? --")
        for index , task in enumerate(tasks, start=1) : 
            print(f"{index}- {task[1]}")

        try : 
            choice = int(input("Wählen Sie die Nummer der Aufgabe : "))
            
            if choice >=1 and choice <= len(tasks) : 
                task_id = tasks[choice-1][0]
                sql = 'delete from tasks where id = %s'
                self.cursor.execute(sql,(task_id,))
                self.db.commit()

                print("Die Aufgabe wurde erfolgreich gelöscht!")
            else:
                print("Ungültige Nummer!")
        except ValueError : 
            print("Bitte gib eine gültige Zahl ein !")              
    
        
      

manager = ToDoManager()

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
        manager.show_tasks()

    elif wahl == 2 : 
        manager.add_tasks() 
        print("Die Aufgabe wurde erfolgreich hinzugefügt !")

    elif wahl == 3 : 
        manager.delete_tasks()
          
    elif wahl == 4 : 
        print('Tschüss')
        break
    else : 
        print("Falsch Wahl !!!")