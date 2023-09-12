import os

if __name__=="__main__":
    print("Welcome to the Robospeaker")
    x=input("What you want to speak: ")
    command=f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"
    os.system(command)
