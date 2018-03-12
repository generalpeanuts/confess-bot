import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import MySQLdb
import sys

bot = discord.Client()

@bot.event
async def on_ready():
	print ("Ready when you are xD")
	print ("I am running on " + bot.user.name)
	print ("With the ID: " + bot.user.id)
	

@bot.event
async def on_message(message):
	if message.content.startswith('#cg'):
		db = MySQLdb.connect("sql12.freesqldatabase.com", "sql12225836", "AcTlV48YTN", "sql12225836")
		sql = """INSERT INTO conf (text) VALUES('%s')""" % (message.content[-4:])
		c = db.cursor()
		try:
			c.execute(sql)
			db.commit()
		except:
			db.rollback()
		db.close()
		await bot.delete_message(message)

@bot.event
async def on_message(message):
	if message.content.startswith('#ch'):
		db2 = MySQLdb.connect("sql12.freesqldatabase.com", "sql12225836", "AcTlV48YTN", "sql12225836")
		sql2 = """SELECT text FROM conf ORDER BY RAND() LIMIT 1"""
		c2 = db2.cursor()
		c2.execute(sql2)
		data = c2.fetchall ()
		await bot.send_message(message.channel, data)
		db2.close()
bot.run("NDIyMDg3OTQ1ODEwMzQ1OTk0.DYZ5Hw.SqfVUiuacGVhVa_EeL67FGtNB0I")