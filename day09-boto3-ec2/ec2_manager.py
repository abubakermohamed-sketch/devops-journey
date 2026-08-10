import boto3
import time
# boto3 automatically uses the credentials from `aws configure` (~/.aws/credentials)
ec2 = boto3.client("ec2", region_name="us-east-1")

INSTANCE_ID = "i-24bnbn55mmnn86823m"  # replace with your actual instance ID


def get_instance_state(instance_id):
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response["Reservations"][0]["Instances"][0]["State"]["Name"]
    return state
def start_instance(instance_id):
    response = ec2.start_instances(InstanceIds=[instance_id])
    state = response["StartingInstances"][0]["CurrentState"]["Name"]
    return state

def stop_instance(instance_id):
    response = ec2.stop_instances(InstanceIds=[instance_id])
    state = response["StoppingInstances"][0]["CurrentState"]["Name"]
    return state

def main():
    state = get_instance_state(INSTANCE_ID)
    print(f"Instance {INSTANCE_ID} is currently: {state}")
    if  state=="stopped":
        start=start_instance(INSTANCE_ID)
        state = get_instance_state(INSTANCE_ID)
        print(f"Instance {INSTANCE_ID} is currently: {state}")

    else:  
           time.sleep(60)
           #state = get_instance_state(INSTANCE_ID)
           print(f"Instance {INSTANCE_ID} is currently: {state}")

          #time.sleep(30)    
    stop=stop_instance(INSTANCE_ID)
    state = get_instance_state(INSTANCE_ID)
    print(f"Instance {INSTANCE_ID} is currently: {state}")

main()
