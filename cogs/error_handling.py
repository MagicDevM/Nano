import discord
from discord.ext import commands

class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        @self.bot.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("You missed a required argument!")
            elif isinstance(error, commands.MissingPermissions):
                await ctx.send("You don't have the permission to use this command.")
            elif isinstance(error, commands.CommandNotFound):
                return
            elif isinstance(error, commands.BadArgument):
                await ctx.send("Some of your arguments are invalid.")
            elif isinstance(error, commands.TooManyArguments):
                await ctx.send("Too Many arguments provided.")
            elif isinstance(error, commands.MissingPermissions):
                await ctx.send("You don’t have permission to use this command.")
            elif isinstance(error, commands.BotMissingPermissions):
                await ctx.send("I don’t have permission to do that.")
            elif isinstance(error, commands.NoPrivateMessage):
                await ctx.send("You can’t use this command in DMs.")
            elif isinstance(error, commands.DisabledCommand):
                await ctx.send("This commabd is currently disabled.")
            elif isinstance(error, commands.CommandOnCooldown):
                await ctx.send("This command is currently on cooldown.")
            else:
                print(f"Unexpected error: {error}")
                error = discord.Embed(title="An unexpected error occured", description=f"An unexpected error occurred while running `{ctx.command}`\n\n**ERROR**: __{error}__", colour=discord.Colour.red())
                await ctx.send(embed=error, ephemeral=True)

async def setup(bot):
    await bot.add_cog(ErrorHandling(bot))