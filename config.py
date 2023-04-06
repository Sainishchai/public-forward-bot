import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "28394784"))
    API_HASH = os.environ.get("API_HASH", "9544a3ad7d8660acbae0dcf553c808e5")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6039043446:AAEfqoWa9qjZst_vZ4-rn0uka9vitYOrozs")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1966376217")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://forward:forward@cluster1.pgynkyr.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste1")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'forward_files')
    SESSION = os.environ.get("SESSION", "BQGxRSAACtT62Vgw4WrpSTTksGRAeN5SNJz6k8gtsti5lgMfACzQ84_2jRozB95aBKyAoTOMgfCUuQCKSz-frS4AJB24M1ADfPUGpimbY7fcNzweu8kE4lTGIegVq5i-meTAPO02x7eeCEH0fOlX3VYH8yjv0OXc6i1UzCiLzGqnajTdpamMTiOt4Goel84FYrArsE1J0rbE7FXMVhJLLS0jM_mLKHCfxPPqJ8nUeuDYLTc_A9YKS6lLDHiMRHW9mh3m2DlN_0TwtqoYogZ0wynqimdt90pmBxgXDIvl8fU8YzZrplTEL59v_od7N1-Sz2yxK1kQqxERfRA9gtAwegweXlOwrgAAAABF5vF9AA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001795790118"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Forwardit_nodejs_27_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
