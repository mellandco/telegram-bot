import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8353236328:AAGQFMU9WUolFr1W6edd9oL7dRDGFa1SwRE"

utm_link = "https://consultant.net.ua/partner/am_ukrain?utm_source=telegram_mell&utm_medium=telegram_mell&utm_campaign=telegram_mell&utm_id=mell&utm_term=telegram_mell&utm_content=telegram_mell"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌐 Перейти на сайт", url=utm_link)]
    ]
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

async def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

if __name__ == "__main__":
    import sys
    if sys.platform == "darwin":
        import nest_asyncio
        nest_asyncio.apply()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    else:
        asyncio.run(main())

