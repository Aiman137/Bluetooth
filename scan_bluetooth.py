
import bluetooth

# Create a list to store the detected devices
devices = []

# Scan for devices
print("Escaneando dispositivos cercanos.. \n")
nearby_devices = bluetooth.discover_devices()
print(f'Encontrados {len(nearby_devices)} dispositivos \n') 


local_addr = bluetooth.read_local_bdaddr()
print("La dirección Bluetooth de este equipo es: ", local_addr)

# Loop through the detected devices and print their name and address
for addr in nearby_devices:
    name = bluetooth.lookup_name(addr)
    devices.append((name, addr))
    print("{}: {}".format(name, addr))
