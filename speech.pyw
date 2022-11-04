from re import sub
from turtle import end_fill
import pyttsx3
import subprocess
import time
engine = pyttsx3.init()

engine.say("Welcome to my world ... Its time to reverse the process and ...enjoy ..to use it")
engine.say(" If you are not able to reverse the process then you will lost the connection")

engine.runAndWait()
count=10
engine.say(f"start the coundown be fast your connection lost within {count} second")
engine.runAndWait()

engine.say(f"{9} second remaining")
engine.say(f"{8} second ")
engine.say(f"{7} second ")
engine.say(f"{6} second ")
engine.say(f"{5} second ")
engine.say(f"{4} second ")
engine.say(f"{3}  ")
engine.say(f"{2}  ")
engine.say(" 1 . your time is over  . best of luck for next time")
engine.runAndWait()


subprocess.call('''shutdown /p''' ,shell=True)

