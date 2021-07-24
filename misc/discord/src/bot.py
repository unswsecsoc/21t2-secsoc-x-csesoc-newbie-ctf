  
#!/usr/bin/env python3
import discord
from discord.ext import commands
from discord.errors import Forbidden
import os

bot_desc = "A bot for a CTF."
game = discord.Game("busy hacking the planet. will only reply to DMs 😳")
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!!"),
    description=bot_desc,
    help_command=None
)

@bot.event
async def on_ready():
    """Callback for successful login."""
    await bot.change_presence(status=discord.Status.online, activity=game)
    print(f"Logged in as {bot.user}")
    for guild in bot.guilds:
        print("Guild:", guild.name)

@bot.command()
async def help(ctx):
    """Help command."""
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.channel.send("```!!help    \tview this message.\n!!hello   \ti say hello!\n!!flooshed\t😳😳```")
    else:
        await ctx.message.delete()


@bot.command()
async def hello(ctx):
    """Hello command."""
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.channel.send("hello!")
    else:
        await ctx.message.delete()


@bot.command()
async def flooshed(ctx):
    """Flooshed command 😳😳"""
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.channel.send("NEWBIE{h4v3_fUn_m4k!nG_it_cR@sH_aNd_bUrN!!} 😳😳")
    else:
        await ctx.message.delete()


if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_BOT_TOKEN", ""), bot=True, reconnect=True)
