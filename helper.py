from urlextract import URLExtract
extract = URLExtract()
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

def fetch_stats(selected_user, df):
    
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
        
    #1,fetch number of messages
    num_messages = df.shape[0]
    #2.Number of words
    words = []
    for messages in df["message"]:
        words.extend(messages.split())
        
    #3.fetch number of media messages
    number_media_messages =  df[df["message"] == "<Media omitted>\n"].shape[0]
    
    #4.fetch number of links
    links = []
    for message in df["message"]:
        links.extend(extract.find_urls(message))
    
    return num_messages, len(words), number_media_messages, len(links)
        

def most_busy_user(df):
    y = df["user"].value_counts().head()
    df = round((df["user"].value_counts()/df.shape[0])*100, 2).reset_index().rename(columns = {"index":"name", "user":"percent"})
    return y, df
        
def create_wordcloud(selected_user,df):
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
        
    wc = WordCloud(width=300, height=300, min_font_size= 8, background_color="white")  
    df_wc = wc.generate(df["message"].str.cat(sep=" "))
    return df_wc
        
def most_common_words(selected_user,df):
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
           
    temp = df[df["message"] != "group notification"]
    temp = temp[temp["message"] != "<Media omitted>\n"]   
    
    f = open("C:/Users/mitul/Desktop/Text Analysis/NLP project/stop_hinglish.txt","r", encoding ="utf-8")
    stopwords = f.read()
    
    words =[]
    for message in temp["message"]:
        for word in message.lower().split():
            if word not in stopwords:
                words.append(word)
    
    most_common = pd.DataFrame(Counter(words).most_common(20))
    return most_common
       
        
       
        
       
        
       
        
       
        
       
        
       
        