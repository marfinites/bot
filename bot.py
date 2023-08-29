import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# Obtenha o token do bot
token = "YOUR_BOT_TOKEN"

# Crie um bot
bot = telebot.TeleBot(token)

# Ative o suporte para a API de pagamentos
bot.enable_payments()

# Crie uma lista de produtos
products = [
  {
    "name": "Hamburguer",
    "description": "Um delicioso hambúrguer feito com carne, pão, queijo e bacon.",
    "price": 10.00,
    "image": "https://example.com/hamburguer.jpg"
  },
  {
    "name": "Batata frita",
    "description": "Uma porção de batatas fritas crocantes.",
    "price": 5.00,
    "image": "https://example.com/batatas-fritas.jpg"
  },
  {
    "name": "Refrigerante",
    "description": "Uma lata de refrigerante gelada.",
    "price": 3.00,
    "image": "https://example.com/refrigerante.jpg"
  }
]

# Crie uma interface de usuário
@bot.on_message()
def handle_message(message):
  if message.text == "/start":
    # Mostre a lista de produtos
    keyboard = InlineKeyboardMarkup(row_width=2)
    for product in products:
      keyboard.add(InlineKeyboardButton(product["name"], callback_data=product["id"]))

    bot.send_message(message.chat.id, "Selecione um produto:", reply_markup=keyboard)

# Crie um bot de conversação
@bot.on_callback_query()
def handle_callback_query(query):
  # Processe o pedido
  product_id = query.data
  product = products[product_id]

  # Envie uma mensagem de confirmação
  bot.send_message(query.from_user.id, f"Você solicitou {product['name']} por {product['price']}.")

# Inicie o bot
bot.polling()
