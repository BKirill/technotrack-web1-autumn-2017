# -*- coding: utf-8 -*-
import socket
from os import listdir


def get_response(request):

    req = request.split()
    path = req[1]
    i = req.index('User-Agent:') + 2
    user = req[i - 1]
    while not req[i].endswith(':'):
        user = user + ' ' + req[i]
        i += 1
    host = req[req.index('Host:') + 1]
    if path.find(host) != -1:
        path = path.replace(host, '')
    ansv = ''
    if req[0] != 'GET':
        ansv = '<html><head><title>Method not allowed</title></head><body><p>Method not allowed</p></body></html>'
        ansv = req[2] + '405 Method Not Allowed\n Content-type: text/html\nContent-Length:' + str(len(ansv)) + '\n\n' + ansv
    elif path == '/':
        ansv = '<html><head><title>Hello</title></head><body><p>Hello mister!<br>You are: ' + user + '</p></body></html>'
        ansv = req[2] + '200 OK\n Content-type: text/html\nContent-Length:' + str(len(ansv)) + '\n\n' + ansv
    elif path == '/media/':
        files = '<br>'.join(listdir('./files/'))
        ansv = '<html><head><title>Media</title></head><body><p>' + files + '</p></body></html>'
        ansv = req[2] + '200 OK\n Content-type: text/html\nContent-Length:' + str(len(ansv)) + '\n\n' + ansv
    elif path == '/test/':
        ansv = request.replace('\n', '<br>')
        ansv = '<html><head><title>Test</title></head><body><p>' + ansv + '</p></body></html>'
        ansv = req[2] + '200 OK\n Content-type: text/html\nContent-Length:' + str(len(ansv)) + '\n\n' + ansv
    elif path.find('/media/') != -1:
        path = path.replace('/media/', '')
        if path in listdir('./files/'):
            f = open('./files/' + path)
            ansv = f.read()
            ansv = ansv.replace('\n', '<br>')
            ansv = '<html><head><title>File</title></head><body><p>' + ansv + '</p></body></html>'
            ansv = req[2] + '200 OK\n Content-type: text/html\nContent-Length:' + str(len(ansv)) + '\n\n' + ansv
        else:
            ansv = '<html><head><title>File not found</title></head><body><p>File not found</p></body></html>'
            ansv = req[2] + '404 Not Found\n Content-type: text/html\nContent-Length:' + str(len(ansv)) + '\n\n' + ansv
    else:
        ansv = '<html><head><title>Page not found</title></head><body><p>Page not found</p></body></html>'
        ansv = req[2] + '404 Not Found\n Content-type: text/html\nContent-Length:' + str(len(ansv)) + '\n\n' + ansv
    return ansv


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #привязываем к сокету хост localhost и порт 8000
server_socket.listen(0)  #устанавливаем сокет в режим прослушивания, максимальное число подключений в очереди - 0

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #печатаем имя подключившегося сокета
        request_string = client_socket.recv(2048)  #получаем запрос от клиента
        client_socket.send(get_response(request_string))  #отправляем клиенту результат обработки запроса
        client_socket.close()
    except KeyboardInterrupt:  #выполнение программы прервано пользователем
        print 'Stopped'
        server_socket.close()  #закрываем соединение
        exit()
