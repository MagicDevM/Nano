import discord
from discord.ext import commands

class System(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name="ping", description="Check the bot's latency.")
    async def ping(self, ctx):
        await ctx.send(f'Pong! **{round(self.client.latency * 1000)}ms**')
    
    @commands.hybrid_command(name="help", description="help command.")
    async def help(self, ctx):
        help = discord.Embed(title="Helper Menu", description="**Command types**:\n- message\n- application commands\n\n**General**:\n- n!help\n- n!ping", colour=discord.Colour.blue())
        help.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=help)

async def setup(client):
    await client.add_cog(System(client))