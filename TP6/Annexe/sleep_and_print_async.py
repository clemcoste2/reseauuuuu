# async_count.py
import asyncio

# définitions des fonctions en async
async def p1():
    for i in range(11):
        print(i)
        # asyncio.sleep et pas time.sleep
        # await pour indiquer que cette ligne va produire de l'attente
        await asyncio.sleep(1)

async def p2():
    for i in range(11):
        print(i)
        await asyncio.sleep(1)

# on récupère l'objet loop
loop = asyncio.get_event_loop()

# on crée une liste de tasks
tasks = [
    loop.create_task(p1()),
    loop.create_task(p2()),
]

# on lance la loop jusqu'à ce que les tâches se terminent
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
