# After modifying any of the files, you need to install the library again with:
# python setup.py install

import solax
import asyncio

async def work():
    r = await solax.real_time_api(ip_address = '192.168.1.36', port = 80, pwd = "admin")
    return await r.get_data()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
data = loop.run_until_complete(work())
print(data)

#-------------------------

#from importlib.metadata import entry_points
#import solax
#import asyncio

#INVERTERS_ENTRY_POINTS = {
#   ep.name: ep.load() for ep in entry_points(group="solax.inverter")
#}

#async def work():
#    inverter = await solax.discover("192.168.1.57", 80, "admin", inverters=[INVERTERS_ENTRY_POINTS.get("x1_boost")], return_when=asyncio.FIRST_COMPLETED)
#    return await inverter.get_data()

#loop = asyncio.new_event_loop()
#asyncio.set_event_loop(loop)
#data = loop.run_until_complete(work())
#print(data)

