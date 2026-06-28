import mysql.connector
import tkinter as tk
from tkinter import messagebox



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
                                ,bg="#4CAF50",fg="white",font=("Arial 10 bold"),command=self.add_tasks)
        self.add_Button.pack(pady=10)

        self.delete_Button = tk.Button(self.root,text="Aufgabe löschen", width=25 
                                ,bg="#f44336",fg="white",font=("Arial 10 bold"), command=self.delete_tasks)
        self.delete_Button.pack(pady=10)

        self.show_tasks()

        self.root.mainloop()
    


    def show_tasks(self) : 
       

        self.ListBox.delete(0,tk.END)


        self.cursor.execute("Select task_name from tasks")
        tasks = self.cursor.fetchall()
        
        
        for index , task in enumerate(tasks,start=1) :
             self.ListBox.insert(tk.END, f"{index}- {task[0]}")




    def add_tasks(self) :
        
        new_task = self.Entry.get()

        if new_task.strip() : 
           sql = "insert into tasks (task_name) Values (%s)"
           val = (new_task,)
           self.cursor.execute(sql,val)
           self.db.commit()
           
           self.Entry.delete(0 , tk.END)

           self.show_tasks()
           # messagebox.showinfo("Erfolg","Die Aufgabe wurde erfolgreich hinzugefügt!")
        else : 
            messagebox.showwarning("Warnung", "Bitte geben Sie einen Aufgabennamen ein!")

        




    def delete_tasks(self) :

        
        try : 
           selected_index = self.ListBox.curselection()[0]
           
           selected_task_text = self.ListBox.get(selected_index)
           task_name = selected_task_text.split("- ",1)[1]
           

           sql = 'delete from tasks where task_name = %s'
           self.cursor.execute(sql,(task_name,))
           self.db.commit()

           self.show_tasks()


        except IndexError:
            messagebox.showwarning("Warnung", "Bitte wählen Sie zuerst eine Aufgabe aus! ")          
    
        
      

manager = ToDoManager()

