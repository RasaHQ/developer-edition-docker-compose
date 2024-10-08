# Quick, Small Deployment of the Rasa Pro Developer Edition

Docker Compose configuration for rapidly getting started with running a bot using the Rasa Pro Developer Edition.
This is intended as a lightweight way to deploy a Rasa assistant that will receive only small amounts of traffic.

Note you will need an [extended license](#) to run Rasa Pro Developer Edition on a server. 

1. Create a VM on your cloud provider of choice, and install Docker. 1vCPU and 2GB RAM should be sufficient unless you've trained a big NLU model.

2. Create a directory and copy in the following files from this repo:
- `docker-compose.yml`
- `endpoints.yml`
- `credentials.yml`
- `actions.py`
- `models/model.tar.gz`

3. Create a file called `.env` in the same directory with the following contents:
```
RASA_PRO_LICENSE=<your Rasa Pro license goes here>
OPENAI_API_KEY=<your OpenAI API key goes here>
```

4. Deploy the bot by running `sudo docker compose up`. (On older docker versions, it would be `sudo docker-compose up`)

5. Send your bot a message by sending a POST request: 

```
curl -XPOST http://<host>:5005/webhooks/rest/webhook -d '{"sender": "test", "message": "Hi"}'
```

## Customization

Now that you have a demo assistant deployed, here are the next steps you might want to take:

1. Upload your own model to replace the default one in the repo.
2. Add your own custom action files, or [build a custom action server image](https://rasa.com/docs/rasa-pro/deploy/deploy-action-server/#using-your-custom-action-server-image)
3. Configure your assistant to respond on other channels by 
modifying the `credentials.yml` file, see [here](https://rasa.com/docs/rasa-pro/connectors/messaging-and-voice-channels)

 
