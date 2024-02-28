import telebot
from flask import Flask, render_template
from keep import keep_alive
keep_alive()
bot = telebot.TeleBot(os.environ.get('token'))

from bs4 import BeautifulSoup
import requests

def getlink():
 url="https://bingotingo.com/best-social-media-platforms/"
 page=requests.get(url)
 html=page.content
 soup = BeautifulSoup(html,"html.parser") 
 job_desc = soup.find(
    'a', 
    class_='su-button su-button-style-soft su-button-wide').get("href")
    
 print(f"job description:{job_desc}")

 url2=job_desc
 page2=requests.get(url2)
 html2=page2.content
 soup2 = BeautifulSoup(html2,"html.parser")
 div = soup2.find(
    'div',class_="public-container noselect")
 div2=div.find('div',class_='pb-links justify-content-center pb-links-noimg row m-0 effect-standard dl-LAYOUT_LIST_SMALL_RND ml-LAYOUT_LIST_SMALL_RND group-container-u')
    
 a=div2.find('a',class_="d-block pb-linkbox pb-desktop-list-small-rnd pb-mobile-list-small-rnd bt-2 mb-2 col-md-12 col-12").get('href')
 finallink=f'https://ln.ki{a}'
 def remove(string):
    return string.replace(" ", "") 
 if "canva" in finallink:
  return remove(finallink)
 else:
   return "link is will be available "
   


@bot.message_handler(commands=['start'])
def send_link(message):
    chat_id = message.chat.id
    link = getlink()
    markup = telebot.types.InlineKeyboardMarkup()
    btn_link = telebot.types.InlineKeyboardButton(text="Get canva pro", url=link)
    markup.add(btn_link)
    bot.send_message(chat_id, "Click the button below to access the link:", reply_markup=markup)

bot.polling()
