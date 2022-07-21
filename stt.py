from email.mime import audio
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
from yaml import safe_dump_all

class Solution:

    def __init__(self) :
        #self.text = "말씀하세요"
        #self.tts = gTTS(text = self.text, lang="ko")
        #self.tts.save(r"C:/Users/bitcamp/mibot/mibot-yolov5/yolov5/stt_test\voice.mp3")
        pass
    
    def save_file(self):
        tts = gTTS(text = "신나는 노래를 들려드릴게요", lang="ko")
        tts.save(r'C:\Users\bitcamp\mibot\mibot-stt\stt_test\music.mp3')

    def speak(self):       
        return playsound.playsound(r'C:/Users/bitcamp/mibot/mibot-stt/stt_test\hi.mp3') 

    def speak2(self):       
        return playsound.playsound(r'C:/Users/bitcamp/mibot/mibot-stt/stt_test\good.mp3')

    def speak3(self):       
        return playsound.playsound(r'C:/Users/bitcamp/mibot/mibot-stt/stt_test\music.mp3')
    
    def get_audio(self):
        r = sr.Recognizer() #음성 인식
        with sr.Microphone() as source: #마이크로폰을 소스로 받아들여 
            audio = r.listen(source) # 오디오로 들어간 뒤
            said = ""
            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print("Exception: " + str(e))
        return said 

    def stt(self):
        self.speak()
        self.text = self.get_audio()
        if " hello " in self.text:
            self.speak2()
        elif " boring " in self.text:
            self.speak3()

if __name__ == "__main__": 
    #Solution().save_file()
    #Solution().speak()
    
    #Solution().get_audio()
    Solution().stt()




