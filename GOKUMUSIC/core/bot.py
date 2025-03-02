from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class GOKU(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="GOKUMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        # Debugging: Cetak informasi bot
        LOGGER(__name__).info(f"Bot Info: ID={self.id}, Name={self.name}, Username=@{self.username}")

        # Debugging: Cetak LOGGER_ID
        LOGGER(__name__).info(f"Logger ID: {config.LOGGER_ID}")

        try:
            # Debugging: Cetak pesan sebelum mengirim
            LOGGER(__name__).info(f"Mengirim pesan ke LOGGER_ID: {config.LOGGER_ID}")
            
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
            )
            # Debugging: Cetak detail error
            LOGGER(__name__).error(f"Error details: {ex}")
            exit()

        # Debugging: Cetak status bot di grup/channel log
        LOGGER(__name__).info(f"Memeriksa status bot di LOGGER_ID: {config.LOGGER_ID}")
        
        try:
            a = await self.get_chat_member(config.LOGGER_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "Please promote your bot as an admin in your log group/channel."
                )
                exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Failed to check bot's admin status in log group/channel.\n  Reason : {type(ex).__name__}."
            )
            # Debugging: Cetak detail error
            LOGGER(__name__).error(f"Error details: {ex}")
            exit()

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
