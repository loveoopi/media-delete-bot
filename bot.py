from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio

api_id = 1474940
api_hash = "779e8d2b32ef76d0b7a11fb5f132a6b6"
bot_token = "7450884496:AAGoAA6xR8sxvFu_1pUdjr-luP5nQ2gLYiE"

app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(~filters.text & filters.group)
async def fwd(bot, message):
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
        f"Hi {user}, I am an auto delete bot for groups.\n\nI can delete any kind of Images and Videos. A simple yet powerful copyright protection for your groups."
    )

app.run()
