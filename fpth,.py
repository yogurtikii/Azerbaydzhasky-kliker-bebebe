import customtkinter
from PIL import Image
import time
import random
import shelve
import os
if os.path.exists("data.db") or os.path.exists("data.db.dat"):
    db = shelve.open("data.db", flag='r')
    ka = db["ka"]
    ur = db["ur"]
    den = db["den"]
    rabota = db["rabota"]
    rabotau = db["rabotau"]
    kopatik = db["kopatik"]
    strimik = db["strimik"]
    kar = db["kar"]
    ura = db["ura"]
    balance = db["balance"]
    timer = db["timer"]
    db.close()
else:
    db = shelve.open("data.db", flag='c')
    db["ka"] = 0
    db["ur"] = 0
    db["den"] = 0
    db["rabotau"] = 1
    db["rabota"] = 1
    db["kopatik"] = False
    db["strimik"] = False
    db["kar"] = 22
    db["ura"] = 50
    db["balance"] = 500
    db["timer"] = 0.0
    
    ka, ur, den, rabotau, rabota = 0, 0, 0, 1, 1
    kopatik, strimik = False, False
    kar, ura, balance, timer = 22, 50, 500, 0.0
    db.close()
i = 0
i1 = 0
i2 = 0
ran = 0
rand = 0
def rast():
    global kartoshka, ka, i, rabota, rabotau
    i+=1
    if i==4:
        ka+=rabota
        kartoshka.configure(text=f"🥔 Азербайджанской картошки : {ka}")
        i=0
def up(sel):
    global up, den, rabota, kopatik, dengi, rabotau, strimik, balance
    sel=up.get()
    if sel == f"Работник на поле азербайджанской картошки: +1 картошка за один урожай (Стоимость - {balance} деняк).":
        if den >= balance:
            up.set("Улучшения")
            rabota+=1
            den-=balance
            dengi.configure(text=f"💵 Деняк : {den}")
            balance+=150
            up.configure(values=[f"Работник на поле азербайджанской картошки: +1 картошка за один урожай (Стоимость - {balance} деняк).", "Работник на урановые рудники: Позволяет копать уран (Стоимость - 5000 деняк).","Сосед, работающий на урановом руднике: +2 к урану за камень (Стоимость - 5000)","Капитанчик, который сидит в подвале: позволяет снимать стримы (надо кликнуть 10 раз на кнопку)(Стоимость - 10000 деняк)."])
        else:
            up.set("Нет деняк!")
            r.after(2000, lambda: up.set("Улучшения"))
    elif sel == "Работник на урановые рудники: Позволяет копать уран (Стоимость - 5000 деняк).":
        if den >= 5000:
            if kopatik != True:
                up.set("Улучшения")
                kopatik=True
                den-=5000
                dengi.configure(text=f"💵 Деняк : {den}")
            else:
                up.set("Улучшения")
        else:
            up.set("Нет деняк!")
            r.after(2000, lambda: up.set("Улучшения"))
    elif sel == "Капитанчик, который сидит в подвале: позволяет снимать стримы (надо кликнуть 10 раз на кнопку)(Стоимость - 10000 деняк).":
        if den >= 10000:
            if strimik != True:
                up.set("Улучшения")
                strimik=True
                den-=10000
                dengi.configure(text=f"💵 Деняк : {den}")
            else:
                up.set("Улучшения")
        else:
            up.set("Нет деняк!")
            r.after(2000, lambda: up.set("Улучшения"))
    elif sel == "Сосед, работающий на урановом руднике: +1 к урану за камень (Стоимость - 5000)":
        if den >= 5000:
            if kopatik == True:
                up.set("Улучшения")
                rabotau+=1
                den-=5000
                dengi.configure(text=f"💵 Деняк : {den}")
            else:
                up.set("Улучшения")
        else:
            up.set("Нет деняк!")
            r.after(2000, lambda: up.set("Улучшения"))
def kopat():
    global uran, ur, i1, kopatik, rabotau
    if kopatik == True:
        i1+=1
        if i1==4:
            ur+=rabotau
            uran.configure(text=f"⛏ Урана : {ur}")
            i1=0
def strim():
    global dengi, den, i2, strimik, ran, ops
    if strimik == True:
        i2+=1
        if i2==10:
            ran=random.randint(246,1000)
            den+=ran
            dengi.configure(text=f"💵 Деняк : {den}")
            i2=0
            
def sell():
    global den, dengi, ka, ur, uran, kartoshka, ran, ura, kar
    for i in range(ka):
        ran=random.randint(1,kar)
        den+=ran
    for i in range(ur):
        ran=random.randint(22,ura)
        den+=ran
    ka=0
    ur=0
    
    kartoshka.configure(text=f"🥔 Азербайджанской картошки : {ka}")

    uran.configure(text=f"⛏ Урана : {ur}")

    dengi.configure(text=f"💵 Деняк : {den}")

def new_news():
    global ran, ura, kar, tutk, tutu, news
    m=[]
    funny_news = ["Бакинский кот случайно выиграл партию в нарды, уронив кубики нужной стороной.","Учёные доказали: чай из стакана армуду автоматически становится в два раза вкуснее.","В Гяндже гранат вырос настолько круглым, что его по ошибке пытались использовать в футбольном матче.","Житель Баку установил рекорд, объяснив дорогу туристу, используя только жесты и слово 'проблема нет'.","На свадьбе в Шемахе танцевали так активно, что сейсмографы зафиксировали небольшое землетрясение.","В Ленкорани местный изобретатель создал устройство, которое автоматически добавляет сахар в чай — пока оно работает только с азербайджанским чаем.","Во дворе в Сумгаите голуби научились играть в домино — соседи утверждают, что птицы выигрывают чаще, чем проигрывают.","Таксисты в Баку начали использовать новый навигационный метод: вместо GPS они спрашивают дорогу у бабушек у подъезда — точность 100 %.","В Нахчыване кот занял место на лавочке в парке и не пускал никого два часа — оказалось, он ждал, пока принесут его любимый кебаб.","В Баку дворник случайно смахнул метлой с тротуара все листья — местные жители подозревают, что это была репетиция идеального осеннего дня.","В Мингечевире местный рыбак поймал рыбу, которая, по его словам, рассказала анекдот — свидетели утверждают, что шутка была действительно смешной.","В одном из бакинских дворов дедушка научил воробьёв играть в лото — теперь они собираются каждую неделю и громко обсуждают ставки.","В Шеки местный почтальон начал доставлять письма, привязывая их к голубям — голуби, правда, иногда возвращаются с ответами, которых никто не ждал.","В Масаллы жители заметили, что после дождя лужи принимают форму граната — учёные пока не могут объяснить это явление.","В Закатале кот залез на крышу и отказался спускаться, пока ему не принесут чай с вареньем — переговоры длились три часа и завершились успехом."]
    ran=random.randint(-10, 10)
    kar+=ran
    if kar < 1:
        kar=1
    if ran < 0:
        m.append(f"Картофельный профицит: рекордный урожай привел к принудительному снижению предельных розничных цен на корнеплод. Нынешняя макс. цена на картошку - {kar}")
    elif ran > 0:
        m.append(f"Цены на картофель устремились вверх: правительство пересмотрело верхний порог стоимости из-за острого дефицита продукции на рынке. Нынешняя макс. цена на картошку - {kar}")
    ran=random.randint(-10, 10)
    ura+=ran
    if ura < 22:
        ura=22
    if ran < 0:
        m.append(f"Урановый профицит: избыток сырья на мировом рынке спровоцировал резкое снижение предельных котировок на радиоактивный металл. Нынешняя макс. цена на уран - {ura}.")
    elif ran > 0:
        m.append(f"Глобальный дефицит урана: критическая нехватка стратегического сырья вынудила регуляторов резко поднять потолок отпускных цен. Нынешняя макс. цена на уран - {ura}")
    m.append(funny_news[random.randint(0,14)])
    tutk.configure(text=f"1 картошка - от 1 до {kar} деняк")
    tutu.configure(text=f"1 уран - от 22 до {ura} деняк")
    news.set("НОВЫЙ ДЕНЬ - НОВЫЕ НОВОСТИ")
    news.configure(values=m)
    r.after(2000, lambda: news.set("Новости Азебайджана лучши новость только у нас!"))
    r.after(60000, new_news)
def check():
    global mf, den, timer, timerl, go
    if den >= 1000000:
        mf.destroy()
        go.configure(text_color="#57A3F2", text=f"Поздравляю вы прошли игру! \n Спасибо за игру! \n Чтоб у вас дома всегда была азербайджанская картошка! \n Чтобы начать все заново удалите файлы \n в той же папке с игрой с названиями по типу data.db \n Расширения могут быть разными и файлов может быть несколько", font=customtkinter.CTkFont(size=19, weight="bold"))
        
    else:
        r.after(1, check)
def autosave():
    global savel
    # Сохранение через shelve
    with shelve.open("data.db", "c") as db:
        db["ka"] = ka
        db["ur"] = ur
        db["den"] = den
        db["rabotau"] = rabotau
        db["rabota"] = rabota
        db["kopatik"] = kopatik
        db["strimik"] = strimik
        db["kar"] = kar
        db["ura"] = ura
        db["balance"] = balance
        db["timer"] = timer
    savel.configure(text="Сохранено!")
    r.after(2000, lambda: savel.configure(text="..."))
    r.after(10000, autosave)
def sosed():
    global ka, kartoshka, rand
    if ka != 0:
        kart=random.randint(1, ka)
        dialog = customtkinter.CTkInputDialog(text = f"К вам пришел сосед и попросил {kart} картошки в кредит! Отдать?", title="Напиши да или нет: ")
        if dialog.get_input() == "да" or dialog.get_input() == "Да":
            ka-=kart
            if random.randint(1, 100) <= 10:
                ka+=kart*3
                dialog = customtkinter.CTkInputDialog(text = "Вам вернули х3 картофли (это окно закройте)")    
            else:
                dialog = customtkinter.CTkInputDialog(text = "Вам не вернули ничего (это окно закройте)")
            kartoshka.configure(text=f"🥔 Азербайджанской картошки : {ka}")
    rand = random.randint(30000, 120000)
    r.after(rand, sosed)
r = customtkinter.CTk()
customtkinter.set_default_color_theme("green")
r.title("Симулятор Азербайджана")
r.geometry('750x650')
r.configure(fg_color="#1a1a1a")
r.resizable(False, False)

go = customtkinter.CTkLabel(r, text="")
go.pack(pady=5, padx=20)

mf = customtkinter.CTkFrame(r,fg_color="#242424", corner_radius=15 )
mf.pack(pady=20, padx=20, fill="both", expand=True)

well = customtkinter.CTkLabel(mf, text_color="#57A3F2", text="Симулятор Азербайджана", font=customtkinter.CTkFont(size=18, weight="bold"))
well.pack(pady=5, padx=20)

tutf = customtkinter.CTkFrame(mf,fg_color="#383838", corner_radius=15 )
tutf.pack(pady=20, padx=20, fill="both")

tutk = customtkinter.CTkLabel(tutf, text_color="#57A3F2", text=f"1 картошка - от 1 до {kar} деняк", font=customtkinter.CTkFont(size=11, weight="bold"))
tutk.pack(pady=5, padx=20)

tutu = customtkinter.CTkLabel(tutf, text_color="#57A3F2", text=f"1 уран - от 22 до {ura} деняк", font=customtkinter.CTkFont(size=11, weight="bold"))
tutu.pack(pady=5, padx=20)

tuts = customtkinter.CTkLabel(tutf, text_color="#57A3F2", text=f"1 стрим - от 264 до 1000 деняк, + его не надо продавать", font=customtkinter.CTkFont(size=11, weight="bold"))
tuts.pack(pady=5, padx=20)

goal = customtkinter.CTkLabel(tutf, text_color="#57A3F2", text=f"Цель - 1000000 деняк", font=customtkinter.CTkFont(size=11, weight="bold"))
goal.pack(pady=5, padx=20)

news = customtkinter.CTkOptionMenu(tutf, values=[], width=500, dynamic_resizing=True)
news.set("Новости Азебайджана лучши новость только у нас!")
news.pack(pady=10, padx=5, side="left")

saveb = customtkinter.CTkButton(tutf, text_color="#1a1a1a", command=autosave, text="Сохраниться")
saveb.pack(pady=10, padx=5, side="left")

butons = customtkinter.CTkFrame(mf,fg_color="#383838", corner_radius=15 )
butons.pack(pady=20, padx=20, fill="both")

butons2 = customtkinter.CTkFrame(butons,fg_color="#474747", corner_radius=15 )
butons2.pack(pady=3, padx=125, fill="both")

sell = customtkinter.CTkButton(butons2, text="Продать все 📠", fg_color="#a6d388", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=24), command=sell)
sell.pack(anchor="w", pady=0, padx=20, side="left")

up = customtkinter.CTkOptionMenu(butons2, values=[f"Работник на поле азербайджанской картошки: +1 картошка за один урожай (Стоимость - {balance} деняк).", "Работник на урановые рудники: Позволяет копать уран (Стоимость - 5000 деняк).","Сосед, работающий на урановом руднике: +1 к урану за камень (Стоимость - 5000)","Капитанчик, который сидит в подвале: позволяет снимать стримы (надо кликнуть 10 раз на кнопку)(Стоимость - 10000 деняк)."], command=up, dynamic_resizing=True)
up.set("Улучшения")
up.pack(pady=5, side="left")

rastit = customtkinter.CTkButton(butons, text="Растить картофан 🥔", fg_color="#f9de60", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=24), command=rast)
rastit.pack(anchor="center", pady=5, padx=20)

kopat = customtkinter.CTkButton(butons, text="Копать уран ⛏", fg_color="#74ff17", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=24), command=kopat)
kopat.pack(anchor="center", pady=5, padx=20)

strimit = customtkinter.CTkButton(butons, text="Стримить 💻", fg_color="#57A3F2", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=24), command=strim)
strimit.pack(anchor="center", pady=5, padx=20)

info = customtkinter.CTkFrame(mf,fg_color="#383838", corner_radius=15 )
info.pack(pady=10, padx=20, fill="both")

kartoshka = customtkinter.CTkLabel(info, text_color="#f9de60", text=f"🥔 Азербайджанской картошки : {ka}")
kartoshka.pack(pady=10, padx=20, side="left")

uran = customtkinter.CTkLabel(info, text_color="#74ff17", text=f"⛏ Урана : {ur}")
uran.pack(pady=0, padx=20, side="left")

dengi = customtkinter.CTkLabel(info, text_color="#a6d388", text=f"💵 Деняк : {den}")
dengi.pack(pady=10, padx=20, side="left")

savel = customtkinter.CTkLabel(info, text_color="#494949", text="...")
savel.pack(pady=10, padx=10, side="left")

r.after(60000, new_news)
r.after(1, check)
r.after(10000, autosave)
rand = random.randint(30000, 120000)
r.after(rand, sosed)
r.mainloop()
