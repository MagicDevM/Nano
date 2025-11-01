import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.hybrid_command(name="members", description="returns the server's member count.")
    async def members(self, ctx):
      await ctx.send(f"**{ctx.guild.name}'s Totsl Members**: {ctx.guild.member_count}")
    @commands.hybrid_command(name="serverinfo", description="Shows information about the current server")
    async def serverinfo(self, ctx):
      guild = ctx.guild
      threads = len(guild.threads)
      total_channels = len(guild.channels) - len(guild.categories)
      total_channels_and_categories = len(guild.channels)
      text_channels = len(guild.text_channels)
      voice_channels = len(guild.voice_channels)
      categories = len(guild.categories)
      stage_channels = len(guild.stage_channels)
      forum_channels = len(guild.forums)
      roles = len(guild.roles)
      banner = guild.banner
      icon = guild.icon
      creation_date = guild.created_at
      description = guild.description
      emojis = len(guild.emojis)
      emoji_limit = guild.emoji_limit
      stickers = len(guild.stickers)
      sticker_limit = guild.sticker_limit
      vanity_link = guild.vanity_url
      id = guild.id
      name = guild.name
      members = guild.member_count
      owner = guild.owner
      verification_level = guild.verification_level
      boost_level = guild.premium_tier
      bans = len([entry.user.id async for entry in guild.bans()])
      
      embed = discord.Embed(title=f"{guild.name}'s Info", description=f"- Basic Info\n**Name**: {name}\n**Description**: {description}\n**Id**: {id}\n**Owner**: {owner.name}\n**Creation Date**: {creation_date.day}/{creation_date.month}/{creation_date.year}\n**Members**: {members}\n\n- Channels & Categories\n**Total Channels**: {total_channels}\n**Total Channels & Categories**: {total_channels_and_categories}\n**Text Channels**: {text_channels}\n**Voice Channels**: {voice_channels}\n**Forum Channels**: {forum_channels}\n**Stage Channels**: {stage_channels}\n**Categories**: {categories}\n\n- Miscellaneous\n**Threads**: {threads}\n**Roles**: {roles}\n**Emojis**: {emojis}/{emoji_limit}\n**Stickers**: {stickers}/{sticker_limit}\n**Booster Level**: {boost_level}\n**Verfication Intensity**: {verification_level}\n**Vanity Link**: {vanity_link}\n**Total Bans**: {bans}", color=discord.Colour.orange())
      embed.set_thumbnail(url=icon)
      embed.set_image(url=banner)
      embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
      await ctx.send(embed=embed)
    
      

async def setup(client):
    await client.add_cog(General(client))