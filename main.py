import os, telegram, pytube, logging, os, googletrans, json, urllib.request, random
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup                           
from telegram.ext import Updater, MessageHandler, ConversationHandler, CallbackQueryHandler, CommandHandler, Filters
from telegram.forcereply import ForceReply
from pytube import YouTube
from time import sleep
from googletrans import Translator
from gtts import gTTS 
from bs4 import BeautifulSoup
import os
PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1001369530:AAGfW_uuJtTsiTXRT_NywUsoR-0VpN3rfO0'
idj = 884653961
idz = 1032936851
idg = -425234062

country_code = ''
YOUTUBE_MUSIC, YOUTUBE_VIDEO, LET_TRANSLATE, TRANSLATED, YOUTUBE_SEARCH, CURHAT = range(6)

def albums(update, context):
    keyboard = [[InlineKeyboardButton("Photo", callback_data='1'),
                 InlineKeyboardButton("Video", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def album_handler(update, context):
    query = update.callback_query

    query.answer()
    print(query.data)
    if query.data == '1':
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      query.edit_message_text('Alright, another me will send you the photo of us🥰')
      media_url = [
        'https://imgur.com/QY3EL5I',
        'https://imgur.com/2WUlZfi',
      ]
      for chats in media_url:
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_PHOTO)
        query.message.reply_photo(chats)
    else:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      query.edit_message_text('Alright, another me will send you the video of us😍')
      media_url = [
        'https://imgur.com/4eAG0Xt.mp4',
        'https://i.imgur.com/57TlMzk.mp4'
      ]
      for chats in media_url:
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_VIDEO)
        query.message.reply_video(chats)

    
def start(update, context):
    msg_array = [
      'ketik slash(/) dulu bih', 
      'terus pilih yang kamu mau'
    ]
    # context.bot.send_message(chat_id=idz, text='hello zahwa')
    url = 'https://imgur.com/u4fUN96'
    msg1 = 'wassupp babyy😘'
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text(msg1)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_PHOTO)
    update.message.reply_photo(url)
    for chats in msg_array:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      update.message.reply_text(chats)


def miss_you(update, context):
    msg_array = [
      'aw, sorry to hear that bih🙁',
      'wish i can be with you rn',
      'another me will try the best to treat you okay?',
    ]
    msg3 = 'itu foto aku lagi ganteng😎, liatin aja ok😘'
    url = 'https://imgur.com/a/KHP6LCf'
    for chats in msg_array:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      update.message.reply_text(chats)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_PHOTO)  
    update.message.reply_photo(url)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text(msg3)

def laper(update, context):
    msg_array = [
      '😅 looks my baby is hungry and ready to eat',
      'mau makan apa bih?',
      'another me gabisa beliin kamu makanan',
      'but the real one can buy you a food😘',
      'just choose what you wanna eat',
      'https://food.grab.com/id/en/',
      'and wait for the real me to chat you okay🤗'
    ]
    url = 'https://imgur.com/a/TRDc3ff'
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_PHOTO) 
    update.message.reply_photo(url)
    for chats in msg_array:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      update.message.reply_text(chats)

def hug_me(update, context):
    msg1 = 'alright, come here🤗'
    msg2 = 'did i give the best hug?'
    url = 'https://imgur.com/jMU82MF'
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text(msg1)   
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_PHOTO)  
    update.message.reply_photo(url)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text(msg2) 

def songs(update, context):
    msg_array = [
      'oke, ini lagu buat km',
      'lagi sending....',
      'sabaaaarrrrrrr'
    ]
    url = open('13.mp3', 'rb')
    for chats in msg_array:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      update.message.reply_text(chats)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_AUDIO)   
    update.message.reply_audio(url, timeout=10000)   


def birthday(update, context):
    msg_array = [
      'happy birthday to the best partner, i could ask for.',
      'you always keep it together,',
      'even when on the inside, you may want to run.'
    ] 
    stc_array = [
      'CAACAgIAAxkBAAJh1F61qZuasV9rLgABZhMEpeM1Yuax9wACtQADe8B9E5Yg38LQuSaEGQQ',
      'CAACAgIAAxkBAAJh1l61qcdQ3srC6MGINMpJhxE4kSZtAALFAAPsfdAGq7Hv4z8AATK5GQQ',
      'CAACAgQAAxkBAAJh2F61qfKNdESShXFjlYwNmA8l73DpAAKVBAACS2nuEDI-aq_9MVlcGQQ'
    ]
    photo = open('zhw.jpg', 'rb')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_PHOTO)
    update.message.reply_photo(photo)   
    for chats in msg_array:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      update.message.reply_text(chats)
    for sticker in stc_array:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      update.message.reply_sticker(sticker)  


def sticker(update, context):
  stc = 'CAACAgIAAxkBAAJhRF61EFfd2vuAuDuUBvNgqMikb5MSAAJtAAOmysgMzM_mSXJgKAkZBA'
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
  update.message.reply_sticker(stc)
  update.message.reply_text('tu zahwa kalo lg sange') 
  
def pink_lava(update, context):
  url = 'https://food.grab.com/id/en/restaurant/richeese-factory-graha-cijantung-delivery/IDGFSTI0000227q'
  msg_array = [
      'oh kamu mau pink lava ya bih',
      'ini kamu pesen aja di grabfood',
      'nanti aku bayarin pake ovo'
    ] 
  for chats in msg_array:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      update.message.reply_text(chats)
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)    
  update.message.reply_text(url)
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
  update.message.reply_text('pilih open with grab ya bih, jangan pake browser') 

def youtube_music(update, context):
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING) 
  update.message.reply_text(reply_markup=ForceReply(selective=True), text='reply this message, and send the link')
  return YOUTUBE_MUSIC   

def youtube_music_handler(update, context):
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING) 
  update.message.reply_text('okay wait...')
  #destination path, recommend to use path where this python file is there
  destination = 'youtube_music/'
  urls = update.message.text
  try:
    yt = YouTube(urls)
    stream = yt.streams.filter(only_audio=True).first()

    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text('downloading the audio file...')
    out_file = stream.download(output_path = destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    url = open(new_file, 'rb')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text('sending the audio file...')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_AUDIO)
    update.message.reply_audio(url) 
    return ConversationHandler.END

  except pytube.exceptions.RegexMatchError:
    update.message.reply_text('make sure you send the correct url')
    print('The Regex pattern did not return any matches for the video: {}'.format(urls))
    update.message.reply_text('try this command again')
    return ConversationHandler.END

  except pytube.exceptions.ExtractError:
    update.message.reply_text('failed to get the video, check the url')
    print ('An extraction error occurred for the video: {}'.format(urls))
    update.message.reply_text('try this command again')
    return ConversationHandler.END

  except pytube.exceptions.VideoUnavailable:
    update.message.reply_text('video is not available')
    print('The following video is unavailable: {}'.format(urls))
    update.message.reply_text('try this command again')
    return ConversationHandler.END 

def youtube_video(update, context):
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
  update.message.reply_text(reply_markup=ForceReply(selective=True), text='Reply this message, and send the link')
  return YOUTUBE_VIDEO   

def youtube_video_handler(update, context):
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
  update.message.reply_text('okay let me search that video')
  destination = 'youtube_video/'
  urls = update.message.text
  try:
    # yt = YouTube(urls)
    # stream = yt.streams.first()
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text('downloading the video file...')
    out_file = YouTube(urls).streams.get_highest_resolution().download(output_path = destination)
    # out_file = stream.download(output_path = destination)

    url = open(out_file, 'rb')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text('sending the video file...')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_VIDEO)
    update.message.reply_video(url)  
    return ConversationHandler.END

  except pytube.exceptions.RegexMatchError:
    update.message.reply_text('make sure you send the correct url')
    print('The Regex pattern did not return any matches for the video: {}'.format(urls))
    update.message.reply_text('try this command again')
    return ConversationHandler.END

  except pytube.exceptions.ExtractError:
    update.message.reply_text('failed to get the video, check the url')
    print ('An extraction error occurred for the video: {}'.format(urls))
    update.message.reply_text('try this command again')
    return ConversationHandler.END

  except pytube.exceptions.VideoUnavailable:
    update.message.reply_text('video is not available')
    print('The following video is unavailable: {}'.format(urls))
    update.message.reply_text('try this command again')
    return ConversationHandler.END

def translate(update, context):
  list_lang = [
    'Indonesian: id \n'
    'Javanese: jw \n'
    'English: en \n'
    'French: fr \n'
    'German: de \n'
    'Korean: ko \n'
  ]
  update.message.reply_text('List Language')
  for lang in list_lang:
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text(lang)
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
  update.message.reply_text(reply_markup=ForceReply(selective=True), text='Reply this message and type the country code\n example: id')  
  return LET_TRANSLATE

def translate_handler(update, context):
  global country_code
  if update.message.text == 'id':
    country_code = 'id'
    update.message.reply_text('Translate to Indonesian')
    update.message.reply_text(reply_markup=ForceReply(selective=True), text='Reply this message and send me the text')
    return TRANSLATED
  elif update.message.text == 'jw':
    country_code = 'jw'
    update.message.reply_text('Translate to Javanese')
    update.message.reply_text(reply_markup=ForceReply(selective=True), text='Reply this message and send me the text')
    return TRANSLATED
  elif update.message.text == 'en':
    country_code = 'en'
    update.message.reply_text('Translate to English')
    update.message.reply_text(reply_markup=ForceReply(selective=True), text='Reply this message and send me the text')
    return TRANSLATED
  elif update.message.text == 'fr':
    country_code = 'fr'
    update.message.reply_text('Translate to French')
    update.message.reply_text(reply_markup=ForceReply(selective=True), text='Reply this message and send me the text')
    return TRANSLATED
  elif update.message.text == 'de':
    country_code = 'de'
    update.message.reply_text('Translate to German')
    update.message.reply_text(reply_markup=ForceReply(selective=True), text='Reply this message and send me the text')
    return TRANSLATED
  elif update.message.text == 'ko':
    country_code = 'ko'
    update.message.reply_text('Translate to Korean')
    update.message.reply_text(reply_markup=ForceReply(selective=True), text='Reply this message and send me the text')
    return TRANSLATED         
  else:
    update.message.reply_text('Languange not found, make sure you type the correct code')  
    return ConversationHandler.END

def translate_result(update, context):
  text = update.message.text
  translator = Translator()
  if country_code == 'id':
    result = translator.translate(text, dest=country_code)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('from language: '+result.src)
    update.message.reply_text('to language: '+result.dest)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('text: '+result.origin)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text('translated text: '+result.text)
    update.message.reply_text('sending voice ...')
    speech = gTTS(text=result.text, lang=country_code, slow=False)
    dirs = "translate/"+text+"_in_"+country_code+".mp3"
    speech.save(dirs)
    url = open(dirs, 'rb')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_AUDIO)  
    update.message.reply_audio(url)  
    return ConversationHandler.END

  elif country_code == 'jw':
    result = translator.translate(text, dest=country_code)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('from language: '+result.src)
    update.message.reply_text('to language: '+result.dest)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('text: '+result.origin)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text('translated text: '+result.text)
    update.message.reply_text('sending voice ...')
    speech = gTTS(text=result.text, lang=country_code, slow=False)
    dirs = "translate/"+text+"_in_"+country_code+".mp3"
    speech.save(dirs)
    url = open(dirs, 'rb')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_AUDIO)  
    update.message.reply_audio(url)  
    return ConversationHandler.END

  elif country_code == 'en':
    result = translator.translate(text, dest=country_code)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('from language: '+result.src)
    update.message.reply_text('to language: '+result.dest)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('text: '+result.origin)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text('translated text: '+result.text)
    update.message.reply_text('sending voice ...')
    speech = gTTS(text=result.text, lang=country_code, slow=False)
    dirs = "translate/"+text+"_in_"+country_code+".mp3"
    speech.save(dirs)
    url = open(dirs, 'rb')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_AUDIO)  
    update.message.reply_audio(url)  
    return ConversationHandler.END

  elif country_code == 'fr':
    result = translator.translate(text, dest=country_code)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('from language: '+result.src)
    update.message.reply_text('to language: '+result.dest)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('text: '+result.origin)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text('translated text: '+result.text)
    update.message.reply_text('sending voice ...')
    speech = gTTS(text=result.text, lang=country_code, slow=False)
    dirs = "translate/"+text+"_in_"+country_code+".mp3"
    speech.save(dirs)
    url = open(dirs, 'rb')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_AUDIO)  
    update.message.reply_audio(url)  
    return ConversationHandler.END

  elif country_code == 'de':
    result = translator.translate(text, dest=country_code)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('from language: '+result.src)
    update.message.reply_text('to language: '+result.dest)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('text: '+result.origin)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text('translated text: '+result.text)
    update.message.reply_text('sending voice ...')
    speech = gTTS(text=result.text, lang=country_code, slow=False)
    dirs = "translate/"+text+"_in_"+country_code+".mp3"
    speech.save(dirs)
    url = open(dirs, 'rb')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_AUDIO)  
    update.message.reply_audio(url)  
    return ConversationHandler.END

  elif country_code == 'ko':
    result = translator.translate(text, dest=country_code)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('from language: '+result.src)
    update.message.reply_text('to language: '+result.dest)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('text: '+result.origin)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('translated text: '+result.text)
    update.message.reply_text('sending voice ...')
    speech = gTTS(text=result.text, lang=country_code, slow=False)
    dirs = "translate/"+text+"_in_"+country_code+".mp3"
    speech.save(dirs)
    url = open(dirs, 'rb')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_AUDIO)  
    update.message.reply_audio(url)  
    return ConversationHandler.END    

def youtube_trending(update, context):
  update.message.reply_text('okay, let me search a trending video for you')
  url = "https://www.youtube.com/feed/trending"
  response = urllib.request.urlopen(url)
  html = response.read()
  soup = BeautifulSoup(html, 'html.parser')
  link = soup.findAll(attrs={'class':'yt-uix-tile-link'})
  randomise = random.sample(link, 2)
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
  update.message.reply_text('trending video found!')
  for vid in randomise:
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
    update.message.reply_text('https://www.youtube.com' + vid['href'])

def youtube_search(update, context):
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
  update.message.reply_text(reply_markup=ForceReply(selective=True), text='Reply this message and send me the keyword')  
  return YOUTUBE_SEARCH

def youtube_search_result(update, context):
  textToSearch = update.message.text
  update.message.reply_text('okay, let me search that video for you')
  query = urllib.parse.quote(textToSearch)
  url = "https://www.youtube.com/results?search_query=" + query
  response = urllib.request.urlopen(url)
  html = response.read()
  soup = BeautifulSoup(html, 'html.parser')
  link = soup.findAll(attrs={'class':'yt-uix-tile-link'})
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
  update.message.reply_text('video found!')
  for vid in link[:2]:
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING) 
    update.message.reply_text('https://www.youtube.com' + vid['href'])
  return ConversationHandler.END

def bosen(update, context):
  stc1 = 'CAACAgIAAxkBAALw8l7l8jKmbA4iUuu9R4k5XdS_B05SAAIUAwACusCVBdUaMrGcC0iCGgQ'
  stc2 = 'CAACAgIAAxkBAALw7l7l8UfHrDd_x6TglpNXutgZ5Qw9AAJUAAN7wH0TlHV_JPVuYHkaBA'
  stc3 = 'CAACAgIAAxkBAALw8F7l8VSXSeUXQStjekke-FlwxSwgAAJ_AAOmysgMlaChOYY6gswaBA'
  msg1 = 'Kamu mah bosen terus'
  msg2 = 'Bosen kenapa deh?'
  msg3 = 'Hmmmm... \n yaudah bentar deh aku coba kasih kamu sesuatu biar ga bosen'
  msg4 = 'si jiaan cuman nitip ke gua buat ngasih ini doang'
  msg_array1 = [
    'ini playlist2 music nya si jian',
    'https://music.apple.com/id/playlist/songs-that-i-hear-when-youre-not-around-smp/pl.u-RRbVvBVF3AJ1qWb',
    'https://music.apple.com/id/playlist/j/pl.u-b3b8VGGCyW2vJgE'
  ]
  msg_array2 = [
    'ini dia nitip playlist2 youtube buat lu, nonton aja dah',
    'https://www.youtube.com/playlist?list=PLAbf_gIWb04EvVTzPINn87y5eOQm0vSwy',
    'https://www.youtube.com/playlist?list=PLAbf_gIWb04GNhyHIAC9GXXcGofuuEkVi',
    'https://www.youtube.com/playlist?list=PLAbf_gIWb04GG_zzRJFwJEFP28Wv3Bie0'
  ]
  msg_array3 = [
    'kalo ga nih order makanan aja dah, kalo udah kasih tau si jiaan aja ntr dibayar ok',
    'https://food.grab.com/id/en/',
    'https://food.grab.com/id/en/restaurant/mcdonald-s-cipayung-delivery/IDGFSTI000007sv',
    'https://food.grab.com/id/en/restaurant/richeese-factory-graha-cijantung-delivery/IDGFSTI0000227q',
    'https://food.grab.com/id/en/restaurant/ayam-gepuk-pak-gembus-tanah-merdeka-ciracas-delivery/IDGFSTI00001zwl'
  ]
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
  update.message.reply_sticker(stc1)
  update.message.reply_text(msg1)
  sleep(4)
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
  update.message.reply_sticker(stc2)
  update.message.reply_text(msg2)
  sleep(4)
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)  
  update.message.reply_sticker(stc3)
  update.message.reply_text(msg3)
  sleep(4)
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
  update.message.reply_text(msg4)
  sleep(2)
  for chats in msg_array1:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      update.message.reply_text(chats)
      sleep(2)
  sleep(2)
  for chatz in msg_array2:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      update.message.reply_text(chatz)
      sleep(2)
  sleep(2)
  for chatt in msg_array3:
      context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
      update.message.reply_text(chatt)
      sleep(2)

def curhat(update, context):
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
  update.message.reply_sticker('CAACAgIAAxkBAALxEF7mCfupv2GzRxj1YdMGz1wNBsG4AALmBwAClvoSBWB2oOUXBn3fGgQ')
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
  update.message.reply_text('yaudah curhat aja')
  context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
  update.message.reply_sticker('CAACAgIAAxkBAALxEl7mChDiUn76jqSYl9xUs-rvZiXyAALnBwAClvoSBbsiCXWBS4AXGgQ')
  update.message.reply_text('kalo udah selesai, bilang "udah" yabih (tanpa kutip)')
  if(update.effective_chat.id == idz):
    context.bot.send_message(chat_id=idj, text='Zahwa mau curhat nih, dengerin yuk')
    return CURHAT
  elif(update.effective_chat.id == idj):
    context.bot.send_message(chat_id=idz, text='Jiaan mau curhat nih, dengerin yuk')
    return CURHAT
  else:
    update.message.reply_text('yang bisa curhat cmn zahwa sama jian, kamu siapa?')
    return ConversationHandler.END

def listen_curhat(update, context):
  curhatan = update.message.text
  if curhatan == 'udah':
    update.message.reply_text('makasih udah mau curhat')
    return ConversationHandler.END
  else:
    if(update.effective_chat.id == idz):
      update.message.reply_text('curhatan kamu bakal dikirim ke Jiaan')
      context.bot.send_message(chat_id=idj, text=curhatan)
    elif(update.effective_chat.id == idj):
      update.message.reply_text('curhatan kamu bakal dikirim ke Zahwa')
      context.bot.send_message(chat_id=idz, text=curhatan)
    else:
      return ConversationHandler.END   

def reminder_birthday():
    bot = telegram.Bot(token=TOKEN)
    msg = [
      'semoga kamu tetap sehat selalu ya, panjang umur \n'
      'rezeki nya lancar, dan semoga yang kamu mau bakal terwujud',
      'amin...',
      'ohiya, jangan sedih terus😒 \n'
      'semangat zahwa, aku tau hidup ini emang susah, berat, bingungin buat kamu. \n \n'
      'tapi percaya deh, kamu pasti bakal nemu jawaban nya, kamu pasti bisa dapetin apa yang kamu mau, dan kamu juga bisa lewatin itu semua kalo kamu emang sabar dan yakin ngejalanin nya.',
      'jangan nyerah ya zahwa, semangat🤗'
    ]
    stc1 = 'CAACAgIAAxkBAAEBrLdf1RQ4NLWYueCM8OozP_W0YhTrhQACZwEAAhZCawpzib7OpZZoIh4E'
    stc2 = 'CAACAgIAAxkBAAEBrLtf1RRbwOs3-V5CYsn95C2mjIbJ-QACtAADe8B9E7SlTBuzXJXGHgQ'
    stc3 = 'CAACAgIAAxkBAAEBrL9f1RSN8LCz8FkWdVZRH7zh_OB7-gACfAEAAhZCawrtoK_LB7yPEx4E'
    stc4 = 'CAACAgIAAxkBAAEBrL1f1RRdl0i_K9AfITSmy4XH3jA8tgACtQADe8B9E5Yg38LQuSaEHgQ'
    stc5 = 'CAACAgIAAxkBAAEBrMlf1RyOw3jBA1dL78qP9iJPWdPL_QACaQADpsrIDONYOer9B49cHgQ'
    bot.send_sticker(idz, stc1)
    bot.send_message(idz, 'mam buah jambu \nsambil menyelem.')
    bot.send_message(idz, 'maaf ya, ganggu kamu malem2.')
    bot.send_sticker(idz, stc2)
    bot.send_chat_action(chat_id=idz, action=telegram.ChatAction.TYPING)
    sleep(2)
    bot.send_message(idz, 'selamat ulang tahun zahwa')
    bot.send_chat_action(chat_id=idz, action=telegram.ChatAction.TYPING)
    bot.send_message(idz, 'dari aku si bot kesayangan kamu😘')
    bot.send_sticker(idz, stc3)
    sleep(2)
    for chats in msg:
      bot.send_chat_action(chat_id=idz, action=telegram.ChatAction.TYPING)
      bot.send_message(idz, chats)
      sleep(2)
    bot.send_sticker(idz, stc4)
    sleep(2)
    bot.send_message(idz, 'btw, hadiahnya ini aja yaa😘')
    bot.send_message(idz, 'https://shopee.co.id/ZR-LEATHER-BAG-COLLECTION-i.129589467.5139055799')
    sleep(2)
    bot.send_chat_action(chat_id=idz, action=telegram.ChatAction.TYPING)
    bot.send_message(idz, 'bye zahwa')
    bot.send_sticker(idz, stc5)


def error_callback(update, context):
  try:
      raise context.error
  except Unauthorized:
      return ConversationHandler.END
      update.message.reply_text('unauthorized, try again...')
  except BadRequest:
      return ConversationHandler.END
      update.message.reply_text('bad request, try again...')
  except TimedOut:
      return ConversationHandler.END
      update.message.reply_text('connection timed out, try again...')
  except NetworkError:
      return ConversationHandler.END
      update.message.reply_text('network error or file size is too big. try again...')

def cancel(update, context):
    print("cancel")
    return ConversationHandler.END

def main():
  updater = Updater (token=TOKEN, use_context=True)
  dispatcher = updater.dispatcher

  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

  create_conversation_handler = ConversationHandler(
        entry_points = [CommandHandler('youtube_music',youtube_music), CommandHandler('youtube_video',youtube_video), CommandHandler("translate", translate), CommandHandler("youtube_search", youtube_search), CommandHandler("curhat", curhat)],

        states = {
            YOUTUBE_MUSIC: [MessageHandler(Filters.text, youtube_music_handler)],
            YOUTUBE_VIDEO: [MessageHandler(Filters.text, youtube_video_handler)],
            LET_TRANSLATE: [MessageHandler(Filters.text, translate_handler)],
            TRANSLATED: [MessageHandler(Filters.text, translate_result)],
            YOUTUBE_SEARCH: [MessageHandler(Filters.text, youtube_search_result)],
            CURHAT: [MessageHandler(Filters.text, listen_curhat)],
        },
        fallbacks = [CommandHandler('cancel',cancel)]
    )
  dispatcher.add_handler(create_conversation_handler)
  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(CommandHandler("miss_you", miss_you))
  dispatcher.add_handler(CommandHandler("laper", laper))
  dispatcher.add_handler(CommandHandler("albums", albums))
  dispatcher.add_handler(CallbackQueryHandler(album_handler))
  dispatcher.add_handler(CommandHandler("hug_me", hug_me))
  dispatcher.add_handler(CommandHandler("songs", songs))
  dispatcher.add_handler(CommandHandler("birthday", birthday))
  dispatcher.add_handler(CommandHandler("sticker", sticker))
  dispatcher.add_handler(CommandHandler("pink_lava", pink_lava))
  dispatcher.add_handler(CommandHandler("youtube_trending", youtube_trending))
  dispatcher.add_handler(CommandHandler("aku_bosen", bosen))

  dispatcher.add_error_handler(error_callback)

 # Start the Bot
  updater.start_webhook(listen="0.0.0.0",
                        port=int(PORT),
                        url_path=TOKEN)
  updater.bot.setWebhook('https://jiaanbot.herokuapp.com/' + TOKEN)
  updater.idle()
  reminder_birthday()

if __name__ == '__main__':
    main()
