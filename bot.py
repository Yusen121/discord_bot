import discord
import dotenv
import os

dotenv.load_dotenv()
my_bot_token = os.getenv("TOKEN")
print(my_bot_token)

intends = discord.Intents.default()
intends.messages_content = True
bot = discord.Client(intends=intends)

@bot.event()
async def on_ready():
    print("my bot is ready")

async def my_message_function(message):
    content = message.content
    bot_response = f"u just sent me {content}"
    await message.channel.send(bot_response)

@bot.event()
async def on_message(message):
    if message.author == bot.user:
        return
    await my_message_function(message)
bot.run(my_bot_token)




