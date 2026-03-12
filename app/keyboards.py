from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardButton, InlineKeyboardMarkup)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Создать напоминание"),
                                      KeyboardButton(text="Изменить напоминание"), 
                                      KeyboardButton(text="Закончить напоминание")],
                                     [KeyboardButton(text="Просмотреть напоминания")],
                                     [KeyboardButton(text="Поддержка"), KeyboardButton(text="Справка")],
                                    ],
                            resize_keyboard=True, 
                            input_field_placeholder="Выберите нужное.."
                            )

spravka = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Что умеет бот?", callback_data = "w_skill"),
                                                 InlineKeyboardButton(text="О проекте", callback_data = "info")], 
                                                 [InlineKeyboardButton(text = "Выход", callback_data = "exit")]
                                                ])