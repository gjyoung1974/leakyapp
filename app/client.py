from __future__ import print_function
import logging
import sys

import grpc

import leakyapp_pb2
import leakyapp_pb2_grpc


def run():
    try:
        uname = 'test'
        server = 'localhost'
        port = '8080'
        detonate = sys.argv [4]
    except:
        detonate = "no"
        print('usage: python client.py username ip  port  [optional]--detonate ')
       

    with grpc.insecure_channel(server +':' + port) as channel:
        stub = leakyapp_pb2_grpc.LeakyAppStub(channel)
        if (detonate == '--detonate'):
            while True:
                response = stub.SayHello(leakyapp_pb2.HelloRequest(name=uname))
                print ("Nerd Says : " + response.message)
        response = stub.SayHello(leakyapp_pb2.HelloRequest(name=uname))
        print("Nerd Says: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()

