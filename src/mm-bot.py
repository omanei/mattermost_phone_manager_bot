from dotenv import load_dotenv
import os
from mmpy_bot import Bot, Settings
from plugins import PhonePlugin

load_dotenv()


bot = Bot(
    settings=Settings(
        MATTERMOST_URL=os.getenv("MATTERMOST_URL"),
        MATTERMOST_PORT=os.getenv("MATTERMOST_PORT"),
        MATTERMOST_API_PATH=os.getenv("MATTERMOST_API_PATH"),
        BOT_TOKEN=os.getenv("BOT_TOKEN"),
    ),
    plugins=[PhonePlugin()],
)

bot.run()
