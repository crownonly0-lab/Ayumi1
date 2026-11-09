import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # মেসেজ পড়ার ইনটেন্ট অন রাখা

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('AYUMI🎀 is online and ready to chat!')

@bot.command()
async def hi(ctx):
    await ctx.send(f'Hello! I am AYUMI🎀, your server companion! 🎀')

bot.run("MTU2OTI3NTg5OTM1Mjk3MzQxNQ.G64KWO.rj57js0WliBxwJjSBY_k2GpEfoZKFiFZKXUyFQ")
