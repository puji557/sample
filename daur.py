import tkinter
import sqlite3

class HomePage:
        homePageWindow = tkinter.Tk()
        homePageWindow.wm_title("Patient Information System")
        tkinter.Label(homePageWindow,text="name",width=20).grid(pady = 15, column = 1, row = 1)
        fnameEntry=tkinter.Entry(homePageWindow,width=50,textvariable="fname").grid(pady = 100, column = 2, row = 2)
        tkinter.Button(homePageWindow,text='submit',width=20,command="database").grid(pady = 15, column = 1, row = 2)
        def database():
            name=StringVar()
            fname=name.get()
            conn=sqlite3.connect('abc.db')
            with conn:
                cur=conn.cursor()
                cur.execute('CREATE TABLE IF NOT EXIST stu(name TEXT)')
                cur.execute('INSERT INTO stu(name) VALUES(?)',(fname,))
                cur.execute('select * from stu')
                for i in cur.fetchall():
                    cur.insert(END,"\t"+name.get())
                cur.close()                    
        homePageWindow.mainloop()
