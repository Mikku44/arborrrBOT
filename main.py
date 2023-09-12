from asyncio.tasks import wait_for
import discord
from discord import *
from discord.ext import commands
import os
import time
from discord.ext.commands import errors
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
import random
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import wait_for_component
#permission 2184440384

TOKEN = os.getenv(
    'ArBot')
pref = "'"
bot = commands.Bot(command_prefix=str(pref), help_command=None)  # กำหนด Prefix
slash = SlashCommand(bot, sync_commands=True)
client = discord.Client()
componenta1 = [(create_button(style=ButtonStyle.green, label="Restart"))]
componenta = [(create_button(style=ButtonStyle.blurple, label="Start"))]



@bot.event
async def on_ready():  # เมื่อระบบพร้อมใช้งาน
    print("Bot Started!")  # แสดงผลใน CMD
    print(f"Logged in as {bot.user}")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Type"+str(pref)+"help to see what is ArborrrBOT!!"))


async def on_command(ctx: errors):
    if isinstance(errors, commands.CommandNotFound):
        await ctx.send("Invalid command!!")


@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Cleared "+str(amount)+"!!")


@bot.command()
async def help(ctx):

    seconds = 1545925769.9618232
    local_time = time.ctime(seconds)
    icon = "https://img.webnovel.com/bookcover/19459283006520105/180/180.jpg?updateTime=1615952706053"
    emBed = discord.Embed(
        title="ArboBOT", description="ArboBOT is discord bot project for Arborrr Communication.!!\n\n", color=0xFFA500)
    emBed.set_author(name="ArboBOT", url=icon, icon_url=icon)
    emBed.set_thumbnail(
        url="https://sites.google.com/site/funnycatmeawww/_/rsrc/1422326075261/home/6997052-funny-cat.jpg?height=60&width=120")
    emBed.set_footer(text='Arbo '+str(local_time))


    embedcom = discord.Embed(title="ArboBOT Commands",
                             discription="A full list of commands is available here.\nCheck out with Commands 'help.\n\n", color=0xFFA500)
    icon = "https://cdn.readawrite.com/articles/2592/2591005/thumbnail/large.gif?8"
    embedcom.set_author(name="ArboBOT", url=icon, icon_url=icon)
    embedcom.set_thumbnail(
        url="https://sites.google.com/site/funnycatmeawww/_/rsrc/1422326075261/home/6997052-funny-cat.jpg?height=60&width=120")
    embedcom.add_field(name=str(pref)+"tmr <number>",
                       value="Use for counting down a number\n\n", inline=True)
    embedcom.add_field(name=str(pref)+"sw <number>",
                       value="Use for counting number with display.\n\n", inline=True)
    embedcom.add_field(name=str(pref)+"clear <number>",
                       value="Use for clearing message channels.\n\n", inline=True)
    embedcom.add_field(name=str(
        pref)+"invite", value="Use for invite Arbo to your server.\n\n", inline=True)
    embedcom.add_field(name=str(pref)+"prefix <new prefix>",
                       value="Use for change prefix (not available).\n\n", inline=True)
    embedcom.add_field(name=str(pref)+"play <music name>",
                       value="Used to play music.\n\n", inline=True)
    embedcom.add_field(name=str(
        pref)+"skip", value="Skips the current song being played.\n\n", inline=True)
    embedcom.add_field(name=str(pref)+"leave",
                       value="Used to disconnect Arbo.\n\n", inline=True)
    embedcom.add_field(name=str(
        pref)+"queue", value="Displays the current songs in queue.\n\n", inline=True)
    embedcom.set_footer(text='Arbo '+str(local_time))
    await ctx.channel.send(embed=emBed)
    button_ctx: componenta = await wait_for_component(bot)
    await button_ctx.send(embed=embedcom)



@bot.event
async def on_message(message):  # ดักรอข้อความใน Chat

    if message.content.startswith('arbo'):
        r = random.randint(0, 3)
        text_message = [("ว่าไง !!! "+str(message.author.name)+" ลองดูวิธีใช้ 'help"),
                        (":astonished: \nฮ๊ะ!!! อะไรครับ??"), ("คุณคือ"+str(message.author.name)+"สินะ!! ผมจะจำไว้"), ":wave:"]
        await message.channel.send(text_message[r])

    await bot.process_commands(message)


bot.run('OTY2NDEwMTI1NzM0NzE5NTcw.YmBVkQ.1KjQAhhMPUihVJy3F5rED-ZHQmo')
