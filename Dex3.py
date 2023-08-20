
from Dex4 import *

@led.on(events.NewMessage(pattern=r'^c', outgoing=True))
async def execute_script(event):
    c = os.popen('screen -X -S mo quit')
    print(c)
    if c:
        try: await event.edit(c.read())
        except: await event.edit('True')
    else:
        try:await event.edit(c.errors)
        except:await event.edit("False")

@led.on(events.NewMessage(pattern=r'^d', outgoing=True))
async def execute_script(event):

    c = os.popen(f"screen -S mo -dm bash -c 'python3 main1.py; exec sh'")
    print(c)
    if c:
        try: await event.edit(c.read())
        except: await event.edit('True')
    else:
        try:await event.edit(c.errors)
        except:await event.edit("False")

led.run_until_disconnected()

