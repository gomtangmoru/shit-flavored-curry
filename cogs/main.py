import discord, asyncio
from discord.ext import commands


class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.hybrid_command()
    async def ping(self, ctx):
        await ctx.send('Pong!')




