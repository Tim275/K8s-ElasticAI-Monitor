# AIOps Mastery: Reducing Log Costs and Optimizing Operations

# Classes

- Introduction

1. Introduction to the course - What we will cover and the sequence of classes
2. Necessary infrastructure - Machines and systems that we will run.
3. AIOps - Introduction to the concept
4. Course objective / Use case

- Environment

5. Deployment to Rancher
6. Kubernetes Deployment
7. Longhorn Configuration
8. DNS Configuration

- ElasticSearch and Kibana

10. ElastiSearch Deployment
11. Kibana Deployment
12. FluentD
13. Deployment of application with problems
14. Monitoring with dashboard in Kibana

- Ollama - GenAI

15. Infrastructure Deployment - Machine
16. Deployment ollama and llama3
17. Test the model/models

- AIOps App

18. Configure the AIOps application and see how it works. 18. Deploying AIOps App
19. Setting up Watcher in Kibana - sending alerts about logs
20. Tracking and monitoring alerts in the Discord channel.
21. Changing models to test the analyses.

- Final

22. Review of all content

# Introduction

## 1. Introduction to the course - What we will cover and the sequence of classes

## 2. Necessary infrastructure - Machines and systems that we will run.

### Linux with no firewall

- Rancher - t3.large - 2/8 - 30gb - gp2
  - Ohio - USD 0.0867 /h
- kubernetes - t3.xlarge - 4/16 - 50gb - gp2
  - Ohio - USD 0.1734 /h
- Ollama - c5.2xlarge - 8/64 - 200gb - gp2
  - Ohio - USD
- Discord Account
- DockerHub Account
- DNS

### System Requirements

UBUNTU 22 LTS
Docker 20.10

Rancher 2.6.9
Kubernetes 1.24.17

ElasticSearch 7.17.3
Kibana 7.17.3

Longhorn

## 3. AIOps - Introduction to the concept

https://www.xenonstack.com/blog/log-analytics-generative-ai

## 4. Course objective / Use case

# Environment

## 5. Rancher Deployment

```sh
cd ~/Dropbox/hotmart_aiops_logs_english

sudo su
curl https://releases.rancher.com/install-docker/20.10.sh | sh
usermod -aG docker ubuntu

$ docker ps -a
$ docker run -d --restart=unless-stopped \
  -p 80:80 -p 443:443 \
  --privileged \
  rancher/rancher:v2.6.9

ssh -i pic.pem ubuntu@3.140.193.119

ssh -i pic.pem ubuntu@18.216.242.38

ssh -i pic.pem ubuntu@18.191.107.234


```

## 6. Kubernetes Deployment

```sh

ssh -i pic.pem ubuntu@3.135.62.162

sudo su
curl https://releases.rancher.com/install-docker/20.10.sh | sh
usermod -aG docker ubuntu

sudo docker run -d --privileged --restart=unless-stopped --net=host -v /etc/kubernetes:/etc/kubernetes -v /var/run:/var/run  rancher/rancher-agent:v2.6.9 --server https://13.59.74.126 --token dff9svgw8h8z6hvkdvqdqxfxx6hknk5hjcsd25fs7kmdz4clp78ft5 --ca-checksum b740dd2823db1225b53a8087520a0f07de8c5a54a83b95c996774aa850c17d76 --etcd --controlplane --worker

```

## 7. Longhorn Configuration

Follow the video

## 8. DNS Configuration

Follow the video

Use your DNS service to point to you Kubernetes machine

# ElasticSearch and Kibana

## 9. ElastiSearch Deployment

Install Helm

```sh
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

```sh
kubectl create namespace logging

echo -n "elastic" | base64
echo -n "1qazXSW@3edc" | base64
```

```sh
kubectl apply -f elastic-cred.yaml

helm repo add elastic https://helm.elastic.co
helm repo update
```

```sh
helm install elk-elasticsearch elastic/elasticsearch -f elastic-no-cert.yaml --namespace logging --set imageTag=7.17.3 --version 7.17.3


helm upgrade elk-elasticsearch elastic/elasticsearch -f elastic-no-cert.yaml --namespace logging --set imageTag=7.17.3 --version 7.17.3


helm delete elk-elasticsearch --namespace logging
```

## 10. Kibana Deployment

```sh
helm install elk-kibana elastic/kibana -f kibana-no-cert.yaml -n logging --set imageTag=7.17.3 --version 7.17.3


helm upgrade elk-kibana elastic/kibana -f kibana-no-cert.yaml -n logging --set imageTag=7.17.3 --version 7.17.3


helm delete elk-kibana -n logging
```

## 11. FluentD

```sh
kubectl apply -f fluentd-infra.yaml
```

## 12. Deployment of application with problems

```sh
cd unhealthy_app
kubectl apply -f deployment.yaml
cd ..
./hit_urls.sh

```

## 13. Monitoring with dashboard in Kibana

Monitor and create the first dahboard.

# Ollama - GenAI

## 14. Infrastructure Deployment - Machine

Folder genai

## 15. Deployment ollama and llama3

Folder genai

## 16. Test the model/models

Folder genai

# AIOps App

## 17. Configure the AIOps application and see how it works.

Folder aiops-app

## 18. Deploying AIOps App

Folder aiops-app

## 19. Setting up Watcher in Kibana - sending alerts about logs

Elastic-watcher.md

## 20. Tracking and monitoring alerts in the Discord channel.

Discord

## 21. Changing models to test analyses.

# Final

## 22. Review

RODA DENTRO DO DevTools

```sh
GET _cat/indices/k8s-infra*?v&bytes=gb


```

# App to generate many kinds of logs. Differ

Logar na maquina do rancher, copiar os arquivos para pasta /home/user/app

app.py
Dockerfile
requirements.txt

```sh
ssh -i pic.pem ubuntu@18.221.23.124

mkdir -p app_nao_saudavel
cd app_nao_saudavel


```

Criar o dashboar com os graficos por namespace.

Fazer build e deploy da aplicação

Depois, quando a aplicação estiver rodando dentro do cluster, iremos usar o script abaixo para gerar carga nela

```sh
chmod +x hit_urls.sh

./hit_urls.sh
```

Fazer o dashboard para poder mostrar as TOP mensagens em agregação, mostrando na tela como fazer para chegar nesse relatorio. E mostrando o relatorio.

---

Fazer o modelo para mostrar os top de mensagens de erro.

## https://chatgpt.com/c/6717a6c4-e590-8004-aab3-959a594967de

# ATIVAR A LICENÇA TRIAL para poder criar webhooks e poder enviar

Ativar a licença trial para poder enviar webhooks.

# TERMINAR

Agora iremos criar a nossa aplicação aiops que irá receber os alertas do Kibana com as mensagens de erro que mais aparecem nos ultimos minutos. Essa aplicação ira rodar na mesma maquina do rancher, e ela ira ter como background o llama32 da Meta que irá fazer as análises dos logs e prover as soluções e mais detalhes.

Fazer a API, terminar, e depois que terminar, testar ela, criando os alertas manualmente, e depois fazer o teste com a carga sendo executada.

# AIOPS-APP

Copiar o conteudo do app da pasta aiops-app

Fazer mandar uma mensagem antes para mostrar o dado RAW que vai ser analisado na API
mostrar o resultado

Pensar em fazer um dashboard mostrando,

- Terminar a aplicaçào e colocar ela dentro do container e rodar local.
- Colocar mais infomrações de LOG quando for publicar no Discrod e quando receber o retorno da analise do modelo.
- Testr outro modelo.

- TERMINAR A DOCUMENTAÇÃO -
- FAZER MATERIAL DO CURSO NO HOTMART

  - Conteúdo Gravado.

- MASTERCLASS PRECISA DO VIMEO -

Fazer a API receber as mensagens e trabalhar e mandar o resultado para algum lugar ou exibir na tela em algum HTML o resultado, simples

- Mexer a aplicação para gerar os logs de erros de maneira randomica e ficar mais parecido com cenario real. Atualizar o script que faz os testes.

- Fazer o deploy do Ollama com o llama 3.2 - e Lincar a API nele.

Webhook URL from Discord

https://discord.com/api/webhooks/1299793506830647419/kCWqbry1tSPkPuPvWJNHGv8WDaFnvedXyUDXbLIZH3WheTe1LX4EDGGc_pNMLvMNz55h

```python

import requests

def send_discord_message(webhook_url, message):
    data = {"content": message}
    requests.post(webhook_url, json=data)


```

Send message to Discord.

```sh
curl -H "Content-Type: application/json" \
     -d '{"content": "Alert: High memory usage detected!"}' \
     https://discord.com/api/webhooks/1299793506830647419/kCWqbry1tSPkPuPvWJNHGv8WDaFnvedXyUDXbLIZH3WheT    docker stop $(docker ps -q --filter "ancestor=rancher/rancher-agent:v2.6.9")
    docker rm $(docker ps -q --filter "ancestor=rancher/rancher-agent:v2.6.9")
    docker stop $(docker ps -q --filter "ancestor=rancher/mirrored-coreos-etcd:v3.5.4")
    docker rm $(docker ps -q --filter "ancestor=rancher/mirrored-coreos-etcd:v3.5.4")e1LX4EDGGc_pNMLvMNz55h
```
