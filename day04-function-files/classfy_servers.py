def classify_server(server_name):
    """Takes a server name and returns its type as a string."""
    if "web" in server_name:
        return "Web Server"
    elif "db" in server_name:
        return "Database Server"
    elif "cache" in server_name:
        return "Cache Server"
    else:
        return "Unknown Type"


def main():
    with open("servers.txt", "r") as f:
        servers = f.read().splitlines()  # splitlines removes the \n from each line
    with open("report.txt","w") as s:

        for server in servers:
           server_type = classify_server(server)
           s.write(f"{server} -> {server_type}\n")

    print(f"\nTotal servers processed: {len(servers)}")


main()
