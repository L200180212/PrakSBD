import tkinter as tk
import tkinter.messagebox
from tkinter import*
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Tiket_kereta"
    )

cursor = db.cursor()

class Pembelian:
    def __init__(self, master):
        self.master = master
        self.master.geometry('450x250')
        self.frame = Frame(self.master)
        self.frame.grid()

        title = Label(self.frame, text="Pendataan Pembelian Tiket", font=('Times', 16, 'bold'))
        l_id_penumpang = Label(self.frame, text="ID Penumpang", font=('Times', 12))
        l_id_tiket = Label(self.frame, text="ID Tiket", font=('Times', 12))
        l_berangkat = Label(self.frame, text="Tanggal Berangkat", font=('Times', 12))
        l_sampai= Label(self.frame, text="Tanggal Sampai", font=('Times', 12))
        
        title.grid(row=0, columnspan=4, pady=10)
        l_id_penumpang.grid(row=1, column=0, sticky=W, padx=3)
        l_id_buku.grid(row=2, column=0, sticky=W, padx=3)
        l_berangkat.grid(row=3, column=0, sticky=W, padx=3)
        l_sampai.grid(row=4, column=0, sticky=W, padx=3)
        
        
        #Entry dan posisi
        self.e_id_penumpang = Entry(self.frame, width=30)
        self.e_id_tiket = Entry(self.frame, width=30)
        self.e_berangkat= Entry(self.frame, width=30)
        self.e_sampai = Entry(self.frame, width=30)
        
        self.e_id_penumpang.grid(row=1, column=1, sticky=W, padx=10)
        self.e_id_tiket.grid(row=2, column=1, sticky=W, padx=10)
        self.e_berangkat.grid(row=3, column=1, sticky=W, padx=10)
        self.e_sampai.grid(row=4, column=1, sticky=W, padx=10)

        #Button dan posisi
        b_insert = Button(self.frame, text="Insert", command=self.insert_pembelian)
        b_update = Button(self.frame, text="Update", command=self.update_pembelian)
        b_show = Button(self.frame, text="Show", command=self.show_pembelian)

        b_insert.grid(row=5, column=0, pady=10, ipadx=10)
        b_update.grid(row=5, column=1, pady=10, ipadx=10)
        b_show.grid(row=5, column=2, pady=10, ipadx=10)
        
    def insert_pembelian(self):
        c = db.cursor()
        sql =f"INSERT INTO pembelian (`id_penumpangFK`,`id_tiketFK`,`tanggal_berangkat`, `tanggal_sampai`)VALUES('{self.e_id_penumpang.get()}','{self.e_id_tiket.get()}','{self.e_berangkat.get()}', '{self.e_sampai.get()}')"         
        c.execute(sql)
        db.commit()
        messagebox.showinfo("","Entry Data Berhasil")
    
    def update_pembelian(self):
        c = db.cursor()
        e1=self.e_id_penumpang.get()
        e2=self.e_id_tiket.get()
      
        sql =f"UPDATE pembelian SET id_tiketFK=%s where id_penumpangFK=%s"
        val = (e1,e2)
        c.execute(sql,val)
        db.commit()
        messagebox.showinfo("","Update Data Berhasil")

    def show_pembelian(self):
        pembelian = Tk()
        pembelian.title("Alur Pembelian Tiket")
        Label(pembelian, text="ID Penumpang").grid(row=0, column=0, sticky=W)
        Label(pembelian, text="ID Tiket").grid(row=0, column=1, sticky=W)
        Label(pembelian, text="Tanggal Berangkat").grid(row=0, column=2, sticky=W)
        Label(pembelian, text="Tanggal Sampai").grid(row=0, column=3, sticky=W)
        
        
        sql="select*from pembelian"
        c.execute(sql)
        pembelian = c.fetchall()

        for i in range(len(pembelian)):
            for j in range(len(pembelian[i])):
                teks=Entry(pembelian)
                teks.grid(row=i+1,column=j)
                teks.insert(END,pembelian[i][j])
    
