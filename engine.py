# Main game engine.
# This is what starts the game and calls out to all functions. 
# Essentially, this is the game.
import pygame
from dotenv import load_dotenv

# Start importing game libs
from game.screen import Screen
from game.db import coreSQL
from game.stages import Stages

class GameEngine():
    def __init__(self):
        self.run = True
        self.framerate = 60
        self.clock = pygame.time.Clock()
        self.screenclass = Screen()

    def startGame(self):
        # Init pygame
        pygame.init()

        # Init pygame screen, return
        return Screen.initScreen(self.screenclass)

    def eventHandler(self):
        '''
        Handles game events.
        Returns keydowns if needed.
        '''
        if pygame.event.get(pygame.QUIT):
            self.run = False

    def gameLoop(self, screen):
        '''
        The main game loop.
        '''
        while self.run:
            # First, we should start our loop with the event manager
            events = self.eventHandler()

            # Now, let's make sure that the game is locked to a framerate.
            self.clock.tick(self.framerate)

            # The last thing we want to do in our loop here is update the screen.
            pygame.display.update()

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
    engine = GameEngine()
    screen, screen_res = GameEngine.startGame(engine)

    # Temp!! load a stage
    Stages.loadStage(1, screen, screen_res)

    # Start the loop!
    GameEngine.gameLoop(engine, screen)

    # Game is over
    print('thank you for playing!')
    pygame.display.quit()
    exit()