import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.hybrid_command(name="members", description="returns the server's member count.")
    async def members(self, ctx):
      await ctx.send(f'Members: **{ctx.guild.member_count}**')

async def setup(client):
    await client.add_cog(General(client))