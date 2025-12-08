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
        self.images = {}

    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event:
                return event
    
    def change_res(self, x, y):
        self.screen = pygame.display.set_mode((x, y))

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
    
    def load_image(self, img_name:str, img_path:str, img_width, img_height):
        self.images.update({img_name: pygame.image.load(img_path).convert_alpha()})
        self.images[img_name]  = pygame.transform.smoothscale(self.images[img_name], (img_width, img_height))
    
    def draw_image(self, img_name, x, y):
        self.render.blit(self.images[img_name], (x, y))

    def draw_text(self, text, surface, font, x, y, color, center) -> None:
        surf = font.render(text, True, color)
        rect = surf.get_rect()
        if center:
            rect.center = (x, y)
        else:
            rect.topleft = (x, y)
        surface.blit(surf, rect)
