import pygame, os
from screeninfo import get_monitors

class Screen():
    def __init__(self):
        self.is_window = os.getenv('IS_WINDOW', 'true')
        self.fs_screen = int(os.getenv('FS_SCREEN', 0))
        self.is_borderless = os.getenv('IS_BORDERLESS', 'false')
        self.window_width = int(os.getenv('WINDOW_WIDTH', 1000))
        self.window_height = int(os.getenv('WINDOW_HEIGHT', 600))
        self.use_vsync = os.getenv('USE_VSYNC', 'false')
        self.pygame_flags = 0
        self.icon = pygame.image.load('./assets/icons/icon.png')

    def initScreen(self):
        # start display
        pygame.display.init()

        if self.is_window.lower() == 'false':
            monitors = get_monitors()
            if len(monitors) < self.fs_screen:
                raise Exception('Your screen variable is too large! Please recheck FS_SCREEN in the .env!')
            
            display = monitors[self.fs_screen]
            self.window_height = display.height
            self.window_width = display.width
            self.pygame_flags = pygame.FULLSCREEN|pygame.NOFRAME

        elif self.is_borderless.lower() == 'true':
            self.pygame_flags = pygame.NOFRAME

        if self.use_vsync.lower() == 'true':
            self.use_vsync = 1
        else:
            self.use_vsync = 0

        # We should init the caption and icon before the screen runs.
        pygame.display.set_caption('BasedFighter V0.1 (soon...)')
        pygame.display.set_icon(self.icon)

        # Start the screen
        screen = pygame.display.set_mode((self.window_width, self.window_height), self.pygame_flags, display=self.fs_screen, vsync=self.use_vsync)
        return (screen, (self.window_width, self.window_height))