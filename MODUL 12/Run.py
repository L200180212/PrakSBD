import tkinter as tk
import tkinter.messagebox
from tkinter import*
import mysql.connector
from penumpang_table import Penumpang
from tiket_table import Tiket
from pembelian_table import Pembelian


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Tiket_kereta"
    )

c=db.cursor()
root=tk.Tk()

def run():
    UI=FPage(root)
    cursor=db.cursor()

class FPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.master.config(bg = 'white')
        self.frame = Frame(self.master, bg = 'white')
        self.frame.pack()
        
        title = Label(self.frame, text='SELAMAT DATANG', font=('Times', 18, 'bold'))
        title.pack()
        title2 = Label(self.frame, text='Pilih Menu', font=('Times', 14))
        title2.pack(pady=20)
        btnPenumpang = Button(self.frame, text="Penumpang", font=(18), command=self.Penumpang)
        btnPenumpang.pack(anchor=CENTER, pady=10, ipadx=9)
        btnTiket = Button(self.frame, text="Tiket", font=(18), command=self.Tiket)
        btnTiket.pack(anchor=CENTER, pady=10, ipadx=20)
        btnPembelian = Button(self.frame, text="Pembelian", font=(18), command=self.Pembelian)
        btnPembelian.pack(anchor=CENTER, pady=10, ipadx=15)

    def Penumpang(self):
        self.Penumpang=Toplevel(self.master)
        self.UI=Penumpang(self.Penumpang)

    def Tiket(self):
        self.Tiket=Toplevel(self.master)
        self.UI=Tiket(self.Tiket)

    def Pembelian(self):
        self.Pembelian=Toplevel(self.master)
        self.UI=Pembelian(self.Pembelian)

run()
