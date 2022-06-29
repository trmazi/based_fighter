import pygame, os

from game.db import gameDatabaseAccess

class Stages():
    '''
    A class for dealing with stages.
    '''
    def loadStage(stage_id, surface: pygame.surface.Surface, screen_res: (tuple)):
        stageclass = gameDatabaseAccess()
        stage = gameDatabaseAccess.loadStage(stageclass, stage_id)

        if stage is None:
            raise Exception(f"Can't load stage {stage_id}! Please check the stage ID you're sending or refresh your repo!")
        
        # Let's load the stage texture
        filename = stage.get_str('filename')
        stage_loaded = pygame.image.load(f'./assets/stages/{filename}')
        print(f'Successfully loaded {filename}')

        # Now, let's throw this on the screen.
        stage_loaded = pygame.transform.smoothscale(stage_loaded, screen_res)
        surface.blit(stage_loaded, (0, 0))
        pygame.display.update()