import os
import random

import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import datetime
from config import apikey

def ai(prompt):
    openai.api_key = apikey
    anstext=f"OpenAi Response for Prompt {prompt} \n ****************************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        print(response["choices"][0]["text"])
        anstext+=response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        #with open(f"Openai/prompt{random.randint(1,100000000000)}","w") as f:
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
            f.write(anstext)
    except Exception as e:
        return "Some Error Occured During Search"
speaker = win32com.client.Dispatch("SAPI.SPVoice")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:

        audio=r.listen(source)
        try:
            print("Recognization")
            query = r.recognize_google(audio,language="en-in")
            print(f"User said :{query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry From Jarvis"
while 1:
    print("Enter the word you want to speak it out by computer")


    while True:
        print("Listening ...")
        text=takeCommand()
        sites=[["Youtube","https://www.youtube.com"],["Google","https://www.google.com"],["Facebook","https://www.facebook.com"]]
        videofile=[["Ceremony","/Users\gypra\Downloads\Ceremony.mp4"],["Induction","/Users\gypra\Downloads\Induction.mp4"]]
        applications=[["telegram","C:/Users\gypra\AppData\Roaming\Telegram Desktop\Telegram.exe"],["adobe reader","C:/Program Files (x86)\Adobe\Reader 8.0\Reader\AcroRd32.exe"]]
        speaker.Speak(text)
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                speaker.Speak(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])
        for videopath in videofile:
            if f"open video {videopath[0]}".lower() in text.lower() in text.lower():
                speaker.Speak(f"Opening video {videopath[0]} Sir...")
                os.startfile(videopath[1])
        if "the time" in text:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir the time is now {strfTime}")
            speaker.Speak(f"Sir the time is now {strfTime}")

        for file in applications:

            if f"Open {file[0]}".lower() in text.lower():

                os.startfile(f"{file[1]}")
        if "Using Artificial Intelligence".lower() in text.lower():
            ai(prompt=text)
        if text.lower()=="stop".lower() or text.lower() == "q".lower():
            break
    break

