from dotenv import load_dotenv
import os
import discord

load_dotenv()

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(name="ping", description="Responds with Pong!")
async def hello(ctx):
    await ctx.respond("Pong!")

bot.run(os.getenv("DISCORD_TOKEN"))