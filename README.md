# Telegram Send
Esse script lê um arquivo com a lista de números e envia uma mensagem para os mesmos via Telegram.

## Atenção
**Script criado com o ojetivo de pesquisa, não utilize para SPAM, uma vez que seu número poderá ser banido do Telegram conforme descrito na sua documentação: https://telegram.org/faq_spam/br**

## Modo de uso
Para utilização deste é nescessário ter o python instalado em seu computador (desenvolvido e testado na versão 3), caso não tenha, faça download em https://www.python.org/.

- Instale a biblioteca Telethon:
```
pip install Telethon
```

- No mesmo diretório do script, deverá ter um arquivo *config.json* com o conteúdo conforme o arquivo de mesmo nome neste repositório, preencha-o com suas informações, caso não tenha essas informações acesse: https://my.telegram.org/
- Crie seu arquivo com os números de destino com o nome *list.txt*
- Envie usando o comando: 
```
py script.py
```
