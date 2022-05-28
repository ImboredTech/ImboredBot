import discord
from discord.ext import commands
import config
import os


bot = commands.Bot(command_prefix=config.prefix)

@bot.event
async def on_ready():
    print("Bot is online!")


@bot.command()
async def load(ctx, extension):
    if ctx.author.id == config.owner_id:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded Cog: {extension}')
    else:
        await ctx.send("You have to be the owner to run this command.")

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == config.owner_id:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded Cog: {extension}')
    else:
        await ctx.send("You have to be the owner to run this command.")

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == config.owner_id:
        if extension == 'all':
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    bot.reload_extension(f'cogs.{filename[:-3]}')
                    await ctx.send("Reloaded all cogs.")
                else:
                    print("Stupid __pycache__ folder.")
        else:
            bot.reload_extension(f'cogs.{extension}')
            await ctx.send(f"Reloaded Cog: {extension}")
    else:
        await ctx.send("You have to be the owner to run this command.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print("Loaded Cogs.")
    else:
        print("Stupid __pycache__ folder.")

bot.run(config.token)