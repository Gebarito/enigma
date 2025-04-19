# ENYGMA CHAT

Python Socket Chat usando o método de criptografia do Enigma.

## Introdução

Implementação do algoritmo de criptografia utilizado na segunda guerra mundial que foi descriptografado posteriormente por Alan Turing.

Este projeto faz parte da disciplina de segurança da informação.

## Requisitos

```sh
git
Python 3.12.3
```

> Este projeto foi desenvolvido e testado em um Ubuntu 22.04 no windows 10 (WSL2).

## Instalando & executando o projeto
#### Clone o repositorio e abra pasta
```sh
git clone https://github.com/Gebarito/enigma.git && cd enigma/src/
```

#### Execute o servidor
```sh
python3 server.py
```

#### Execute os clientes
Abra o diretorio do repositorio e execute:
```sh
python3 client.py
```
> Para cada novo cliente é necessário uma nova instancia de um terminal.  <br />

## Como usar
O servidor recebe as mensagens criptografadas e repassa para os clientes conectados nele para simular
o que acontecia com o Enigma na segunda guerra (as mensagens eram passadas em canal aberto porem criptografadas)./
O cliente pode enviar mensagens criptografadas e ouvir mensagens a descriptografando.  <br />
Para desligar o servidor execute `cntrl + D` ou `cntrl + C`.  <br />
Para sair do cliente faça o mesmo ou digite `quit` no shell.

## Referencias
https://en.wikipedia.org/wiki/Enigma_machine  <br />
http://wiki.franklinheath.co.uk/index.php/Enigma/Sample_Messages  <br />
https://github.com/Goncalo-Chambel/EnigmaMachine <br />
https://github.com/TiagoValdrich/python-socket-chat  <br />
https://www.dio.me/articles/faca-o-seu-proprio-chat-utilizando-python-atraves-de-sockets
