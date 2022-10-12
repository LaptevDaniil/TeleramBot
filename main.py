import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import keyboards as kb
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
ID = []
buys = []


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_rest(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, 'Выберите ресторан!', reply_markup=kb.inline_kb1_rest)


@dp.callback_query_handler(lambda c: c.data == 'buy')
async def process_callback_rest(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, 'Выберите количество!', reply_markup=kb.inline_kb1_buy)

@dp.callback_query_handler(lambda c: c.data == 'done')
async def process_callback_rest(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, 'Мы отправили ваш заказ!')


@dp.callback_query_handler(lambda c: c.data == 'kfc')
async def process_callback_kfc(callback_query: types.CallbackQuery):
    for i in range(len(ID[0])):
        if ID[i][1] != username:
            await bot.send_message(ID[i][0], f"Пользователь {username} хочет заказать в KFC",
                                   reply_markup=kb.inline_kb1)
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, 'Выберите товары!', reply_markup=kb.inline_kb1_list_kfc)

@dp.callback_query_handler(lambda c: c.data == 'vkus')
async def process_callback_kfc(callback_query: types.CallbackQuery):
    for i in range(len(ID[0])):
        if ID[i][1] != username:
            await bot.send_message(ID[i][0], f"Пользователь {username} хочет заказать в Вкусно и точка",
                                   reply_markup=kb.inline_kb1)
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, 'Выберите товары!', reply_markup=kb.inline_kb1_list_vkus)

@dp.callback_query_handler(lambda c: c.data == 'dodo')
async def process_callback_kfc(callback_query: types.CallbackQuery):
    for i in range(len(ID[0])):
        if ID[i][1] != username:
            await bot.send_message(ID[i][0], f"Пользователь {username} хочет заказать в Додо Пицца",
                                   reply_markup=kb.inline_kb1)
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, 'Выберите товары!', reply_markup=kb.inline_kb1_list_dodo)

@dp.callback_query_handler(lambda c: c.data == 'begin')
async def process_callback_begin(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, "Бот заработал!", reply_markup=kb.inline_kb1)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    ID.append([message.from_user.id, message.from_user.first_name])
    global username
    username = message.from_user.first_name
    await message.answer("Бот заработал!", reply_markup=kb.inline_kb1)

if __name__ == '__main__':
   executor.start_polling(dp)