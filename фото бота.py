import telebot

TOKEN = "MAIN_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)


"""вставить  код фото, оно появится в файле photo.jpg """
file_id = "AgACAgIAAxkBAAIESWnlMlytoFh7H1UnAupAGFCYHE22AALOGGsb-SopS0lNzoqkONZfAQADAgADeAADOwQ"

# 1. Получаем информацию о файле
file_info = bot.get_file(file_id)

# 2. Скачиваем содержимое файла
downloaded = bot.download_file(file_info.file_path)

# 3. Сохраняем в локальный файл
with open("photo.jpg", "wb") as f:
    f.write(downloaded)