import bluetooth

print("Escaneando dispositivos bluetooth \n")

dispositivos = bluetooth.discover_devices()

numero_de_dispositivos = len(dispositivos)
print("Se han encontrado un total de: ", numero_de_dispositivos)
for addr, name, device_class in dispositivos:

        print("\n")

        print("Device:")

        print("Device Name: %s" % (name))

        print("Device MAC Address: %s" % (addr))

        print("Device Class: %s" % (device_class))

        print("\n")
