from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message
import re
from phone import save_phone

class PhonePlugin(Plugin):
    @listen_to("^8[0-9]{10}$", re.IGNORECASE)
    async def get_phone(self, message: Message):
        response = save_phone(phone=message.text, user_id=message.user_id)
        self.driver.reply_to(message, response)
    
        