from aiogram import types, Dispatcher


async def echo_message(message: types.Message):
    if message.text.isdigit():
        try:
            result = int(message.text) ** 2
            await message.answer(result)
        except ValueError:
            await message.answer("ввeдите число или слово")
    else:
        await message.answer(message.text)


def register_message_handler_echo(dp: Dispatcher):
    dp.register_message_handler(echo_message)
