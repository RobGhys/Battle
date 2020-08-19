import os
from pygame import mixer


def play_music(file, repeat):
    """
        Play music
    """
    sound_path = os.path.join('sounds', file)
    mixer.music.load(sound_path)
    mixer.music.play(repeat)
