import mysql.connector
import tkinter as tk




class ToDoManager:
    
    def __init__(self):

        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'ilovemycatarmin',
            database = 'ToDo_DB'
        )
        self.cursor = self.db.cursor()

        self.root = tk.Tk()
        self.root.title("Meine To-Do Liste")
        self.root.geometry("500x600")
        self.root.config(bg ="#f0f0f0")

        self.Label = tk.Label(self.root,text="Meine Aufgaben", font=("Arial 16 bold"), bg="#f0f0f0")
        self.Label.pack(pady=20)

        self.ListBox = tk.Listbox(self.root,width=40,height=15,font=("Arial 12"))
        self.ListBox.pack(pady=10)

        self.Entry = tk.Entry(self.root,width=35, font =("Arial 12"))
        self.Entry.pack(pady=5)

        self.add_Button = tk.Button(self.root,text="Aufgabe hinzüfugen", width=25 
                                ,bg="#4CAF50",fg="white",font=("Arial 10 bold"))
        self.add_Button.pack(pady=10)

        self.delete_Button = tk.Button(self.root,text="Aufgabe löschen", width=25 
                                ,bg="#f44336",fg="white",font=("Arial 10 bold"))
        self.delete_Button.pack(pady=10)

        self.root.mainloop()
    


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

