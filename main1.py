
from Dex4 import *



@led.on(events.NewMessage(pattern=r't', outgoing=True))
async def execute_script(event):
    user = event.message.message[2:]
    x = 0
    while True:
     i = 0
     while True:
      i += +1
      x += +1
      if i == 100:
       sleep(1)
       break
      sleep(0.1)
      req = requests.get(f"https://t.me/{user}")
      if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
       take = await led(UpdateUsernameRequest(user))
       if take :
        requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text=« new hutting »
« UserName » : « @{user} »
---------------------------------
« attempts » : « {x} »
----------------------------------
« Save » : « Channel »
----------------------------------
« owner » :  @isiraqi »""")
      else:
       print(f"NOOO : {user}" + ' ' + str(i)+" "+str(x))





@led.on(events.NewMessage(pattern=r'x', outgoing=True))
async def execute_script(events):
    await events.edit('okay')
    await led.send_message('botfather', '/newbot')
    sleep(1)
    await led.send_message('botfather', 'Dex')
    x = 0
    while True:
        i=0
        while True:
            i += +1
            x += +1
            u = str(''.join((random.choice(uss) for i in range(2))))
            e = str(''.join((random.choice(rr) for i in range(1))))
            user = e + u + 'bot'
            if i == 150:
                if 'off' in open('check.txt', 'r').read() :
                    print('Godd+++++++++++++++++++++++++++++++')
                s= open('check.txt', 'w')
                s.write(str(x))
                s.close()
                sleep(1)
                break
            sleep(0.165)
            req = requests.get(f"https://t.me/{user}")
            if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
                p = requests.get(f"https://fragment.com/username/{user}").text
                sleep(0.3)
                if 'Unavailable' in p:
                    try:
                        z = await led.send_message('botfather', user)
                        if z:

                            await led.send_message('botfather', '/newbot')
                            sleep(1)
                            await led.send_message('botfather', 'Dex')

                    except Exception:
                        pass
            else:
                pass
                print('me',(f"NOOO : {user}" + ' ' + str(i) + " " + str(x)))

@led.on(events.NewMessage(pattern=r'e', outgoing=True))
async def execute_script(event):
    s = open('main.txt', 'w').write('off')
    await event.edit(s)

@led.on(events.NewMessage(pattern=r'p', outgoing=True))
async def execute_script(event):
    s = open('check.txt', 'r').read()
    await event.edit(s)

try:
    led.run_until_disconnected()
except Exception:
    pass