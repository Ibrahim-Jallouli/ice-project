import sys
import Ice
from services.music2_service_ice import Music2ServiceI

def run_ice_server():
    try:
        with Ice.initialize() as communicator:
            print("Ice initialized successfully!")
            adapter = communicator.createObjectAdapterWithEndpoints("Music2ServiceAdapter", "default -p 10001")
            adapter.add(Music2ServiceI(), Ice.stringToIdentity("Music2Service"))
            adapter.activate()
            print("Server started.")
            communicator.waitForShutdown()
    except Ice.Exception as e:
        print("An error occurred during Ice initialization:", e)

if __name__ == '__main__':
    run_ice_server()
