import argparse
import boto3
import time
import datetime
# boto3 automatically uses the credentials from `aws configure` (~/.aws/credentials)
ec2 = boto3.client("ec2", region_name="us-east-2")
#today = date.today().isoformat()

INSTANCE_ID = "i-0d40b26d4a2422cd7"  # replace with your actual instance ID



parser = argparse.ArgumentParser(description="EC2 management tool")
parser.add_argument("command", choices=["list", "start", "stop", "report"], help="Action to perform")
parser.add_argument("instance_id", nargs="?", help="Instance ID (required for start/stop)")

def get_instance_state(instance_id):
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response["Reservations"][0]["Instances"][0]["State"]["Name"]
    return state

def list_instances():
    response = ec2.describe_instances()
    instances = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]
            # Name tag might not exist, so we need to handle that safely
            name = "N/A"
            if "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Name":
                        name = tag["Value"]
            instances.append({"id": instance_id, "state": state, "name": name})
    return instances
def start_instance(instance_id):
    response = ec2.start_instances(InstanceIds=[instance_id])
    state = response["StartingInstances"][0]["CurrentState"]["Name"]
    return state

def stop_instance(instance_id):
    response = ec2.stop_instances(InstanceIds=[instance_id])
    state = response["StoppingInstances"][0]["CurrentState"]["Name"]
    return state

def write_report():
    today=datetime.datetime.now()
    instances = list_instances()
    with open("report.txt", "w") as file:
         for instance in instances:
        #with open("report.txt", "w") as file:
             file.write(f"{today}:Instance_id is: {instance['id']}, state is: {instance['state']}, name is: {instance['name']}\n")


def main():
     
    args = parser.parse_args()

    if args.command == "list":
        instances = list_instances()
        for instance in instances:
            print(f"Instance_id is: {instance['id']}, state is: {instance['state']}, name is: {instance['name']}")
            #with open("report.txt", "w") as file:
                 #file.write(f"{today}:Instance_id is: {instance['id']}, state is: {instance['state']}, name is: {instance['name']}\n")
    elif args.command == "start":
        if args.instance_id is None:
            print("Error: instance_id is required for start")
        else:
            start_instance(args.instance_id)
            state = get_instance_state(args.instance_id)
            print(f"Instance {args.instance_id} is now: {state}")

    elif args.command == "stop":
        if args.instance_id is None:
            print("Error: instance_id is required for stop")
        else:
            stop_instance(args.instance_id)
            state = get_instance_state(args.instance_id)
            print(f"Instance {args.instance_id} is now: {state}")
    elif args.command == "report":
          write_report()
main()
