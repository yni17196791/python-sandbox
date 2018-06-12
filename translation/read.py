"""
**予めトークンを取得しておく必要がある**
同フォルダ内のprint_token.pyを実行し、認証とトークンの取得をしておくこと。
トークンはprinted_token.txt内に平文で取得される。
"""

import json
import requests
import os, tkinter, tkinter.filedialog, tkinter.messagebox

printed_token = open("printed_token.txt", "r")
areas = printed_token.readlines()
areas[0] = areas[0].strip("\n")

# 処理ファイルの選択
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*.txt")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('Google翻訳API','処理するテキストファイルを選択してください。\n一行あたり2000文字が翻訳の上限です。')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
f = open(file, 'r', encoding="utf-8_sig")

# 出力ファイルの選択
tkinter.messagebox.showinfo('Google翻訳API','書き込むファイルを選択してください。\n名前が被ると前の内容が消えるので注意！')
translatedfile = tkinter.filedialog.asksaveasfilename(filetypes = fTyp, initialdir = iDir)
translated = open(translatedfile, "w+", encoding="utf-8_sig")

line = f.readline()
while line:
  """
  **set your access token**
  1.sinup Google cloud pratform.(GCP)
  1.install google cloud sdk and setup it,
  2.get service-account key file from GCP (it's maybe json file)
  3.type command "gcloud auth activate-service-account --key-file=XXXXXXXXXXXXX.json"
  4.type command "gcloud auth print-access-token"
  5.token show display .  copy it and set this file and run.
  more detail:
  https://cloud.google.com/translate/docs/premium
  """
  token = areas[0] # set token here

  #REST api / "premium translation" url not euqal "normal transration" url !
  url = "https://translation.googleapis.com/language/translate/v2"
  #oldurl = "https://www.googleapis.com/language/translate/v2"

  # translate / en -> ja
  source = "en"
  target = "ja"

  # new translation needed
  model = "nmt"

  # translate target chars / must be less than 2K characters.
  # see : https://cloud.google.com/translate/docs/translating-text#translate-translate-text-python
  # this is sample chars from : http://web-tan.forum.impressrd.jp/e/2016/11/17/24396
  q = line

  payload = {
      'target':target,
      'source':source,
      'q':q,
      'model':model
  }

  headers = {
      'Content-Type':'application/json',
      'Authorization': 'Bearer ' + token,
  }

  response = requests.get(url,params=payload,headers=headers)

  # JSON decode
  jObj = json.loads(response.text)

  print(jObj)
  translated.write(jObj["data"]["translations"][0]["translatedText"]+"\n")
  # json.dump(jObj.translations.translatedText.decode(), translated)
  # translated.write(jObj)

  line = f.readline()
  # g = open('translated.txt', 'r', encoding="utf-8_sig")

f.close
translated.close
printed_token.close
# g.close
