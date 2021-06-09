[![GitHub Issues][issues-shield]][issues-url]
[![Forks][forks-shield]][forks-url]
[![GitHub Stars][stars-shield]][stars-url]
[![Contributors][contributors-shield]][contributors-url]


# Discord Bot 

This repo contains code to create an AI replica of Elon Musk that can chat and moderate user interactions on Discord. Its conversation abilities come from Microsoft's [DialoGPT conversational model](https://huggingface.co/microsoft/DialoGPT-medium) fine-tuned using conversation transcripts of Elon Musk's appearance on the Joe Rogan Experience, the Lex Fridman Podcast and a Clubhouse interview. Its moderation abilities come from Unitary's [Multilingual Toxic Comment Classifier](https://huggingface.co/unitary/multilingual-toxic-xlm-roberta) which allow it to assess the toxicity of a comment and warn users when they make use of foul language, kicking them out of the channel if they get 3 strikes.

Wanna try it out? Here's an invite link to the Discord server: https://discord.gg/kTgvqAWWx8

Here is a demo of the bot in action.

You can also directly chat with the model hosted on Hugging Face's Model Hub.


## Structure

Here is a list of the projects contained in this repository, classified according to the domain they belong to.

**Vision:**

- **[mask-wear](https://github.com/luca-martial/fastai-v1-projects/tree/master/mask-wear)**: The goal of this project was to build an image classifier that identifies whether a person is wearing their mask properly or imporperly. Data was collected using Google Images. 

## Contributing

Contributions are what make the open source community a great place to learn, inspire, and create. Any contributions you make are really helpful!

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
