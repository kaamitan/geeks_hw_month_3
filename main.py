from config import bot, dp, root
from aiogram import executor  # type: ignore
import logging
from handlers import command, quiz, game, fsm_reg, store, echo


async def botA(_):
    for i in root:
        await bot.send_message(i, "Бот включен")


async def botD(_):
    for i in root:
        await bot.send_message(i, "Бот выключен")


command.register_commands(dp)
quiz.register_quiz(dp)
game.register_game(dp)
# fsm_reg.reg_handler_fsm_store(dp)
store.register_handlers_store(dp)
echo.register_message_handler_echo(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=botA, on_shutdown=botD)
