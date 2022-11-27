import httpx
import os
import asyncio

token = ''
headers = {
  'authorization': token,
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36',
  'content-type': 'application/json'
}
amouunt = 20
name = ''
forum_id = ''

async def threadSpam(name, amount, id):
  async with httpx.AsyncClient() as http:
    for i in range(amount):
        thread = await http.post(
          f'https://discord.com/api/v9/channels/{id}/threads?use_nested_fields=true',
          json={
              "name": name,
              "auto_archive_duration": 1440,
              "applied_tags": [],
              "message": {
                  "content":name
              }
          },
          headers=headers)
        print(thread.content)

        if thread.status_code == 429:
            ratelimit = thread.json()['retry_after']
            print(f'Ratelimited: {ratelimit}')
            await asyncio.sleep(int(ratelimit))
            thread = await http.post(
              f'https://discord.com/api/v9/channels/{id}/threads?use_nested_fields=true',
              json={
                  "name": name,
                  "auto_archive_duration": 1440,
                  "applied_tags": [],
                  "message": {
                      "content":name
                  }
              },
              headers=headers)
            print(thread.content)


asyncio.run(threadSpam(name, amount, forum_id))
