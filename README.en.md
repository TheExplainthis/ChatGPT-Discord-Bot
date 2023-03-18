# ChatGPT Discord Bot

[中文](README.md) | English

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/TheExplainthis/ChatGPT-Discord-Bot)](https://github.com/TheExplainthis/ChatGPT-Discord-Bot/releases/)


ChatGPT is integrated with Discord, allowing teams to collaborate, communicate, and be more efficient. By following the installation steps below, you too can import ChatGPT into your Discord.

## Update
- 2023/03/03 Model change to chat completion: `gpt-3.5-turbo`

## Introduction
By importing the ChatGPT bot into every channel on Discord, simply enter `/chat` in the input box and the keyword `/chat message` will automatically be inserted. You can then enter text to interact with ChatGPT, as shown in the figure below:
![Demo](https://github.com/TheExplainthis/ChatGPT-Discord-Bot/blob/main/demo/chatgpt-discord-bot-en.gif)

## Installation Steps
### Obtaining Tokens
- Get the API Token given by OpenAI:
    1. Register/login to your account on [OpenAI](https://beta.openai.com/) platform
    2. There is a profile picture in the upper right corner. Click on it and select `View API keys`.
    3. Click on `Create new secret key` in the middle.
    - Note: Each API has a free quota and restrictions. For details, please see [OpenAI Pricing](https://openai.com/api/pricing/).
- Obtain Discord Token:
    1. Log in to [Discord Developer](https://discord.com/developers/applications)
    2. Create a bot:
        1. Enter the left side `Applications`
        2. Click `New Application` in the upper right corner and enter the name of the bot > After confirmation, enter the new page.
        3. Click on the left side `Bot`
        4. Click on the right side `Add Bot`
        5. `MESSAGE CONTENT INTENT` below needs to be turned on
        6. Click `Save Change`
        7. The token can be viewed by selecting `View Token` on the top or it will be a `Reset Token` button if it has already been applied.
    3. Set up OAuth2
        1. Click on `OAuth2` in the left column
        2. Click on `URL Generator` in the left column
        3. In the right column, select bot under `SCOPES` and select `Administrator` under `BOT PERMISSIONS` at the bottom right
        4. Copy the URL at the bottom and paste it into your browser
        5. Choose the server you want to add the bot to
        6. Click `Continue` > `Authorize`

### Project Setup
1. Fork the Github project:
    1. Register/login to [GitHub](https://github.com/)
    2. Go to [ChatGPT-Discord-Bot](https://github.com/TheExplainthis/ChatGPT-Discord-Bot)
    3. Click `Star` to support the developer
    4. Click `Fork` to copy all the code to your own repository
2. Deployment (free space):
    1. Go to [replit](https://replit.com/)
    2. Click `Sign Up` and sign in directly with your `Github` account and authorize -> click `Skip` to skip the initialization setup
    3. In the middle of the homepage, click `Create` -> a dialog box will appear, click `Import from Github` in the upper right corner
    4. If you haven't added your Github repository yet, click the link `Connect GitHub to import your private repos.` -> check `Only select repositories` -> choose `ChatGPT-Discord-Bot`
    5. Go back to step 4, at this point, the `Github URL` can choose the `ChatGPT-Discord-Bot` project -> click `Import from Github.`

### Project Execution
1. Environment variable settings
    1. After completing the previous step of importing, click on `Tools` at the bottom left of the `Replit` project management page, then click on `Secrets`.
    2. After clicking `Got it` on the right side, you can add environment variables, which need to be added:
        1. OpenAI API Token:
            - key: `OPENAI_API`
            - value: `[obtained from step one above] sk-FoXXXX`
        2. Desired model:
            - key: `OPENAI_MODEL_ENGINE`
            - value: `gpt-3.5-turbo`
        3. ChatGPT wants the assistant to play the role of a keyword (currently, no further usage instructions have been officially released, and players can test it themselves).
            - key: `SYSTEM_MESSAGE`
            - value: `You are a helpful assistant.`
        4. Discord Token:
            - key: `DISCORD_TOKEN`
            - value: `[obtained from step one above] MTA3NXXX`
2. Start execution
    1. Click `Run` at the top
    2. After successful execution, the right-hand screen will display `Hello. I am alive!`, and **copy the URL** in the upper right corner of the screen, which will be used in the next step
    - Note: if there are no requests within an hour, the program will stop running, so the next step is needed
3. CronJob periodic request sending
    1. Register/login to [cron-job.org](https://cron-job.org/en/)
    2. Select `CREATE CRONJOB` in the upper right corner of the backend
    3. Enter `ChatGPT-Discord-Bot` for `Title` and enter the URL from the previous step for URL
    4. Set it to run every `5 minutes`
    5. Click on `CREATE`


## Commands
| Command | Description |
| --- | ----- |
| `/chat` |  Type `/chat` in the input box followed by `message` to call the ChatGPT model and generate text.|
| `/reset` | ChatGPT remembers the last ten questions and answers. Calling this command will clear the history.|
| `/imagine` | Type `/imagine` in the input box followed by `prompt` to call the DALL·E 2 model and generate an image.|

## Support Us
Like this free project? Please consider [supporting us](https://www.buymeacoffee.com/explainthis) to keep it running.

[<a href="https://www.buymeacoffee.com/explainthis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="45px" width="162px" alt="Buy Me A Coffee"></a>](https://www.buymeacoffee.com/explainthis)

## Related Projects
- [chatGPT-discord-bot](https://github.com/Zero6992/chatGPT-discord-bot)

## License
[MIT](LICENSE)
