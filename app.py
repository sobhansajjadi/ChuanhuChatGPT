from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, \
    filters, InlineQueryHandler, Application, CallbackContext, CallbackQueryHandler, ConversationHandler
from telegram import Update
import openai
class TelegramBot:
    """
    Class representing a ChatGPT Telegram Bot.
    """

    def init(self):
        print("HELLO")
        self.TOKEN = "6252991905:AAHj7riNlmu5N_PK8xpja_38ARJ2RJ_DVs0"
        self.api = "a"
        pass
    async def start(self, update: Update, context: CallbackContext):
        await update.message.reply_text("Welcome to your Telegram bot!")

    async def prompt(self, update: Update, context: CallbackContext):
        user_id = update.message.from_user.id
        message_text = update.message.text
        messages= [{"role": "user","content": message_text}]
        print(f"User {user_id} sent: {message_text}")
        openai.api_key = self.api
        openai.api_base = "https://api.gateai.ir"

        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            max_tokens=1000,
            messages=messages,
            temperature=0.5,
            n=1,
            stream=False
        )
        if "choices" in response and "message" in response.choices[0]:  # non-streaming
            await update.message.reply_text(response.choices[0]["message"]["content"].strip())
        else:
            await update.message.reply_text("??")


    async def post_init(self, application: Application) -> None:
        """
        Post initialization hook for the bot.
        """


    def main(self):

        application = ApplicationBuilder() \
            .token(self.TOKEN) \
            .post_init(self.post_init) \
            .concurrent_updates(True) \
            .build()


        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.prompt))
        application.run_polling()

if name == 'main':
    tb = TelegramBot()
    tb.main()