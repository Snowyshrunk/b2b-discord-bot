import discord
from discord.exe import commands, tasks
from mcstatus.exe import JavaServer

intents = discord.Intents.default()
intents.message_content = (True)

bot = commands.Bot(commands.when_mentioned_or("s!"), intents=intents)
server = JavaServer.lookup("play.back2basics.gg")

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(1187561310729273408)
    await channel.send(f"Welcome {member.mention} to Back 2 Basics!")

@tasks.loop(seconds = 300)
async def loop():
    status = server.status()
    await bot.change_presence(status=discord.Status.online , activity=discord.Game(f"on B2B with other {status.players.online} players!"))


@bot.listen("on_message")
async def on_message(message: discord.Message):

    if message.author.id == bot.user.id:
        return
    
    if message.content.startswith('!ip'):
        await message.reply('the server ip is play.back2basics.gg\n you can join using latest version!')
    
    if message.content.startswith('!dc'):
        await message.reply('invite link for discord server is [Back2Basics](discord.back2basics.gg)')

    if message.content.startswith('!swu'):
        await message.reply('to sum it up quickly spiro sold swu casue he was too bussy and wanted the server to be looked after by some one with more time for it, pizza mc bought it then ran it into the ground and deleted it with maybe 10minists of notice to the player base.')

    if message.content.startswith('!ranks'):
        await message.reply('this is a new server ranks are not transferable from other servers to this server')

    if message.content.startswith('!world'):
        await message.reply('this world was relesed on the 24th December 2023 \n so it is <t:1703452320:R> old')

    if message.content.startswith('!border'):
        await message.reply('the current world border is set to 5k~ blocks')



token = ("BOT_TOKEN")
loop.start
bot.run(token)