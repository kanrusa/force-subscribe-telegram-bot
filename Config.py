import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1284849048:AAE10minjZ3FxdgKf4h3Ro3tpOrKKFTPWVY"
    DATABASE_URL = "postgres://vlrwadbjiukelz:3e199c3a45253c45ecb0852a07f38a80970f90edd9289cab41790258ef48b926@ec2-34-202-88-122.compute-1.amazonaws.com:5432/dc6nvtn3cphufs"
    APP_ID = "1701281"
    API_HASH = "3b605acece943445fd1b0dbc461141ea"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Hanya untuk grup @birojodohroleplayer**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__Ini adalah bot khusus untuk mute pengguna di grup bjrp yang belum sub channel @birojodohroleplayer.\nLearn more at /help__"
