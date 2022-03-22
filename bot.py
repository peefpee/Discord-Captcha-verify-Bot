import discord
from discord.ext import commands

from captcha.image import ImageCaptcha
import random

bot = commands.Bot(command_prefix='.', description="This is a Helper Bot") #put command prefix

@bot.command()
async def verify(ctx):
  
  await ctx.reply('Please Check your DMS To verify')
  await ctx.author.send('You need to solve this captcha to verify!')
  image= ImageCaptcha()
  timee = datetime.datetime.now().timestamp()
  n = random.randrange(9999)
  data = image.generate(str(n))
  e = f'captcha/{timee}{ctx.author.id}.png'
  image.write(str(n), e)
  await ctx.author.send(file=discord.File(e))
  def check(m):
        return m.content == str(n)

  msg = await bot.wait_for("message", check=check)
  await ctx.author.send(f"You have been verified")
  role = ctx.guild.get_role(roleid) #put verified role id
  await ctx.author.add_roles(role)
@bot.event
async def on_member_join(member):

  await member.send('You need to solve this captcha to verify!')
  image= ImageCaptcha()
  timee = datetime.datetime.now().timestamp()
  n = random.randrange(9999)
  data = image.generate(str(n))
  e = f'captcha/{timee}{ctx.author.id}.png'
  image.write(str(n), e)
  await member.send(file=discord.File(e))
  def check(m):
        return m.content == str(n)

  msg = await bot.wait_for("message", check=check)
  await member.send(f"You have been verified")
  role = ctx.guild.get_role(roleid) # put the role id of the verified role
  await ctx.author.add_roles(role)


bot.run('urbottoken') # put discord bot token
