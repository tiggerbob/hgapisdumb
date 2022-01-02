from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pyautogui

r = sr.Recognizer()

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def clickOnImage(imageFile):
    icon_location = pyautogui.locateOnScreen(imageFile)    
    icon_point = pyautogui.center(icon_location)
    pyautogui.click(x=icon_point.x, y=icon_point.y)

while(True):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.5)
            audio2 = r.listen(source2)
            myText = r.recognize_google(audio2)
            myText = myText.lower()

            print("You said: " + myText)
            log = open("log.txt", "a")
            time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            log.write(myText + " " + time + "\n")
            log.close()
            
            if "close" in myText and "tab" in myText:
                try: 
                    clickOnImage('searchCloseTabIncognito.png')
                except:
                    speakText("nope can't find it")
            if "google" in myText:
                try: 
                    clickOnImage('newTabIncognito.png')

                    searchTermIndex = myText.find("google") + 6
                    searchTerm = myText[searchTermIndex::]
                    for char in searchTerm:
                        pyautogui.typewrite(char)
                    pyautogui.typewrite(['enter'])
                except:
                    speakText("you might want to try opening google chrome first")
            if "images" in myText:
                try:
                    clickOnImage('images.png')
                except:
                    try: 
                        clickOnImage('images1.png')
                    except:
                        speakText("for the love of god i can't find it")
            if "exit" in myText:
                break
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occured")