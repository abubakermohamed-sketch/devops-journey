def classify_server(name):
    if "web" in name:
        return "Web Server"
    elif "db" in name:
        return "Database Server"
    elif "cache" in name:
        print("Hello")
        return "Cache Server"
    else:
        return "Unknown Type"


def main():
    print("Testing a bind mount!")
    with open("inventory.txt", "r") as f:
        servers = f.read().splitlines()

    with open("report.txt", "w") as f:
        for server in servers:
            server_type = classify_server(server)
            line = f"{server} -> {server_type}"
            print(line)
            f.write(line + "\n")

    print(f"\nProcessed {len(servers)} servers. Report written to report.txt")


main()
