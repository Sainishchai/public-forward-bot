import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "28394784"))
    API_HASH = os.environ.get("API_HASH", "9544a3ad7d8660acbae0dcf553c808e5")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6047745215:AAEfzK-DMl6Siohi7JFAmVqXaHmgG7_-ODc")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1966376217")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://nk:nk@cluster0.1wfgayy.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'nk_files')
    SESSION = os.environ.get("SESSION", "BQGYqWYAAq79U-wXJkQMdXXk6vO7XcJoQ5nQZMDjlExhKNhs87a7PyZqal_HWdY9nnrK0ovQyVLRUdHV8lUPKY1xvf_Q1BIpqPJ9M_INhUTK7BTNlEd7i_UB_VcsvZpoh_mpSQTuQDbkuQfn5KnMAqEV5u5isCqyg03gk2PgULwIdkhmGZA6YX4WNtPMlkzehl3Gz2fCYboik4Fre6TVRCycFCNRJak6M9iowuvd-pZU93WwwaaQqkvFGfHY0gq241JLle2apQSpoZAcRTkvV8tjXWYB8cuZT-S2XdYlA-mfJ_uEMTTFFShjVicVDONN_3OrbT7mJ9IlaIanzltho_UFe1sV0wAAAABKf7lXAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001927033569"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Auto_forward_files27_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
