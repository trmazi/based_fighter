import pygame

class Attract():
    '''
    The entire attract scene and all of its core funtions
    '''
    def __init__(self):
        self.run = True
        self.game_start = False
        self.framerate = 60
        self.clock = pygame.time.Clock()

    def eventHandler(self):
        '''
        Handles game events in attract mode.
        Returns states if needed.
        '''
        if pygame.event.get(pygame.QUIT):
            self.run = False

    def attractLoop(self, screen):
        '''
        The attract loop.
        Has the warning screen, title screen, demo play. 
        '''
        while self.run:
            # First, we should start our loop with the event manager
            events = self.eventHandler()

            # Now, let's make sure that the game is locked to a framerate.
            self.clock.tick(self.framerate)

            # The last thing we want to do in our loop here is update the screen.
            pygame.display.update()