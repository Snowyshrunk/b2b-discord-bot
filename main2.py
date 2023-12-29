import discord
from discord.ext import commands, tasks
from mcstatus import JavaServer

intents = discord.Intents.default()
intents.message_content = (True)

bot = commands.Bot(commands.when_mentioned_or("s!"), intents=intents)

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(1187561310729273408)
    await channel.send(f"Welcome {member.mention} to Back 2 Basics!")

@tasks.loop(seconds = 20)
async def myLoop():
    print("loop")
    await bot.wait_until_ready()
    print("ready")
    server = JavaServer.lookup("back2basics.gg:25565")#needs to be replaced with server ip and port (play.back2basics.gg doesn't work due to the play.)
    print(f'{server}')
    status = server.status()
    print(f'{status.players.online}')
    players = status.players.online
    await bot.change_presence(status=discord.Status.online , activity=discord.Game(f"with {players} other players on play.back2basics.gg !"))

@bot.slash_command()
async def ip(ctx):
    await ctx.respond('the server ip is play.back2basics.gg\n you can join using latest version!')

@bot.slash_command()
async def dc(ctx):
    await ctx.respond('invite link for discord server is [Back2Basics](discord.back2basics.gg)')

@bot.slash_command()
async def swu(ctx):
    await ctx.respond('to sum it up quickly spiro sold swu cause he was too busy and wanted the server to be looked after by some one with more time for it, pizza mc bought it then ran it into the ground and deleted it with maybe 10 minutes of notice to the player base.')

@bot.slash_command()
async def ranks(ctx):
    await ctx.respond('this is a new server ranks are not transferable from other servers to this server')

@bot.slash_command()
async def world(ctx):
    await ctx.respond('this world was released on the 24th December 2023 \n so it is <t:1703452320:R> old')

@bot.slash_command()
async def border(ctx):
    await ctx.respond('the current world border is set to 5k~ blocks')

token = ("BOT_TOKEN")
myLoop.start()
bot.run(token)