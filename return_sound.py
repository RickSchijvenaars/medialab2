import multiprocessing
from playsound import playsound


music_list = {
    "red": "samples/cold_funk.mp3",
    "purple" : "samples/ruud.m4a",
}


def return_sound_from_color(color):
    p = multiprocessing.Process(target=playsound, args=(music_list[color],))
    p.start()

    input("press ENTER to stop playback")
    p.terminate()




