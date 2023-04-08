'''
Simple bot that checks reservations
for the next n days.
'''

import turboself

import discord
from discord.ext import tasks
from datetime import datetime, timedelta


bot = discord.Client(intents = discord.Intents.all())
client = turboself.Client('xxx', 'xxx', debug = True, login = False)

userid = 00000000000000000000000 # Enter user id here

fov = timedelta(days = 7) # How far the bot can see

@bot.event
async def on_ready() -> None:
    # Start the looper
    
    print('Bot started')
    
    author = await bot.fetch_user(userid)
    looper.start(author)


@tasks.loop(hours = 12)
async def looper(author: discord.User) -> None:
    # Check loop
    
    print('Updating data')
    today = datetime.now()
    
    # Attempt to connect
    client.clear_cache()
    client.login()
    
    weeks = list(client.get_reservations())
    
    for week in weeks:
        for day in week.days:
            
            # Break if day too far
            if day.date - today > fov: return
            
            if day.can_eat and not day.eat:
                # Has not reserved
                
                print('Sending message for day', day.date)
                
                raw = day.date.strftime('%A, %d %B %Y')
                await author.send(f':warning: You do not have reserved for `{raw}`.')

bot.run('bot_token_here')