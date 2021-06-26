import discord
import os
import sys
import time
client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행 준비가 되었을 때 행동할 것
    print('Logged in as')
    print(client.user.name) # 클라이언트의 유저 이름을 출력합니다.
    print(client.user.id) # 클라이언트의 유저 고유 ID를 출력합니다.
    # 고유 ID는 모든 유저 및 봇이 가지고있는 숫자만으로 이루어진 ID입니다.
    print('------')

@client.event
async def on_message(message): # 입력되는 메세지에서 찾기
    if message.content.startswith('!eval '): # 만약 메세지가 '!ping'으로 시작된다면
        code = message.content[6:]
        silent = ("-s" in code)
        
        code = code.replace("-s", "")
        args = {
            "discord": discord,
            "json": json,
            "sys": sys,
            "os": os,
            "time": time,
            "import": __import__,
            "message": message,
            "client": client
        }
        
        try:
            exec(f"async def ij5_eval():{'  '+code}", args)
            a = time.time()
            response = await eval("ij5_eval()", args)
            if silent or (response is None) or isinstance(response, discord.Message):
                del args, code
                return
            
            await message.channel.send(f"```py\n{response}````{type(response).__name__} | {(time() - a) / 1000} ms`")
        except Exception as e:
            await message.channel.send(f"Error occurred:```\n{type(e).__name__}: {str(e)}```")
        
        del args, code, silent
client.run(os.getenv("dctoken"))
