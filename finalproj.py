import sys
import cv2

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog,QMainWindow

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from deepface import DeepFace
from pyqtgraph import PlotWidget
import time
import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia as wiki

from pygame import mixer
import random
from mutagen.mp3 import MP3
from threading import Thread

##################################################**TOM PLAYER**##################################################################

def music_stat(songlist):
    selection = random.choice(songlist)
    speak("playing music")
    mixer.init()
    mixer.music.set_volume(0.2)
    mixer.music.load(selection)
    song = MP3(selection)
    mixer.music.play(0)
    songLength = song.info.length
  
    time.sleep(songLength+1)
    mixer.quit()
    

##################################################**CHATBOT EMOTION FEED**############################################################################

def happy():
    global happy_songs
    speak("i am glad to see that you are happy")
    time.sleep(1)
    speak("would you like to hear a energitic song")
    
    ans = getans()
    if ('yes' in ans) or ("ya" in ans) or ("yeah" in ans):
       
        music_stat(happy_songs)
        
      
    else:
        speak('no problem')
        time.sleep(1)
        speak("how would you like me to help you")
        
        elsepart()
        
def disgust():
    global disgust_songs
    speak("did something worry you?")
    ans = getans()
    if ('yes' in ans) or ("ya" in ans) or ("yeah" in ans):
        speak("dont worry every thing will be fine")
        speak("would you like to hear some motivational songs")
        ans = getans()
        if ('yes' in ans) or ("ya" in ans) or ("yeah" in ans):
            music_stat(disgust_songs)
            
            
        else:
            speak("ok we will speak some thing else, ask me anything")
            elsepart()
    else:
        speak("ok we will speak some thing else, ask me anything")
        elsepart()
        
def sad():
    global sad_songs
    speak("you seem a little sad")
    time.sleep(1)
    speak("Would you like to hear something to boost your mood")
    
    ans = getans()
    if ('yes' in ans) or ("ya" in ans) or ("yeah" in ans):
         music_stat(sad_songs)
        
      

    else:
        speak("it's ok")
        time.sleep(1)
        speak("is there anything else i can do")
        elsepart()

def fear():
    speak("You seem a little frightened")
    global fear_songs
    time.sleep(1)
    speak("Is there a problem")
    ans = getans()
    if 'yes' in ans:
        speak("you are strong enough to face anything...")
        speak("would you like to listen to some motivational songs ;  ")
        ans = getans()
        if ('yes' in ans) or ("ya" in ans) or ("yeah" in ans):
            selection = random.choice(fear_songs)
            mixer.music.load(selection)
            mixer.music.play()
            music_stat(fear_songs)
            
        
            
        else:
            speak("belive in you, you can reach the sky")
            elsepart()
    else:
        speak("ok we will speak some thing else, ask me anything")
        elsepart()
def angry():
    speak("Looks like some one is angry")
    time.sleep(1)
    speak("want to talk about it")
    global angry_songs

    ans = getans()
    if 'yes' in ans:
        time.sleep(7)
        speak("stay calm")
        speak("do  some breating exercise,it will help you to stay cool")
        speak("Would you like to hear something relaxing music to stay cool")
        ans = getans()
        if ('yes' in ans) or ("ya" in ans) or ("yeah" in ans):
            
            music_stat(angry_songs)
            
        else:
            speak("hope you will be fine")
            time.sleep(1)
            speak("ask me something you want to hear from me")
            elsepart()
    else:
        speak("ask me something you want to hear from me")
        elsepart()
        
def surprise():
    speak("seem to be surprised")
    global surprise_songs
    time.sleep(1)
    speak("hope it was a good one")
    speak("want to surprise yourself  with the exiting music")
    ans = getans()
    if ('yes' in ans) or ("ya" in ans) or ("yeah" in ans):
        
        music_stat(surprise_songs)
        
        

    else:
        speak("well everything will be alright")
        speak("ask me something you want to hear from me")
        elsepart()

####################################** GENERAL CHAT **##########################################################################################    

def general_functions(Command):
    #global flag

    if 'what is ' in Command or 'who is 'in Command:
        speak('Searching ...')
        if 'what is ' in Command:
            Command = Command.replace("what is ", "")
        else:
            Command = Command.replace("who is ", "")
        results = wiki.summary (Command, sentences = 3)
        speak("According to Wikipedia  "+ results)
        
        

    elif 'time' in Command:
        strTime = datetime.datetime.now().strftime("%I:%M:%S")
        times= f"The time is {strTime}"
        speak(times)

    elif 'how are you' in Command:
        speak('I am fine, Thank you ')
        time.sleep(1)
        speak("hope you are doing well")
    elif 'fine ' in Command or 'good' in Command:
        speak("Glad to hear that")

    

    elif 'who made you' in Command or 'who created you' in Command:
        speak("I have been created by the thespians")

    elif "who i am" in Command:
        speak("If you talk then definately your human.")

    elif "play music" in Command:
        global happy_songs
        music_stat(happy_songs)
        

    elif 'i love u ' in Command:
        speak("hoo thats kind, I love you too")

    elif "who are you" in Command:
        speak("I am your virtual assistant created by the thespians")

    elif 'reason for you' in Command:
        speak("I was created as a Minor project by the thespians")

    elif ("write a note" in Command) or ("take a note" in Command):
        speak("What should i write, sir")
        note = takeCommand()
        window.usrLabel.setText(str(note))
        
        strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
        file = open('tom.txt', 'w')
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
        
        

    elif "show note" in Command:
        speak("Showing Notes")
        file = open("tom.txt", "r") 
        print(file.read())
        speak(file.read(6))


######################################################**FLOW FOR ELECUTION**#########################################################################  

def start():
    
    hour = int(datetime.datetime.now().hour)
    
    if hour>= 0 and hour <12:
        speak("Good Morning")
        #window.inLabel.setText("Good Morning")# formal or informal

    elif hour>= 12 and hour<16:
        speak("Good Afternoon")
        #window.inLabel.setText("Good Afternoon")

    else:
        speak("Good Evening")
        #window.inLabel.setText("Good Evening")

    assistant_name = "tom"
    speak ("I am your assistant "+assistant_name)
   
    time.sleep(1)
    mainexe()
        
def mainexe():
    while True:
        sentiblock() 
    

        
def sentiblock():
    
        
    curemo= window.emo[-1] 
    
    if curemo == 'sad':
            sad()

    elif curemo == 'angry':
            angry()

    elif curemo == 'disgust':
            disgust()

    elif curemo == 'fear':
            fear()

    elif curemo == 'surpirse':
            surprise()
    else:
            happy()
            
        
def getans():
    x=takeCommand()
    while x=="":
        x=takeCommand()
    else:
        window.usrLabel.setText(str(x))
        
        return x
def timer():
    x= takeCommand()
    count=0
    while x=="":
        count+=1
        x=takeCommand()
        if(count==3):
            break
    else:
        
        window.usrLabel.setText(str(x))
        
        return x
    
def elsepart():
    query = timer()
    general_functions(query)
####################################################** SPEAKER AND LISTENER**########################################################################  
            
def speak(audio):
    engine.say(audio) 
    window.inLabel.setText(str(audio))
    engine.runAndWait()
    
def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:

        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        speak("listening...") 
        audio = r.listen(source)
    try:
        speak("Recognizing...") 
        ans = r.recognize_google(audio,language = 'en-in')
        if isinstance(ans, str):
            query = ans.lower()
        else:
            query=""
    except Exception as e:
        speak(e)
        speak("Unable to Recognize your voice ,say louder..")
               
        query=""

    return(query) 



########################################################** UI FACEDETECTION PRE-REQUISITES**##############################################################3


class FaceDetection(QDialog):
    
    def __init__(self):
        
        super(FaceDetection,self).__init__()
        loadUi('face_detection2.ui',self)
        self.timecap={}
        self.emo =['happy']
        
        self.image=None
        self.processedImage=None
        self.startButton.clicked.connect(self.start_webcam)
        self.stopButton.clicked.connect(self.stop_webcam)
        self.closeButton.clicked.connect(self.gotograph)
        self.musick=0
        
        
        self.face_Enabled=True
        self.faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.x = Thread(target=start, daemon=True)
        self.check=1

#########################################** START AND STOP OF PROGRAM  EXECUTION **#######################################   

    def start_webcam(self):
        self.capture=cv2.VideoCapture(0)
        

        
        if mixer.get_init():
            if (mixer.music.get_busy() != True) and (self.check==1):
                mixer.music.unpause()
        if(not self.x.is_alive()):
            self.x.start()
        
        

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)
        
        
    def stop_webcam(self):
        if mixer.get_init():
            if mixer.music.get_busy() == True:
                    mixer.music.pause()
            self.check=0
            
        self.timer.stop()
        exit()
            
        
        

        
        
        
############################################** VIDEO PROCESSING THROUGH IMAGE  **################################################## 

    def update_frame(self):
        ret,self.image=self.capture.read()
        
        self.image=cv2.flip(self.image,1)

        detected_image=self.detect_face(self.image)
        self.displayImage(detected_image)
        


    def detect_face(self,img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.faceCascade.detectMultiScale(gray,1.2,5,minSize=(90,90))
        try:
            self.predictions= DeepFace.analyze(self.image, actions = ['emotion']) #GETTIND DATA FROM PRE-TRAINED MODEL
            self.timecap[time.time()]=self.predictions['emotion']['happy']
        except:
            pass

        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            x=self.predictions['dominant_emotion']
            self.emo.append(x) 
            
            cv2.putText(img,
                 x,
                (50,50),
                font,3,
                (0,0,255),
                2,
                cv2.LINE_4)
            
        return img

  
        
    def displayImage(self,img):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888

        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        
        
        outImage=outImage.rgbSwapped()
        self.processedImgLabel.setPixmap(QPixmap.fromImage(outImage))
        self.processedImgLabel.setScaledContents(True)
        
        
########################################** GRAPH PLOTTING **####################################################################     
        
        
    def gotograph(self):
        self.stop_webcam
        if mixer.get_init():
            if mixer.music.get_busy() == True:
                mixer.quit()
        
        z=set(self.emo)
        max=0
        for i in z:
            if(self.emo.count(i)> max ):
                max=self.emo.count(i)
                domtemo= i
        quotes={'happy':" ALWAYS BE HAPPY ","sad":"NOTHING SHAKES THE SMILING HEARTS", "disgust": " NEVER LOSE HOPE ,BETTER DAYS ARE AHEAD"
                ,"fear": "HOPE IS THE ONLY  THING STRONGER THAN FEAR", "surprise":"UNEXPECTED MOMENTS ARE ALWAYS SWEETER ","neutral":" SMILE , IT SUITES YOU!"}
        
        PlotGraph=plot_graph()
        PlotGraph.feedLabel.setText(quotes[domtemo])
        widget.addWidget(PlotGraph)
        widget.setCurrentIndex(widget.currentIndex()+2)
        pltSignal = PlotGraph.widgetSignal
        pltSignal.setStyleSheet("border : 5px solid green;"
                                "padding : 5px;")
        x,y=[],[]
        for i in self.timecap.keys():
            x.append(i)
            
        for i in self.timecap.values():
            y.append(i)
        
        pltSignal.setLabel('left', 'Hapiness')
        pltSignal.setLabel('bottom', 'Time instance')
        pltSignal.plot(x, y, clear = True)
        
    
        
        
    

###############################################** initialization OF GRAPH UI**##################################################       
      
class plot_graph(QMainWindow):
    def __init__(self):
        super(plot_graph,self).__init__()
        loadUi('graph_box.ui',self)
      
        
        
    

##############################################** MAIN FUNCTION **###############################################################

if __name__=='__main__':
    app=QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    window=FaceDetection()
    widget.addWidget(window)
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    
    happy_songs =["stereohearts.mp3"]
    sad_songs= []
    angry_songs=[]
    fear_songs=[]
    surprise_songs=[]
    
    disgust_songs=[]
    
    
    
    
    
    
    
    
    window.setWindowTitle('Face Detection App')
   
    print(window.timecap)
   
    widget.setFixedHeight(781)
    widget.setFixedWidth(1165)
    widget.show()
    sys.exit(app.exec_())
###########################################**  END  OF PROGRAM **###############################################################