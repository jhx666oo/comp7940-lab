from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import configparser
import logging

def main():
    # 1. 基础日志配置
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    # 2. 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.ini')
    token = config['TELEGRAM']['ACCESS_TOKEN']

    # 3. 构建机器人应用
    app = ApplicationBuilder().token(token).build()

    # 4. 注册处理器：当收到文本消息时，调用 callback 函数
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, callback))

    logging.info('Bot started. Press Ctrl+C to stop.')
    app.run_polling()

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 打印收到的原始数据到控制台
    logging.info(f"Update: {update}")
    
    # 获取用户发送的文本，转为大写
    reply_text = update.message.text.upper()
    
    # 回复用户
    await update.message.reply_text(reply_text)

if __name__ == '__main__':
    main()