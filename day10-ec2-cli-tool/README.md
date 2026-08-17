# EC2 CLI Management Tool

A command-line tool built with Python and boto3 to manage AWS EC2 instances directly from the terminal.

## Features
- `list` — shows all EC2 instances with ID, state, and name
- `start <instance_id>` — starts a specific instance
- `stop <instance_id>` — stops a specific instance
- `report` — generates a timestamped report file of all instances

## Usage
```bash
python3 ec2_tool.py list
python3 ec2_tool.py start instance_id
python3 ec2_tool.py stop instance_id
python3 ec2_tool.py report
```

## What I learned
- Using `argparse` to build real CLI tools with subcommands and arguments
- Parsing nested AWS API responses (Reservations → Instances)
- Input validation before calling AWS actions
- Avoiding the "file opened inside a loop" bug when writing reports
- boto3 client setup and using stored AWS credentials securely (no hardcoded keys)
