import discord, os, server, random
from discord.ext import commands

#UptimeRobot is being weird, so i'm using GitHub to take this code and host it on Heroku.
#if you find things you would wish to chande or is broken, make a pull request in GitHub.
#plz plz PLZ boost my server at https://discord.gg/6GPjN8C
#feel free to base your not off of mine, but give me credit

prefix="cs!"
token=os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

def make_embed(title, desc, color):
  return discord.Embed(title=title, description=desc, color=color)

def replaceSpaces(string): 
  string = string.strip() 
  i = len(string) 
  space_count = string.count(' ') 
  new_length = i + space_count * 2
  if new_length > 1000: 
    return -1
  index = new_length - 1
  string = list(string)  
  for _ in range(i - 2, new_length - 2): 
    string.append('0')  
  for j in range(i - 1, 0, -1): 
    if string[j] == ' ': 
      string[index] = '0'
      string[index - 1] = '2'
      string[index - 2] = '%'
      index = index - 3
    else: 
      string[index] = string[j] 
      index -= 1
  return ''.join(string)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(f'{prefix}help'))
  print(f'{client.user} is online')

@client.event
async def on_command_error(ctx, error):
  embed = make_embed(title="Error", desc="", color=discord.Color.red())
  embed.add_field(name=":face_with_raised_eyebrow: ", value=error)
  await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = make_embed(title="Help", desc="", color=discord.Color.red())
    embed.add_field(name="Commands", value=f"{prefix}hello (aliases: {prefix}hi, {prefix}hey), {prefix}ping, {prefix}repl, {prefix}twitch, {prefix}youtube, {prefix}google, {prefix}8ball")
    await ctx.send(embed=embed)

@client.command(aliases=['hi', 'hey'])
async def hello(ctx):
  await ctx.send(f'Hello, {ctx.author.name}!')

@client.command()
async def ping(ctx):
  await ctx.send('pong')

@client.command()
async def repl(ctx, *, term):
  await ctx.send(f"https://replsearch.johndo3.repl.co/results?q={replaceSpaces(term)}")

@client.command()
async def twitch(ctx, *, term):
  await ctx.send(f"https://twitch.tv/search?term={replaceSpaces(term)}")

@client.command()
async def youtube(ctx, *, term):
  await ctx.send(f"https://www.youtube.com/results?search_query={replaceSpaces(term)}")

@client.command()
async def google(ctx, *, term):
  await ctx.send(f"https://www.google.com/search?q={replaceSpaces(term)}")

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = ["It is certain.",
              "It is decidedly so.",
              "Without a doubt.",
              "Yes - definitely.",
              "You may rely on it.",
              "As I see it, yes.",
              "Most likely.",
              "Outlook good.",
              "Yes.",
              "Signs point to yes.",
              "Reply hazy, try again.",
              "Ask again later.",
              "Better not tell you now.",
              "Cannot predict now.",
              "Concentrate and ask again.",
              "Don't count on it.",
              "My reply is no.",
              "My sources say no.",
              "Outlook not so good.",
              "Very doubtful."]
  embed = make_embed(title="Magic 8 Ball", desc="", color=discord.Color.red())
  embed.add_field(name=":8ball:", value=random.choice(responses))
  await ctx.send(embed=embed)

@client.command(aliases=['surprise'])
async def rickroll(ctx):
  await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

server.server()
client.run(token)
