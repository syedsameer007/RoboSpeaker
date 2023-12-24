import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker ")
    while True:
        Speak1 = pyttsx3.init()
        x=input("Enter What you want me to Speak")
        if x=="Quite":
             Speak1.say("Bye Bye Friend")
             Speak1.runAndWait()
             break
        
        Speak1.say(x)
        Speak1.runAndWait()



