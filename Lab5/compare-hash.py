hassh_obtenidos = [
    {"client_hassh": "0e4584cb9f2dd077dbf8ba0df8112d8e", "client_info": "SSH-2.0-OpenSSH_7.3p1 Ubuntu-1ubuntu0.1"},
    {"client_hassh": "06046964c022c6407d15a27b12a6a4fb", "client_info": "SSH-2.0-OpenSSH_7.7p1 Ubuntu-4ubuntu0.3"},
    {"client_hassh": "ae8bd7dd09970555aa4c6ed22adbbf56", "client_info": "SSH-2.0-OpenSSH_8.3p1 Ubuntu-1ubuntu0.1"},
    {"client_hassh": "78c05d999799066a2b4554ce7b1585a6", "client_info": "SSH-2.0-OpenSSH_9.0p1 Ubuntu-1ubuntu7.3"}
]

# Leer la base de datos HASSH
with open('hasshdb', 'r') as f:
    hassh_db_lines = f.readlines()

hassh_db = {}
for line in hassh_db_lines:
    parts = line.strip().split(' ', 1)
    if len(parts) == 2:
        hassh_db[parts[0]] = parts[1]

for hassh in hassh_obtenidos:
    client_hassh = hassh["client_hassh"]
    if client_hassh in hassh_db:
        print(f"Match found for HASSH: {client_hassh}")
        print(f"Expected: {hassh_db[client_hassh]}")
        print(f"Obtained: {hassh['client_info']}\n")
    else:
        print(f"No match found for HASSH: {client_hassh}\n")
