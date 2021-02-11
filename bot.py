import discord
from discord.ext.commands import bot, Bot
import os

bot = Bot(command_prefix='논!')

@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다!')

@bot.command()
async def 주인(ctx):
    await ctx.send('qPluxxy')

@bot.command()
async def 안녕(ctx):
    await ctx.send('반....갑....다........')

@bot.command()
async def 핑(ctx):
    await ctx.send('퐁! {0}'.format(round(bot.latency*1000))+'ms')

access_token = os.environ["BOT_TOKEN"]    
bot.run(access_token)
