import telebot
import requests

# Enter the API of your Telegram bot
BOT_TOKEN = 'Enter the API of your Telegram bot'

# Initialize the bot with your token
bot = telebot.TeleBot(BOT_TOKEN)

def format_number(num):
    if num >= 1_000_000_000_000:
        return f"{num / 1_000_000_000_000:.3f} T"
    elif num >= 1_000_000_000:
        return f"{num / 1_000_000_000:.3f} B"
    elif num >= 1_000_000:
        return f"{num / 1_000_000:.3f} M"
    elif num >= 1_000:
        return f"{num / 1_000:.3f} k"
    else:
        return str(num)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, "Salutations, esteemed user,\n\n"
                          "I am your devoted cryptocurrency assistant. Here are the commands you can use:\n\n"
                          "1. /start - To initiate our grand endeavor\n"
                          "2. /price +[crypto name] - To inquire the current price of a specified cryptocurrency\n"
                          "3. /mc +[crypto name] - To ascertain the market capitalization of a chosen cryptocurrency\n"
                          "4. /vol +[crypto name] - To determine the 24-hour trading volume of a specified cryptocurrency\n"
                          "5. /balance +[wallet address] - Fetch the balance of the wallet\n"
                          "6. /stats +[crypto name] - Fetch the up-to-date statistics of said currency\n"
                          "7. /help - To receive guidance on the full suite of commands at your disposal")


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Would be my utmost pleasure to assist you,\n\n"
                          "1. /start - To initiate our grand endeavor\n"
                          "2. /price +[crypto name] - To inquire the current price of a specified cryptocurrency\n"
                          "3. /mc +[crypto name] - To ascertain the market capitalization of a chosen cryptocurrency\n"
                          "4. /vol +[crypto name] - To determine the 24-hour trading volume of a specified cryptocurrency\n"
                          "5. /balance +[wallet address] - Fetch the balance of the wallet\n"
                          "6. /stats +[crypto name] - Fetch the up-to-date statistics of said currency\n"
                          "7. /help - To receive guidance on the full suite of commands at your disposal")


# Function to get the latest price of a cryptocurrency
def get_crypto_price(crypto):
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd')
    data = response.json()
    return data[crypto]['usd']


# Command handler to get the latest price of a cryptocurrency
@bot.message_handler(commands=['price'])
def send_crypto_price(message):
    try:
        # Extract the cryptocurrency name from the message text
        crypto_name = message.text.split()[1].lower()
        price = get_crypto_price(crypto_name)
        bot.send_message(message.chat.id, f"The current price of {crypto_name} is: ${format_number(price)}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}, maybe try writing the full name and not the ticker of the Currency (example: Bitcoin and not BTC)")


# Function to get the market cap of a cryptocurrency
def get_crypto_market_cap(crypto):
    response = requests.get(f'https://api.coingecko.com/api/v3/coins/{crypto}')
    data = response.json()
    return data['market_data']['market_cap']['usd']


# Command handler to get the market cap of a cryptocurrency
@bot.message_handler(commands=['mc'])
def send_crypto_market_cap(message):
    try:
        # Extract the cryptocurrency name from the message text
        crypto_name = message.text.split()[1].lower()
        market_cap = get_crypto_market_cap(crypto_name)
        bot.send_message(message.chat.id, f"The market cap of {crypto_name} is: ${format_number(market_cap)}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}, maybe try writing the full name and not the ticker of the Currency (example: Bitcoin and not BTC)")


# Function to get the 24h trading volume of a cryptocurrency
def get_crypto_volume(crypto):
    response = requests.get(f'https://api.coingecko.com/api/v3/coins/{crypto}')
    data = response.json()
    return data['market_data']['total_volume']['usd']


# Command handler to get the 24h trading volume of a cryptocurrency
@bot.message_handler(commands=['vol'])
def send_crypto_volume(message):
    try:
        # Extract the cryptocurrency name from the message text
        crypto_name = message.text.split()[1].lower()
        volume = get_crypto_volume(crypto_name)
        bot.send_message(message.chat.id, f"The 24h trading volume of {crypto_name} is: ${format_number(volume)}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}, maybe try writing the full name and not the ticker of the Currency (example: Bitcoin and not BTC)")


