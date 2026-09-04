# In-memory data store (RAM). Replace with a real DB later.

USERS = {}      # key: username -> user dict
DEVICES = {}    # key: device_serial -> device dict
VEHICLES = {}   # key: vin -> vehicle dict
TELEMETRY = []  # list of telemetry records
