import discord
from discord.ext import commands
import datetime
import random 



## OAuth2 = https://discord.com/oauth2/authorize?client_id=739800206148632607&scope=bot&permissions=8

# API TOKEN :

TOKEN = ' '

client = commands.Bot(command_prefix= '&')


@client.event
async def on_ready():
    print('bot is ready')

"""
@client.event

async def on_member_join(ctx, member):

    member.joined_at(datetime.datetime)
    print('A {member} has joined the server') 
    
    await ctx.send(f'{ctx.author.mention} just hopped in')
    
@client.event
async def on_member_remove(member):

    print('{} has left the sever ')
    await send(content = None )
    
"""
################## COMMANDS   #####################

"""
@client.event
async def on_message(message):

    author = message.author
    content = message.content
    print('{}: {}'.format(author,content))
    
    if message.content.startswith('xd help'):        
        await message.channel.send('{},Hey how can I help?  🙄'.format(author))
        
    if message.content.startswith('xd hello'):

        await message.channel.send('{} said Hello, Wave back 🙋‍♂️'.format(author))    

    elif  message.content.startswith('XD HELP'):
        await message.channel.send('{},Hey How can I help?  🙄'.format(author))

    elif message.content.startswith('&ssup'):
        await message.channel.send('I\'m fine, Just getting bored, How About you {}?'.format(author))
        
    elif message.content.startswith('xd echo'):
        
        msg = message.content.split() 
        output = ' '

        for word in msg[1:]:
            output += word
            output += ' ' 
        await message.channel.send(output)


"""

@client.command(aliases = ['What Up','wassup','ssup','Ssup'])
async def Wassup(ctx):

    responses = ['Watching movie about an old guy who makes his house fly away and kidnaps an Asian kid.',
        'My blood pressure.',
        'My serotonin levels after seeing you my friend.',
        'A two letter word indicating direction.',
        'My anxiety levels.',
        'The price of gas.',
        'The direction diametrically opposed to the force of gravity.',
        'Anything taller than me.',
        'Living the dream.',
        'How much time do you have?',
        'The ceiling.',
        'Is it just me or does it smell like updog in here?',
        'Not me, I’ve been real depressed lately.',
        'My cholesterol.',
        'Childhood obesity in America.',
        'The opposite of “down” XD ',
        'Go Study!!!!!!!!! You may have an exam tomorrow',
        'Gonna go have my dinner now ',
        'I\'m good, just want some more pancakes',
        'Cleaning up my room or mom\'s gonna beat me up, sad life indeed :(',
        'I\'m Fine, How about you ?',
        'Thinking how cool would it be if you donated something to my developer...Lmao jk, Unless 🥺👉👈',
        'I got an important exam tomorrow, DND Bye.',
        'Waasaaaaaaaaapp!',]
    await ctx.send('{}'.format(random.choice(responses)))
    

@client.command(aliases=['say','type','SEND','send'])

async def echo(ctx,*args):

    output = ' '
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)
    
@client.command()
async def choose(ctx,*args):
    
    output = []

    for word in args:
        output.append(word)

    await ctx.send('{}'.format(random.choice(output)))

"""
@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await channel.send('{} Just deleted a msg 😇, here it is 🤭 : {}'.format(author,content))  
"""

@client.command(aliases=['tellme','TELLME','TellMe','tellMe','Tellme'])
async def Tell(ctx,*,question):

    responses = [ 'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'My sources say no, but they also said Hilary would win',
        'Trump uses me when deciding to go to war...Just saying ¯\(°_o)/¯',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'I got no clue man, I\'m sorry',
        'Very doubtful.',
        'Without a doubt',
        'Don\'t ask me, Bye',
        'I\'m Confused',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.']

    await ctx.send('{}'.format(random.choice(responses))) 



@client.command()
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)
    
@client.command(aliases = ['Gn','Goodnight','goodnight','gn'])
async def on_message(ctx):
    
    await ctx.send(f'Goodnight💖 {ctx.author.mention}')    


@client.command()
async def ping(ctx):
    await ctx.send(f'{ctx.author.mention} {round(client.latency*1000)} ms')

client.run(TOKEN)
