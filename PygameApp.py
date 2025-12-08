import pygame
import os

class PygameApp:
    def __init__(self, w:int, h: int, fullscreen:bool):
        pygame.init()
        self.LOGICAL_WIDTH = 1920
        self.LOGICAL_HEIGHT = 1080
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()
        self.running = True
        self.render = pygame.Surface((self.LOGICAL_WIDTH, self.LOGICAL_HEIGHT))
        self.base_dir = os.path.dirname(__file__)
        self.fonts = {}
        self.state = ""

    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event:
                return event
    
    def pygame_draw(self):
        win_w, win_h = self.screen.get_size()
        # print(win_w, win_h)
        scaled = pygame.transform.smoothscale(self.render, (win_w, win_h))
        self.screen.blit(scaled, (0, 0))

        pygame.display.flip()
        self.clock.tick(60)
    
    def add_font(self, font_name:str, font:str, font_size:int):
        self.fonts.update({font_name: pygame.font.Font( \
            os.path.join(self.base_dir,"fonts", font), font_size)})
    
    def pygame_close(self)->None:
        pygame.quit()