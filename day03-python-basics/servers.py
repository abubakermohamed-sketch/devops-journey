servers=["web-01", "web-02", "db-01", "cache-01"]
for server in servers:
    if "web" in server:
        print(f"{server} is web server")
    elif "db" in server:
         print(f"{server} is database server")
    else:
         print(f"{server} is something else") 
print(f"\nTotal servers: {len(servers)}")
