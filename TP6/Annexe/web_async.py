import requests
import sys
import asyncio
import aiohttp
import aiofiles


async def get_content(url):
    async with aiohttp.ClientSession() as request:
            async with request.get(url) as response:
                await asyncio.sleep(1)
                response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    return response.text

async def write_content(content, file_path):
    with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
        await asyncio.sleep(1)
        file.write(content)
        await asyncio.sleep(1)
        file.flush()
    print(f"written to {file_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    content = get_content(url)

    file_path = './URL'
    write_content(content, file_path)

loop = asyncio.get_event_loop()

# on crée une liste de tasks
tasks = [
    loop.create_task(get_content()),
    loop.create_task(write_content()),
]

# on lance la loop jusqu'à ce que les tâches se terminent
loop.run_until_complete(asyncio.wait(tasks))
loop.close()