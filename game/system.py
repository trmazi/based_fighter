import pygame, os

class systemTestMenu:
    '''
    Class for the system test menu. Lets you change settings of the game and whatnot. 
    Applies them to the database.
    '''

    def __init__(self, surface: pygame.surface.Surface, resolution: tuple, clock: pygame.time.Clock, framerate: int) -> None:
        self.testing = True
        self.current_select = 0
        self.len_settings = 0
        self.test_state = None # If the test state is None, return the main test menu. Otherwise, render the test menu that we care about.

        self.text_color = (255, 255, 255)
        self.surface = surface
        self.resolution = resolution
        self.clock = clock
        self.framerate = framerate

        # Now, we should load the system font path into a var. We'll do a simple check on it to be safe.
        font_path = './assets/fonts/testmenu.ttf'
        if os.path.exists(font_path):
            self.system_font = font_path
        else: raise Exception(f"Can't load the system test menu font! Please check that {font_path} exists!")
        
        pygame.display.set_caption('BasedFighter V0.1 (Test Menu)')
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2 and self.testing:
                    self.current_select = self.current_select+1 if self.current_select+1 < self.len_settings else 0
                if event.key == pygame.K_DOWN and self.testing:
                    self.current_select = self.current_select+1 if self.current_select+1 < self.len_settings else 0
                if event.key == pygame.K_UP and self.testing:
                    self.current_select = self.current_select-1 if self.current_select-1 >= 0 else self.len_settings-1
                if event.key == pygame.K_KP_ENTER and self.testing:
                    self.test_state = self.current_select

    def mainTestMenu(self):
        # First off, let's make sure that the screen has been wiped.
        self.surface.fill((0, 0, 0))

        test_options = [
            'Input Test',
            'Game Options',
            'Coin Options',
            'Network Options',
            'Input Options',
            'All Factory Settings',
            'Leave Test Mode'
        ]

        self.len_settings = len(test_options)
        self.current_select = 0

        while self.testing != False:
            # Tick the clock for good luck!
            self.clock.tick(self.framerate)

            # Let's do an event check
            self.eventHandler()

            # Because test menu is in default state, load the main test menu.
            self.surface.fill((0, 0, 0))

            self.drawTestMenuText('Test Menu', (255, 255, 255), self.surface, self.resolution[0]/2, 40, 50, 1)

            buffer = int(100*self.resolution[1]/768)
            index = 0
            for option in test_options:
                if index == self.current_select:
                    self.text_color = (255, 0, 0)
                self.drawTestMenuText(option, self.text_color, self.surface, self.resolution[0]/2, buffer, 25, 1)
                buffer += int(30*self.resolution[1]/768)
                self.text_color = (255, 255, 255)
                index +=1

            if self.test_state == 6:
                # We will now leave test mode.
                self.test_state = None
                self.surface.fill((0, 0, 0))
                print('Now leaving testing mode...')
                self.testing = False

            pygame.display.update()

        return None # Send the game back to an init state.