import pygame, os

class systemTestMenu:
    '''
    Class for the system test menu. Lets you change settings of the game and whatnot. 
    Applies them to the database.
    '''

    def __init__(self, surface: pygame.surface.Surface, resolution: tuple, clock: pygame.time.Clock, framerate: int) -> None:
        self.testing = True
        self.test_state = None # If the test state is None, return the main test menu. Otherwise, render the test menu that we care about.

        self.surface = surface
        self.resolution = resolution
        self.clock = clock
        self.framerate = framerate

        # Now, we should load the system font path into a var. We'll do a simple check on it to be safe.
        font_path = './assets/fonts/testmenu.ttf'
        if os.path.exists(font_path):
            self.system_font = font_path
        else: raise Exception(f"Can't load the system test menu font! Please check that {font_path} exists!")

        self.mainTestMenu()

    def drawTestMenuText(self, text: str, color: tuple, surface: pygame.surface.Surface, x: int, y: int, size: int, align: int):
        font = pygame.font.Font(self.system_font, int(size*self.resolution[1]/768))
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()

        if align == 0:
            textrect.topleft = (x, y)
        elif align == 1:
            textrect.center = (x, y)
        elif align == 2:
            textrect.topright = (x, y)
        else: raise Exception('Unknown font position! Please use 0, 1, 2!')

        surface.blit(textobj, textrect)

    def eventHandler(self):
        '''
        Handles game events.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.testing = False
                print('thank you for playing!')
                pygame.display.quit()
                exit()

    def mainTestMenu(self):
        # First off, let's make sure that the screen has been wiped.
        self.surface.fill((0, 0, 0))

        test_options = [
            'Input Test',
            'Game Options',
            'Coin Options',
            'Network Options',
            'Input Options',
            'All Factory Settings'
        ]

        while self.test_state == None and self.testing != False:
            # Tick the clock for good luck!
            self.clock.tick(self.framerate)

            # Let's do an event check
            self.eventHandler()

            # Because test menu is in default state, load the main test menu.
            self.surface.fill((0, 0, 0))

            self.drawTestMenuText('Test Menu', (255, 255, 255), self.surface, self.resolution[0]/2, 40, 50, 1)

            buffer = int(100*self.resolution[1]/768)
            for option in test_options:
                self.drawTestMenuText(option, (255, 255, 255), self.surface, self.resolution[0]/2, buffer, 25, 1)
                buffer += int(25*self.resolution[1]/768)
            
            pygame.display.update()