import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "28394784"))
    API_HASH = os.environ.get("API_HASH", "9544a3ad7d8660acbae0dcf553c808e5")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5847064573:AAGC0OerM5XtAjKjQ1JLy0jAKrkDcM3osI4")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1966376217")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://forward:forward@cluster1.pgynkyr.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste1")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'forward_files')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001795790118"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@nish_27_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
