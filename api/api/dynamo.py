import boto3
from model import Todo
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.getenv('TABLE', 'test'))

TOOD = Todo()

class Dynamo:
    def create(self, **kwargs):
        try:
            table.put_item(
                    Item=json.dumps({
                        'string': 'string'|123|Binary(b'bytes')|True|None|set(['string'])|set([123])|set([Binary(b'bytes')])|[]|{}
                    }),
                    ReturnValues='ALL_NEW'
                )
        except Exception as e:
            print(e)
            
                            

    def update(self, **kwargs):
    
    def delete(self, **kwargs):

    def get(self, **kwargs):

