# File name: sound.py (File that contains audio for digitas app)

from kivy.core.audio import SoundLoader
from engine.settings import appvar

def Hotsnd():
    reload(appvar)
    if appvar.appvar == 1:
        sound = SoundLoader.load("engine/sound/click.wav")
        sound.play()
    else:
       pass
