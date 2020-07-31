import discord
from discord.ext import commands

token = "NzM4NDQwMzc5NDQzMTgzNzI4.XyL8Mg.23PtdJTYgkVIiJU_09ecSFULpIM"

bot = commands.Bot(command_prefix='!')

##repeat
@bot.command(pass_context=True)
async def rpt(ctx, *args):
    await ctx.send(args)

##give role
@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 738505305549307975:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == "man":
            role = discord.utils.get(guild.roles, name = "men")
        elif payload.emoji.name == "wmn":
            role = discord.utils.get(guild.roles, name = "women")
        ##elif payload.emoji.name == "":
            ##role = discord.utils.get(guild.roles, name = "other")

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)

##remove role
@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 738505305549307975:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == "man":
            role = discord.utils.get(guild.roles, name = "men")
        elif payload.emoji.name == "wmn":
            role = discord.utils.get(guild.roles, name = "women")
        ##elif payload.emoji.name == "":
            ##role = discord.utils.get(guild.roles, name = "other")

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)

bot.run(token)