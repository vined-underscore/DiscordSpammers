import httpx
import os
import asyncio

token = ''
headers = {
  'authorization': f'Bot {token}',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36',
  'content-type': 'application/json'
}
name = ''
amount = 20
channel_id = ''

async def threadSpam(name, amount, id):
  async with httpx.AsyncClient() as http:
    for i in range(amount):
        thread = await http.post(
          f'https://discord.com/api/v9/channels/{id}/threads',
          json={
            'name': f'{name} {i}',
            'type': 10,
            'auto_archive_duration': 1440,
            'location': 'Thread Browser Toolbar'
          },
          headers=headers)
        print(thread.content)

        if thread.status_code == 429:
            ratelimit = thread.json()['retry_after']
            print(f'Ratelimited: {ratelimit}')
            await asyncio.sleep(int(ratelimit))
            thread = await http.post(
              f'https://discord.com/api/v9/channels/{id}/threads',
              json={
                'name': f'{name} {i+1}',
                'type': 10,
                'auto_archive_duration': 1440,
                'location': 'Thread Browser Toolbar'
              },
              headers=headers)
            print(thread.content)


asyncio.run(threadSpam(name, amount, channel_id))
