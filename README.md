[![GitHub Issues][issues-shield]][issues-url]
[![Forks][forks-shield]][forks-url]
[![GitHub Stars][stars-shield]][stars-url]
[![Contributors][contributors-shield]][contributors-url]


# ElonBot: The Discord AI Bot for Chatting and Moderation

<img src="https://github.com/luca-martial/elon-bot/blob/main/botdp.png" width=300><br>

This repo contains code to create an AI replica of Elon Musk that can chat and moderate user interactions on Discord. Its conversation abilities come from Microsoft's [DialoGPT conversational model](https://huggingface.co/microsoft/DialoGPT-medium) that I fine-tuned on conversation transcripts of Elon Musk's appearance on the Joe Rogan Experience, the Lex Fridman Podcast and a Clubhouse interview. Its moderation abilities come from Unitary's [Multilingual Toxic Comment Classifier](https://huggingface.co/unitary/multilingual-toxic-xlm-roberta) allowing it to assess the toxicity of a message, warn users when they're using foul language and kick them out of the server after 3 strikes.

## Try It Out!

Wanna try it out? Here's an invite link to the Discord server (read message history is disabled). 

**Warning: give Elon a couple of minutes to get connected to his brain over at [Hugging Face](https://huggingface.co/). Until then, he'll spew some nonsense about how his brain has overheated.**

Invite link: https://discord.gg/kTgvqAWWx8 

## Demo

Here is a demo of a conversation about Tesla:

<img src="https://github.com/luca-martial/elon-bot/blob/main/gifs/tesla.gif" width=500><br>

Here is a demo of a conversation about colonizing Mars:

<img src="https://github.com/luca-martial/elon-bot/blob/main/gifs/spacex.gif" width=500><br>

Here is a demo of a conversation about bitcoin and dogecoin, along with an example of an abusive user getting kicked out:

<img src="https://github.com/luca-martial/elon-bot/blob/main/gifs/kick_bitcoin.gif" width=500><br>

You can also directly chat with the model hosted on [Hugging Face's Model Hub](https://huggingface.co/luca-martial/DialoGPT-Elon):

<img src="https://github.com/luca-martial/elon-bot/blob/main/gifs/hf_api.gif" width=500><br>

## Abilities in Detail

- Intelligent(ish) chatting
- Automated responses to messages about bitcoin and dogecoin
- Detecting toxic messages in multiple languages and reacting to them
- Kicking users out of server after 3 instances of toxic messages
- Tells users how many strikes they have (message `!kick` to use this functionality)

## Repository Structure

- **[data](https://github.com/luca-martial/elon-bot/tree/main/data)**: Folder containing webscraped transcripts from Elon's interviews on [Clubhouse](https://zamesin.me/clubhouse-elon-musk-interview/) and the [Lex Fridman podcast](https://lexfridman.com/wordpress/wp-content/uploads/2019/11/elon_musk_lex_fridman_2_transcript.pdf), as well as a [ready-to-use dataset](https://www.kaggle.com/christianlillelund/joe-rogan-experience-1169-elon-musk) retrieved from Kaggle of Elon's interview on the Joe Rogan Experience
- **[elon_bot.ipynb](https://github.com/luca-martial/elon-bot/blob/main/elon_bot.ipynb)**: Notebook for processing transcripts, fine tuning the DialoGPT model on the Elon's interview transcripts and pushing the fine-tuned model to Hugging Face
- **[main.py](https://github.com/luca-martial/elon-bot/blob/main/main.py)**: Python script for all Discord bot functionalities
- **[keep_alive.py](https://github.com/luca-martial/elon-bot/blob/main/main.py)**: Python script allowing bot to stay up

## Credit

None of this work would have been possible without the following immensly valuable public contributions:

- [freeCodeCamp](https://www.freecodecamp.org/)'s amazing tutorial: [Code a Discord Bot with Python - Host for Free in the Cloud](https://www.youtube.com/watch?v=SPTfmiYiuok)
- [Lynn Zheng](https://ruolinzheng08.github.io/)'s great [tutorial](https://www.freecodecamp.org/news/discord-ai-chatbot/) on freeCodeCamp and [repo](https://github.com/RuolinZheng08/twewy-discord-chatbot), as well as [Rostyslav Neskorozhenyi](https://www.linkedin.com/in/slanj/)'s great [Medium article](https://towardsdatascience.com/make-your-own-rick-sanchez-bot-with-transformers-and-dialogpt-fine-tuning-f85e6d1f4e30) and [Colab notebook](https://colab.research.google.com/drive/15wa925dj7jvdvrz8_z3vU7btqAFQLVlG) for fine tuning Microsoft's [DialoGPT conversational model](https://huggingface.co/microsoft/DialoGPT-medium) to have conversations with a video game or movie character
- [Nathan Cooper](https://github.com/ncoop57)'s awesome [tutorial](https://nathancooper.io/i-am-a-nerd/chatbot/deep-learning/gpt2/2020/05/12/chatbot-part-1.html) on creating open-dialog chatbots
- [Dale Markowitz](https://daleonai.com/)'s [insightful post](https://daleonai.com/build-your-own-ai-moderator-bot-for-discord-with-the-perspective-api) on building your own AI moderator bot for Discord

## Contributing

Any contributions you make are really helpful!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingContribution`)
3. Commit your Changes (`git commit -m 'Add some AmazingContribution'`)
4. Push to the Branch (`git push origin feature/AmazingContribution`)
5. Open a Pull Request

## Reporting Issues

Does something seem off? Make sure to [report it](https://github.com/luca-martial/elon-bot/issues).

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/luca-martial/elon-bot.svg
[issues-url]: https://github.com/luca-martial/elon-bot/issues

[forks-shield]: https://img.shields.io/github/forks/luca-martial/elon-bot.svg
[forks-url]: https://github.com/luca-martial/elon-bot/forks

[stars-shield]: https://img.shields.io/github/stars/luca-martial/elon-bot.svg
[stars-url]: https://github.com/luca-martial/elon-bot/stargazers

[contributors-shield]: https://img.shields.io/github/contributors/luca-martial/elon-bot.svg
[contributors-url]: https://github.com/luca-martial/elon-bot/contributors
