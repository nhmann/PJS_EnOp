import logging
import asyncio
import sys
import pandas as pd
sys.path.insert(0, "..")

from asyncua import ua, Server
from asyncua.common.methods import uamethod

@uamethod
def func(parent, value):
    return value * 2

async def main():
    _logger = logging.getLogger('asyncua')
    # setup the server
    server = Server()
    await server.init()
    server.set_endpoint('opc.tcp://0.0.0.0:4840/opcua/server_output/')

    # setup the namespace
    uri = 'http://pjs.uni-wue.de/server_output'
    idx = await server.register_namespace(uri)

    # Read Sensor Data
    df = pd.read_csv("sensor.csv")
    # Only use sensor data from 03 and 01 (preference)
    sensor_data = pd.concat([df["dateTime"], df["output (kWh)"]], axis=1)
    
    # populating our address space
    # server.nodes, contains links to very common nodes like objects and root
    obj = await server.nodes.objects.add_object(idx, 'PV system')
    varDateTime = await obj.add_variable(idx, 'dateTime', 0, ua.VariantType.String)
    varOutput = await obj.add_variable(idx, 'output (kWh)', 0, ua.VariantType.Double)
    
    # Set Variables to be writable by clients
    await varDateTime.set_writable()
    await varOutput.set_writable() 
    
    await server.nodes.objects.add_method(ua.NodeId('ServerMethod', 2), ua.QualifiedName('ServerMethod', 2), func, [ua.VariantType.Int64], [ua.VariantType.Int64])
    _logger.info('Starting server!')
    async with server:
        while True:
            for row in sensor_data.itertuples():
                valDateTime = row[1]
                valOutput = row[2]
                
                # giving values
                await varDateTime.write_value(valDateTime)
                await varOutput.write_value(valOutput)
                
                # wait 1 second before repeating
                await asyncio.sleep(1)
                
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)