from pydub import AudioSegment
from pydub.playback import play

sound=AudioSegment.from_mp3("ritual.mp3")

play(sound)