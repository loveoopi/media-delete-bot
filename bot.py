from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio

api_id = 20377539
api_hash = "06a137a486d972ce8db3fd6e78fb6fbb"
bot_token = "7570729692:AAG82DbQ8TArL3JeUhPfte8tfMotEV8GEb8"

app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(~filters.text & filters.group)
async def fwd(bot, message):
    # Check if the message is from the specified user IDs
    if message.from_user and message.from_user.id in [7287487344, 7618324945, 8146040173, 6717909593]:
        return  # Skip deletion for these users
    try:
        await bot.delete_messages(message.chat.id, message.id)
    except FloodWait as e:
        print(f'There is a flood wait for about: {e}')
        await asyncio.sleep(e.x)  
    except Exception as f:
        print(f"Execution failed because: {f}")

@app.on_message(filters.command('start'))
async def start(bot, message):
    user = message.from_user.first_name
    await message.reply(
        f"Hi {user}, I am an auto delete bot for groups.\n\nI can delete any kind of Images and Videos. A simple yet powerful copyright protection for your groups. I am made by @kingXkingz. "
    )

app.run()
