#!/usr/bin/python3

import discord
import requests
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'Xiaomilove!'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# ログイン&準備が完了したら一度だけ実行される
@client.event
async def on_ready():
    # コンソールにBOTとしてログインした名前とUSER-IDを出力
    print('Logged in as')
    print('BOT-NAME :', client.user.name)
    print('BOT-ID   :', client.user.id)
    print('------')

# メッセージを受信するごとに実行される
@client.event
async def on_message(message):

    e = requests.get("https://correctjp.work/api/all.php?text="+message.content+"&user="+str(message.author))
    # BOTとメッセージの送り主が同じ人なら処理しない
    if client.user == message.author:
        return

    elif message.content.startswith('怪しい日本語　ヘルプ'):
       typee = "normal"
       inputxt = message.content[6:]
       inputxt.strip()
       print("ヘルプ")
       r = requests.get("https://correctjp.work/api/help.php")
       await message.channel.send(r.text)

    elif message.content.startswith('怪しい日本語 ヘルプ'):
       typee = "normal"
       inputxt = message.content[6:]
       inputxt.strip()
       print("ヘルプ")
       r = requests.get("https://correctjp.work/api/help.php")
       await message.channel.send(r.text)

    elif message.content.startswith('怪しい日本語　status'):
       typee = "normal"
       inputxt = message.content[6:]
       inputxt.strip()
       print("Status")
       r = requests.get("https://correctjp.work/api/status.php")
       await message.channel.send(r.text)

    elif message.content.startswith('怪しい日本語 status'):
       typee = "normal"
       inputxt = message.content[6:]
       inputxt.strip()
       print("Status")
       r = requests.get("https://correctjp.work/api/status.php")
       await message.channel.send(r.text)

    elif message.content.startswith('怪しい日本語'):
       typee = "normal"
       inputxt = message.content[6:]
       inputxt.strip()
       r = requests.get("https://correctjp.work/api/discordbot.php?text="+inputxt+"&user="+str(message.author))
       r = requests.get("https://correctjp.work/api/index.php?type="+typee+"&text="+inputxt+"&json=no")
       print(r.text)
       await message.channel.send(r.text)

    elif client.user in message.mentions: # 話しかけられたかの判定
        reply = message.content
#        print(reply)
       # rmv = reply.split('<')[-1].split('>')[0]
       # rmv2 = reply.strip('<')[-1].strip('>')[0]
       # print(rmv)
       # print(rmv2)
        reply2 = reply.lstrip("<@598172167548567563>　")
        print(reply2)
   #     reply.strip(rmv)
        urll = "https://correctjp.work/api/index.php?type=normal&text="+reply2+"&json=no"
        print(urll)
        r = requests.get(urll)
        await message.channel.send(r.text)

client.run(TOKEN)
