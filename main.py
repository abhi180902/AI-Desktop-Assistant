import pyttsx3  # text to speech conversion library
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from PIL import Image


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def play_song(song_name):
    music_folder = "D:\\my_music"
    song_found = False

    # Get a list of all files in the music folder
    all_songs = os.listdir(music_folder)

    # Search for the specified song in the folder
    for song in all_songs:
        if song_name.lower() in song.lower():  # Case insensitive search
            os.startfile(os.path.join(music_folder, song))

    if song_name not in all_songs:
        print(f"Song '{song_name}' not found in the music folder.")

def open_word_document(file_path):
    try:
        os.system(f"start {file_path}")
        print(f"Opening {file_path}...")
        speak(f"opening d")
    except Exception as e:
        print(f"Error: {e}")

def open_images_in_folder(folder_path):
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print("Folder doesn't exist.")
            return

        # Get a list of files in the folder
        files = os.listdir(folder_path)

        # Filter only image files
        image_files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))
                       and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        if not image_files:
            print("No image files found in the folder.")
            return

        # Open each image file
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            img = Image.open(image_path)
            img.show()  # Opens the image using the default image viewer

    except Exception as e:
        print(f"An error occurred: {e}")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abhisheksangamad1802@gmail.com', 'fkyc aftt ucje vzuv')
    server.sendmail('abhisheksangamad1802@gamil.com', to, content)
    server.close()

def WishMe():   # wishes us according to the time
    hour = int(datetime.datetime.now().hour)  #from 0 to 24
    if hour >= 0 and hour < 12:
        speak("good Morning!")

    elif hour >= 12 and hour < 18:
        speak("good Afternoon!")

    else:
        speak("good Evening!")

    speak("I Am An A I , how can i help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()  # helps in recognising the audio.
    with sr.Microphone() as source:  # uses microphone as source
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query =  r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please")
        return "None"
    return query

if __name__ == '__main__':
    WishMe()
    while True:   # a while loop does things as long as the condition is true.
    # if 1:     # if statement gives you once the possibility to do something or not (or something else).
        query = takeCommand().lower()  # query takes command and convert it into lower case for user help
        # logic for executing tasks based on query.
        # todo: add more sites
        sites = [['youtube', 'https://www.youtube.com'], ['google', 'https://www.google.com'],
             ['w3schools', 'https://www.w3schools.com'],['stack overflow','https://www.stackoverflow.com'],['linkedin','https://www.linkedin.com/feed/']]
        for site in sites:
            if f"open {site[0]}" in query:
                speak(f"opening {site[0]} ")
                webbrowser.open(site[1])

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia','')  # for removing wikipedia.
            result = wikipedia.summary(query, sentences=2)  # sentences depends on user choice like how many lines he wants print from wikipedia.
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'play music' in query:
            music_dir = 'D:\\my_music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M;%S")
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            speak('opening vs code')
            vscodePath = 'C:\\Users\\PRASAD SANGAMAD\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(vscodePath)

        elif 'email to abhishek' in query:
            try:
                speak('What should i do:')
                content = takeCommand()
                to = 'abhisheksangamad2002@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                print("sorry i am not able to send the email at the moment, try again")

        elif 'open my document' in query:
            # Example usage: Replace 'path/to/your/document.docx' with the actual file path
            file_path = "D:\\dbms\\croprecommender.docx"
            open_word_document(file_path)

        elif 'open my photos' in query:
            folder_path = 'D:\\my photos'
            open_images_in_folder(folder_path)

        # todo: add a feature to play a specific song
        elif 'play first song' in query:
            play_song("apna_bana_le.mp3")

        elif 'play second song' in query:
            play_song("chand_sifarish.mp3")

        elif 'play third song' in query:
            play_song("kaagadada_doniyalli.mp3")

        elif 'play fourth song' in query:
            play_song("seethakalam.mp3")

        elif 'play fifth song' in query:
            play_song("taja_samachara.mp3")

        elif 'play sixth song' in query:
            play_song("abc.mp3")

        elif 'quit the chat' in query:
            print('quitting the chat')
            speak('thank you, have a great day')
            exit()  # used to terminate the current running program.



