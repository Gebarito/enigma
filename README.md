# ENYGMA CHAT

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
git clone  && cd enigma-chat/src/
```

#### Execute o servidor
```sh
python3 server.py
```

#### Execute os clientes
Para cada novo cliente é necessário uma nova instancia de um terminal.\
Abra o diretorio do repositorio e execute:
```sh
python3 client.py
```

## Como usar
O servidor recebe as mensagens criptografadas e repassa para os clientes conectados nele para simular
o que acontecia com o Enigma na segunda guerra (as mensagens eram passadas em canal aberto porem criptografadas).\
O cliente pode enviar mensagens criptografadas e ouvir mensagens a descriptografando.\
Para desligar o servidor execute `cntrl + D` ou `cntrl + C`.\
Para sair do cliente faça o mesmo ou digite `quit` no shell.

## Bibliografia & material de apoio
http://wiki.franklinheath.co.uk/index.php/Enigma/Sample_Messages
