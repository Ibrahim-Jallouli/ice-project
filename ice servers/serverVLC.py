import sys
import Ice
from services.music3_service_ice import MusicService3I

def run_ice_server():
    try:
        # Create properties and set Ice.MessageSizeMax
        props = Ice.createProperties()
        props.setProperty("Ice.MessageSizeMax", "10000000")

        # Initialize InitializationData object with properties
        initData = Ice.InitializationData()
        initData.properties = props

        # Initialize Ice communicator
        with Ice.initialize(initData) as communicator:
            print("Ice initialized successfully!")
            adapter = communicator.createObjectAdapterWithEndpoints("Music3ServiceAdapter", "default -p 10002")
            adapter.add(MusicService3I(), Ice.stringToIdentity("Music3Service"))
            adapter.activate()
            print("Server started.")
            communicator.waitForShutdown()
    except Ice.Exception as e:
        print("An error occurred during Ice initialization:", e)

if __name__ == '__main__':
    run_ice_server()
