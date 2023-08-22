import requests
import json
from win32com.client import Dispatch
from dotenv import load_dotenv
import os

load_dotenv()

def speak(String):
    speaker = Dispatch("SAPI.spVoice")
    speaker.speak(String)


if __name__ == "__main__":
    # This line gets the news data from the News API in string format which we will later convert in
    # json using json.loads function.
    APIKEY = os.getenv("APIKEY")
    news = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={APIKEY}")
    # This line parses the news data in json and due to this we can choose what we want to print or read.
    parsedNews = json.loads(news.text)
    # This line is just to make it easier to grab article. It is just making a variable which grabs the
    # article from the parsed news data.
    topnews = parsedNews["articles"]

    for i in range(10):
        # this line splits the title of the news from "-" sign and reads only the part before "-" sign.
        splittedTitle = (topnews[i]["title"]).split("-")[0]
        # This is the function that reads whatever string is given to it as an argument.
        # In this case I have given it news number to read, the source name of the news, the title,
        # and the description of the news.
        speak(f"News {i + 1} is from " + topnews[i]["source"]["name"] + "..." + "The title is: " +
              splittedTitle + "..." + "The description is: " + str(topnews[i]["description"]))