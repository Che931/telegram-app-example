from telethon import TelegramClient
from settings import API_HASH, API_ID, CHANNEL_NAME

client = TelegramClient('anon', API_ID, API_HASH)


async def main():
    user = await client.get_me()
    print("Connected as @{0} +{1} |\n".format(user.username, user.phone))

    print("Some of your chats:")
    async for chat in client.iter_dialogs(10):
        print("Chat => {0} - {1}".format(chat.id, chat.name))

    print("\nLatest messages from your preferred channel:")
    async for message in client.iter_messages(CHANNEL_NAME, limit=10):
        print("@{0}({1}) => {2}".format(message._sender.username,
                                        message.date,
                                        message.text))

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
