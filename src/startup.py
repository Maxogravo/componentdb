import os

def setup():
    print("Welcome to component db!")
    with open("node_data/node_role.txt", "w") as f:
        role = input("Enter node role (server/client/local): ")
        f.write(role)
    if role == "client":
        with open("node_data/server_ip.txt", "w") as f:
            server_ip = input("Enter server IP address: ")
            f.write(server_ip)
    else:
        pass
    

if os.path.exists("node_data/node_role.txt"):
    with open("node_data/node_role.txt", "r") as f:
        role = f.read().strip()
    if role == "server":
        os.system("python src/server.py")
    elif role == "client":
        os.system("python src/client.py")
    else:
        os.system("python src/local.py")
else:
    setup()