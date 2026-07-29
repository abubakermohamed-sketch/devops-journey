def classify_server(name):
    if "web" in name:
      return "Web Server"
    elif "db" in name:
      return "Database Server"
    elif "cache" in name:
      return "Cache Server"
    elif "lb" in name:
      return "Load Balancer"
    elif "mail" in name:
      return "Mail Server"
    else:
      return "Unknown Type"
def count_by_type(servers):
   counts={} # empty dictionary
   counts["Web Server"] = 0  # create a key with value 0
   counts["Database Server"] = 0  # create a key with value 0
   counts["Cache Server"] = 0  # create a key with value 0
   counts["Load Balancer"] = 0  # create a key with value 0
   counts["Mail Server"] = 0  # create a key with value 0
  
   for server in servers:
     if "web" in server:
        counts["Web Server"] = counts.get("Web Server", 0) + 1
        print( "Hello")  
     elif "db" in server:
        counts["Database Server"] = counts.get("Database Server", 0) + 1
     elif "cache" in server:
        counts["Cache Server"] = counts.get("Cache Server", 0) + 1
     elif "lb" in server:
        counts["Load Balancer"] = counts.get("Load Balancer", 0) + 1
     else:
        counts["Mail Server"] = counts.get("Mail Server", 0) + 1
   return counts     

def main():

    with open("inventory.txt","r") as f:
        server_name=[]
        servers=f.read().splitlines()
    for server in servers:     
        
        server_type=  classify_server(server)
        server_name.append(server_type)
       # print(server_name)
    with open("report.txt", "w") as s:
     for server in servers:
        server_type = classify_server(server)  # recompute here
        s.write(f"{server} -> {server_type}\n")
        
     s.write(f"\nSummary: {count_by_type(servers)}\n")
    print(f"\nTotal servers processed: {len(servers)}")

main()
