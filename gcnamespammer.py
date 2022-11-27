import httpx, asyncio, random, string
import os

token = ''
letters = string.ascii_letters + string.digits
amount = 100
name = ''
gc_id = ''

async def nameSpam():
  async with httpx.AsyncClient() as http:
    for i in range(amount):
      r = await http.patch(
          f'https://discord.com/api/v9/channels/{gc_id}',
          headers = {
            'authorization': token,
            'content-type': 'application/json',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari',
          },
          json = {
            'name': f'{name} {"".join(random.sample(letters, k=6))}'
          }
        )
      print(r.content)
      if r.status_code == 429:
        ratelimit = r.json()['retry_after']
        print(f'Ratelimit: {ratelimit}')
        await asyncio.sleep(int(ratelimit))
        r = await http.patch(
          f'https://discord.com/api/v9/channels/{gc_id}',
          headers = {
            'authorization': token,
            'content-type': 'application/json',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari',
          },
          json = {
            'name': f'{name} {"".join(random.sample(letters, k=6))}'
          }
        )

asyncio.run(nameSpam())
