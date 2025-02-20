import discord
from discord.ext import commands

client = commands.Bot (commands_prefix="!CheakSate")

@client.command()
async def hi(ctx):
    await ctx.send ("hello")
    
client.run("MTM0MjE0MTY4OTE3NDY5MTk5Mw.Gt_p6Q.SGyRZisJH286vYD9TY7dl1Nw9bYqe3kpfw59g0")
