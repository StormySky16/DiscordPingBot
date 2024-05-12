from discord.ext import commands
import discord
import time

BOT_TOKEN = "" #paste Bot token within quotes
CHANNEL_ID = 0 #replace 0 with desired channel ID

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
repeat = False
@bot.event
async def on_ready():
    print("Hello World!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello World!")

@bot.command()
async def hello(ctx):
    user = ctx.author
    await ctx.send("Hello!")

@bot.command()
async def ping(ctx):
    user = ctx.author
    id = user.id
    await ctx.send("<@" + str(id) + ">")

@bot.command()
async def start(ctx):
    global repeat 
    repeat = True
    user = ctx.author
    id = user.id
    while repeat:
        await ctx.send("<@" + str(id) + "> ")
        time.sleep(0.5)
        

@bot.command()
async def stop(ctx):
    global repeat
    repeat = False

bot.run(BOT_TOKEN)