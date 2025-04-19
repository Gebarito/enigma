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
> Para cada novo cliente é necessário uma nova instancia de um terminal.\

## Como usar
O servidor recebe as mensagens criptografadas e repassa para os clientes conectados nele para simular
o que acontecia com o Enigma na segunda guerra (as mensagens eram passadas em canal aberto porem criptografadas).\
O cliente pode enviar mensagens criptografadas e ouvir mensagens a descriptografando.\
Para desligar o servidor execute `cntrl + D` ou `cntrl + C`.\
Para sair do cliente faça o mesmo ou digite `quit` no shell.

## Bibliografia & material de apoio
https://en.wikipedia.org/wiki/Enigma_machine
http://wiki.franklinheath.co.uk/index.php/Enigma/Sample_Messages
https://github.com/TiagoValdrich/python-socket-chat
