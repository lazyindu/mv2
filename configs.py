# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/LazyUrlHunterrBOT'>Lazy Url Hunterr</a> is an open source project.

    Devs: 
        <a href='https://t.me/mRiderDM'>â¤ï¸ LazyDeveloper â¤ï¸</a>
    
    
ð¤ My Name: <a href='https://t.me/LazyUrlHunterrBOT'>Lazy URL Hunterr</a>
ð Language: <a href='https://www.python.org'>Python V3</a>
ð Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>
ð¡ Server: <a href='https://heroku.com'>Heroku</a>
ð¡ Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>
ð¨âð» Developer Channel: <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a></b>
"""

    ABOUT_HELP_TEXT = """<b>ð Developer : <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {},

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

       Â»Â»Â» <b>Happy Hunting</b> Â«Â«Â«

ðºThank You <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>ðº </b>
"""


    START_MSG = """
<b>Hello Baby ! {},

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.

     Â»Â»Â»Â» <b>Happy Hunting</b> Â«Â«Â«Â« </b>

ð¸<b>Donate us to Keep Aliveð¸</b>
Â»Â» A small amount of â¹5 - â¹20 - â¹50 - â¹100 will be great help !

             ðº Thank You ðº 
"""

