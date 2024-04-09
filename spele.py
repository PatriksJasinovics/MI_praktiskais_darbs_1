from customtkinter import *
import algoritmi

set_appearance_mode("light")
set_default_color_theme("green")
app = CTk()
app.geometry("900x600")
app.title("Praktiskais darbs 1")

#definē cik katram spēlētājam ir punkti spēles sākumā
global datora_sakuma_punkti
datora_sakuma_punkti = 50
global speletaja_sakuma_punkti
speletaja_sakuma_punkti = 50
global genereta_virkne
genereta_virkne = ""

#vai dators sāk spēli
global vai_dators_sak_speli
vai_dators_sak_speli = False
def dators_sak_speli():
    global vai_dators_sak_speli
    if checkbox.get():
        vai_dators_sak_speli = True
    else:
        vai_dators_sak_speli = False

#virknes garuma ievades lauku izvade uz ekrāna
slider_frame = CTkFrame(app, fg_color="transparent")
slider_frame.pack(pady=30)
#funkcija kas atgriež slīdmēra vērtību un izvada to uz ekrāna
def virknes_gar_izvele(garums):
    virknes_garums.configure(text=int(garums))

#virknes garuma izvēles slīdmēra nosaukums
slider_teksts = CTkLabel(slider_frame,
    text="Izvēlieties spēles skaitļu virknes garumu",
    font=("Segoe UI Semilight", 34))
slider_teksts.pack(pady=10)

#virknes garuma izvēles slīdmērs
slider = CTkSlider(slider_frame,
    from_=15,
    to=25,
    width=500,
    height=40,
    #ja grib lai slaideris iet pa vienības inkrementiem 
    #number_of_steps=10, 
    command = virknes_gar_izvele)

slider.pack(pady=20)
slider.set(20)

#teksta lauks virknes garumam
virknes_garums = CTkLabel(slider_frame,
    text="20",
    font=("Segoe UI Semibold", 32))
virknes_garums.pack()

checkbox = CTkCheckBox(slider_frame, 
    text = "Spēli pirmais sāk Dators",
    font=("Segoe UI", 24),
    checkbox_height=20,
    checkbox_width=20,
    command=dators_sak_speli)
checkbox.pack(pady=10)


#sākuma ekrāna pogu funkcionalitāte
def minimax_izsaukums():
    slider_frame.destroy()
    pogas_frame.destroy()
    global izveletais_algoritms
    izveletais_algoritms = "minimax"
    global genereta_virkne
    global datora_sakuma_punkti
    global speletaja_sakuma_punkti
    genereta_virkne = algoritmi.virknes_gen(int(slider.get()))
    veidot_speles_skatu_minimax(genereta_virkne, datora_sakuma_punkti, speletaja_sakuma_punkti)


def alpha_beta_izsaukums():
    slider_frame.destroy()
    pogas_frame.destroy()
    global izveletais_algoritms
    izveletais_algoritms = "alphabeta"
    global genereta_virkne
    global datora_sakuma_punkti
    global speletaja_sakuma_punkti
    genereta_virkne = algoritmi.virknes_gen(int(slider.get()))
    veidot_speles_skatu_alpha_beta(genereta_virkne, datora_sakuma_punkti, speletaja_sakuma_punkti)
    
#pogu izveide uz ekrāna
pogas_frame = CTkFrame(app, fg_color="transparent")
pogas_frame.pack(pady=20)

pogas_teksts = CTkLabel(pogas_frame,
    text="Izvēlieties datora algoritmu",
    font=("Segoe UI Semilight", 32))
pogas_teksts.pack(pady=10)

button = CTkButton(pogas_frame,
    text="Minimax",
    font=("Segoe UI", 28), 
    width=200,
    height=130,
    command=minimax_izsaukums)
button.pack(side = LEFT,
    padx=40,
    pady=7,
    anchor="center")
button = CTkButton(pogas_frame,
    text="Alpha-Beta",
    font=("Segoe UI", 28), 
    width=200,
    height=130,
    command=alpha_beta_izsaukums)
button.pack(side = LEFT,
    padx=40,
    pady=7,
    anchor="center")

#programmas footer jeb kājene
footer_frame = CTkFrame(app, fg_color="transparent")
footer_frame.pack(pady=10,
    side = BOTTOM,
    anchor= "s")
footer_teksts = CTkLabel(footer_frame,
    text="1. Praktiskais darbs, 42. komanda, Mākslīgā intelekta pamati, RTU 2024. gads",
    font=("Segoe UI Semilight", 18)).pack()

#definē spēles lauka izskatu, kur redzama izveidotā skaitļu virkne, abu spēlētāju punkti un gājienu izvēles pogas

#izveido datora gājiena teksta objektu, bet to nezīmē
gajiena_info_frame = CTkFrame(app, fg_color="transparent")
gajiena_info_data_frame = CTkFrame(gajiena_info_frame, fg_color="transparent")
global datora_gajiens
datora_gajiens = CTkLabel(gajiena_info_data_frame,
    text="nav", #jānomaina uz patieso datora pirmo gājienu
    font=("Segoe UI Semibold", 28))

#izveido skaitļu virknes teksta objektu, bet to nezīmē
skaitlu_virkne_frame = CTkFrame(app, 
        fg_color="transparent")
global skaitlu_virkne
skaitlu_virkne = CTkLabel(skaitlu_virkne_frame,
        font=("Segoe UI", 40),
        text=" ".join(str(genereta_virkne))
        )
global speles_title
speles_title = CTkLabel(skaitlu_virkne_frame,
    text="Ģenerētā skaitļu virkne",
    font=("Segoe UI Semilight", 28))

#izveido datoru un spēlētāja punktu teksta objektus, bet to nezīmē
global datora_punkti
datora_punkti = CTkLabel(gajiena_info_data_frame,
    text=str(datora_sakuma_punkti),
    font=("Segoe UI Semibold", 28))

global speletaja_punkti
speletaja_punkti = CTkLabel(gajiena_info_data_frame,
    text=str(speletaja_sakuma_punkti),
    font=("Segoe UI Semibold", 28))
#izveido gājiena pogas objektu, bet to nezīmē
global gajiena_pogas_frame
gajiena_pogas_frame = CTkFrame(app, fg_color="transparent")
global gajiena_pogas_title
gajiena_pogas_title = CTkLabel(gajiena_pogas_frame,
        text="Izvēlieties ciparu, kuru izņemt no skaitļu virknes",
        font=("Segoe UI Semilight", 24))



#izveido spēles beigu skatu, kad virknē vairs nav ciparu
def speles_iznakums(datora_punkti, speletaja_punkti):
    
    
    speles_title.pack_forget()
    skaitlu_virkne.configure(text="Spēles beigas! Skaitļu virkne ir tukša!",
            font=("Segoe UI Semibold", 35))
    poga_cipars_1.pack_forget()
    poga_cipars_2.pack_forget()
    poga_cipars_3.pack_forget()
    jaunas_speles_info = CTkLabel(gajiena_pogas_frame,
        text="Lai spēlētu vēlreiz, nepieciešams aizvērt šo logu un palaist programmu vēlreiz.",
        font=("Segoe UI Semilight", 20))
    jaunas_speles_info.pack(pady=30)
    
    

    if speletaja_punkti > datora_punkti: #spēlētājs uzvar
        print("cilveks uzvar")
        gajiena_pogas_title.configure(text="Spēlētājs uzvarēja!",
            font=("Segoe UI Semibold", 80),
            text_color="dark green")

    elif speletaja_punkti < datora_punkti: #dators uzvar
        print("dators uzvar")
        gajiena_pogas_title.configure(text="Dators uzvarēja!",
            font=("Segoe UI Semibold", 80),
            text_color="dark red")
    else: #neizšķirts
        print("neizšķirts")
        gajiena_pogas_title.configure(text="Neizšķirts!",
            font=("Segoe UI Semibold", 80))
        


def speles_skats(genereta_virkne):
    #skaitļu virknes lauka izveide un parādīšana
    skaitlu_virkne_frame = CTkFrame(app, 
        fg_color="transparent")
    skaitlu_virkne_frame.pack(pady=20)
    #virsraksts
    global speles_title
    speles_title = CTkLabel(skaitlu_virkne_frame,
        text="Ģenerētā skaitļu virkne",
        font=("Segoe UI Semilight", 28))
    speles_title.pack(pady=15)
    #skaitļu virkne
    #skaitļu virkne tiek ģenerēta ar ārējo funkciju no grupas biedra izveidotā alpha-beta algoritma faila
    global skaitlu_virkne
    skaitlu_virkne = CTkLabel(skaitlu_virkne_frame,
        font=("Segoe UI", 40),
        text=" ".join(str(genereta_virkne))
        )
    skaitlu_virkne.pack(pady=10)
    
    #izmaina skaitļu virkni pēc katra gājiena
    #skaitlu_virkne.configure(text=str(GameState.))

    #spēlētāju punktu un datora veiktā gājiena lauka izveide (pašreizējā gājiena info)
    gajiena_info_frame = CTkFrame(app, fg_color="transparent")
    gajiena_info_frame.pack(pady=15)

    gajiena_info_title_frame = CTkFrame(gajiena_info_frame, fg_color="transparent", border_width=2, border_color="black")
    gajiena_info_title_frame.pack(pady=15)

    speletaja_punkti_title = CTkLabel(gajiena_info_title_frame,
        text="Spēlētāja punkti",
        font=("Segoe UI Semibold", 28),
        text_color="dark green")
    speletaja_punkti_title.pack(side = LEFT,
        pady = 10,
        padx = 50
        )
    datora_gajiens_title = CTkLabel(gajiena_info_title_frame,
        text="Datora gājiens",
        font=("Segoe UI Semilight", 24))
    datora_gajiens_title.pack(side = LEFT,
        pady = 10,
        padx = 50
        )
    datora_punkti_title = CTkLabel(gajiena_info_title_frame,
        text="Datora punkti",
        font=("Segoe UI Semibold", 28),
        text_color="dark red")
    datora_punkti_title.pack(side = LEFT,
        pady = 10,
        padx = 50
        )
    
    gajiena_info_data_frame = CTkFrame(gajiena_info_frame, fg_color="transparent")
    gajiena_info_data_frame.pack(pady=5)
    
    global speletaja_punkti
    global speletaja_sakuma_punkti
    speletaja_punkti = CTkLabel(gajiena_info_data_frame,
        text=str(speletaja_sakuma_punkti),
        font=("Segoe UI Semibold", 28))
    speletaja_punkti.pack(side = LEFT,
        pady = 5,
        padx = 135
        )
    global datora_gajiens
    datora_gajiens = CTkLabel(gajiena_info_data_frame,
        text="nav", #jānomaina uz patieso datora pirmo gājienu
        font=("Segoe UI Semibold", 28))
    datora_gajiens.pack(side = LEFT,
        pady = 5,
        padx = 120
        )
    global datora_sakuma_punkti
    global datora_punkti
    datora_punkti = CTkLabel(gajiena_info_data_frame,
        text=str(datora_sakuma_punkti),
        font=("Segoe UI Semibold", 28))
    datora_punkti.pack(side = LEFT,
        pady = 5,
        padx = 135
        )

    #lietotāja iespējamo gājienu pogu lauka izveide
    global gajiena_pogas_frame
    gajiena_pogas_frame = CTkFrame(app, fg_color="transparent")
    gajiena_pogas_frame.pack(pady=25)
    global gajiena_pogas_title
    gajiena_pogas_title = CTkLabel(gajiena_pogas_frame,
        text="Izvēlieties ciparu, kuru izņemt no skaitļu virknes",
        font=("Segoe UI Semilight", 24))
    gajiena_pogas_title.pack(pady=10)

    #pārbauda vai cipars 1 vēl ir spēles skaitļu virknē
    if "1" in genereta_virkne:
        pogas_stavoklis = "normal"
    else:
        pogas_stavoklis = "disabled"
    global poga_cipars_1
    poga_cipars_1 = CTkButton(gajiena_pogas_frame,
        text="1",
        fg_color="#DDFFFF",
        hover_color="#49F6F6",
        width=130,
        height=100,
        border_width=2,
        border_color="black",
        text_color="black",
        font=("Segoe UI Semibold", 60),
        state=pogas_stavoklis,
        text_color_disabled="#808080",
        command=speletaja_gajiens1)
    poga_cipars_1.pack(side = LEFT,
        padx=60)
    
    #pārbauda vai cipars 2 vēl ir spēles skaitļu virknē
    if "2" in genereta_virkne:
        pogas_stavoklis = "normal"
    else:
        pogas_stavoklis = "disabled"
    global poga_cipars_2
    poga_cipars_2 = CTkButton(gajiena_pogas_frame,
        text="2",
        fg_color="#DDFFFF",
        hover_color="#49F6F6",
        width=130,
        height=100,
        border_width=2,
        border_color="black",
        text_color="black",
        font=("Segoe UI Semibold", 60),
        state=pogas_stavoklis,
        text_color_disabled="#808080",
        command=speletaja_gajiens2)
    poga_cipars_2.pack(side = LEFT,
        padx=60)
    
    #pārbauda vai cipars 3 vēl ir spēles skaitļu virknē
    if "3" in genereta_virkne:
        pogas_stavoklis = "normal"
    else:
        pogas_stavoklis = "disabled"
    global poga_cipars_3
    poga_cipars_3 = CTkButton(gajiena_pogas_frame,
        text="3",
        fg_color="#DDFFFF",
        hover_color="#49F6F6",
        width=130,
        height=100,
        border_width=2,
        border_color="black",
        text_color="black",
        font=("Segoe UI Semibold", 60),
        state=pogas_stavoklis,
        text_color_disabled="#808080",
        command=speletaja_gajiens3)
    poga_cipars_3.pack(side = LEFT,
        padx=60)

#pārbaude vai cipars ir skaitļu virknē un vai pogu nevajag izslēgt
def vai_poga_pieejama():
    global poga_cipars_1
    if "1" in speles_stavoklis.skaitli:
        poga_cipars_1.configure(state="normal")
    else:
        poga_cipars_1.configure(state="disabled")

    global poga_cipars_2
    if "2" in speles_stavoklis.skaitli:
        poga_cipars_2.configure(state="normal")
    else:
        poga_cipars_2.configure(state="disabled")
    
    global poga_cipars_3
    if "3" in speles_stavoklis.skaitli:
        poga_cipars_3.configure(state="normal")
    else:
        poga_cipars_3.configure(state="disabled")

def speletaja_gajiens1():

    global speles_stavoklis
    print("speletajs izvelejas ciparu 1")
    print(speles_stavoklis.datora_gajiens) #vajag but false
    
    
    #genereta_virkne = genereta_virkne.remove(1)
    speles_stavoklis = speles_stavoklis.make_move("1")
    global skaitlu_virkne
    skaitlu_virkne.configure(text=" ".join(str(speles_stavoklis.skaitli)))

    speletaja_punkti.configure(text=str(speles_stavoklis.player_punkti))
    #šito checku uzlikt arī pirms spēlētāja gājiena, jo dators var paņemt 
    # pēdējo ciparu un tad lietotājam nav iespēja to paņemt savā gājienā

    vai_poga_pieejama()
    global izveletais_algoritms

    if len(list(speles_stavoklis.skaitli)) != 0:
        if izveletais_algoritms == "minimax":
            datora_minimax_gajiens()
        else:
            datora_alphabeta_gajiens()

    else:
        
        speles_iznakums(speles_stavoklis.datora_punkti, speles_stavoklis.player_punkti)
        

        

def speletaja_gajiens2():

    global speles_stavoklis
    print("speletajs izvelejas ciparu 2")
    print(speles_stavoklis.datora_gajiens) #vajag but false
    
    speles_stavoklis = speles_stavoklis.make_move("2")

    global skaitlu_virkne
    skaitlu_virkne.configure(text=" ".join(str(speles_stavoklis.skaitli)))

    datora_punkti.configure(text=str(speles_stavoklis.datora_punkti))
    speletaja_punkti.configure(text=str(speles_stavoklis.player_punkti))

    vai_poga_pieejama()
    global izveletais_algoritms

    if len(list(speles_stavoklis.skaitli)) != 0:
        if izveletais_algoritms == "minimax":
            datora_minimax_gajiens()
        else:
            datora_alphabeta_gajiens()

    else:
        speles_iznakums(speles_stavoklis.datora_punkti, speles_stavoklis.player_punkti)
        

def speletaja_gajiens3():

    global speles_stavoklis
    print("speletajs izvelejas ciparu 3")
    print(speles_stavoklis.datora_gajiens) #vajag but false
    speles_stavoklis = speles_stavoklis.make_move("3")
    
    
    datora_punkti.configure(text=str(speles_stavoklis.datora_punkti))

    global skaitlu_virkne
    skaitlu_virkne.configure(text=" ".join(str(speles_stavoklis.skaitli)))

    
    #šito checku uzlikt arī pirms spēlētāja gājiena, jo dators var paņemt 
    # pēdējo ciparu un tad lietotājam nav iespēja to paņemt savā gājienā

    vai_poga_pieejama()
    global izveletais_algoritms

    if len(list(speles_stavoklis.skaitli)) != 0:
        if izveletais_algoritms == "minimax":
            datora_minimax_gajiens()
        else:
            datora_alphabeta_gajiens()

    else:
        speles_iznakums(speles_stavoklis.datora_punkti, speles_stavoklis.player_punkti)
        

def datora_minimax_gajiens():
    global speles_stavoklis
    print("datora gajiens")
    print(speles_stavoklis.datora_gajiens)

    global datora_esosais_gajiens
    datora_esosais_gajiens = algoritmi.best_moveM(speles_stavoklis)
    print(datora_esosais_gajiens)
    global datora_gajiens
    datora_gajiens.configure(text=datora_esosais_gajiens)

    speles_stavoklis = speles_stavoklis.make_move(datora_esosais_gajiens)

    global skaitlu_virkne
    skaitlu_virkne.configure(text=" ".join(str(speles_stavoklis.skaitli)))
    datora_punkti.configure(text=str(speles_stavoklis.datora_punkti))
    speletaja_punkti.configure(text=str(speles_stavoklis.player_punkti))

    vai_poga_pieejama()

    if len(list(speles_stavoklis.skaitli)) == 0:
        speles_iznakums(speles_stavoklis.datora_punkti, speles_stavoklis.player_punkti)

    

def datora_alphabeta_gajiens():
    global speles_stavoklis
    print("datora gajiens")
    print(speles_stavoklis.datora_gajiens)

    global datora_esosais_gajiens
    datora_esosais_gajiens = algoritmi.best_move(speles_stavoklis)
    print(datora_esosais_gajiens)
    global datora_gajiens
    datora_gajiens.configure(text=datora_esosais_gajiens)
    

    speles_stavoklis = speles_stavoklis.make_move(datora_esosais_gajiens)
    

    global skaitlu_virkne
    skaitlu_virkne.configure(text=" ".join(str(speles_stavoklis.skaitli)))
    datora_punkti.configure(text=str(speles_stavoklis.datora_punkti))
    speletaja_punkti.configure(text=str(speles_stavoklis.player_punkti))

    vai_poga_pieejama()

    if len(list(speles_stavoklis.skaitli)) == 0:
        speles_iznakums(speles_stavoklis.datora_punkti, speles_stavoklis.player_punkti)
        
    



#pēc algoritma izvēles izveidot spēles skatu 
def veidot_speles_skatu_minimax(genereta_virkne, datora_punkti_value, speletaja_punkti_value):
   
    print("minimax algoritms")

    speles_skats(genereta_virkne)

    global speles_stavoklis
    global vai_dators_sak_speli
    if vai_dators_sak_speli: #ja checkbox true tad dators sāk spēli
        print("datora pirmais gajiens")
        speles_stavoklis = algoritmi.AlphaBeta(genereta_virkne, datora_punkti_value, speletaja_punkti_value, True)
        global datora_esosais_gajiens
        datora_esosais_gajiens = algoritmi.best_moveM(speles_stavoklis)
        global datora_gajiens
        datora_gajiens.configure(text=datora_esosais_gajiens)
        speles_stavoklis = speles_stavoklis.make_move(datora_esosais_gajiens)
        global skaitlu_virkne
        global datora_punkti
        global speletaja_punkti
        skaitlu_virkne.configure(text=" ".join(str(speles_stavoklis.skaitli)))
        datora_punkti.configure(text=str(speles_stavoklis.datora_punkti))
        speletaja_punkti.configure(text=str(speles_stavoklis.player_punkti))

    else:
        speles_stavoklis = algoritmi.AlphaBeta(genereta_virkne, datora_punkti_value, speletaja_punkti_value, False)

    
    

def veidot_speles_skatu_alpha_beta(genereta_virkne, datora_punkti_value, speletaja_punkti_value):
    
    print("alpha-beta algoritms")
    
    speles_skats(genereta_virkne)
    
    global speles_stavoklis
    global vai_dators_sak_speli
    if vai_dators_sak_speli: #ja checkbox true tad dators sāk spēli
        print("datora pirmais gajiens")
        speles_stavoklis = algoritmi.AlphaBeta(genereta_virkne, datora_punkti_value, speletaja_punkti_value, True)
        global datora_esosais_gajiens
        datora_esosais_gajiens = algoritmi.best_move(speles_stavoklis)
        global datora_gajiens
        datora_gajiens.configure(text=datora_esosais_gajiens)
        speles_stavoklis = speles_stavoklis.make_move(datora_esosais_gajiens)
        global skaitlu_virkne
        global datora_punkti
        global speletaja_punkti
        skaitlu_virkne.configure(text=" ".join(str(speles_stavoklis.skaitli)))
        datora_punkti.configure(text=str(speles_stavoklis.datora_punkti))
        speletaja_punkti.configure(text=str(speles_stavoklis.player_punkti))

    else:
        speles_stavoklis = algoritmi.AlphaBeta(genereta_virkne, datora_punkti_value, speletaja_punkti_value, False)
    



#galvenā funkcija lai tiktu izvadīts spēles GUI
app.mainloop()