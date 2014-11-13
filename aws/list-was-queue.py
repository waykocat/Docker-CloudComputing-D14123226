# This script created a queue
#
# Author - Paul Doyle Aug 2013
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='AKIAIR7EH3TNSTDUCWKA', aws_secret_access_key='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')

#this line creates a queue
newQueue = conn.create_queue("queue4Messages")

#creating messages

#we get the queue where we want to write in

#q = conn.get_all_queues()
q = conn.get_queue('queue4Messages')

#then we create the message object
m = Message()

 #we want to create 100messages, 
strmessage = "That message "


for i in range(1,100):
    newM = strmessage + str(i) 
    m.set_body('message')
    q.write(m)

rs = q.get_messages()

m = rs[5]
messagereceived = m.get_body()
print messagereceibed


#deleting all the messages
for i in range(1,100):
    m = rs[i]
    q.delete_message(m)

