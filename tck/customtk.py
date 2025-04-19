from  customtkinter import*
from PIL import Image
from socket import*#імпортуємо моудль
import threading
from translate import Translator
translator = Translator(from_lang="ru", to_lang="en")

client = socket(AF_INET , SOCK_STREAM)
# client.connect(("6.tcp.eu.ngrok.io",17952))
client.connect(("localhost",12345))

normal_nik = "user1"
load_image = Image.open("Imagee.png")#загрузка фото
img = CTkImage(light_image=load_image,size= (50,50))#тоже загрузка
windows = CTk()
windows.configure(fg_color="blue")
windows.title("пупсичек")
windows.geometry("390x500")
f1 = CTkFrame(windows,width=350,height=380,fg_color="black")#f = фрейм
f1.pack_propagate(False)
f2 = CTkFrame(windows,width=350,height=60)
f2.pack_propagate(False)

def recive():
    while 1:
        try:
            prinyat_sms = client.recv(1024).decode()
            gde_smotret_tekst.configure(state="normal")
            gde_smotret_tekst.insert(END,"server:" + prinyat_sms + "\n")
            gde_smotret_tekst.configure(state='disable')
        except:
            pass    
threading.Thread(target=recive).start()#поток

def click():#когда нажимаеш на кнопку чтоб переносился текст
    
    sms = ent.get()
    client.send(sms.encode())
    ent.delete(0,END)
    gde_smotret_tekst.configure(state="normal")
    gde_smotret_tekst.insert(END,normal_nik + sms + "\n")
    gde_smotret_tekst.configure(state='disable')

    try:#ето трай для того чтоб можно было поменять ник
        if sms == "00":
            neww_win = CTkToplevel()
            neww_win.configure(fg_color="blue")
            neww_win.title("Вибір кольору")
            neww_win.geometry("300x200")
            def change_us():
                global normal_nik
                normal_nik = us_entry.get()
                neww_win.destroy()
                
            us_entry = CTkEntry(neww_win, placeholder_text="Введи новій нік", width=200, height=40)
            us_entry.pack(pady=20)

            us_btn = CTkButton(neww_win, text="Змінити нік", command=change_us)
            us_btn.pack(pady=10)

    except:
        pass

    try:#етот трай для того чтоб поменять задний фон
        if sms == "0":
            new_win = CTk()
            new_win.configure(fg_color="blue")
            new_win.title("Вибір кольору")
            new_win.geometry("300x200")
            def change_bg():
                color_text = color_entry.get()
                try:
                    color_eng = translator.translate(color_text).lower()
                    windows.configure(fg_color=color_eng)
                except:
                     pass

            color_entry = CTkEntry(new_win, placeholder_text="Введи колір", width=200, height=40)
            color_entry.pack(pady=20)

            color_btn = CTkButton(new_win, text="Змінити колір", command=change_bg)
            color_btn.pack(pady=10)

            new_win.mainloop()
    except:
        pass

def on_enter(event):#текст только вместо кнопки ентер
    click()
ent = CTkEntry(f2,placeholder_text="ТЕКСТ ТУТ",width=230,height=40,)
ent.bind("<Return>", on_enter)

ent.pack(side='left')
b1 = CTkButton(f2,text="S E N D",image = img,compound="right",width=10, command=click)
b1.pack(side = "right")
f1.pack(pady = 20)
f2.pack(pady = 20)
gde_smotret_tekst = CTkTextbox(f1,state='disable', width=300, height=360,)
gde_smotret_tekst.configure(state="normal")  
gde_smotret_tekst.insert(END, "якщо тобі не подобається фон віправ 0 та напиши який колір ти хочешь(можно як на російсікій та і на англ,щоб змінити нік відправ 00)\n")  
gde_smotret_tekst.configure(state="disable")  
gde_smotret_tekst.pack()



windows.mainloop()
