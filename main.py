import disnake
import apikey
import requests
from disnake.ext import commands

intents = disnake.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents.all()
)

headers = {
    'X-CMC_PRO_API_KEY': apikey.btc,
    'accepts': 'application/json'
}

btc = {
    'start': '1',
    'limit': '1',
    'convert': 'EUR'
}

url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=btc, headers=headers).json()


coins = json['data']

coins[0]

for x in coins:
    if x['symbol'] == 'BTC':
        token = x['quote']['EUR']['price']
    print(x["symbol"], x['quote']['EUR']['price'])


@bot.event
async def on_member_join(member):
    general_channel: disnake.TextChannel = bot.get_channel(1022069363580354580)
    await general_channel.send(
        content=f"Bienvenue {member.display_name} je t'invite à te présenter ici <#1009873129046290525>")


@bot.event
async def on_ready():
    print(f"Le bot et prêt  |  {bot.user}")


@bot.command()
async def test(ctx) -> None:
    await ctx.reply("Works!")


@bot.command()
async def ainz(ctx):
    await ctx.reply("Seigeur Ainz Ooal Gown")


@bot.command()
async def info(ctx):
    server = ctx.guild
    number_of_text_channel = len(server.text_channels)
    number_of_voice_channel = len(server.voice_channels)
    numbers_of_person = server.member_count
    server_name = server.name
    message = f"Le serveur {server_name} contient {numbers_of_person} personnes. \nLe serveur a {number_of_voice_channel} chat vocal et {number_of_text_channel} chat textuel"
    await ctx.send(message)


@bot.command()
async def clear(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    for content in messages:
        await content.delete()


@bot.command()
async def ban(ctx, user: disnake.User, *reason):
    reason = " ".join(reason)
    embed = disnake.Embed(title="**Banissement**", description="Un modérateur a frappe !")
    embed.set_author(name=ctx.author.name)
    embed.set_thumbnail(
        url="https://discords.com/_next/image?url=https%3A%2F%2Fcdn.discordapp.com%2Femojis%2F849656179863977984.gif%3Fv%3D1&w=64&q=75")
    embed.add_field(name="Modérateur", value=ctx.author.name, inline=False)
    embed.add_field(name="Membre banni", value=user.name, inline=False)
    embed.add_field(name="Raison du ban", value=reason, inline=False)
    await ctx.send(embed=embed)
    await ctx.guild.ban(user, reason=reason)


@bot.command()
async def kick(ctx, user: disnake.User, *reason):
    reason = " ".join(reason)
    embed = disnake.Embed(title="**Kick**", description="Un modérateur à kick!")
    embed.set_author(name=ctx.author.name)
    embed.set_thumbnail(
        url="https://discords.com/_next/image?url=https%3A%2F%2Fcdn.discordapp.com%2Femojis%2F723096791230316544.png%3Fv%3D1&w=64&q=75")
    embed.add_field(name="Modérateur", value=ctx.author.name, inline=False)
    embed.add_field(name="Membre kick", value=user.name, inline=False)
    embed.add_field(name="Raison du ban", value=reason, inline=False)
    await ctx.send(embed=embed)
    await ctx.guild.kick(user, reason=reason)


@bot.command()
async def btc(ctx):
    await ctx.send(f'Le Bitcoin est à : ||{token}|| €')

bot.run(apikey.keybot)
