from TOSUMUSIC.core.bot import TOSU
from TOSUMUSIC.core.dir import dirr
from TOSUMUSIC.core.git import git
from TOSUMUSIC.core.userbot import Userbot
from TOSUMUSIC.music import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = TOSU()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
