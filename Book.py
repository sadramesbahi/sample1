from sqlite3 import *
from tkinter import *
import sqlite3


class gui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Contact Book")
        self.root.geometry("490x260+550+200")
        self.background = "#24282d"
        self.root.resizable(width=False,height=False)
        self.root.config(bg=self.background)

        #Lable List For Contacts
        self.listbox = Listbox(self.root,width=30,height=15,background="white")
        self.listbox.place(relx=0.8,rely=0.5,anchor="c")


        self.conn = sqlite3.connect("newdata.db")
        self.cur = self.conn.cursor()


        self.cur.execute('CREATE TABLE IF NOT EXISTS moshakhasat(nam NVARCHAR,family NVARCHAR,shomare INT)')
        self.cur.execute("SELECT * FROM moshakhasat")
        self.rows = self.cur.fetchall()
        self.nam = list()
        self.fam = list()
        self.numb = list()
        for i in self.rows:
            self.nam.append(i[0])
            self.fam.append(i[1])
            self.numb.append(i[2])
        self.rows_len = self.rows.__len__()
        self.counter = 0
        while self.rows_len > self.counter:
            self.x = "{0} - {1} - {2}".format(self.nam[self.counter],self.fam[self.counter],self.numb[self.counter])
            self.listbox.insert(END,self.x)
            self.counter += 1




        # Contact Name Label 
        self.namelabel = Label(self.root,text=" Contact Name :",bg=self.background,fg="white",font=("calibri",12),anchor="w",justify=LEFT)
        self.namelabel.place(relx=0.115, rely=0.07,anchor="c")
        # Contact Name Entry 
        self.nameentry = Entry(self.root,bg="white",fg=self.background,width=22,borderwidth=2)
        self.nameentry.place(relx=0.46,rely=0.07,anchor="c")
        # Contact Family Lable
        self.familylable = Label(self.root,text ="    Contact Family :" ,bg=self.background,fg="white",borderwidth=2,font=("calibri",12))
        self.familylable.place(relx=0.108,rely=0.17,anchor="c")
        # Contact Family Entry
        self.familyentry = Entry(self.root,bg="white",fg=self.background,width=22,borderwidth=2)
        self.familyentry.place(relx=0.46,rely=0.17,anchor="c")
        # Contact Number Label 
        self.numberlable= Label(self.root,text ="    Contact Number :" ,bg=self.background,fg="white",borderwidth=2,font=("calibri",12))
        self.numberlable.place(relx=0.115,rely=0.27,anchor="c")
        # Contact Number Entry 
        self.numberentry = Entry(self.root,bg="white",fg=self.background,width=22,borderwidth=2)
        self.numberentry.place(relx=0.46,rely=0.27,anchor="c")



        # Add Contact Button  
        self.addbutton = Button(self.root,text="Add Contact",bg="#3c434b",fg="white",borderwidth=2,height=2,padx=31,command=self.add)
        self.addbutton.place(relx=0.46,rely=0.45,anchor="c")
        # Delet Contact Button 
        self.deletecontact = Button(self.root,text="Delete Contact  ",bg="#3c434b",fg="white",borderwidth=2,height=2,padx=21,command=self.delete)
        self.deletecontact.place(relx=0.15,rely=0.45,anchor="c")
        # Edit List Button 
        self.editbutton = Button(self.root,text="Edit Contact",bg="#3c434b",fg="white",borderwidth=2,height=2,padx=31,command=self.edit)
        self.editbutton.place(relx=0.15,rely=0.65,anchor="c")
        # Exit App Button
        self.exitbutton = Button(self.root,text="Exit App",bg="#3c434b",fg="white",borderwidth=2,height=2,padx=118,command=self.exit)
        self.exitbutton.place(relx=0.305,rely=0.9,anchor="c")
        #Search Contact Button
        self.searchcontact= Button(self.root,text=" Search Contact",bg="#3c434b",fg="white",borderwidth=2,height=2,padx=23,command=self.search)
        self.searchcontact.place(relx=0.46,rely=0.65,anchor="c")


        self.root.mainloop()

    def add(self):
        self.finalcontact = self.nameentry.get() +" - "+self.familyentry.get()+" - "+ self.numberentry.get()
        self.namee = self.nameentry.get()
        self.numbere = self.numberentry.get()
        self.fame = self.familyentry.get()

        self.conn = sqlite3.connect("newdata.db")
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS moshakhasat(nam NVARCHAR,family NVARCHAR,shomare INT)')

        self.lg = self.listbox.get(0,END)
        if self.finalcontact not in self.lg:
            self.listbox.insert(END,self.finalcontact)
            self.cur.execute("INSERT INTO moshakhasat(nam,family,shomare) VALUES(?,?,?)",(self.namee,self.fame,self.numbere))
            self.conn.commit()
        else:
            pass            
            
        


        self.nameentry.delete(0,END)
        self.familyentry.delete(0,END)
        self.numberentry.delete(0,END)





    def delete(self):
        self.selectedcontact = self.listbox.get(ANCHOR)
        self.info = self.selectedcontact.split(" - ")
        self.nu = self.info[2]
        self.f = self.info[1]
        self.n = self.info[0]
        self.cur.execute("DELETE FROM moshakhasat WHERE shomare = '"+ self.nu +"' AND nam = '" + self.n + "' AND family = '"+ self.f +"'")
        self.listbox.delete(ANCHOR)
        self.conn.commit()



    def search(self):
        self.root2 = Tk()
        self.root2.geometry("350x150+200+200")
        self.root2.config(bg=self.background)

        self.contact_info = Label(self.root2,text="Contact info :",bg=self.background,fg="white",font=("calibri",12),anchor="w",justify=LEFT)
        self.contact_info.place(relx=0.17 ,rely= 0.1,anchor="c")
    
        self.contact_info_entry = Entry(self.root2,width=25,borderwidth=3,bg="white",fg=self.background)
        self.contact_info_entry.place(relx=0.58 , rely=0.1,anchor="c")


        self.listbox2 = Listbox(self.root2,width=43,height=6)
        self.listbox2.place(relx=0.43,rely=0.6,anchor="c")

        self.submitb = Button(self.root2,text="Submit",width=6,height=1,bg="#3c434b",fg="white",command=self.searchsubmit)
        self.submitb.place(relx=0.92,rely=0.11,anchor="c")

    def searchsubmit(self):
        self.listbox2.delete("end")
        self.searchedcontact = self.contact_info_entry.get()
        self.lg = self.listbox.get(0,END)
        if self.searchedcontact not in self.lg:
            self.result = self.cur.execute("SELECT * FROM moshakhasat WHERE nam like '%" + self.searchedcontact +"%'")
            self.conn.commit()
            self.listbox2.insert("end",self.result.fetchall())
               
                
            
            

    def edit(self):
            self.root3 = Tk()
            self.root3.title("Contact Book")
            self.root3.geometry("350x150+208+350")
            self.background = "#24282d"
            #self.root3.overrideredirect(True)
            self.root3.resizable(width=False,height=False)
            self.root3.config(bg=self.background)

            self.le = Label(self.root3,text="Contact Name :",bg=self.background,fg="white",font=("calibri",12),anchor="w",justify=LEFT)
            self.le.place(relx=0.2,rely=0.1,anchor="c")

            self.le1 = Label(self.root3,text="   Contact Family :",bg=self.background,fg="white",font=("calibri",12),anchor="w",justify=LEFT)
            self.le1.place(relx=0.188,rely=0.27,anchor="c")

            self.le2 = Label(self.root3,text="   Contact Number :",bg=self.background,fg="white",font=("calibri",12),anchor="w",justify=LEFT)
            self.le2.place(relx=0.2,rely=0.44,anchor="c")

            self.edit_entry_name = Entry(self.root3,bg="white",fg=self.background,borderwidth=2,width=29)
            self.edit_entry_name.place(relx=0.7,rely=0.1,anchor="c")

            self.edit_entry_family = Entry(self.root3,bg="white",fg=self.background,borderwidth=2,width=29)
            self.edit_entry_family.place(relx=0.7,rely=0.27,anchor="c")

            self.edit_entry_number= Entry(self.root3,bg="white",fg=self.background,borderwidth=2,width=29)
            self.edit_entry_number.place(relx=0.7,rely=0.44,anchor="c")

            self.be = Button(self.root3,text="Submit",bg="#3c434b",height=2,fg="white",borderwidth=3,padx=133,command=self.editsubmit)
            self.be.place(relx=0.5,rely=0.83,anchor="c")

            self.lg = self.listbox.get(ANCHOR)
            self.x = self.lg.split(" - ")
            self.o = self.x[0]
            self.o1 = self.x[1]
            self.o2 = self.x[2]
            self.edit_entry_name.insert("end",self.o)
            self.edit_entry_family.insert("end",self.o1)
            self.edit_entry_number.insert("end",self.o2)



    def editsubmit(self):
        self.finalcontact = self.edit_entry_name.get()+" - "+self.edit_entry_family.get()+" - "+ self.edit_entry_number.get()
        self.listget = self.listbox.get(0,END)
        if self.finalcontact in self.listget:
            pass
        else:
            self.listbox.insert(END,self.finalcontact) 
            self.listbox.delete(ANCHOR)
            self.en = self.edit_entry_name.get()
            self.enu = self.edit_entry_family.get()
            self.enum = self.edit_entry_number.get()
            if self.en != self.x[0] or self.enu != self.x[1] or self.enum != self.x[2]:
                self.cur.execute("UPDATE moshakhasat SET nam = '"+ self.en +"' WHERE nam = '"+ self.o +"' ")
                self.cur.execute("UPDATE moshakhasat SET family = '"+ self.enu +"' WHERE family = '"+ self.o1 +"'  ")
                self.cur.execute("UPDATE moshakhasat SET shomare = '"+ self.enum +"' WHERE shomare = '"+ self.o2 +"'  ")
                self.conn.commit()


            self.nameentry.delete(0,END)
            self.numberentry.delete(0,END)

            

            self.root3.mainloop()



    def exit(self):
        self.cur.close()
        self.root.destroy()
        
    

play = gui()
