from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8323378299:AAFEWRyW_5fgGLYcBWqUbuEe-8SUF9UcxVE"

utm_link = "https://consultant.net.ua/partner/ukrain_am?utm_source=telegram_mell&utm_medium=telegram_mell&utm_campaign=telegram_mell&utm_id=mell&utm_term=telegram_mell&utm_content=telegram_mell"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🌐 Перейти на сайт", url=utm_link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "🇺🇦 Професійна допомога військового юриста — захистимо ваші права!\n\n"
        "Допомагаємо мобілізованим, військовослужбовцям та їхнім родинам у найважливіших питаннях:\n"
        "✔ Оскарження рішень ВЛК\n"
        "✔ Виплати військовим\n"
        "✔ Юридичний супровід по СЗЧ\n"
        "✔ Відстрочка від мобілізації\n\n"
        "Не відкладайте — захистіть свої права вже сьогодні!\n\n"
        "👇 Залишайте заявку на сайті, щоб отримати кваліфіковану консультацію"
    )

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
