import discord
from discord.ext import commands
from discord.ext.commands import Bot
client = commands.Bot(command_prefix="UwU ")

@client.event
async def on_ready():
    print("bot is ready")
    
@client.command()
async def hewwo(ctx):
    await ctx.send("hewwo wowwd")
        
@client.command()
async def suicide(ctx):
    await ctx.send("fucking kill me please help put me out of this misery fucking end my suffering please")
    
@client.command()
async def hewp(ctx):
    await ctx.send("This is the Help Section of Fuwwy Muwway's Bot. Might be updated. Check github for updates (if muwway adds me to gihub that is uwu).\n```UwU is my prefix.\nUse UwU alongside my commands to trigger them, uwu.``` Might make a list of commands if Muwway is feewing cute uwu. Bye fow now fuwwy fwiends uwu.")
        
@client.command()
async def invite(ctx):
    await ctx.send("Heres's my invite link: https://discord.com/api/oauth2/authorize?client_id=798553197652344872&permissions=0&scope=bot")
        
client.run("bot token")
