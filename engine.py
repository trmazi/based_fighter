# Main game engine.
# This is what starts the game and calls out to all functions. 
# Essentially, this is the game.
import pygame
from dotenv import load_dotenv

# Start importing game libs
from game.screen import Screen
from game.db import coreSQL

# Import scenes
from game.system import systemTestMenu

from game.stages import Stages

class GameEngine():
    def __init__(self):
        self.run = True
        self.framerate = 60
        self.clock = pygame.time.Clock()
        self.screenclass = Screen()

        # Let's start up the game.
        self.screen, self.resolution = self.startGame()

        # Current scene/screen state. Here's a list of them.
        # - STARTUP
        # - TESTMODE
        # - ATTRACT
        # - GAMEMODE
        # We will init this with None so that the engine can decide what to do.

        self.current_state = None
        self.current_events = None

        # Now, we begin the loop
        self.engineLoop()

    def startGame(self):
        # Init pygame
        pygame.init()

        # Init pygame screen, return
        return Screen.initScreen(self.screenclass)

    def eventHandler(self):
        '''
        Handles game events.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                print('thank you for playing!')
                pygame.display.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2 and self.current_state != 'TESTMODE':
                    self.current_state = 'TESTMODE'

    def engineLoop(self):
        '''
        The main loop of the engine. Everything is started by this loop.
        '''
        while self.run:
            # First, we should start our loop with the event manager
            self.eventHandler()

            # Now, let's make sure that the game is locked to a framerate.
            self.clock.tick(self.framerate)

            # Now, we just have to do whatever state the event manager is in.
            if self.current_state == None:
                pygame.display.set_caption('BasedFighter V0.1 (idle)')

                pass
            elif self.current_state == 'TESTMODE':
                print('Starting test mode...')
                systemTestMenu(self.screen, self.resolution, self.clock, self.framerate)
                self.current_state = None

if __name__ == "__main__":
    # load the .env
    env_state = load_dotenv()
    if not env_state:
        raise Exception('Failed to load the .env file! Please reload your repo.')

    # Init the DB
    dbclass = coreSQL()
    if not coreSQL.checkForDB(dbclass):
        raise Exception('Failed to find the game database! Please reload your repo.')

    # Call to the game
    GameEngine()

    # Game is over
    print('thank you for playing!')
    pygame.display.quit()
    exit()