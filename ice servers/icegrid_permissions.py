import sys
import Ice
import IceGrid

# Define your custom permissions verifier
class MyPermissionsVerifier(Ice.Object):
    def checkPermissions(self, userId, password, current=None):
        # Replace this with your authentication logic
        if userId == "root" and password == "root":
            return True
        return False

# Initialize Ice communicator
with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("DemoIceGrid/Registry")
    registry = IceGrid.RegistryPrx.checkedCast(base)

    # Create an instance of your custom permissions verifier
    permissions_verifier_impl = MyPermissionsVerifier()

    # Add your verifier to the communicator
    adapter = communicator.createObjectAdapterWithEndpoints("PermissionsVerifierAdapter", "tcp -h localhost -p 10000")
    adapter.add(permissions_verifier_impl, Ice.stringToIdentity("PermissionsVerifier"))
    adapter.activate()

    # Obtain proxy for your verifier
    permissions_verifier_proxy = adapter.createProxy(Ice.stringToIdentity("PermissionsVerifier"))

    # Set the Admin Permissions Verifier property
    registry.setProperty("IceGrid.Registry.AdminPermissionsVerifier", permissions_verifier_proxy)

    # Now you should be able to authenticate with username "root" and password "root"
