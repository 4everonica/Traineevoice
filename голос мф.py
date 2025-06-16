from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ТЕКСТЫ И СООБЩЕНИЯ
main_menu_text = "🏠 *Главное меню*\n\nВыберите раздел:"
faq_menu_text = "❓ *Популярные вопросы*\n\nВыберите тему:"
contacts_text = """
📞 *Контакты*

Все основные вопросы ты можешь задать своему руководителю и тренеру.

Если решить вопрос не получилось — обращайся к нам:

🧑💼 По обучению и работе тренера:
Юлия Низовцева  
📧 yuliya.n.nizovtseva@megafon.ru

💰 По любым административным вопросам:
Дарья Танина  
📧 daria.tanina@megafon.ru
"""

# ПОПУЛЯРНЫЕ ВОПРОСЫ
faq_sections = {
    'schedule': {
        'title': '🗓️ График',
        'questions': {
            'schedule_1': {
                'q': '📅 Какой график работы будет на время обучения?',
                'a': 'График 5/2, с 9:00 до 18:00. Суббота и воскресенье выходной.'
            },
            'schedule_2': {
                'q': '🔄 Можно ли изменить график после обучения?',
                'a': 'График формируется на месяц вперед. Для изменения времени начала рабочих смен следующего месяца сообщи руководителю до 10 числа текущего месяца. Для замены на один день используй Teleopti.'
            }
        }
    },
    'org': {
        'title': '📅 Организационные вопросы',
        'questions': {
            'org_1': {
                'q': '🌴 После обучения когда я смогу взять отпуск?',
                'a': 'После перехода на должность специалиста, руководитель распланирует твой отпуск на весь год.'
            },
            'org_2': {
                'q': '💬 Могу ли я отпроситься с обучения?',
                'a': 'Обучение важно посещать регулярно. При непредвиденных обстоятельствах сразу сообщи тренеру.'
            },
            'org_3': {
                'q': '💻 На обучении сломался компьютер. Что делать?',
                'a': 'Воспользуйся другим устройством или сообщи тренеру — вместе найдём решение.'
            },
            'org_4': {
                'q': '⚡ Отключили свет/интернет. Что делать?',
                'a': 'Уточни сроки восстановления и сообщи тренеру. Рассмотри альтернативные варианты подключения.'
            },
            'org_5': {
                'q': '🤒 Я плохо себя чувствую. Могу ли я пару дней отлежаться?',
                'a': 'Открой больничный и сообщи тренеру и руководителю.'
            },
            'org_6': {
                'q': '🚪 Можно ли уволиться во время обучения?',
                'a': 'Если работа не подходит, расскажи тренеру и руководителю — вместе разберемся.'
            }
        }
    },
    'study': {
        'title': '🎓 Учёба и адаптация',
        'questions': {
            'study_1': {
                'q': '📚 Что если я не сдам экзамен?',
                'a': 'Ты сможешь пересдать после повторения материала и дополнительной стажировки.'
            },
            'study_2': {
                'q': '👨🏫 Сколько времени со мной будет наставник?',
                'a': 'В первый месяц план работы снижен, ведущий специалист поможет. Пройдёшь программу адаптации.'
            }
        }
    },
    'money': {
        'title': '💰 Деньги и плюшки',
        'questions': {
            'money_1': {
                'q': '💵 Сколько мне будут платить и когда?',
                'a': 'Стоимость часа указана в договоре. Налог 13%. Выплаты: 25 и 10 числа.'
            },
            'money_2': {
                'q': '🧾 Где посмотреть расчетный листок?',
                'a': 'https://msk-sap-mvp.megafon.ru/irj/portal' 
            },
            'money_3': {
                'q': '🏥 Когда предоставят ДМС?',
                'a': 'Через 3 месяца после начала работы.'
            },
            'money_4': {
                'q': '💸 Когда платят по больничному?',
                'a': 'Первые 3 дня — компания, остальное — ФСС в течение 10 дней.'
            },
            'money_5': {
                'q': '🏆 Когда премия за успешную сдачу экзамена?',
                'a': '10 или 25 числа, в зависимости от даты перевода на должность.'
            },
            'money_6': {
                'q': '🔁 Мне нужна дополнительная стажировка. Её оплатят?',
                'a': 'Да, конечно!'
            }
        }
    }
}


# --- ФУНКЦИИ ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("❓ Популярные вопросы", callback_data='faq')],
        [InlineKeyboardButton("📞 Контакты", callback_data='contacts')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(main_menu_text, reply_markup=reply_markup, parse_mode='Markdown')


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'faq':
        keyboard = [
            [InlineKeyboardButton("🗓️ График", callback_data='schedule')],
            [InlineKeyboardButton("📅 Организационные вопросы", callback_data='org')],
            [InlineKeyboardButton("🎓 Учёба и адаптация", callback_data='study')],
            [InlineKeyboardButton("💰 Деньги и плюшки", callback_data='money')],
            [InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(faq_menu_text, reply_markup=reply_markup, parse_mode='Markdown')

    elif query.data == 'contacts':
        await query.edit_message_text(contacts_text, parse_mode='Markdown', disable_web_page_preview=True)

    elif query.data in faq_sections:
        section = faq_sections[query.data]
        keyboard = [[InlineKeyboardButton(q['q'], callback_data=f"{query.data}_{key}")] for key, q in section['questions'].items()]
        keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='faq')])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(section['title'], reply_markup=reply_markup, parse_mode='Markdown')

    elif '_' in query.data and query.data.split('_')[0] in faq_sections:
        sec_key, q_key = query.data.split('_', 1)
        question = faq_sections[sec_key]['questions'][q_key]
        keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data=sec_key)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        text = f"*{question['q']}*\n\n{question['a']}"
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

    elif query.data == 'back_to_main':
        keyboard = [
            [InlineKeyboardButton("❓ Популярные вопросы", callback_data='faq')],
            [InlineKeyboardButton("📞 Контакты", callback_data='contacts')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(main_menu_text, reply_markup=reply_markup, parse_mode='Markdown')


# --- ЗАПУСК БОТА ---
if __name__ == '__main__':
    application = ApplicationBuilder().token('7838122467:AAFFUgO54VatqZTivXCAO0frGrFPgkrdp-k').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    application.run_polling()