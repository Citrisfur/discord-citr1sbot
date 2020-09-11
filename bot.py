# bot.py
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='c!')

@bot.command(name='status', help="Displays a message if the bot's script is running")
async def status(ctx):
	await ctx.send("Citr1sbot is online.")

@bot.command(name='note', help="recite a note")
async def note(ctx):
	nameCheck = True
	
	await ctx.send("Name of note?")
	while nameCheck == True:
		name = await bot.wait_for('message')
		if name.author == ctx.author:
			nameCheck = False
	filename = "/home/brandin/Desktop/Discord Citr1sbot/notes/" + str(name.author).lower() + name.content.lower() + ".txt"
	if os.path.exists(filename):
		f = open(filename, 'r')
		await ctx.send(f.read())
		f.close()
	else:
		await ctx.send("You do not have a note named " + name.content.lower() + ".")

@bot.command(name='noteadd', help="create or append to a note")
async def noteadd(ctx):
	nameCheck = True
	noteCheck = True
	
	await ctx.send("Name of note?")
	while nameCheck == True:
		name = await bot.wait_for('message')
		if name.author == ctx.author:
			nameCheck = False
	filename = "/home/brandin/Desktop/Discord Citr1sbot/notes/" + str(name.author).lower() + name.content.lower() + ".txt"
	if os.path.exists(filename):
		await ctx.send("Appending to note " + name.content + " created by " + str(name.author) + ". Contents?")
		while noteCheck == True:
			note = await bot.wait_for('message')
			if note.author == ctx.author:
				noteCheck = False
		f = open(filename, 'a')
		f.write(note.content)
		f.close()
	else:
		await ctx.send("Note name " + name.content + " created by " + str(name.author) + ". Contents?")
		while noteCheck == True:
			note = await bot.wait_for('message')
			if note.author == ctx.author:
				noteCheck = False
		
		f = open(filename, 'w')
		f.write(note.content)
		f.close()
	await ctx.send("Note saved.")

@bot.command(name='noteremove', help="remove a note")
async def noteremove(ctx):
	nameCheck = True
	
	await ctx.send("Name of note?")
	while nameCheck == True:
		name = await bot.wait_for('message')
		if name.author == ctx.author:
			nameCheck = False
	filename = "/home/brandin/Desktop/Discord Citr1sbot/notes/" + str(name.author).lower() + name.content.lower() + ".txt"
	if os.path.exists(filename):
		os.remove(filename)
		await ctx.send("Note removed.")
	else:
		await ctx.send("You do not have a note named " + name.content.lower() + ".")

@bot.command(name='notelist', help="lists user's notes")
async def notelist(ctx):
	list = "Notes that " + str(ctx.author) + " owns:\n"
	
	for file in os.listdir("/home/brandin/Desktop/Discord Citr1sbot/notes/"):
		if str(ctx.author).lower() in file:
			list += file.replace(str(ctx.author).lower(), '') + "\n"
	if list == '':
		await ctx.send("You do not have any notes.")
	else:
		await ctx.send(list.replace(".txt", "").rstrip())
	
bot.run(TOKEN)
