import tkinter as tk
import tkinter.messagebox
from tkinter import*
import mysql.connector
from tiket_del import delete_tiket

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tiket_kereta"
    )

cursor = db.cursor()

class Tiket:
    def __init__(self, master):
        self.master = master
        self.master.title("Database Tiket")
        self.master.geometry('300x300')
        self.frame = Frame(self.master)
        self.frame.grid()

        title = Label(self.frame, text="Database Tiket", font=('Times', 16, 'bold'))
        l_id= Label(self.frame, text="ID Tiket", font=('Times', 12))
        l_nama = Label(self.frame, text="Nama kereta", font=('Times', 12))
        l_kelas = Label(self.frame, text="Kelas", font=('Times', 12))
        l_asal = Label(self.frame, text="Asal", font=('Times', 12))
        l_tujuan = Label(self.frame, text="Tujuan", font=('Times', 12))
        l_no = Label(self.frame, text="Nomor Kursi", font=('Times', 12))
        
        title.grid(row=0, columnspan=4, pady=10)
        l_id.grid(row=1, column=0, sticky=W, padx=3)
        l_nama.grid(row=2, column=0, sticky=W, padx=3)
        l_kelas.grid(row=3, column=0, sticky=W, padx=3)
        l_asal.grid(row=4, column=0, sticky=W, padx=3)
        l_tujuan.grid(row=5, column=0, sticky=W, padx=3)
        l_no.grid(row=6, column=0, sticky=W, padx=3)
        
        #Entry dan posisi
        self.e_id = Entry(self.frame, width=30)
        self.e_nama = Entry(self.frame, width=30)
        self.e_kelas = Entry(self.frame, width=30)
        self.e_asal = Entry(self.frame, width=30)
        self.e_tujuan = Entry(self.frame, width=30)
        self.e_no = Entry(self.frame, width=30)
        
        self.e_id.grid(row=1, column=1, sticky=W, padx=10)
        self.e_nama.grid(row=2, column=1, sticky=W, padx=10)
        self.e_kelas.grid(row=3, column=1, sticky=W, padx=10)
        self.e_asal.grid(row=4, column=1, sticky=W, padx=10)
        self.e_tujuan.grid(row=5, column=1, sticky=W, padx=10)
        self.e_no.grid(row=6, column=1, sticky=W, padx=10)


        #Button dan posisi
        b_insert = Button(self.frame, text="Insert", command=self.insert_tiket)
        b_update = Button(self.frame, text="Update", command=self.update_tiket)
        b_show = Button(self.frame, text="Show", command=self.show_tiket)
        b_delete = Button(self.frame, text="Delete", command=self.delete_tiket)
        

        b_insert.grid(row=7, column=0, pady=10, ipadx=10)
        b_update.grid(row=7, column=1, pady=10, ipadx=10)
        b_show.grid(row=8, column=1, pady=10, ipadx=10)
        b_delete.grid(row=8, column=0, pady=10, ipadx=10)
        
    def insert_tiket(self):
        cursor = db.cursor()
        sql =f"INSERT INTO tiket (`id_tiket`,`nama_kereta`,`kelas`, `asal`, `tujuan`, 'no_kursi')VALUES('{self.e_id.get()}','{self.e_nama.get()}','{self.e_kelas.get()}', '{self.e_asal.get()}', '{self.e_tujuan.get()}', '{self.e_no.get()}')"         
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo("","Entry Data Berhasil")
        
    
    def update_tiket(self):
        c = db.cursor()
        e1=self.e_nama.get()
        e2=self.e_kelas.get()
        e3=self.e_asal.get()
        e4=self.e_tujuan.get()
        e5=self.e_no.get()
        e6=self.e_id.get()
        sql =f"UPDATE tiket SET nama_kereta=%s, kelas=%s ,asal=%s, tujuan=%s, no_kursi=%s where id_tiket=%s"
        val = (e1,e2,e3,e4,e5,e6)
        c.execute(sql,val)
        db.commit()
        messagebox.showinfo("","Update Data Berhasil")

    def show_tiket(self):
        c = db.cursor()
        show = Tk()
        show.title("Data Tiket")
        Label(show, text="ID Tiket").grid(row=0, column=0, sticky=W)
        Label(show, text="Nama Kereta").grid(row=0, column=1, sticky=W)
        Label(show, text="Kelas").grid(row=0, column=2, sticky=W)
        Label(show, text="Asal").grid(row=0, column=3, sticky=W)
        Label(show, text="Tujuan").grid(row=0, column=4, sticky=W)
        Label(show, text="Nomor kursi").grid(row=0, column=5, sticky=W)

        
        sql="select*from tiket"
        c.execute(sql)
        Buku = c.fetchall()

        for i in range(len(tiket)):
            for j in range(len(tiket[i])):
                teks=Entry(show)
                teks.grid(row=i+1,column=j)
                teks.insert(END,tiket[i][j])

    def delete_tiket(self):
        self.delete_tiket=Toplevel(self.master)
        self.UI=delete_tiket(self.delete_tiket)
        
        
    
