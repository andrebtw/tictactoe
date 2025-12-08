from game_gui import game
import pygame

class Menu:
    def __init__(self, menu_name:str, menu_list:list, back_button:bool):
        self.name = menu_name
        self.menu_content = menu_list
        self.return_button = back_button
        self.text_surface = []
        self.text_rect = []
        
    def create_menu(self, surface, font, w, h):
        count = len(self.menu_content)
        line_height = font.get_linesize()
        spacing = int(line_height * 1.5)

        total_height = spacing * (count - 1)
        start_y = h // 2 - total_height // 2
        

        for i, menu in enumerate(self.menu_content):
            text_width, text_height = font.size(menu)
            print(text_width)
            self.text_surface.append(font.render(menu, True, (255, 255, 255)))
            y = start_y + i * spacing
            rect = self.text_surface[i].get_rect(center=(w // 2, y))
            self.text_rect.append(rect)
    
    def draw_menu(self, surface):
        for i, menu in enumerate(self.text_surface):
            surface.blit(self.text_surface[i], self.text_rect[i])
        
    def check_menu_click(self, event):
        # print("loop down")
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # scale mouse pointer to logical res of 1080p
            x, y = event.pos
            win_w, win_h = game.screen.get_size()
            x = x // (win_w / game.LOGICAL_WIDTH)
            y = y // (win_h / game.LOGICAL_HEIGHT)
            for i, menu in enumerate(self.text_surface):
                if self.text_rect[i].collidepoint((x, y)):
                    print(f"{self.menu_content[i]} clicked")
                    return self.menu_content[i]
        return None
