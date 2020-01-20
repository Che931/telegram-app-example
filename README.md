# TELEGRAM-APP-EXAMPLE

A simple example to understand how Telethon library works. [Read More!](https://docs.telethon.dev/en/latest/index.html)

## Installing:

* Create a virtual enviroment to avoid some dependencies problems
* Install dependencies `pip install -r requirements.txt`
* Rename `settings.example.py` to  `settings.py`. You must not commit that file. 
* Visit [Telegram website](https://my.telegram.org/auth) and create a new app.
* Paste APP api_id and APP api_hash into  `settings.py`
* Paste one of your dialogs' name into `CHANNEL_NAME` to get its latest msgs. 

In the first run the library will require your phone number to send you an activation code. The number must include the prefix (+1, +34...) .
Some extra files will be created and if you remove then, the activation process will be required again.
 
### TODO:

- Send a test message to yourself
- Show X messages from every channel
- Listen incoming messages
