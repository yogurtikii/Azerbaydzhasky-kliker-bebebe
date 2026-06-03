import customtkinter
from PIL import Image
import time
import random
import shelve
import os
from CTkMessagebox import CTkMessagebox
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
    cena = db["cena"]
    profit = db["profit"]
    rep = db["rep"]
    proc = db["proc"]
    choise = db["choise"]
    cheats = db["cheats"]
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
    db["cena"] = 0
    db["profit"] = 0
    db["rep"] = 0
    db["proc"] = 0
    db["choise"] = "Нет"
    db["cheats"] = False
    ka, ur, den, rabotau, rabota = 0, 0, 0, 1, 1
    kopatik, strimik = False, False
    kar, ura, balance, timer = 22, 50, 500, 0.0
    cena, profit, rep, proc, choise = 0, 0, 0, 0, "Нет"
    cheats = False
    db.close()
i = 0
i1 = 0
i2 = 0
ran = 0
rand = 0
geti = ""
ins = []
summ = 0
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
            up.configure(values=[f"Работник на поле азербайджанской картошки: +1 картошка за один урожай (Стоимость - {balance} деняк).", "Работник на урановые рудники: Позволяет копать уран (Стоимость - 5000 деняк).","Сосед, работающий на урановом руднике: +1 к урану за камень (Стоимость - 5000)","Капитанчик, который сидит в подвале: позволяет снимать стримы (надо кликнуть 10 раз на кнопку)(Стоимость - 10000 деняк)."])
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
    global mf, den, go, ka, ur, rabotau, rabota, kopatik, strimik, kar, ura, balance, timer, cena, profit, rep, proc, choise
    if den >= 1000000:
        mf.destroy()
        go.configure(text_color="#57A3F2", text=f"Поздравляю вы прошли игру! \n Спасибо за игру! \n Чтоб у вас дома всегда была азербайджанская картошка! \n Выши сохранения были очщенны \n Вам теперь доступны читы!", font=customtkinter.CTkFont(size=19, weight="bold"))
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
        db["cena"] = 0
        db["profit"] = 0
        db["rep"] = 0
        db["proc"] = 0
        db["choise"] = "Нет"
        db["cheats"] = True
        ka, ur, den, rabotau, rabota = 0, 0, 0, 1, 1
        kopatik, strimik = False, False
        kar, ura, balance, timer = 22, 50, 500, 0.0
        cena, profit, rep, proc, choise = 0, 0, 0, 0, "Нет"
        cheats = True
        db.close()
    else:
        r.after(1, check)
def autosave():
    global savel, ka, ur, den, rabotau, rabota, kopatik, strimik, kar, ura, balance, timer, cena, profit, rep, proc, choise
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
        db["cena"] = cena
        db["profit"] = profit
        db["rep"] = rep
        db["proc"] = proc
        db["choise"] = choise
    savel.configure(text="Сохранено!")
    r.after(2000, lambda: savel.configure(text="..."))
    r.after(10000, autosave)
def sosed():
    global ka, kartoshka, rand
    if ka != 0:
        kart=random.randint(1, ka)
        msg = CTkMessagebox(
        title="Сосед!", 
        message=f"К вам пришел сосед и попросил в долг {kart} картошки, отдать?", 
        icon="question",
        option_1="Отдать",
        option_2="Не отдавать"
    )
        if msg.get() == "Отдать":
            ka-=kart
            if random.randint(1, 100) <= 10:
                ka+=kart*3
                alert = CTkMessagebox(
                title="Сосед!", 
                message="Вам отдали х3 картошки!", 
                icon="info",
                option_1="OK"
            )
            else:
                aler = CTkMessagebox(
                title="Сосед!", 
                message="Вам не отдали ничего!", 
                icon="info",
                option_1="OK"
            )
            kartoshka.configure(text=f"🥔 Азербайджанской картошки : {ka}")
    rand = random.randint(30000, 120000)
    r.after(rand, sosed)
def com():
    global profit, cena, kar, rand, rep, proc, choise
    randch = random.randint(1, 2)
    profit = random.randint(60, 90)
    proc = random.randint(20, 50)
    proc = round(proc*0.01, 2)
    cena = random.randint(kar - random.randint(1, 3), kar + random.randint(1, 10))
    grocery_chains = ["Пятёрочка", "Магнит", "Перекрёсток", "Чижик", "Красное & Белое", "Бристоль", "Лента", "ВкусВилл", "Ашан", "Дикси", "Монетка", "Да!", "О’КЕЙ", "METRO Cash & Carry", "Ярче!", "Спар (SPAR)", "Азбука Вкуса", "Глобус", "Магнит Семейный", "Самокат"]
    choise=random.choice(grocery_chains)
    if randch == 1:
        msg = CTkMessagebox(
        title=f"{choise}", 
        message=f"К вам пришел представитель компаниии {choise}, и предложил забирать каждый день у тебя {proc*100}% картошки, и отдавать {profit}% от дохода продавая картошку по {cena} деняк, согласиться?", 
        icon="question",
        option_1="Согласиться",
        option_2="Не cоглашаться"
    )
        if msg.get() == "Согласиться":
            rep=100
            r.after(60000, yes)
            kontl.configure(text=f"Контракт с {choise} \n Забирают картошки в день: {proc*100}% \n Комиссия: {100-profit}% \n Продают картошку по {cena} деняк \n Репутации: {rep}")
        else:
            rand = random.randint(120000, 300000)
            r.after(rand, com)
            cena, profit, rep, proc, choise = 0, 0, 0, 0, "Нет"
    else:
        rand = random.randint(120000, 300000)
        r.after(rand, com)
def yes():
    global ka, rep, cena, den, rand, proc, profit, choise
    if rep != 0:
        if ka < 5:
            if ka == 0:
                rep-=10
                msg = CTkMessagebox(
                title="Потеря потерь", 
                message=f"Вы потеряли: 10 репутации \n Сейчас репутации: {rep}", 
                icon="info",
                option_1="OK",
            )
                kontl.configure(text=f"Контракт с {choise} \n Забирают картошки в день: {proc*100}% \n Комиссия: {100-profit}% \n Продают картошку по {cena} деняк \n Репутации: {rep}")
            else:
                rep-=10
                msg = CTkMessagebox(
                title="Потеря потерь", 
                message=f"Вы потеряли: 10 репутации \n Сейчас репутации: {rep}", 
                icon="info",
                option_1="OK",
            )
                msg = CTkMessagebox(
                title="Отчет", 
                message=f"Отчет за продажи: \n Упаковки: -18 деняк \n Картошки продано: {round(ka*(proc))} \n Денег получено: {round(round(ka*proc)*cena*(profit/100))} \n Итого: {round(round(ka*proc)*cena*(profit/100))-18}", 
                icon="info",
                option_1="OK",
            )
                den+=round(round(ka*(proc))*cena*(profit/100))-18
                ka-=round(ka*proc)
                kontl.configure(text=f"Контракт с {choise} \n Забирают картошки в день: {proc*100}% \n Комиссия: {100-profit}% \n Продают картошку по {cena} деняк \n Репутации: {rep}")
        else:
            msg = CTkMessagebox(
            title="Отчет", 
            message=f"Отчет за продажи: \n Упаковки: -18 деняк \n Картошки продано: {round(ka*(proc))} \n Денег получено: {round(round(ka*proc)*cena*(profit/100))} \n Итого: {round(round(ka*proc)*cena*(profit/100))-18}", 
            icon="info",
            option_1="OK",
        )
            rep+=2
            den+=round(round(ka*(proc))*cena*(profit/100))-18
            ka-=round(ka*proc)
        kontl.configure(text=f"Контракт с {choise} \n Забирают картошки в день: {proc*100}% \n Комиссия: {100-profit}% \n Продают картошку по {cena} деняк \n Репутации: {rep}")
        dengi.configure(text=f"💵 Деняк : {den}")
        kartoshka.configure(text=f"🥔 Азербайджанской картошки : {ka}")
        if rep != 0:
            r.after(60000, yes)
        else:
            msg = CTkMessagebox(
            title="Плаки плаки", 
            message=f"С вами разорвали контракт! \n К вам могут прийти новые представители!", 
            icon="info",
            option_1="OK",
        )
            cena, profit, rep, proc, choise = 0, 0, 0, 0, "Нет"
            rand = random.randint(120000, 300000)
            r.after(rand, com)
            kontl.configure(text=f"Контракт с {choise} \n Забирают картошки в день: {proc*100}% \n Комиссия: {100-profit}% \n Продают картошку по {cena} деняк \n Репутации: {rep}")
def kont():
    global rep, rand
    msg = CTkMessagebox(
        title="Внимание!", 
        message=f"Вы хотите рассторгнуть контракт, вы уверенны?", 
        icon="warning",
        option_1="ОК",
        option_2="ОТМЕНА"
    )
    if msg.get() == "ОК":
        msg = CTkMessagebox(
        title="Плаки плаки", 
        message=f"Вы разорвали контракт! \n К вам могут прийти новые представители!", 
        icon="info",
        option_1="OK",
    )
        cena, profit, rep, proc, choise = 0, 0, 0, 0, "Нет"
        kontl.configure(text=f"Контракт с {choise} \n Забирают картошки в день: {proc*100}% \n Комиссия: {100-profit}% \n Продают картошку по {cena} деняк \n Репутации: {rep}")
        rand = random.randint(120000, 300000)
        r.after(rand, com)
def invs():
    global geti, inc, komps, inw
    inw = customtkinter.CTkToplevel(r)
    inw.title("Инвестиции 📈")
    inw.geometry('300x300')
    inw.configure(fg_color="#1a1a1a")
    inw.resizable(False, False)
    inww = customtkinter.CTkLabel(inw, text_color="#57A3F2", text=" Выберете компанию и сумму вклада: \n Через минуту деньги зачислятся на баланс", font=customtkinter.CTkFont(size=10, weight="bold"))
    inww.pack(pady=5, padx=20)
    inc = customtkinter.CTkEntry(inw, placeholder_text="Сумма")
    inc.pack(pady=10)
    komps = customtkinter.CTkOptionMenu(inw, values=["50% на повышенеие, 50% на понижение, разброс цен маленький", "75% на понижение, 25% на повышение, разброс цен средний", "90% на понижение, 10% на повышение, разброс цен большой", "99% на понижение, 1% на повышение, разброс цен огромный"], width=200, dynamic_resizing=True)
    komps.set("Компании")
    komps.pack(pady=10, padx=5)
    invb = customtkinter.CTkButton(inw, text="Выбрать", fg_color="#57A3F2", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=15), command=invok)
    invb.pack(anchor="center", pady=0, padx=20)
def mini():
    global den, summ, ins
    if random.randint(1, 2) == 1:
        rando=random.randint(1, 100)
        den+=rando
        ins.append(f"Инвестиции: +{rando}")
    else:
        rando=random.randint(1, 100)
        den-=rando
        ins.append(f"Инвестиции: -{rando}")
    den+=summ
    dengi.configure(text=f"💵 Деняк : {den}")
    inso.configure(values=ins)
def sred():
    global den, summ, ins
    if random.randint(1, 4) == 1:
        rando=random.randint(1, 1000)
        den+=rando
        ins.append(f"Инвестиции: +{rando}")
    else:
        rando=random.randint(1, 1000)
        den-=rando
        ins.append(f"Инвестиции: -{rando}")
    den+=summ
    dengi.configure(text=f"💵 Деняк : {den}")
    inso.configure(values=ins)
def big():
    global den, summ, ins
    if random.randint(1, 10) == 1:
        rando=random.randint(1, 10000)
        den+=rando
        ins.append(f"Инвестиции: +{rando}")
    else:
        rando=random.randint(1, 10000)
        den-=rando
        ins.append(f"Инвестиции: -{rando}")
    den+=summ
    dengi.configure(text=f"💵 Деняк : {den}")
    inso.configure(values=ins)
def gigant():
    global den, summ, ins
    if random.randint(1, 100) == 1:
        rando=random.randint(1, 100000)
        den+=rando
        ins.append(f"Инвестиции: +{rando}")
    else:
        rando=random.randint(1, 100000)
        den-=rando
        ins.append(f"Инвестиции: -{rando}")
    den+=summ
    dengi.configure(text=f"💵 Деняк : {den}")
    inso.configure(values=ins)
def invok():
    global geti, inc, komps, inw, den, ins, inv, summ
    geti=komps.get()
    summ=int(inc.get())
    den-=summ
    dengi.configure(text=f"💵 Деняк : {den}")
    inw.destroy()
    inv.configure(state="disabled")
    if geti == "50% на повышенеие, 50% на понижение, разброс цен маленький":
        r.after(60000, mini)
    elif geti == "75% на понижение, 25% на повышение, разброс цен средний":
        r.after(60000, sred)
    elif geti == "90% на понижение, 10% на повышение, разброс цен большой":
        r.after(60000, big)
    elif geti == "99% на понижение, 1% на повышение, разброс цен огромный":
        r.after(60000, gigant)
    else:
        den+=summ
    r.after(120000, lambda: inv.configure(state="normal"))
def reset():
    global ka, ur, den, rabotau, rabota, kopatik, strimik, kar, ura, balance, timer, cena, profit, rep, proc, choise
    msg = CTkMessagebox(
        title="Внимание!", 
        message=f"Вы хотите обнулить сохранения, вы уверены?", 
        icon="warning",
        option_1="OK",
        option_2="ОТМЕНА"
    )
    if msg.get() == "OK":
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
        db["cena"] = 0
        db["profit"] = 0
        db["rep"] = 0
        db["proc"] = 0
        db["choise"] = "Нет"
        ka, ur, den, rabotau, rabota = 0, 0, 0, 1, 1
        kopatik, strimik = False, False
        kar, ura, balance, timer = 22, 50, 500, 0.0
        cena, profit, rep, proc, choise = 0, 0, 0, 0, "Нет"
        db.close()
        r.destroy()
def setd():
    global den, che
    try:
        den=int(che.get())
        dengi.configure(text=f"💵 Деняк : {den}")
    except ValueError:
        print(".")
def setk():
    global ka, chke
    try:
        ka=int(chke.get())
        kartoshka.configure(text=f"🥔 Азербайджанской картошки : {ka}")
    except ValueError:
        print(".")
def setu():
    global ur, chue
    try:
        ur=int(chue.get())
        uran.configure(text=f"⛏ Урана : {ur}")
    except ValueError:
        print(".")
def kops():
    global chkob, kopatik
    kopatik=bool(chkob.get())
def strs():
    global chstb, strimik
    strimik=bool(chstb.get())
def setura():
    global ura, churae
    try:
        ura=int(churae.get())
        tutu.configure(text=f"1 уран - от 22 до {ura} деняк")
    except ValueError:
        print(".")
def setkar():
    global kar, chkare
    try:
        kar=int(chkare.get())
        tutk.configure(text=f"1 картошка - от 1 до {kar} деняк")
    except ValueError:
        print(".")
def cheatsd():
    global che, chke, chue, chkob, chstb, churae, chkare
    ch = customtkinter.CTkToplevel(r)
    ch.title("Читы")
    ch.geometry('600x600')
    ch.configure(fg_color="#1a1a1a")
    ch.resizable(False, False)
    
    chdf = customtkinter.CTkFrame(ch, fg_color="#383838", corner_radius=15)
    chdf.pack(pady=5, padx=10)
    che = customtkinter.CTkEntry(chdf, placeholder_text="Колво деняк:")
    che.pack(pady=5, padx=10, side = "left")
    chdb = customtkinter.CTkButton(chdf, text="Установить", fg_color="#a6d388", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=14), command=setd) 
    chdb.pack(padx=10, side="left")

    chkf = customtkinter.CTkFrame(ch, fg_color="#383838", corner_radius=15)
    chkf.pack(pady=5, padx=10)
    chke = customtkinter.CTkEntry(chkf, placeholder_text="Колво картошки:")
    chke.pack(pady=5, padx=10, side = "left")
    chkb = customtkinter.CTkButton(chkf, text="Установить", fg_color="#a6d388", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=14), command=setk) 
    chkb.pack(padx=10, side="left")

    chuf = customtkinter.CTkFrame(ch, fg_color="#383838", corner_radius=15)
    chuf.pack(pady=5, padx=10)
    chue = customtkinter.CTkEntry(chuf, placeholder_text="Колво урана:")
    chue.pack(pady=5, padx=10, side = "left")
    chub = customtkinter.CTkButton(chuf, text="Установить", fg_color="#a6d388", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=14), command=setu) 
    chub.pack(padx=10, side="left")
    
    chkarf = customtkinter.CTkFrame(ch, fg_color="#383838", corner_radius=15)
    chkarf.pack(pady=5, padx=10)
    chkare = customtkinter.CTkEntry(chkarf, placeholder_text="Макс. цена на картошку")
    chkare.pack(pady=5, padx=10, side = "left")
    chkarb = customtkinter.CTkButton(chkarf, text="Установить", fg_color="#a6d388", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=14), command=setkar) 
    chkarb.pack(padx=10, side="left")
    
    churaf = customtkinter.CTkFrame(ch, fg_color="#383838", corner_radius=15)
    churaf.pack(pady=5, padx=10)
    churae = customtkinter.CTkEntry(churaf, placeholder_text="Макс. цена на уран")
    churae.pack(pady=5, padx=10, side = "left")
    churab = customtkinter.CTkButton(churaf, text="Установить", fg_color="#a6d388", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=14), command=setura) 
    churab.pack(padx=10, side="left")
    
    chkof = customtkinter.CTkFrame(ch, fg_color="#383838", corner_radius=15)
    chkof.pack(pady=5, padx=10)
    chkoe = customtkinter.CTkLabel(chkof, text_color="#57A3F2", text="Можно копать уран", font=customtkinter.CTkFont(size=11, weight="bold"))
    chkoe.pack(pady=5, padx=10, side = "left")
    vako = customtkinter.IntVar(value=0)
    chkob = customtkinter.CTkSwitch(chkof, onvalue=1, offvalue=0, command=kops, variable=vako, text="") 
    chkob.pack(padx=10, side="left")
    
    chstf = customtkinter.CTkFrame(ch, fg_color="#383838", corner_radius=15)
    chstf.pack(pady=5, padx=10)
    chste = customtkinter.CTkLabel(chstf, text_color="#57A3F2", text="Можно стримить", font=customtkinter.CTkFont(size=11, weight="bold"))
    chste.pack(pady=5, padx=10, side = "left")
    vast = customtkinter.IntVar(value=0)
    chstb = customtkinter.CTkSwitch(chstf, onvalue=1, offvalue=0, command=strs, variable=vast, text="") 
    chstb.pack(padx=10, side="left")
    
r = customtkinter.CTk()
customtkinter.set_default_color_theme("green")
r.title("Симулятор Азербайджана")
r.geometry('750x750')
r.configure(fg_color="#1a1a1a")
r.resizable(False, False)

go = customtkinter.CTkLabel(r, text="")
go.pack()

mf = customtkinter.CTkFrame(r,fg_color="#242424", corner_radius=15 )
mf.pack(pady=5, padx=20, fill="both", expand=True)

well = customtkinter.CTkLabel(mf, text_color="#57A3F2", text="Симулятор Азербайджана", font=customtkinter.CTkFont(size=18, weight="bold"))
well.pack(pady=5, padx=20)

tutf = customtkinter.CTkFrame(mf,fg_color="#383838", corner_radius=15 )
tutf.pack(pady=5, padx=20, fill="both")

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

butons = customtkinter.CTkFrame(mf,fg_color="#383838", corner_radius=15 )
butons.pack(pady=5, padx=20, fill="both")

butons2 = customtkinter.CTkFrame(butons,fg_color="#474747", corner_radius=15 )
butons2.pack(pady=3, padx=5, fill="both")

sell = customtkinter.CTkButton(butons2, text="Продать все 📠", fg_color="#a6d388", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=24), command=sell)
sell.pack(anchor="w", pady=0, padx=10, side="left")

up = customtkinter.CTkOptionMenu(butons2, values=[f"Работник на поле азербайджанской картошки: +1 картошка за один урожай (Стоимость - {balance} деняк).", "Работник на урановые рудники: Позволяет копать уран (Стоимость - 5000 деняк).","Сосед, работающий на урановом руднике: +1 к урану за камень (Стоимость - 5000)","Капитанчик, который сидит в подвале: позволяет снимать стримы (надо кликнуть 10 раз на кнопку)(Стоимость - 10000 деняк)."], command=up, dynamic_resizing=True)
up.set("Улучшения")
up.pack(pady=5, side="left")

inv = customtkinter.CTkButton(butons2, text="Инвестиции 📈", fg_color="#57A3F2", width=100, text_color="#1a1a1a", font=customtkinter.CTkFont(size=15), command=invs)
inv.pack(anchor="w", pady=0, padx=10, side="left")

inso = customtkinter.CTkOptionMenu(butons2, values=ins, width=100, dynamic_resizing=True)
inso.set("История инвестиций")
inso.pack(pady=10, padx=5, side="left")

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

kontf = customtkinter.CTkFrame(mf,fg_color="#383838", corner_radius=15 )
kontf.pack(padx=20, fill="both")

dataf = customtkinter.CTkFrame(mf, fg_color="#383838", corner_radius=15)
dataf.pack(padx=20, pady=3, fill="both")

saveb = customtkinter.CTkButton(dataf, text_color="#1a1a1a", command=autosave, text="Сохраниться")
saveb.pack(pady=5, padx=5, side="left")

resetb = customtkinter.CTkButton(dataf, text_color="#1a1a1a", command=reset, text="Удалить сохранения", fg_color="#ff5858")
resetb.pack(pady=5, padx=5, side="left")

if cheats == True:
    cheatsb = customtkinter.CTkButton(dataf, text_color="#1a1a1a", command=cheatsd, text="Читы", fg_color="#f9de60", state="normal")
    cheatsb.pack(pady=5, padx=5, side="left")  
if rep == 0:
    cena, profit, rep, proc, choise = 0, 0, 0, 0, "Нет"

kontl = customtkinter.CTkLabel(kontf, text_color="#57A3F2", text=f"Контракт с {choise} \n Забирают картошки в день: {proc*100}% \n Комиссия: {100-profit}% \n Продают картошку по {cena} деняк \n Репутации: {rep}", font=customtkinter.CTkFont(size=16, weight="bold"))
kontl.pack(pady=5, padx=20)

kontb = customtkinter.CTkButton(kontf, text="Рассторгнуть контракт", fg_color="#57A3F2", width=200, text_color="#1a1a1a", font=customtkinter.CTkFont(size=24), command=kont)
kontb.pack(anchor="center", pady=5, padx=20)

r.after(60000, new_news)
r.after(1, check)
r.after(10000, autosave)
rand = random.randint(30000, 120000)
r.after(rand, sosed)
if rep == 0:
    rand = random.randint(120000, 300000)
    r.after(rand, com)
if rep != 0:
    r.after(60000, yes)
r.mainloop()
