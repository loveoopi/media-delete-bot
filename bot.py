from pyrogram import Client, filters
from pyrogram.errors import FloodWait, Flood
import asyncio
import time

api_id = 20377539
api_hash = "06a137a486d972ce8db3fd6e78fb6fbb"
bot_token = "7570729692:AAGV4Nxqex83pIX7jT7n6wCQhjhsuppYPEY"

app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(~filters.text & filters.group)
async def fwd(bot, message):
    # Check if the message is from the specified user IDs
    if message.from_user and message.from_user.id in [7287487344, 7907871597]:
        return  # Skip deletion for these users
    try:
        await bot.delete_messages(message.chat.id, message.id)
    except FloodWait as e:
        print(f'Flood wait: {e.x} seconds')
        await asyncio.sleep(e.x)  
    except Exception as f:
        print(f"Error: {f}")

@app.on_message(filters.command('start'))
async def start(bot, message):
    user = message.from_user.first_name
    await message.reply(
        f"Hi {user}, I am an auto delete bot for groups.\n\nI can delete any kind of Images and Videos. A simple yet powerful copyright protection for your groups. I am made by @kingXkingz. "
    )

@app.on_message(filters.command('id'))
async def get_id(bot, message):
    if message.from_user:
        await message.reply(f"Your user ID is: `{message.from_user.id}`")
    else:
        await message.reply("Could not get user ID")

# Handle startup with flood wait
async def main():
    try:
        print("Starting bot...")
        await app.start()
        print("Bot started successfully!")
        await asyncio.Event().wait()  # Keep running
    except FloodWait as e:
        print(f"Flood wait during startup: {e.x} seconds")
        print(f"Waiting {e.x} seconds before retrying...")
        await asyncio.sleep(e.x)
        await main()
    except Exception as e:
        print(f"Error during startup: {e}")
    finally:
        await app.stop()

if __name__ == "__main__":
    # Wait for 20 minutes (the flood wait time) before starting
    print("Waiting for flood wait to expire...")
    time.sleep(1236)  # Wait the required time
    asyncio.run(main())
