from telegram.ext import *
from weather_handler import hourly_rain,daily_rain,hourly_uvi,daily_uvi,sunrise_time,sunset_time,psi_reading
import constants
import responses as R


print("Bot started")
def start(update,context):
    update.message.reply_text("type something to get started!\n"
                              "/help to see the available commands!")


def help(update, context):
    update.message.reply_text("Ello! Welcome to wentd bot! I provide detailed weather forecasts which can be accessed through the following commands!\n"
                              "/daily_rain_forecast -> provides you with rain forecast for the following day\n"
                              "/hourly_rain_forecast -> provides you with rain forecast for the following hour\n"
                              "/daily_uvi_forecast -> provides you with uv radiation forecast for the following day\n"
                              "/hourly_uvi_forecast -> provides you with uv radiation forecast for the following hour\n"
                              "/sunrise -> provides you with sunrise timing for the current day and next day\n"
                              "/sunset -> provides you with sunset timing for the current day and next day\n"
                              "/psi -> provides you with current psi reading")


def handle(update,context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update,context):
    print(f"{update} caused error {context}")

def rain_daily(update,context):
    reply = str(daily_rain())
    update.message.reply_text(f"expecting {reply}")

def rain_hourly(update,context):
    reply = str(hourly_rain())
    update.message.reply_text(f"expecting {reply}")

def uvi_hourly(update,context):
    reply = str(hourly_uvi())
    update.message.reply_text(f"expecting {reply}")

def uvi_daily(update,context):
    reply = str(daily_uvi())
    update.message.reply_text(f"expecting {reply}")

def sunrise(update,context):
    reply = sunrise_time()
    update.message.reply_text(f"sunrise time for today is {reply[0]}\n"
                              f"sunrise time for tomorrow is {reply[1]}")

def sunset(update,context):
    reply = sunset_time()
    update.message.reply_text(f"sunset time for today is {reply[0]}\n"
                              f"sunset time for tomorrow is {reply[1]}")

def psi(update,context):
    reply = psi_reading()
    update.message.reply_text(f"current psi reading is {reply} ")

def main():
    updater = Updater(constants.API_key,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("daily_rain_forecast",rain_daily))
    dp.add_handler(CommandHandler("hourly_rain_forecast", rain_hourly))
    dp.add_handler(CommandHandler("hourly_uvi_forecast", uvi_hourly))
    dp.add_handler(CommandHandler("daily_uvi_forecast", uvi_daily))
    dp.add_handler(CommandHandler("sunrise", sunrise))
    dp.add_handler(CommandHandler("sunset", sunset))
    dp.add_handler(CommandHandler("psi", psi))
    dp.add_handler(MessageHandler(Filters.text,handle))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()