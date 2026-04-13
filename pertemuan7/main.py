import json

# Compile Proses
# Logika Program
ip = "10.5.5"

# Runtime
# Variable yang dibuat saat program berjalan
with open("config.json", "r") as f:
    config = json.load(f)
    #ip adalah sebuah objek, maka config bisa diakses dengan menggunakan key "ip address"
    ip = config["ip address"]


print(ip)