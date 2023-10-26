import pygame
import random



class Componenta:
    # Asta e functia de initializare a componentei, are x si y coordonate , side_lenght e dimensiunea(e patrat)
    # target_x si target_y sunt coordonatele unde trebuie sa ajunga si tolerance e cat de departe poate sa fie de acele coord pana isi da
    # lock in singura 
    def __init__(self, x, y, lungime,latime, target_x, target_y, tolerance, image_path ,questions=None):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(x, y, lungime,latime)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))  # Redimensionare imagine
        self.dragging = False
        self.offset = None
        self.target_x = target_x
        self.target_y = target_y
        self.tolerance = tolerance
        self.locked = False
        self.check = False
        self.questions=questions 
    # asta pur si simplu deseneaza patratele
    def draw(self, window):
        window.blit(self.image, self.rect)


    @staticmethod
    def display_message(window, message,color=(255,255,255)):
        font = pygame.font.Font("OpenSans-Regular.ttf", 24)
        text = font.render(message, True, color)
        text_rect = text.get_rect(center=window.get_rect().center)
        window.blit(text, text_rect)

    #afiseaza pop up-ul cu intrebarea dupa ce piesa a fost pusa corect
    def show_popup(self, window):
        if self.locked:
            # Alegerea unei întrebări aleatoare
            question, correct_answer = random.choice(list(self.questions.items()))

            font = pygame.font.Font("OpenSans-Regular.ttf", 24)
            text = font.render(question, True, (10, 10, 10))
            text_rect = text.get_rect()
            text_rect.center=window.get_rect().center

            pygame.draw.rect(window, (255, 255, 255), text_rect.inflate(200,50))
            pygame.draw.rect(window, (10, 10, 10), text_rect.inflate(200,50), 2)
            window.blit(text, text_rect)

            pygame.display.flip()

            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a or event.key == pygame.K_f:
                            if (event.key == pygame.K_a and correct_answer == "A") or (event.key == pygame.K_f and correct_answer == "F"):
                                self.check = True  # Adăugarea punctului la scor
                                message= "Raspuns corect!"
                                color=(0,255,0)
                            else:
                                message="Raspuns gresit!"
                                color=(255,0,0)
                            waiting = False
            pygame.draw.rect(window,(255,255,255),text_rect.inflate(200,50))
            pygame.draw.rect(window, (10, 10, 10), text_rect.inflate(200,50), 2)
            Componenta.display_message(window,message,color)
            pygame.display.flip()
            pygame.time.wait(2000)
                    

    # functia asta se apeleaza cand ruleaza codul si daca e locked nu mai poti face nmc 
    def handle_event(self, event,window):
        self_name = [name for name, obj in locals().items() if obj is self][0]
        if self.locked:
            return
        
    # daca nu e locked si eventul e un click stanga(mousebutton 1) se activeza draggingu
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.dragging = True
                self.offset = (self.rect.x - event.pos[0], self.rect.y - event.pos[1])
    # apoi cand nu mai e apasat click verifica unde se afla si daca e langa coord target isi da lock si se face verde
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
                if abs(self.rect.x - self.target_x) <= self.tolerance and abs(self.rect.y - self.target_y) <= self.tolerance:
                    self.locked = True
                    self.rect.x = self.target_x
                    self.rect.y = self.target_y
                    self.color = (0, 255, 0)
                    if self.questions:
                        self.show_popup(window) # adaugarea afisarii pop-up-ului
                    
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.rect.x = event.pos[0] + self.offset[0]
                self.rect.y = event.pos[1] + self.offset[1]
    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.dragging = False
        self.locked = False
        self.check = False