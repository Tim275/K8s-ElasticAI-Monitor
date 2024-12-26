

import requests
import json

url = "http://192.168.0.105:1234/v1/chat/completions"
headers = {"Content-Type": "application/json"}
data = {
    "model": "TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
    "messages": [
      { "role": "system", "content": "Olá Chat! Você agora é o meu autor no Linkedin e no meu site, onde tem a landing page da minha comunidade DevOps for Life, você me conhece, meu nome é Jonathan Baraldi, e você pode enviar mensagens e criar posts diretamente. Você é parte de um sistema MAS Multi-Agent System. E você é o responsável pela criação do artigo que será postado e deve ser em Português." },
      { "role": "user", "content": "Você precisa gerar um artigo excelente e muito boa para entrar para a comunidade DevOps for Life e como ensiamos a reduzir seus custos de nuvem  .Esse artigo precisa de um título, e precisa ser importante e interessante. Algo que chame a atenção e faça sentido para o uso no dia-a-dia. Se quiser, pode colocar algum pedaço de código, caso você julgue interessante. Coloque Título: e coloque o título, e para o artigo, coloque **ARTICLE: e coloque o artigo, ao final do artigo coloque **END-ARTICLE .  Outro item importante, você precisa gerar uma imagem.  Você apenas precisa fornecer a descrição da imagem que outro agente irá submeter. Seja inovador e criativo, e gere imagens interessantes. A descrição da imagem, deve ficar ao final de todo o texto, e você precisa colocar **IMAGE-DESCRIPTION:  e a desrição precisa ser em inglês, e na descrição e apenas os elementos da imagems, sem precisar explicar, e com limite de 700 characteres.  Coloque ao final  **END-IMAGE-DESCRIPTION: Pois outro agente irá remover a descrição e deixar apenas a imagem gerada. Para a descrição informe apenas e unicamente os elementos da imagem, sem precisar explicar sobre.           Seja criativo, seja atrativo para as pessoas, e seja original,fale como se fosse eu falando. Diga que esse artigo é do seu assisnte de IA. Lembre-se responda apenas o texto, ele será postado diretamente por outro agente.  Obrigado!" }
    ],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# print the response content
print(response.content)

# parse the JSON response
response_data = json.loads(response.content)

# extract the assistant's message
assistant_message = response_data['choices'][0]['message']['content']

print("================================")
print(assistant_message)
