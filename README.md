[![GitHub Issues][issues-shield]][issues-url]
[![Forks][forks-shield]][forks-url]
[![GitHub Stars][stars-shield]][stars-url]
[![Contributors][contributors-shield]][contributors-url]


# ElonBot: The Discord AI Bot for Chatting and Moderation

This repo contains code to create an AI replica of Elon Musk that can chat and moderate user interactions on Discord. Its conversation abilities come from Microsoft's [DialoGPT conversational model](https://huggingface.co/microsoft/DialoGPT-medium) fine-tuned using conversation transcripts of Elon Musk's appearance on the Joe Rogan Experience, the Lex Fridman Podcast and a Clubhouse interview. Its moderation abilities come from Unitary's [Multilingual Toxic Comment Classifier](https://huggingface.co/unitary/multilingual-toxic-xlm-roberta) allowing it to assess the toxicity of a message, warn users when they're using foul language and kick them out of the server when they get 3 strikes.

## Try It Out!

Wanna try it out? Here's an invite link to the Discord server: https://discord.gg/kTgvqAWWx8

## Demo

Here is a demo of a conversation about Tesla:

<img src="https://github.com/luca-martial/elon-bot/blob/main/gifs/tesla.gif" width=500><br>

Here is a demo of a conversation about colonizing Mars:

<img src="https://github.com/luca-martial/elon-bot/blob/main/gifs/spacex.gif" width=500><br>

Here is a demo of a conversation about bitcoin and dogecoin:

<img src="https://github.com/luca-martial/elon-bot/blob/main/gifs/kick.gif" width=500><br>

You can also directly chat with the model hosted on [Hugging Face's Model Hub](https://huggingface.co/luca-martial/DialoGPT-Elon):

## Detailed Abilities

- Intelligent chatting
- Automated responses to messages about bitcoin and dogecoin
- Detecting toxic messages and reacting to them
- Kicking users out of server after 3 instances of toxic messages
- Tells users how many strikes they have (message `!kick` to use this functionality)

## Repository Structure

- **[mask-wear](https://github.com/luca-martial/fastai-v1-projects/tree/master/mask-wear)**: The goal of this project was to build an image classifier that identifies whether a person is wearing their mask properly or imporperly. Data was collected using Google Images. 

## Credit

None of this work would have been possible without the following immensly valuable public contributions:

- freeCodeCamp's amazing tutorial: [Code a Discord Bot with Python - Host for Free in the Cloud](https://www.youtube.com/watch?v=SPTfmiYiuok)
- [Lynn Zheng](https://ruolinzheng08.github.io/)'s great [tutorial](https://www.freecodecamp.org/news/discord-ai-chatbot/) on freeCodeCamp and [repo](https://github.com/RuolinZheng08/twewy-discord-chatbot), as well as [Rostyslav Neskorozhenyi](https://www.linkedin.com/in/slanj/)'s great [Medium article]((https://towardsdatascience.com/make-your-own-rick-sanchez-bot-with-transformers-and-dialogpt-fine-tuning-f85e6d1f4e30)) and [Colab notebook](https://colab.research.google.com/drive/15wa925dj7jvdvrz8_z3vU7btqAFQLVlG) for fine tuning Microsoft's [DialoGPT conversational model](https://huggingface.co/microsoft/DialoGPT-medium) to have conversations with a video game or movie character
- [Nathan Cooper](https://github.com/ncoop57)'s awesome [tutorial](https://nathancooper.io/i-am-a-nerd/chatbot/deep-learning/gpt2/2020/05/12/chatbot-part-1.html) on open-dialog chatbots
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
