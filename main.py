import pygame
import pygame_menu
from button import Button
import componenta
from componenta import Componenta

pygame.init()

width, height = 1280 , 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Componenta Corecta")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray  =(150, 150, 150)
# Crearea dicționarului cu întrebări și răspunsuri
questions_procesor = {
"Procesorul este creierul computerului? (A/F)": "A",
"Procesorul este responsabil pentru stocarea datelor? (A/F)": "F",
"Procesorul se ocupă cu executarea instrucțiunilor? (A/F)": "A",
"Procesorul gestionează direct afișarea grafică? (A/F)": "F",
"Procesorul utilizează BIOS pentru a se inițializa? (A/F)": "A",
"Procesorul este încorporat pe placa de bază a computerului? (A/F)": "A",
"Numărul de nuclee ale procesorului indică viteza acestuia? (A/F)": "F",
"Procesorul este responsabil pentru rețeaua computerului? (A/F)": "F",
"Procesoarele mai rapide consumă mai multă energie? (A/F)": "A",
"Frecvența procesorului măsoară viteza acestuia? (A/F)": "A",
"Procesoarele cu mai multe nuclee pot executa mai multe sarcini simultan? (A/F)": "A"
}

questions_placa_video = {
"Placa video este responsabilă pentru generarea imaginilor pe monitor? (A/F)": "A",
"Placa video stoca permanent datele? (A/F)": "F",
"Placa video execută codul programului? (A/F)": "F",
"Placa video este necesară pentru a porni computerul? (A/F)": "F",
"Placa video utilizează RAM pentru funcționare? (A/F)": "A",
"Placa video este o componentă necesară pentru gaming de înaltă calitate? (A/F)": "A",
"Placa video poate fi utilizată pentru a îmbunătăți performanța procesorului? (A/F)": "F"
}

questions_hdd = {
"HDD-ul este responsabil pentru stocarea permanentă a datelor? (A/F)": "A",
"HDD-ul este responsabil pentru procesarea datelor? (A/F)": "F",
"Viteza de rotație a HDD-ului afectează viteza de acces la date? (A/F)": "A",
"HDD-urile SSD sunt mai rapide decât HDD-urile tradiționale? (A/F)": "A",
"Toate computerele au nevoie de un HDD pentru a funcționa? (A/F)": "F",
"HDD-ul se poate degrada în timp, ceea ce poate duce la pierderea datelor? (A/F)": "A",
"HDD-urile pot fi utilizate pentru a îmbunătăți performanța procesorului? (A/F)": "F"
}

questions_sursa = {
"Sursa furnizează energie componentelor PC-ului? (A/F)": "A",
"Sursa este responsabilă pentru procesarea datelor? (A/F)": "F",
"Puterea sursei de alimentare trebuie să fie adecvată pentru componentele PC-ului? (A/F)": "A",
"Sursa poate influența performanța computerului? (A/F)": "A",
"Sursa este necesară pentru a porni computerul? (A/F)": "A",
"Sursa poate preveni supratensiunea și proteja componentele PC-ului? (A/F)": "A",
"Sursa poate îmbunătăți viteza de procesare a computerului? (A/F)": "F"
}

questions_ram = {
"RAM-ul este folosit pentru stocarea temporară a datelor? (A/F)": "A",
"RAM-ul păstrează datele și atunci când computerul este oprit? (A/F)": "F",
"Cantitatea de RAM afectează viteza computerului? (A/F)": "A",
"RAM-ul este responsabil pentru generarea imaginilor pe monitor? (A/F)": "F",
"RAM-ul este necesar pentru a porni computerul? (A/F)": "A",
"RAM-ul poate fi considerat memoria de lucru a computerului? (A/F)": "A",
"RAM-ul este un tip de stocare permanentă? (A/F)": "F",
"RAM-ul nu poate fi actualizat sau extins? (A/F)": "F",
"DDR, SDRAM, și RDRAM sunt tipuri de RAM? (A/F)": "A",
"Mai mult RAM înseamnă că poți rula mai multe programe simultan? (A/F)": "A",
"RAM-ul este doar responsabil pentru stocarea datelor, nu și pentru procesarea lor? (A/F)": "A",
"RAM-ul se măsoară în gigaocteți (GB)? (A/F)": "A",
"Toate datele din RAM se șterg atunci când repornești computerul? (A/F)": "A",
"Dacă RAM-ul este defect, computerul va funcționa normal? (A/F)": "F",
"RAM-ul cu viteza mai mare îmbunătățește performanța generală a computerului? (A/F)": "A",
"RAM-ul poate fi folosit pentru a stoca date în mod permanent? (A/F)": "F",
"RAM-ul poate fi folosit pentru a procesa date? (A/F)": "F",
"RAM-ul este responsabil pentru afișarea imaginilor pe monitor? (A/F)": "F"
}

questions_battery = {
"Bateria BIOS păstrează setările de bază ale sistemului când computerul este oprit? (A/F)": "A",
"Bateria BIOS este responsabilă pentru alimentarea procesorului? (A/F)": "F",
"Bateria BIOS poate fi înlocuită dacă se epuizează? (A/F)": "A",
"Bateria BIOS păstrează data și ora în computer? (A/F)": "A",
"O baterie BIOS obișnuită este o baterie litiu CR2032? (A/F)": "A",
"Bateria BIOS durează de obicei peste 10 ani? (A/F)": "A",
"Dacă bateria BIOS este scoasă, toate setările BIOS vor fi resetate la valorile implicite de fabrică? (A/F)": "A",
"Computerul nu va putea porni dacă bateria BIOS este scoasă? (A/F)": "F",
"Înlocuirea bateriei BIOS necesită rescrierea sau reconfigurarea manuală a BIOS-ului? (A/F)": "A",
"Bateria BIOS este necesară pentru funcționarea monitorului? (A/F)": "F",
"Bateria BIOS poate fi reîncărcată în timpul utilizării computerului? (A/F)": "F",
"Bateria BIOS poate fi folosită pentru a alimenta alte componente ale computerului? (A/F)": "F"
}

pygame.mixer.music.load("melodie.mp3")
pygame.mixer.music.play()

# Aici intializez componentele

procesor=Componenta(1191 , 360 , 89, 88, 419, 307, 50,"CPU.png",questions_procesor)
placa_video_side=Componenta(944 , 18, 336 , 206 , 226, 200, 50,"VIDEO_SIDE1.png",questions_placa_video)
hdd=Componenta(1169 , 75 , 109, 160, 658, 424, 20,"HDD.png",questions_hdd)
sursa=Componenta(1156 , 168 , 130 , 129 , 23, 12, 20,"SURSA.png",questions_sursa)
ram1_side=Componenta(1104 , 542  , 176 , 61, 358, 532, 50,"RAM_SIDE.png",questions_ram)
ram2_side=Componenta(1104 , 456  , 176 , 61, 358, 506, 50,"RAM_SIDE.png",questions_ram)
ram3_side=Componenta(1104 , 370  , 176 , 61, 358, 470, 50,"RAM_SIDE.png",questions_ram)
ram4_side=Componenta(1104 , 284  , 176 , 61, 358, 444, 50,"RAM_SIDE.png",questions_ram)
battery=Componenta(1174 , 671 , 37, 38, 140 , 377, 50,"BATERIE.png",questions_battery)

pin4=Componenta(1053,622,98,91,515,170,50,"4 pin_.png",None)
pin24=     Componenta(1069 ,332,211,160,  170,540,50,"24 pin_.png",None)
usb=       Componenta(1223,605,43 ,115,-10  ,465,50,"USB.png",None)
audio=     Componenta(1126,606,43 ,114,-12  ,432,50,"Audio.png",None)
cabluripow=Componenta(878 ,567,176,168,-10  ,390,50,"Cabluripow.png",None)
sata =  Componenta(1004 ,105,176,168,593  ,395,50,"SATA1.png",None)
cpufan=Componenta(1220,523,31,197,400,200,50,"CPU fan.png",None)
lvl1 = Button(1009,139,"LVL1.png",1)
lvl2 = Button(894,278,"LVL2.png",1)
#lvl2.lock()
lvl3 = Button(783,413,"LVL3.png",1)
#lvl3.lock()
options = Button(189,116,"OPTIONS.png",1)
quit = Button(196,377,"QUIT.png",1)
next_level_button = Button(795,244 , "NXT.png", 1)
main_menu_button = Button(263, 244, "MAIN.png", 1)
main_menu_button1=Button(457,160,"MAIN BUT.png",1)
main_menu_options= Button(568, 499, "MAIN MUSIC.png", 1)
musicon=Button(785, 210, "ON.png", 1)
musicoff=Button(244, 210, "OFF.png", 1)


nextlevel_imagine=pygame.image.load("MAIN-NXT.png")
final_image=pygame.image.load("MAIN1.png")
background_image = pygame.image.load("Backgroundlvl1.png")
BG2=pygame.image.load("Backgroundlvl2.png")
mainMenu = pygame.image.load("LVL SELECT.png")
BG3=pygame.image.load("Backgroundlvl3.png")
BGOptions=pygame.image.load("MUSIC.png")

componentelvl1 = [procesor,sursa,cpufan,pin4]
componentelvl2 = [placa_video_side,ram1_side,ram2_side,ram3_side,ram4_side,battery]
componentelvl3 = [hdd,pin24,usb,audio,cabluripow,sata]

scor = 10
def reset_lvl1():
    global scor
    scor = 10
    procesor.reset(1191 , 360)
    sursa.reset(1156 , 168 )
    cpufan.reset(1220,523)
    pin4.reset(1053,622)

def reset_lvl2():
    global scor
    scor = 30
    placa_video_side.reset(944 , 18)
    ram1_side.reset(1104 ,  542 )
    ram2_side.reset(1104 , 456 )
    ram3_side.reset(1104 ,  370 )
    ram4_side.reset(1104 , 284 )
    battery.reset(1174 , 671)


def reset_game():
    # Reset the score and any other game variables
    global scor
    scor = 10

    # Reset the component positions and unlock any locked levels
    procesor.reset(1191 , 360)
    sursa.reset(1156 , 168 )
    cpufan.reset(1220,523)
    pin4.reset(1053,622)
    placa_video_side.reset(944 , 18)
    ram1_side.reset(1104 ,  542 )
    ram2_side.reset(1104 , 456 )
    ram3_side.reset(1104 ,  370 )
    ram4_side.reset(1104 , 284 )
    battery.reset(1174 , 671)
    hdd.reset(1069 ,332)
    pin24.reset(1069 ,332)
    usb.reset(1223,605)
    audio.reset(1126,606)
    cabluripow.reset(878 ,567)
    sata.reset(1004 ,105)
    lvl1.unlock()
    lvl2.lock()
    lvl3.lock()

def display_final_score(window, score):
    font = pygame.font.Font(None, 100)  # Choose the font for the text
    text = font.render('Final Score: ' + str(score), True, (255, 255, 255))  # Create the text
    text_rect = text.get_rect()
    text_rect.center = (650,100)  # Center the text
    window.blit(text, text_rect)  # Draw the text

def display_score(window, score):
    font = pygame.font.Font(None, 50)  # Choose the font for the text
    text = font.render('Score: ' + str(score), True, (255, 255, 255))  # Create the text
    text_rect = text.get_rect()
    text_rect.topright = (window.get_width() - 600, 20)  # Set the top-right corner of the text rectangle
    window.blit(text, text_rect)  # Draw the text

# Aici se deseneaza toate chestiile initiale 
def draw_objectslvl1():
    window.fill((157, 219, 240))
    window.blit(background_image, (0, 0))
    for componenta in componentelvl1:
        componenta.draw(window)
    display_score(window,scor)
    pygame.display.update()

def draw_nextlvl():
    window.blit(nextlevel_imagine, (0, 0))
    next_level_button.update(window)
    main_menu_button.update(window)
    pygame.display.update()

def draw_nextlvl3():
    window.fill((0, 0, 0))
    window.blit(final_image, (0, 0))
    main_menu_button1.update(window)
    display_final_score(window, scor)
    pygame.display.update()


def draw_objectslvl2():
    window.fill((157, 219, 240))
    window.blit(BG2, (0, 0))
    for componenta in componentelvl2:
        componenta.draw(window)
    display_score(window,scor)
    pygame.display.update()

def draw_objectslvl3():
    window.fill((157, 219, 240))
    window.blit(BG3, (0, 0))
    for componenta in componentelvl3:
        componenta.draw(window)
    display_score(window,scor)
    pygame.display.update()

def draw_objectsoptions():
    window.fill((157, 219, 240))
    window.blit(BGOptions, (0, 0))
    main_menu_options.update(window)
    musicon.update(window)
    musicoff.update(window)
    pygame.display.update()

running = True
def optiuni():
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_options.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                if musicon.checkForInput(MENU_MOUSE_POS):  # Check if next level button is clicked
                    pygame.mixer.music.play()
                if musicoff.checkForInput(MENU_MOUSE_POS):  # Check if next level button is clicked
                    pygame.mixer.music.stop()
    
        draw_objectsoptions()

def next_level():
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.checkForInput(MENU_MOUSE_POS):
                    reset_lvl1()
                    main_menu()

                if next_level_button.checkForInput(MENU_MOUSE_POS):  # Check if next level button is clicked
                    level2()
        draw_nextlvl() 
        pygame.display.update()
        
def next_level3():
    global score
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button1.checkForInput(MENU_MOUSE_POS):
                    reset_game()
                    main_menu()
        draw_nextlvl3() 
        pygame.display.update()
        
def next_level2():
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.checkForInput(MENU_MOUSE_POS):
                    reset_lvl1()
                    reset_lvl2()
                    main_menu()

                if next_level_button.checkForInput(MENU_MOUSE_POS):  # Check if next level button is clicked
                    level3()
        draw_nextlvl() 
        pygame.display.update()


def level1():
    global scor
    if lvl1.locked == True:
        return
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            for componenta in componentelvl1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and componenta.rect.collidepoint(event.pos):
                        if componenta == pin4:
                            componenta.image = pygame.transform.scale(componenta.image, (29, 96))
                            componenta.image = pygame.image.load("4 pin top.png").convert_alpha()
                        if componenta == cpufan:
                            componenta.image = pygame.transform.scale(componenta.image, (21, 67))
                            componenta.image = pygame.image.load("fan toop.png").convert_alpha()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        componenta.handle_event(event, window)
                        if componenta == pin4 and pin4.locked==False:
                            componenta.image = pygame.image.load("4 pin_.png").convert_alpha()
                        if componenta == cpufan and cpufan.locked==False:
                            componenta.image = pygame.image.load("CPU fan.png").convert_alpha()

                componenta.handle_event(event, window)
                if componenta.locked == True and componenta.check == True:
                    scor += 10
                    componenta.check = False  # prevent adding score multiple times for the same component
                    draw_objectslvl1()  # redraw screen with updated score
            counter = 0
            for componenta in componentelvl1:
                if componenta.locked == True:
                    counter += 1
            if counter == len(componentelvl1):
                lvl2.unlock()
                for componenta in componentelvl1:
                    if componenta.check == True:
                        scor += 10
                next_level()
        draw_objectslvl1()
        pygame.display.flip()



def level2():
   global scor
   if lvl2.locked==True:
        return
   while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            for componenta in componentelvl2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and componenta.rect.collidepoint(event.pos):
                        if componenta==placa_video_side:
                            componenta.image = pygame.transform.scale(componenta.image, (29,244))
                            componenta.image = pygame.image.load("VIDEO_TOP.png").convert_alpha()
                        if componenta==ram1_side or componenta== ram2_side or componenta==ram3_side or componenta==ram4_side:
                            componenta.image = pygame.transform.scale(componenta.image, (176,61))
                            componenta.image = pygame.image.load("RAM_TOP.png").convert_alpha()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        componenta.handle_event(event, window)
                        if componenta == placa_video_side and placa_video_side.locked==False:
                            componenta.image = pygame.image.load("VIDEO_SIDE1.png").convert_alpha()
                        if componenta==ram1_side and ram1_side.locked==False:
                            componenta.image = pygame.image.load("RAM_SIDE.png").convert_alpha()
                        if componenta==ram2_side and ram2_side.locked==False:
                            componenta.image = pygame.image.load("RAM_SIDE.png").convert_alpha()
                        if componenta==ram3_side and ram3_side.locked==False:
                            componenta.image = pygame.image.load("RAM_SIDE.png").convert_alpha()
                        if componenta==ram4_side and ram4_side.locked==False:
                            componenta.image = pygame.image.load("RAM_SIDE.png").convert_alpha()
    
                componenta.handle_event(event,window)
                if componenta.locked == True and componenta.check == True:
                    scor += 10
                    componenta.check = False  # prevent adding score multiple times for the same component
                    draw_objectslvl1()  # redraw screen with updated score
            counter = 0
            for componenta in componentelvl2:
                if componenta.locked == True:
                  counter += 1
            if counter== len(componentelvl2):
                lvl3.unlock()
                for componenta in componentelvl2:
                    if componenta.check== True:
                        scor += 10
                next_level2()

        draw_objectslvl2()
        pygame.display.flip()


def level3():
    global scor
    if lvl3.locked==True:
        return
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            for componenta in componentelvl3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and componenta.rect.collidepoint(event.pos):
                        if componenta==usb:
                            componenta.image = pygame.transform.scale(componenta.image, (58,40))
                            componenta.image = pygame.image.load("usb top.png").convert_alpha()
                        if componenta==audio:
                            componenta.image = pygame.transform.scale(componenta.image, (61,40))
                            componenta.image = pygame.image.load("audio top.png").convert_alpha()
                        if componenta==cabluripow:
                            componenta.image = pygame.transform.scale(componenta.image, (21,67))
                            componenta.image = pygame.image.load("Cabluri.png").convert_alpha()
                        if componenta==pin24:
                            componenta.image = pygame.transform.scale(componenta.image, (61,51))
                            componenta.image = pygame.image.load("24 pin top.png").convert_alpha()
                        if componenta==sata:
                            componenta.image = pygame.transform.scale(componenta.image, (61,51))
                            componenta.image = pygame.image.load("sata.png").convert_alpha()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        componenta.handle_event(event, window)
                        if componenta==usb and usb.locked==False:
                            componenta.image = pygame.image.load("USB.png").convert_alpha()
                        if componenta==audio and audio.locked==False:
                            componenta.image = pygame.image.load("Audio.png").convert_alpha()
                        if componenta==cabluripow and cabluripow.locked==False:
                            componenta.image = pygame.image.load("Cabluripow.png").convert_alpha()
                        if componenta==pin24 and pin24.locked==False:
                            componenta.image = pygame.image.load("24 pin_.png").convert_alpha()
                        if componenta==sata and sata.locked==False:
                            componenta.image = pygame.image.load("SATA1.png").convert_alpha()
                componenta.handle_event(event,window)
                if componenta.locked == True and componenta.check == True:
                    scor += 10
                    componenta.check = False  # prevent adding score multiple times for the same component
                    draw_objectslvl1()  # redraw screen with updated score
            counter = 0
            for componenta in componentelvl3:
                if componenta.locked == True:
                  counter += 1
            if counter== len(componentelvl3):
                for componenta in componentelvl3:
                    if componenta.check== True:
                        scor += 10
                next_level3()

        draw_objectslvl3()

def main_menu():
    while True:
        window.fill((157, 219, 240))
        window.blit(mainMenu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for button in [lvl1,lvl2,lvl3,quit,options]:
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1.checkForInput(MENU_MOUSE_POS):
                    level1()
                if lvl2.checkForInput(MENU_MOUSE_POS):
                    level2()
                if lvl3.checkForInput(MENU_MOUSE_POS):
                    level3()
                if options.checkForInput(MENU_MOUSE_POS):
                    optiuni()
                if quit.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()

        pygame.display.update()

main_menu()
