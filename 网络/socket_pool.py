#!/usr/bin/env python

import socket
import select
import time
import getopt
import sys
import random

_work_mode = None
_proto = None
_server_ip = None
_server_port = None

def get_host_ip():
    """
    get host ip address
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('1.2.3.4', 22))
        ip = s.getsockname()[0]
    except Exception as e:
        print e
    finally:
        s.close()

    return ip


def parse_opts():
    """
    parse commond
    """
    global _work_mode
    global  _proto
    global  _server_ip
    global  _server_port
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:p:P:sch", \
        ["srv_ip=", "port=", "server=", "proto=", "client", "server", "help"])
        if len(opts) == 0:
            usage()
            sys.exit(0)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit(0)
            elif opt in ("-i", "--srv_ip"):
                _server_ip = arg
            elif opt in ("-p", "--port"):
                _server_port = int(arg)
            elif opt in ("-P", "--proto"):
                _proto = arg
            elif opt in ("--server"):
                _work_mode = 's'
            elif opt in ("--client"):
                _work_mode = 'c'
            else:
                usage()
                sys.exit(0)
    except getopt.GetoptError:
        print "parse options fail, arp tool exit"
        sys.exit(1)


def usage():
    """
    print usage
    """
    print "usage: python socket_tool.py"
    print "options: "
    print "   -h, --help:       show this help infomation"
    print "   -i, --srv_ip:     set server ip address"
    print "   -p, --port:       set server port"
    print "   -P, --proto:      set protocol: UDP|TCP"
    print "   -s, --server:     set work_mode: server"
    print "   -c, --client:     set work_mode: client"


class L4Client(object):
    """
    socket client
    """
    def __init__(self, proto="tcp"):
        self.proto = proto
        if proto == "udp":
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.conn.settimeout(2) # 不设置timeout，client会阻塞在recvfrom处
        else:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            #self.conn.bind(('100.64.64.11', 49181))

    def get_bytes(self, nbytes, generator):
        """Get nbytes from generator"""
        result = ""
        for i in range(nbytes):
            result += next(generator)
        return result

    def random_data(self):
        """Random bytes"""
        while True:
            yield chr(random.randint(0, 255))

    def run(self):
        """
        start socket client
        :return:
        """
        index = 0
        server_addr = (_server_ip, _server_port)
        try:
            if self.proto == "udp":
                while True:
                    self.conn.sendto(("Hello, UDP server. index: %d" % index).encode(),
                                     server_addr)
                    data, addr = self.conn.recvfrom(1024)
                    sip, sport = self.conn.getsockname()
                    print("%s receive data: <%s> from server: <%s> sip:sport: %s %s" \
                    % (time.time(), data.decode(), addr, sip, sport))
                    sys.stdout.flush()
                    index += 1
                    time.sleep(1)
            else:
                #import pdb; pdb.set_trace()
                self.conn.connect(server_addr)
                while True:
                    # payload = self.random_data()
                    # data = self.get_bytes(1500, payload)
                    # self.conn.send(data.encode())
                    # Bind local port
                    self.conn.send(("Hello, TCP server. index: %d" % index).encode())
                    data = self.conn.recv(1024)
                    print("%s receive data: <%s> from server" \
                    % (time.time(), data.decode()))
                    sys.stdout.flush()
                    index += 1
                    # if index == pk_num:
                    #     break
                    time.sleep(1)
        except:
            print("%s Server has exception, attempt to reconnect after (1s) ..." % time.time())
            sys.stdout.flush()
            self.conn.close()
            time.sleep(1)  # 断开连接后,每10s重新连接一次
            L4Client(self.proto).run()
        finally:
            print("Client closed ...")
            sys.stdout.flush()
            self.conn.close()


class L4Server(object):
    """
    socket server
    """
    def __init__(self, proto="tcp"):
        self.host = "0.0.0.0"
        self.port = _server_port
        self.proto = proto

        if proto == "udp":
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.serversocket.bind((self.host, self.port))
        else:
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.serversocket.bind((self.host, self.port))
            self.serversocket.listen(1000)
            self.serversocket.setblocking(0)

    def run(self):
        """
        start socket server
        :return:
        """
        index = 0
        try:
            if self.proto == "udp":
                while True:
                    data, addr = self.serversocket.recvfrom(1024)
                    if not data:
                        print("client not sent data !")

                    print("UDP server receive data: <%s> from client: <%s>"
                          % (data.decode(), addr))
                    self.serversocket.sendto(("Hello, UDP client. index: %d" % index).encode(),
                                             addr)
                    index += 1
            else:
                response = ("Hello, TCP client. index: %d" % index).encode()
                epoll = select.epoll()
                epoll.register(self.serversocket.fileno(), select.EPOLLIN)

                connections = {}
                requests = {}
                responses = {}
                endflag = 'close scoket'

                while True:
                    events = epoll.poll(1)
                    for fid, event in events:
                        if fid == self.serversocket.fileno():
                            connection, address = self.serversocket.accept()
                            connection.setblocking(0)
                            epoll.register(connection.fileno(), select.EPOLLIN)
                            connections[connection.fileno()] = connection
                            requests[connection.fileno()] = ''
                            responses[connection.fileno()] = response.encode()

                        elif event & select.EPOLLIN:
                            try:
                                requests[fid] = connections[fid].recv(1024)
                                if len(str(requests[fid].decode())) == 0:
                                    connections[fid].shutdown(socket.SHUT_RDWR)
                                    break
                                else:
                                    print("TCP server receive data: <%s>"
                                          % str(requests[fid].decode()))
                                    byteswritten = connections[fid].send(responses[fid])
                                    index += 1
                                if endflag in requests[fid]:
                                    epoll.modify(fid, select.EPOLLOUT)
                                    connections[fid].setsockopt(socket.IPPROTO_TCP,
                                                                socket.TCP_CORK, 1)
                                    print('-' * 40 + '\n' + requests[fid].decode()[:-2])
                            except:
                                continue

                        elif event & select.EPOLLOUT:
                            byteswritten = connections[fid].send(responses[fid])
                            responses[fid] = responses[fid][byteswritten:]
                            if len(responses[fid]) == 0:
                                connections[fid].setsockopt(socket.IPPROTO_TCP,
                                                            socket.TCP_CORK, 0)
                                epoll.modify(fid, 0)
                                connections[fid].shutdown(socket.SHUT_RDWR)

                        elif event & select.EPOLLHUP:
                            epoll.unregister(fid)
                            connections[fid].close()
                            del connections[fid]
        except Exception as e:
            print("server excepted: %s ..." % e)
            if self.proto == "TCP":
                epoll.unregister(self.serversocket.fileno())
            self.run()

        finally:
            print("server closed ...")


if __name__ == "__main__":
    parse_opts()
    if _proto is None:
        print "set protocol !!! <UDP|TCP>"
        sys.exit(1)

    if _work_mode is None:
        print "set work_mode !!! <Client|Server>"
        sys.exit(1)

    if _work_mode == 's':
        sc = L4Server(_proto)

    if _work_mode == 'c':
        if _server_ip is None or _server_port is None:
            print "set server_ip and server_port when work on client mode !!!"
            sys.exit(1)

        sc = L4Client(_proto)

    sc.run()
