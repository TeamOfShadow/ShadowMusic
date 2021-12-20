from pyrogram.types import InlineKeyboardButton


def leaveall_markup(user_id):
    buttons = [
        [
            InlineKeyboardButton(text="Assistant 1", callback_data="Assistant_1"),
            InlineKeyboardButton(text="Assistant 2", callback_data="Assistant_2"),
        ],
        [
            InlineKeyboardButton(text="Assistant 3", callback_data="Assistant_3"),
            InlineKeyboardButton(text="Assistant 4", callback_data="Assistant_4"),
        ],
        [
            InlineKeyboardButton(text="Assistant 5", callback_data="Assistant_5"),
        ],
        [
            InlineKeyboardButton(text="🗑 Close", callback_data=f"close"),
        ]
    ]
    return buttons
