from discord_webhook import AsyncDiscordWebhook
import asyncio

#list of webhooks
webhooks = [
    'https://discord.com/api/webhooks/1046470821381677208/ZTRWDzXaaerxsPrtZ0E8jxL0_cOfp68I6PYUgZMdKqo2zpi0zYy5PzFmq5yFZGjcgqTa'
]
message = ''


async def send_webhook(url, message):
    webhook = AsyncDiscordWebhook(url=url, rate_limit_retry=True, content=message)
    await webhook.execute()

async def main():
    while True:
        funcs = [send_webhook(url, message) for url in webhooks]
        await asyncio.gather(*funcs)


asyncio.run(main())
