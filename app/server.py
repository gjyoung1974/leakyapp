from concurrent import futures
import logging

import grpc

import leakyapp_pb2
import leakyapp_pb2_grpc
import random
import re


class LeakyApp(leakyapp_pb2_grpc.LeakyApp):

    def SayHello(self, request, context):
        uname = str (request.name)
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:=]')
        if(regex.search(uname) == None):
            print ('Responding to ' + uname)
            messages = ['Where is my coffee?', 'Is this legal?', 'Don\'t drink and root', 'Credit card number 3438 0202 1052 1426 ', 'I want to go to a mall' ]
            msg = uname +', ' + messages[random.randint(0,4)]
            return leakyapp_pb2.HelloReply(message= msg ) 
        else:
            return leakyapp_pb2.HelloReply(message = 'I see you dont follow by rules')
         
            


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    leakyapp_pb2_grpc.add_LeakyAppServicer_to_server(LeakyApp(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()
   


if __name__ == '__main__':
    logging.basicConfig()
    serve()
    print('Server is ready to receive request !!')