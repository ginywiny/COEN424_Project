### EC2
- Set the AWS access keys before anything in config.yaml
```
aws_access_key_id:
aws_secret_access_key: 
```

- Set lambda configuration 
1. Environment Variables:
```
PYTHONPATH = /mnt/fs1/lib
DGLDEFAULTDIR = /tmp/dgl
```

2. File System:
Set user created EFS file system and access points
```
Local mount path = /mnt/fs1
```

- SSH
You can get the EC2 IP from here: https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#InstanceDetails:instanceId=i-0fccf2ed4ad1472a9
Just remember to login to the right account.
```
ssh -i ~/.ssh/pair.pem ec2-user@ec2-44-212-26-45.compute-1.amazonaws.com
```
ec2-44-212-26-45.compute-1.amazonaws.com will be different


- For installing requirements in EFS through EC2
```
sudo pip3 install -r /tmp/requirements.1.txt --target /mnt/efs/fs1/lib --no-cache-dir
```

Remember to start the EC2 instance. It contains the EFS with an Access Point which the Lambda points to to resolve runtime dependencies.
