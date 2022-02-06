import os
import discord
import asyncio
import time
import requests as rq
from discord.ext import commands
from discord.ext import tasks


## Setup
client = commands.Bot(command_prefix=['^'])
client.remove_command('help')


## Events
@client.event
async def on_ready():
    print('BOT RUN SHOD!')
    client.my_current_task = live_status.start()

## Players Count Function // Callable Everywhere, returns number
def pc():
    try:
        resp = rq.get('http://109.72.192.93/players.json').json()
        return(len(resp))
    except:
        return('ONLINE')



## Players Command
@client.command()
@commands.has_permissions(administrator=True) 
async def players(ctx):
    
    timenow = time.strftime("%H:%M")
    resp = rq.get('http://109.72.192.93/players.json').json()
    total_players = len(resp)
    if len(resp) > 25:
        for i in range(round(len(resp) / 25)):
            embed = discord.Embed(title='DISCORD Bot', description='Server Players', color=discord.Color.blurple())
            embed.set_footer(text=f'Total Players : {total_players} | DISCORD Bot | {timenow}')
            count = 0
            for player in resp:
                embed.add_field(name=player['name'], value='ID : ' + str(player['id']))
                resp.remove(player)
                count += 1
                if count == 25:
                    break
                else:
                    continue

            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='DISCORD Bot', description='Server Players', color=discord.Color.blurple())
        embed.set_footer(text=f'Total Players : {total_players} | FiveMBot | {timenow}')
        for player in resp:
            embed.add_field(name=player['name'], value='ID : ' + str(player['id']))
        await ctx.send(embed=embed)

## Live Status
@tasks.loop()
async def live_status(seconds=1):
    pcount = pc()
    Dis = client.get_guild(927648876628951070) #Int

    activity = discord.Activity(type=discord.ActivityType.watching, name=f'👑 {pcount}')
    await client.change_presence(activity=activity)
    await asyncio.sleep(15)

    activity = discord.Activity(type=discord.ActivityType.watching, name=f'✨ {Dis.member_count}')
    await client.change_presence(activity=activity)
    await asyncio.sleep(15)

## Help Command
@client.command()
@commands.has_permissions(administrator=True) 
async def help(ctx):
    
    embed=discord.Embed(title="HAZARD COMPANY", description="HAZARD COMPANY Bot Commands List", color=0xfff700)
    embed.set_author(name="Welcome To HAZARD COMPANY Bot", url="HAZARD COMPANY", icon_url="https://cdn.discordapp.com/attachments/863136519346978846/879672442283495464/c072cb6e4ac81b89.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863136519346978846/879672442283495464/c072cb6e4ac81b89.png")
    embed.add_field(name="^say", value="Payam Dadan Be Sorat Embed", inline=False)
    embed.add_field(name="^hsay", value="Payam Dadan Bdon Embed", inline=False)
    embed.add_field(name="^run", value="Server run shod Embed", inline=False)
    await ctx.send(embed=embed)
      
## Say Commands
@client.command(pass_content=True, aliases=['s'])
@commands.has_permissions(administrator=True) 
async def say(ctx, *, text):
    
    try:
        await ctx.message.delete()
        timenow = time.strftime("%H:%M")
        embed=discord.Embed(title="HAZARD NEWS", description=" ", color=0xfff705)
        embed.set_author(name="Discord", url="https://discord.gg/wrTMbHeSZV", icon_url="https://cdn.discordapp.com/attachments/927671059719802920/927691926558351390/download.png")
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.add_field(name="**Announce : **", value=text, inline=False)
        embed.set_footer(text=f"{ctx.message.author} | HAZARD COMPANY | {timenow}")
        await ctx.send(embed=embed)
    except Exception as err:
        print(err)
    
@client.command(pass_context=True, aliases=['hs'])
@commands.has_permissions(administrator=True) 
async def hsay(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

client.run('OTM2OTY2MTQ3MjA1NjMyMDAw.YfU3uQ.3KtplKo3-fczN5cH_oBlM9hvGnE')