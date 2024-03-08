import sys
import Ice
from services.music1_service_ice import Music1ServiceI

def run_ice_server():
    try:
        with Ice.initialize() as communicator:
            print("Ice initialized successfully!")
            adapter = communicator.createObjectAdapterWithEndpoints("Music1ServiceAdapter", "default -p 10000")
            adapter.add(Music1ServiceI(), Ice.stringToIdentity("Music1Service"))
            adapter.activate()
            print("Server started.")
            communicator.waitForShutdown()
    except Ice.Exception as e:
        print("An error occurred during Ice initialization:", e)

if __name__ == '__main__':
    run_ice_server()
