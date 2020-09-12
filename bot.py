# bot.py
import os
from random import randint
from discord.ext import commands
from dotenv import load_dotenv
from time import sleep

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')

bot = commands.Bot(command_prefix='c!')
bot.remove_command('help')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

@bot.command(name='help')
async def help(ctx, command=''):
    header = '''
All commands for Citr1sbot begin with the prefix 'c!'. Most commands are also formatted into user-friendly strings, instead of returning primital values.
In the usage statements, parameters specified with {curly braces} required, while (parenthesis) are optional.
For any issues, please contact @Citrisfur#0404, or nathanscoy@gmail.com.
'''
    noteHeader = '''
This command relates to the notetaking funtions of Citr1sbot.
Notes can have one of the three states private, public, or editable. By default, notes are created private. Notes can only be deleted by the note's creator.
private: notes can only be edited or read by the note author.
public: notes can only be edited by the author, but read by all.
editable: notes can be read and edited by all.
'''
    commandList = {
        "help": '''
help // Displays a list of commands that Citr1sbot can recognize.
    Usage: c!help (command)
    [string] command - specifies a command to display additional information about.''',
        "ping": '''
ping // Returns the bot's latency in seconds.
    Usage: c!ping''',
        "halfjoke": '''
halfjoke // Returns a halfjoke, cortesy of JSchlatt.
    Usage: c!halfjoke (count) (time)
    [integer] count - the number of jokes to tell
    [integer] time - the amount of wait time between each joke''',
    }
    
    noteCommandList = {
        "note": '''
note // Reads the contents of a specified note.
    Usage: c!note {note-name} (user-name)
    [string] note-name - the name of the note to read. the note must be public, unless you are the author.
    [string/mention] user-name - the name of the user that owns the note. if blank, the note must be owned by the user.''',
        "addnote": '''
addnote // Creates a note with user-inputted content.
    Usage: c!addnote {note-name} (type)
    [string] note-name - the name of the note to create.
    [string] public - specifies the note type. values 'public', 'pub', 'editable' or 'edit' are excepted, all others are ignored.''',
        "deletenote": '''
deletenote // Deletes a note previously created by the user.
    Usage: c!removenote {note-name}
    [string] note-name - the name of the note to delete.''',
        "editnote": '''
editnote // Returns the message link to the original message used to populate the note with. When edited, saved, and reacted to with any emoji, the new message will be saved into the note.
    Usage: c!editnote {note-name}
    [string] note-name - the name of the note to edit.''',
        "listnotes": '''
listnotes // Lists all notes a user owns.
    Usage: c!listnotes (user-name) (editable)
    [string/mention] user-name - specifies notes that a specific user owns. private notes owned by other users will not be listed.
    [string/boolean/char] editable - specify whether editable notes on the current server are also listed, seperatly. values 'editable', 'yes' and 'y' are accepted.''',
        "permnote": '''
typenote // Changes the type of a note.
    Usage: c!typenote {note-name} {type}
    [string] note-name - the note to change the type of
    [string] type - the type to change the note to. values 'private', 'pri', 'public', 'pub', 'editable', and 'edit' are accepted.''',
    }

    if command != '':
        if command.lower() in commandList:
            await ctx.send(header + commandList[command.lower()])
        elif command.lower() in noteCommandList:
            await ctx.send(header + noteHeader + noteCommandList[command.lower()])
        else:
            await ctx.send("The specified command doesn't exist. Recheck the typing, or try the command list with c!help.")
    else:
        await ctx.send(header + '''
== Command List ==

help
ping
halfjoke
note
addnote
deletenote
editnote
listnotes
typenote
''')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("Citr1sbot is latent by " + str(bot.latency) + " seconds.")
    
@bot.command(name='halfjoke')
async def halfjoke(ctx, count=1, time=0):
    await ctx.message.delete()
    halfjokes = ["I've spent the last four years looking for my ex-girlfriend's killer.", "I recently decided to sell my vaccuum cleaner.", "My girlfriend told me to go out and get her something that makes her look sexy.", "Where there's a will...", "I've just written a song about tortillas.", "My wife just found out I replaced our bed with a trampoline.", "Hedgehogs, eh?", "You can never lose a homeless person.", "I asked God for a bike.", "The first time I got a universal remote control, I thought to myself.", "Say what you want.", "Of course I should clean my windows.", "The potato should go in the front.", "There's no domestic violence going on.", "Wow, that's gotta be the fastest we've ever gotten to the accident site.", "This is my stepladder.", "I dreamed I was forced to eat a giant marshmallow.", "Prison.", "I'm very sorry sir, but it looks like your wife was hit by a bus."]

    try:
        count = int(count)
    except:
        pass

    try:
        time = int(time)
    except:
        pass

    while count != 0:
        await ctx.send(halfjokes[randint(0, len(halfjokes))])
        count -= 1
        sleep(time)

@bot.command(name='note')
async def note(ctx, noteName, userName=''):
    pass
	# filename = "C:\\Users\\Your New Gaming PC\\Documents\\Discord Bots\\Discord Citr1sbot\\notes\\" + str(ctx.author).lower() + noteName.lower() + ".txt"
	# if os.path.exists(filename):
		# f = open(filename, 'r')
		# await ctx.send(f.read())
		# f.close()
	# else:
		# await ctx.send("You do not have a note named " + noteName + ".")

@bot.command(name='addnote')
async def addnote(ctx, noteName, noteType=''):
    pass
    # noteCheck = True
    
    # filename = "C:\\Users\\Your New Gaming PC\\Documents\\Discord Bots\\Discord Citr1sbot\\notes\\" + str(ctx.author).lower() + noteName.lower() + ".txt"
    # if os.path.exists(filename):
        # await ctx.send("You currently have a note named " + noteName + ". Use the 'note' command to read its contents, or 'editnote' to edit it.")
    # else:
        # await ctx.send("Note name " + noteName + " created by " + str(ctx.author) + ". Contents?")
        # while noteCheck:
            # note = await bot.wait_for('message')
            # if note.author == ctx.author:
                # noteCheck = False
        
        # f = open(filename, 'w')
        # f.write(note.content)
        # f.close()
    # await ctx.send("Note saved.")

@bot.command(name='noteremove')
async def noteremove(ctx):
	pass
    # nameCheck = True
	
	# await ctx.send("Name of note?")
	# while nameCheck == True:
		# name = await bot.wait_for('message')
		# if name.author == ctx.author:
			# nameCheck = False
	# filename = "C:\\Users\\Your New Gaming PC\\Documents\\Discord Bots\\Discord Citr1sbot\\notes\\" + str(name.author).lower() + name.content.lower() + ".txt"
	# if os.path.exists(filename):
		# os.remove(filename)
		# await ctx.send("Note removed.")
	# else:
		# await ctx.send("You do not have a note named " + name.content.lower() + ".")

@bot.command(name='notelist')
async def notelist(ctx):
	pass
    # list = "Notes that " + str(ctx.author) + " owns:\n"
	
	# for file in os.listdir("C:\\Users\\Your New Gaming PC\\Documents\\Discord Bots\\Discord Citr1sbot\\notes"):
		# if str(ctx.author).lower() in file:
			# list += file.replace(str(ctx.author).lower(), '') + "\n"
	# if list == "Notes that " + str(ctx.author) + " owns:\n":
		# await ctx.send("You do not have any notes.")
	# else:
		# await ctx.send(list.replace(".txt", "").rstrip())

@bot.event
async def on_command_error(ctx, error):
    usages = {
        "note": "Usage: c!note {note-name} (user-name)",
        "addnote": "Usage: c!addnote {note-name} (type)",
        "removenote": "Usage: c!removenote {note-name}",
        "editnote": "Usage: c!editnote {note-name}",
        "listnotes": "Usage: c!listnotes (user-name) (editable)",
        "typenote": "Usage: c!typenote {note-name} {type}"
    }
    
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(usages.get(ctx.invoked_with))
    elif (str(error) == "Converting to \"int\" failed for parameter \"count\".") or (str(error) == "Converting to \"int\" failed for parameter \"time\"."):
        await halfjoke(ctx)
    else:
        await ctx.send(str(error))

    # elif isinstance(error, commands.errors.CheckFailure):
		# await ctx.send("You do not have the mod role.")

bot.run(TOKEN)
