import tkinter as tk
import speedtest
from tkinter import messagebox

st = speedtest.Speedtest()
root=tk.Tk()
root.geometry("400x400")
root.title("Hız Ölçer")
root.configure(bg="black")
font=("Serif",15,"bold")

def check():
    messagebox.showinfo("Confirmation",'''Hız Testi Başlatılıyor...
1 Dakikaya Kadar Sürebilir''')

    d.configure(text=str(st.download()//10**6)+"Mbps")
    u.configure(text=str(st.upload()//10**6)+"Mbps")
    p.configure(text=str(int(st.results.ping))+"ms")
    l.configure(text="Test Başarılı")


dspeed=tk.Label(root,text="İndirme Hızı:",bg="black",fg="yellow",font=font)
dspeed.place(x=10,y=50)
d=tk.Label(root,text="0 Mbps",bg="black",fg="yellow",font=font)
d.place(x=250,y=50)

uspeed=tk.Label(root,text="Yükleme Hızı:",bg="black",fg="yellow",font=font)
uspeed.place(x=10,y=100)
u=tk.Label(root,text="0 Mbps",bg="black",fg="yellow",font=font)
u.place(x=250,y=100)

ping=tk.Label(root,text="Ping:",bg="black",fg="yellow",font=font)
ping.place(x=10,y=150)
p=tk.Label(root,text="0 ms",bg="black",fg="yellow",font=font)
p.place(x=250,y=150)

l=tk.Label(root,text="Hız Testini Başlatmak İçin Aşağağıdaki Butona Tıklayın",bg="black",fg="yellow",font=(15))
l.place(x=10,y=250)
b=tk.Button(root,text="Hız Testini Başlat",command=check,bg="Yellow",fg="black")
b.place(x=50,y=300,height=40,width=300)

h=tk.Label(root,text="by Daisyhax",bg="black",fg="yellow",font=(15))
h.place(x=300,y=360)


root.mainloop()

    