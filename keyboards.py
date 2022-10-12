from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

import main_dodo as m_dodo
#import main_kfc as m_kfc

inline_btn_1 = InlineKeyboardButton('Создать заказ!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

btn_rest = [
    [
        types.InlineKeyboardButton('KFC', callback_data='kfc'),
    #    types.InlineKeyboardButton('Вкусно и точка', callback_data='vkus'),
        types.InlineKeyboardButton('Додо Пицца', callback_data='dodo')
    ],
    [types.InlineKeyboardButton('Назад', callback_data='begin')]
]
inline_kb1_rest = InlineKeyboardMarkup(inline_keyboard=btn_rest)
'''
btn_list_kfc = []
inline_kb1_list_kfc = types.InlineKeyboardMarkup()
for info in m_kfc.infos:
    if info.text.split('\n')[1] != 'Будет позже':
        inline_kb1_list_kfc.append('info.text.replace("\n", " ").replace(" ₽", "₽")')


btn_list_kfc = []
for info in m_kfc.arr_kfc:
    btn_list_kfc.append([types.InlineKeyboardButton(info, callback_data='buy')])
inline_kb1_list_kfc = InlineKeyboardMarkup(inline_keyboard=btn_list_kfc)
'''
btn_list_dodo = []
for info in m_dodo.arr_dodo:
    btn_list_dodo.append([types.InlineKeyboardButton(info, callback_data='buy')])
inline_kb1_list_dodo = InlineKeyboardMarkup(inline_keyboard=btn_list_dodo)


btn_list_buy = [
    [
        types.InlineKeyboardButton('1', callback_data='kfc'),
        types.InlineKeyboardButton('2', callback_data='kfc'),
        types.InlineKeyboardButton('3', callback_data='kfc')
    ],
    [
        types.InlineKeyboardButton('4', callback_data='kfc'),
        types.InlineKeyboardButton('5', callback_data='kfc'),
        types.InlineKeyboardButton('6', callback_data='kfc')
    ],
    [
        types.InlineKeyboardButton('7', callback_data='kfc'),
        types.InlineKeyboardButton('8', callback_data='kfc'),
        types.InlineKeyboardButton('9', callback_data='kfc')
    ],
    [
        types.InlineKeyboardButton('10', callback_data='kfc')
    ]
]
inline_kb1_buy = InlineKeyboardMarkup(inline_keyboard=btn_list_buy)

inline_btn_buy_more_dodo = InlineKeyboardButton('Выбрать ещё товары!', callback_data='dodo')
inline_btn_buy_done = InlineKeyboardButton('Всё!', callback_data='done')
inline_kb1_buy_more_dodo = InlineKeyboardMarkup(inline_keyboard=btn_list_buy)

