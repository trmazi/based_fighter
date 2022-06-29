from os.path import exists
import sqlite3, json

from game.validated import ValidatedDict

class coreSQL():
    '''
    Core SQL datas, like connections.
    '''
    def __init__ (self):
        self.db_path = './assets/db/game.db'

    def makeConnection(self):
        return sqlite3.connect(self.db_path)

    def checkForDB(self):
        '''
        Checks to see if the database file exists.
        '''
        database_exists = exists(self.db_path)
        if database_exists:
            return True
        else: return False

class gameDatabaseAccess():
    '''
    Class that lets the game access the db.
    '''
    def __init__ (self):
        dbclass = coreSQL()
        self.connection = coreSQL.makeConnection(dbclass)
        self.cursor = self.connection.cursor()

    def loadStage(self, stageID):
        '''
        Given a stageID, return data for it.
        '''
        self.cursor.execute(f"SELECT * FROM stages where id={stageID}")
        result = self.cursor.fetchone()

        if result is None:
            self.connection.close()
            return None

        stageID, stagename, filename, data = result
        self.connection.close()
        return ValidatedDict({
            'id': stageID,
            'name': stagename,
            'filename': filename, 
            'data': json.loads(data)
        })

    def loadAllStages(self):
        '''
        Given nothing, return a list of the stages.
        '''
        self.cursor.execute(f"SELECT * FROM stages")
        result = self.cursor.fetchall()

        for stage in result:
            print(stage)