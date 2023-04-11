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
    SESSION = os.environ.get("SESSION", "BQFIc8EAJLxzVMlO2Quz9g93XoZT5d-rKWcRLwMJY7Z6012scKUGqWzuLW5dhj7tdOWY3Rd1uqzPd5TDICkd_2E3geccllI63VTmz9jaHCdA9RFtguP8N54rryViqRRt6FUtWQehW2GVmBOAHqrUem56k1Fvvl5kcNYGEdNJiamAbMudY1PPGtEcLwLc1FX3AbX9lgwghvO9WLESx4mxTMHsuBNeTcYJ__5qdoSdBgynclH1P6koAR18ouKL5flZgtPp1e4SCcpqkeWQRAEeJXnlZFbDWOlX5uauuYzbkbSm6nRx6JTaRqjJakmmhr453MLOWYq1BF_sXWl5ZEhxbNCGndplWAAAAABF5vF9AA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001795790118"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@nish_27_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
