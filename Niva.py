import pyttsx3                                    
import datetime
import speech_recognition as sr                   
import pyaudio                                  
import wikipedia                                  
import webbrowser
import os
import sys
import smtplib
from email.message import EmailMessage
import pywhatkit                                   
import MyAlarm      
import ecapture as ec                
import pyjokes                                     
from speedtest import Speedtest                    
from pywikihow import search_wikihow               
import pyautogui                                   
import poetpy                                      
import random
from forex_python.converter import CurrencyRates   
import requests                                    
import bs4                                        
import time
import wolframalpha                                
from quote import quote                            
import winshell as winshell                        
from geopy.geocoders import Nominatim             
from geopy import distance
import turtle
import random
import SnakeGame as snake_game
import Record as record
import requests
from PIL import Image

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
        
    speak("I am Niva (Python Voice Assistant). Tell me how may I help you.")


def get_command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1

        audio = rec.listen(source)

        try:
            print("Recognizing...")
            query = rec.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "None"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "None"

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query


if __name__ == '__main__':
    wish_user()
    while True: 
        query = get_command().lower()
        home_user_dir = os.path.expanduser("~")

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif ('images' or 'image') in query:
            speak("Please provide the desired keywords to search related Images")
            txt=get_command()
            speak("Providing Images of"+txt)
            response=requests.get("https://source.unsplash.com/random?{0}".format(txt))
            file=open('sample_image.jpg','wb')
            file.write(response.content)
            img=Image.open(r"sample_image.jpg")
            img.show()
            file.close
        


        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")


        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.datetime.today().strftime('%Y-%m-%d')
            print(strDate)
            speak(f"The date is {strDate}")

        elif 'open visual studio code' in query:
            os.startfile(home_user_dir + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\"
                         "Programs\\Visual Studio Code\\Visual Studio Code")


        elif 'open notepad' in query:
            os.startfile("C:\\Windows\\notepad.exe")

        elif 'open pycharm' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe")


        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")


        elif ('hu r u' or 'are you' ) in query:
            speak("I am Niva (Python Voice Assistant), developed by Augnik Banerjee and I seek to improve more day by day! ")
        elif 'what you want to do' in query:
            speak("I want to help lazy people complete their work")

        elif 'alexa' in query:
            speak("I don't know Alexa, but I've heard of Alexa. If you have Alexa, "
                        "I may have just triggered Alexa. If so, sorry Alexa.")

        elif 'google assistant' in query:
            speak("He was my classmate, too intelligent guy. We both are best friends.")

        elif 'siri' in query:
            speak("Siri, She's a competing virtual assistant on   a competitor's phone. "
                        "Not that I'm competitive or anything.")

        elif 'cortana' in query:
            speak("I thought you'd never ask. So I've never thought about it.")

        elif 'niva' in query:
            speak("Are you joking. You're coming in loud and clear.")

        elif 'what language you use' in query:
            speak("I am written in Python and I generally speak english.")

        elif 'send email' in query:

            def send_mail(receiver, subject, message):

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('your_email@something.com', 'your_password')

                email = EmailMessage()
                email['From'] = 'your_email@something.com'
                email['To'] = receiver
                email['Subject'] = subject
                email.set_content(message)
                server.send_message(email)


            email_list = {
                'Augnik': 'shresnik2004@gmail.com',
                'Baba': 'jbanerjee1977@gmail.com',
                'name': 'something@something.com',
                'assitant': 'something@something.com'
            }


            def get_mail_info():
                speak('To whom you want to send email')
                name = get_command()
                receiver = email_list[name]
                print(receiver)
                speak('What is the subject of your email?')
                subject = get_command()
                speak('Tell me the text in your email')
                message = get_command()

                send_mail(receiver, subject, message)

                speak('Hey lazy person. Your email is sent Successfully.')

                speak('Do you want to send more email?')
                send_more = get_command()
                if 'yes' in send_more:
                    get_mail_info()


            get_mail_info()

        elif 'play' in query:
            cmd_info = query.replace('play', '')
            speak(f'Playing {cmd_info} ')
            print(cmd_info)
            pywhatkit.playonyt(cmd_info)

        elif 'search' in query:
            query = query.replace('search', '')
            pywhatkit.search(query)
        
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")

        elif 'set alarm' in query:
            speak("Tell me the time to set an Alarm. For example, set an alarm for 11:21 AM")
            a_info = get_command()
            a_info = a_info.replace('set an alarm for', '')
            a_info = a_info.replace('.', '')
            a_info = a_info.upper()
            MyAlarm.alarm(a_info)

        elif 'exit' in query:
            speak("Exiting ...")
            sys.exit()

        elif 'close command prompt' in query:
            os.system("TASKKILL /F /IM cmd.exe")


        # elif "camera" or "take a photo" in query:
        #     ec.capture(0,"robo camera","img.jpg")

        elif 'close visual studio code' in query:
            os.system("TASKKILL /F /IM Code.exe")

        elif 'close notepad' in query:
            os.system("TASKKILL /F /IM notepad.exe")

        elif 'close pycharm' in query:
            os.system("TASKKILL /F /IM pycharm64.exe")


        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")


        elif 'close spotify' in query:
            os.system("TASKKILL /F /IM Spotify.exe")

        elif 'price of' in query:
            query = query.replace('price of', '')
            query = "https://www.amazon.in/s?k=" + query[-1] #indexing since I only want the keyword
            webbrowser.open(query)

        elif 'poem' in query:
            speak('Poem of which author you want to listen?')
            auth = get_command()
            poem = poetpy.get_poetry('author', auth, 'title,linecount') 
            poems = poetpy.get_poetry('author', auth, 'lines')  

            poem_len = len(poem)
            # print(poem_len)
            poem_no = random.randint(1, poem_len)
            print("Title- ", poem[poem_no]['title'])
            speak(f"Title- {poem[poem_no]['title']}")
            print("No. of lines-", poem[poem_no]['linecount'])
            speak(f"No. of lines- {poem[poem_no]['linecount']}")
            poem_str = '\n'
            print("Poem-\n", poem_str.join(poems[poem_no]['lines']))
            speak(f"Poem-\n {poem_str.join(poems[poem_no]['lines'])}")

        elif 'resume' in query or 'pause' in query:
            pyautogui.press("playpause")

        elif 'previous' in query:
            pyautogui.press("prevtrack")

        elif 'next' in query:
            pyautogui.press("nexttrack")

        elif 'convert currency' in query:
            try:
                curr_list = {
                    'dollar': 'USD', 'taka': 'BDT', 'dinar': 'BHD',
                    'rupee': 'INR', 'afghani': 'AFN', 'real': 'BRL',
                    'yen': 'JPY', 'peso': 'ARS', 'pound': 'EGP', 'rial': 'OMR',
                    'lek': 'ALL', 'kwanza': 'AOA', 'manat': 'AZN', 'franc': 'CHF'
                }

                cur = CurrencyRates()
                # print(cur.get_rate('USD', 'INR'))
                speak('From which currency u want to convert?')
                from_cur = get_command()
                src_cur = curr_list[from_cur.lower()]
                speak('To which currency u want to convert?')
                to_cur = get_command()
                dest_cur = curr_list[to_cur.lower()]
                speak('Tell me the value of currency u want to convert.')
                val_cur = float(get_command())
                # print(val_cur)
                print(cur.convert(src_cur, dest_cur, val_cur))
                        
            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")

        elif 'covid-19' in query or 'corona' in query:
            speak('For which region you want to see the Covid-19 cases. '
                        'Overall cases in the world or any specific country?')
            c_query = get_command()
            if 'overall' in c_query or 'over all' in c_query or 'world' in c_query or 'total' in c_query or 'worldwide' in c_query:
                def world_cases():
                    try:
                        url = 'https://www.worldometers.info/coronavirus/'
                        info_html = requests.get(url)
                        info = bs4.BeautifulSoup(info_html.text, 'lxml')
                        info2 = info.find('div', class_='content-inner')
                        new_info = info2.findAll('div', id='maincounter-wrap')
                        # print(new_info)
                        print('Worldwide Covid-19 information--')
                        speak('Worldwide Covid-19 information--')

                        for i in new_info:
                            head = i.find('h1', class_=None).get_text()
                            counting = i.find('span', class_=None).get_text()
                            print(head, "", counting)
                            speak(f'{head}: {counting}')

                    except Exception as e:
                        pass


                world_cases()

            elif 'country' in c_query or 'specific country' in c_query:
                def country_cases():
                    try:
                        speak('Tell me the country name.')
                        c_name = get_command()
                        c_url = f'https://www.worldometers.info/coronavirus/country/{c_name}/'
                        data_html = requests.get(c_url)
                        c_data = bs4.BeautifulSoup(data_html.text, 'lxml')
                        new_data = c_data.find('div', class_='content-inner').findAll('div', id='maincounter-wrap')
                        # print(new_data)
                        print(f'Covid-19 information for {c_name}--')
                        speak(f'Covid-19 information for {c_name}')

                        for j in new_data:
                            c_head = j.find('h1', class_=None).get_text()
                            c_counting = j.find('span', class_=None).get_text()
                            print(c_head, "", c_counting)
                            speak(f'{c_head}: {c_counting}')

                    except Exception as e:
                        pass


                country_cases()

        elif 'weather' in query or 'temperature' in query:
            try:
                speak("Tell me the city name.")
                city = get_command()
                api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=eea37893e6d01d234eca31616e48c631"
                w_data = requests.get(api).json()
                weather = w_data['weather'][0]['main']
                temp = int(w_data['main']['temp'] - 273.15)
                temp_min = int(w_data['main']['temp_min'] - 273.15)
                temp_max = int(w_data['main']['temp_max'] - 273.15)
                pressure = w_data['main']['pressure']
                humidity = w_data['main']['humidity']
                visibility = w_data['visibility']
                wind = w_data['wind']['speed']
                sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
                sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))

                all_data1 = f"Condition: {weather} \nTemperature: {str(temp)}°C\n"
                all_data2 = f"Minimum Temperature: {str(temp_min)}°C \nMaximum Temperature: {str(temp_max)}°C \n" \
                            f"Pressure: {str(pressure)} millibar \nHumidity: {str(humidity)}% \n\n" \
                            f"Visibility: {str(visibility)} metres \nWind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                            f"\nSunset: {sunset}"
                speak(f"Gathering the weather information of {city}...")
                print(f"Gathering the weather information of {city}...")
                print(all_data1)
                speak(all_data1)
                print(all_data2)
                speak(all_data2)

            except Exception as e:
                pass

        elif 'month' in query or 'month is going' in query:
            def tell_month():
                month = datetime.datetime.now().strftime("%B")
                speak(month)

            tell_month()

        elif 'day' in query or 'day today' in query:
            def tell_day():
                day = datetime.datetime.now().strftime("%A")
                speak(day)

            tell_day()

        elif "calculate" in query:
            try:
                app_id = "JUGV8R-RXJ4RP7HAG"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")

        elif 'quote' in query or 'quotes' in query:
            speak("Tell me the author or person name.")
            q_author = get_command()
            quotes = quote(q_author)
            quote_no = random.randint(1, len(quotes))
            # print(len(quotes))
            # print(quotes)
            print("Author: ", quotes[quote_no]['author'])
            print("-->", quotes[quote_no]['quote'])
            speak(f"Author: {quotes[quote_no]['author']}")
            speak(f"He said {quotes[quote_no]['quote']}")

        elif 'what' in query or 'who' in query:    
            
            client = wolframalpha.Client("JUGV8R-RXJ4RP7HAG")
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print("No results found!!")

        elif 'empty recycle bin' in query or 'clear recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                print("Recycle Bin is cleaned successfully.")
                speak("Recycle Bin is cleaned successfully.")

            except Exception as e:
                print("Recycle bin is already Empty.")
                speak("Recycle bin is already Empty.")

        elif 'write a note' in query or 'make a note' in query:
            speak("What should I write, sir??")
            note = get_command()
            file = open('Notes.txt', 'a')
            speak("Should I include the date and time??")
            n_conf = get_command()
            if 'yes' in n_conf:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(str_time)
                file.write(" --> ")
                file.write(note)
                speak("Point noted successfully.")
            else:
                file.write("\n")
                file.write(note)
                speak("Point noted successfully.")

        elif 'show me the notes' in query or 'read notes' in query:
            speak("Reading Notes")
            file = open("Notes.txt", "r")
            data_note = file.readlines()
            # for points in data_note:
            print(data_note)
            speak(data_note)

        elif 'distance' in query:
            geocoder = Nominatim(user_agent="Singh")
            speak("Tell me the first city name??")
            location1 = get_command()
            speak("Tell me the second city name??")
            location2 = get_command()

            coordinates1 = geocoder.geocode(location1)
            coordinates2 = geocoder.geocode(location2)

            lat1, long1 = coordinates1.latitude, coordinates1.longitude
            lat2, long2 = coordinates2.latitude, coordinates2.longitude

            place1 = (lat1, long1)
            place2 = (lat2, long2)

            distance_places = distance.distance(place1, place2)

            print(f"The distance between {location1} and {location2} is {distance_places}.")
            speak(f"The distance between {location1} and {location2} is {distance_places}")

        elif 'screenshot' in query:
            sc = pyautogui.screenshot()
            sc.save('pa_ss.png')
            print("Screenshot taken successfully.")
            speak("Screenshot taken successfully.")

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute volume' in query:
            pyautogui.press("volumemute")

        elif 'shut down' in query:
            print("Do you want to shutdown you system?")
            speak("Do you want to shutdown you system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                
                os.system("shutdown /s /t 1")

        elif 'restart' in query:
            print("Do you want to restart your system?")
            speak("Do you want to restart your system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                
                os.system("shutdown /r /t 1")

        elif 'log out' in query:
            print("Do you want to logout from your system?")
            speak("Do you want to logout from your system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                os.system("shutdown -l")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'internet speed' in query:
            st = Speedtest()
            print("Wait!! I am checking your Internet Speed...")
            speak("Wait!! I am checking your Internet Speed...")
            dw_speed = st.download()
            up_speed = st.upload()
            dw_speed = dw_speed / 1000000
            up_speed = up_speed / 1000000
            print('Your download speed is', round(dw_speed, 3), 'Mbps')
            print('Your upload speed is', round(up_speed, 3), 'Mbps')
            speak(f'Your download speed is {round(dw_speed, 3)} Mbps')
            speak(f'Your upload speed is {round(up_speed, 3)} Mbps')


        elif 'how to' in query:
            try:
                # query = query.replace('how to', '')
                max_results = 1
                data = search_wikihow(query, max_results)
                # assert len(data) == 1
                data[0].print()
                speak(data[0].summary)
            except Exception as e:
                speak('Sorry, I am unable to find the answer for your query.')
                        
        elif 'news' in query or 'news headlines' in query:
            url = "https://news.google.com/news/rss"
            client = webbrowser(url)
            xml_page = client.read()
            client.close()
            page = bs4.BeautifulSoup(xml_page, 'xml')
            news_list = page.findAll("item")
            speak("Today's top headlines are--")
            try:
                for news in news_list:
                    print(news.title.text)
                    # print(news.pubDate.text)
                    speak(f"{news.title.text}")
                    # speak(f"{news.pubDate.text}")
                    print()

            except Exception as e:
                pass

        elif 'snake game' in query:
            try:
                print("Starting the game!")
                speak("Starting the game!")
                snake_game.game()
            except Exception as e:
                pass
