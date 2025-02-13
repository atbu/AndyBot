import os
import discord
import random
import youtube_dl
import time

from dotenv import load_dotenv
from discord.ext import commands, tasks
from itertools import cycle

description = 'This is a description!'

bot = commands.Bot(command_prefix=';', description=description, case_insensitive=True)

andy_quotes = [
    'I fell.',
    'I want that one.',
    'I don\'t like it.',
    'I want my stuff back.',
    'Fine! Fine! _(van crashes)_ Fine!',
    'Yeah, I know.',
    'I want to go to Florida.',
    'I want a whippy.',
    'I want a rabbit.',
    'It\'s his birthday, he\'s not dead!',
    'I don\'t like red.',
    'It was a bird!',
    'I can\'t read.'
]

andy_gifs = [
    'https://tenor.com/view/little-britain-andy-pipkin-i-want-that-one-point-matt-lucas-gif-16789249',
    'https://tenor.com/view/unimpressed-whatever-andy-pipkin-not-interested-whateva-gif-17678224',
    'https://tenor.com/view/yeah-i-know-little-britain-gif-7717727'
]

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}   

playing_statuses = ['with Lou', 'with my wheelchair', 'with a bird', 'without friends']
watching_statuses = ['insects', 'blind people', 'the Dominos delivery van', 'Shrek', 'how to grow an empire']
listening_statuses = ['Lou', 'deaf people', 'Karl Pilkington\'s podcast', 'the Ricky Gervais Show']
streaming_statuses = ['Andy']

@tasks.loop(seconds = 30)
async def changeStatus():
    status_category = random.randint(1,4)

    if status_category == 1:
        await bot.change_presence(activity=discord.Game(name=random.choice(playing_statuses)))
    if status_category == 2:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(watching_statuses)))
    if status_category == 3:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=random.choice(listening_statuses)))
    if status_category == 4:
        await bot.change_presence(activity=discord.Streaming(name=next(streaming_statuses), url=None))

# Triggered when the bot is ready.
@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    changeStatus.start()

class TextCommands(commands.Cog, name='Text Commands'):

    @commands.command(brief='How did he get up there?')
    async def tree(self,message):
        await message.send('I fell.')

    @commands.command(brief='Which one does he want?')
    async def choice(self,message):
        await message.send('I want that one!')

    @commands.command(brief='Does he like it?')
    async def opinion(self,message):
        await message.send('I don\'t like it!')

    @commands.command(brief='*watches all his things burning*')
    async def fire(self,message):
        await message.send('I want my stuff back.')

    @commands.command(brief='Andy causes an incident.')
    async def van(self,message):
        await message.send('Fine! Fine! _(van crashes)_ Fine!')

    @commands.command(brief='Does Andy know?')
    async def knowledge(self,message):
        await message.send('Yeah, I know!')

    @commands.command(brief='Helsinki!')
    async def helsinki(self,message):
        await message.send('I want to go to Florida!')

    @commands.command(brief='Cone.')
    async def icecream(self,message):
        await message.send('I want a whippy!')

    @commands.command(brief='Andy decides he wants a snake.')
    async def petshop(self,message):
        await message.send('I want a rabbit!')

    @commands.command(brief='I want that one.')
    async def card(self,message):
        await message.send('It\'s his birthday, he\'s not dead!')

    @commands.command(brief='Are you sure you want red?')
    async def red(self,message):
        await message.send('I don\'t like red.')

    @commands.command(brief='What happened here?')
    async def cement(self,message):
        await message.send('It was a bird!')

    @commands.command(brief='Andy goes to the library.')
    async def book(self,message):
        await message.send('I can\'t read.')

    @commands.command(brief='A random Andy quote.')
    async def quote(self,message):
        await message.send(random.choice(andy_quotes))

    @commands.command(brief='A random GIF of Andy.')
    async def gif(self,message):
        await message.send(random.choice(andy_gifs))

class VoiceCommands(commands.Cog, name='Voice Commands'):

    @commands.command(brief='Yeah, I know.')
    async def yik(self,message):

        if not message.author.voice:
            await message.send('you are not connected to a voice channel')
            return
        else:
            channel = message.author.voice.channel

        voice_client = await channel.connect()

        guild = message.guild

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('andy-mp3s/yik.mp3'))
        voice_client.play(source)

        while voice_client.is_playing():
            time.sleep(0.1)
        await voice_client.disconnect()

    @commands.command(brief='Andy causes an incident.')
    async def fine(self,message):

        if not message.author.voice:
            await message.send('you are not connected to a voice channel')
            return
        else:
            channel = message.author.voice.channel

        voice_client = await channel.connect()

        guild = message.guild

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('andy-mp3s/fine.mp3'))
        voice_client.play(source)

        while voice_client.is_playing():
            time.sleep(0.1)
        await voice_client.disconnect()

    @commands.command(brief='What happened here?')
    async def bird(self,message):
        if not message.author.voice:
            await message.send('you are not connected to a voice channel')
            return
        else:
            channel = message.author.voice.channel

        voice_client = await channel.connect()

        guild = message.guild

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('andy-mp3s/bird.mp3'))
        voice_client.play(source)

        while voice_client.is_playing():
            time.sleep(0.1)
        await voice_client.disconnect()

    @commands.command(brief='I don\'t like it.')
    async def idli(self,message):

        if not message.author.voice:
            await message.send('you are not connected to a voice channel')
            return
        else:
            channel = message.author.voice.channel

        voice_client = await channel.connect()

        guild = message.guild

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('andy-mp3s/idli.mp3'))
        voice_client.play(source)

        while voice_client.is_playing():
            time.sleep(0.1)
        await voice_client.disconnect()

    @commands.command(brief='Andy and Lou go to the shop.')
    async def birthday(self,message):

        if not message.author.voice:
            await message.send('you are not connected to a voice channel')
            return
        else:
            channel = message.author.voice.channel

        voice_client = await channel.connect()

        guild = message.guild

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('andy-mp3s/birthday.mp3'))
        voice_client.play(source)

        while voice_client.is_playing():
            time.sleep(0.1)
        await voice_client.disconnect()

    @commands.command(brief='Andy and Lou go to the shop.')
    async def library(self,message):

        if not message.author.voice:
            await message.send('you are not connected to a voice channel')
            return
        else:
            channel = message.author.voice.channel

        voice_client = await channel.connect()

        guild = message.guild

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('andy-mp3s/library.mp3'))
        voice_client.play(source)

        while voice_client.is_playing():
            time.sleep(0.1)
        await voice_client.disconnect()

    @commands.command(brief='Andy and Lou go to a very nice restaurant.')
    async def restaurant(self,message):

        if not message.author.voice:
            await message.send('you are not connected to a voice channel')
            return
        else:
            channel = message.author.voice.channel

        voice_client = await channel.connect()

        guild = message.guild

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('andy-mp3s/smurf.mp3'))
        voice_client.play(source)

        while voice_client.is_playing():
            time.sleep(0.1)
        await voice_client.disconnect()

    @commands.command(brief='Which one does he want?')
    async def thatone(self,message):

        if not message.author.voice:
            await message.send('you are not connected to a voice channel')
            return
        else:
            channel = message.author.voice.channel

        voice_client = await channel.connect()

        guild = message.guild

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('andy-mp3s/thatone.mp3'))
        voice_client.play(source)

        while voice_client.is_playing():
            time.sleep(0.1)
        await voice_client.disconnect()

bot.add_cog(TextCommands())
bot.add_cog(VoiceCommands())

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(DISCORD_TOKEN)