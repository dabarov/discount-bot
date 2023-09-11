import asyncio
import math
from string import Template

import aiohttp
import requests

BASE_URL = Template(
    "https://api.technodom.kz/katalog/api/v1/products/category/noutbuki?city_id=5f5f1e3b4c8a49e692fefd70&limit=${limit}&page=${page}"
)


async def get_laptops(limit: int = 10, page: int = 1):
    url = BASE_URL.substitute(limit=limit, page=page)
    print(url, type(url))
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_json = await response.json()
            data = response_json.get("payload")
            for object in data:
                print(object.get("price"))


async def main():
    response = requests.get(BASE_URL.substitute(limit=10, page=1))
    response_json = response.json()
    limit = response_json["limit"]
    total = response_json["total"]
    number_of_pages = math.ceil(total / limit)
    tasks = []
    for page in range(1, number_of_pages + 1):
        task = asyncio.create_task(get_laptops(limit=limit, page=page))
        tasks.append(task)
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
