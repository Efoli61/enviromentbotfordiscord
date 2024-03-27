import discord
from discord.ext import commands
import time  # Importing time module for delay

# Define intents
intents = discord.Intents.default()
intents.messages = True  # Enable message events

# Create a bot instance with intents
bot = commands.Bot(command_prefix="?", intents=intents)

# Event to print a message when the bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


# Command to provide information about reducing trash production
@bot.command()
async def info(ctx):
    await ctx.send("To reduce trash production, consider the following recommendations:")
    time.sleep(1)
    await ctx.send("1. Use reusable shopping bags instead of plastic bags.")
    time.sleep(1)
    await ctx.send("2. Avoid single-use items like plastic cutlery and straws.")
    time.sleep(1)
    await ctx.send("3. Recycle materials like paper, plastic, glass, and aluminum.")
    time.sleep(1)
    await ctx.send("4. Compost organic waste like food scraps and yard trimmings.")
    time.sleep(1)
    await ctx.send("5. Buy products with minimal packaging or packaging that is recyclable or biodegradable.")
    time.sleep(1)
    await ctx.send("6. Support businesses that prioritize sustainability.")
    time.sleep(1)
    await ctx.send("Remember, small changes can make a big difference.")

bot.run("token")
