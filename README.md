# check-username-teleton

## Overview

This script checks if a list of Telegram usernames exists or not using the [Telethon](https://docs.telethon.dev/) library, which provides a convenient interface for interacting with the Telegram API. The usernames are read from an input file, checked, and the available ones are saved to an output file in JSON format.

## Features

- Reads a list of usernames from a text file.
- Checks the availability of each username on Telegram.
- Handles potential rate limiting using `FloodWaitError`.
- Saves the available usernames in a JSON file for later use.

## Installation

Before running this script, you need to have Python and the `Telethon` library installed. Follow the instructions below to get started:

### Prerequisites

- Python 3.6+
- A Telegram API ID and Hash from [my.telegram.org](https://my.telegram.org/).

### Installing `Telethon`

You can install the `Telethon` library using `pip`:

```bash
pip install telethon
```

Alternatively, you can install the latest version directly from GitHub:

```bash
pip install git+https://github.com/LonamiWebs/Telethon.git
```

### Setting Up the API Credentials

To interact with the Telegram API, you need an API ID and an API Hash. You can get these by logging into [my.telegram.org](https://my.telegram.org/) and creating a new application. Use these values in the script:

```python
api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone_number = '+123456789'
```

## How the Script Works

1. **Client Setup**: The script initializes a `TelegramClient` using the API credentials and the phone number for login.
2. **Reading Usernames**: It reads the usernames from an input text file (`file-name.txt`), where each username is listed on a new line.
3. **Checking Username Availability**: It calls the `CheckUsernameRequest` function to check if the username exists. If the username is available, it adds it to a list.
4. **Handling FloodWaitError**: If too many requests are sent to Telegram's servers in a short time, the script waits for the required time (to avoid being blocked) and then retries.
5. **Saving Results**: After checking all usernames, the available usernames are saved to a JSON file (`available_usernames.json`).

## Example Usage

1. Set up your `api_id`, `api_hash`, and `phone_number` in the script.
2. Create a text file (`file-name.txt`) with one username per line.
3. Run the script using Python:

```bash
python check_username.py
```

4. The results will be saved in `available_usernames.json`

## Disclaimer

This script is provided as-is and is meant for educational purposes. By using this code, you acknowledge that you are responsible for any actions taken and that the creators of this script hold no liability for any issues or misuse. Always respect Telegram's terms and conditions.

For any questions or issues, feel free to contact us on Telegram:

[Telegram Contact](https://t.me/cipher_black) --> @cipher_black
