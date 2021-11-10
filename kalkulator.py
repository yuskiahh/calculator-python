from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("Calculator")
root.geometry("320x400")
root["bg"] = "white"

myfont = font.Font(size=15)

e = Entry(root, width=25, borderwidth=0)
e["font"] = myfont
e["bg"] = "white"
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)


def angka(nilai):
    sebelum = e.get()
    e.delete(0, END)
    e.insert(0, str(sebelum)+str(nilai))


def tambah():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = float(nomor_awal)
    e.delete(0, END)


def kurang():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = float(nomor_awal)
    e.delete(0, END)


def kali():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = float(nomor_awal)
    e.delete(0, END)


def bagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = float(nomor_awal)
    e.delete(0, END)

def pangkat():
    nomor_awal = e.get()
    global n_awal
    n_awal = float(nomor_awal)
    e.delete(0,END)
    e.insert(0,n_awal **2)

def akar():
    nomor_awal = e.get()
    global n_awal
    n_awal = float(nomor_awal)
    e.delete(0,END)
    e.insert(0,math.sqrt(n_awal))


def hapus():
    e.delete(0, END)


def samadengan():
    nomor_akhir = e.get()
    e.delete(0, END)
    if mtk == "penjumlahan":
        e.insert(0, n_awal + float(nomor_akhir))
    elif mtk == "pengurangan":
        e.insert(0, n_awal - float(nomor_akhir))
    elif mtk == "perkalian":
        e.insert(0, n_awal * float(nomor_akhir))
    elif mtk == "pembagian":
        try:
            hitung = n_awal / float(nomor_akhir)
            e.insert(0, hitung)
        except ZeroDivisionError:
            e.insert(0, "Tidak terdefinisi")


btn1 = Button(root, text="1", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka(1))
btn2 = Button(root, text="2", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka(2))
btn3 = Button(root, text="3", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka(3))
btn4 = Button(root, text="4", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka(4))
btn5 = Button(root, text="5", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka(5))
btn6 = Button(root, text="6", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka(6))
btn7 = Button(root, text="7", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka(7))
btn8 = Button(root, text="8", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka(8))
btn9 = Button(root, text="9", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka(9))
btn0 = Button(root, text="0", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka(0))
koma = Button(root, text=".", padx=30, bg="#c7c7c7",
              fg="#000000", pady=20, command=lambda: angka("."))

tambah = Button(root, text="+", padx=30, bg="#df52ff", fg="white", pady=20, command=tambah)
kurang = Button(root, text="-", padx=30, bg="#df52ff",fg="white", pady=20, command=kurang)
kali = Button(root, text="x", padx=30, bg="#df52ff", fg="white", pady=20, command=kali)
bagi = Button(root, text="/", padx=30, bg="#df52ff", fg="white", pady=20, command=bagi)
pangkat = Button(root,text="x2",padx = 30,bg="#df52ff",fg="white", pady = 20,command=pangkat)
akar = Button(root,text="sq2",padx = 25,bg="#df52ff",fg="white", pady = 20,command=akar)
hapus = Button(root, text="C", padx=30, bg="#df52ff", fg="white", pady=20, command=hapus)
samadengan = Button(root, text="=", padx=70, bg="#df52ff", fg="white", pady=20, command=samadengan)

btn1.grid(row=4, column=0, pady=2)
btn2.grid(row=4, column=1, pady=2)
btn3.grid(row=4, column=2, pady=2)
btn4.grid(row=3, column=0, pady=2)
btn5.grid(row=3, column=1, pady=2)
btn6.grid(row=3, column=2, pady=2)
btn7.grid(row=2, column=0, pady=2)
btn8.grid(row=2, column=1, pady=2)
btn9.grid(row=2, column=2, pady=2)
btn0.grid(row=5, column=1, pady=2)
koma.grid(row=5, column=0, pady=2)

tambah.grid(row=4, column=3, pady=2)
kurang.grid(row=3, column=3, pady=2)
kali.grid(row=2, column=3, pady=2)
bagi.grid(row=1, column=3, pady=2)
pangkat.grid(row=1, column=1, pady=2)
akar.grid(row=1, column=2, pady=2)
hapus.grid(row=1, column=0, pady=2)
samadengan.grid(row=5, column=2, pady=2, columnspan=4)


root.mainloop()
