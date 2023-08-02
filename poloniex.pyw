#
# ------------------------------------------------------------------------------------
# Poloniex widget
# ------------------------------------------------------------------------------------
# Author: Adam Blaszczyk
#         http://wyciekpamieci.blogspot.com
# Date:   2023-08-02
# ------------------------------------------------------------------------------------
#
# Requirements:
#         - Python 3.x
#         - polo-sdk-python repo
#           Clone the polosdk repository (https://github.com/poloniex/polo-sdk-python)
#           to the path where the poloniex.pyw file will run:
#             \polosdk
#             poloniex.pyw
#

from tkinter import *
from tkinter import simpledialog
from polosdk import RestClient

symbol = "BTC_USDT"

client = RestClient()
response = client.markets().get_price(symbol)['price']

root = Tk()
root.title("Poloniex")
root.geometry("220x40")

def btn_ticker_click():
    global symbol
    prev_symbol = symbol
    s = simpledialog.askstring("Poloniex", "Enter symbol (e.g. btc, ETH):")
    symbol = s.upper() + "_USDT"
    
    try:
       response = client.markets().get_price(symbol)['price']   
       lbl_price.config(text=response)
    except:
       symbol = prev_symbol

    btn_ticker.config(text=symbol)

def price_update():
    response = client.markets().get_price(symbol)['price']
    lbl_price.config(text=response)
    lbl_price.after(2000, price_update)

btn_ticker = Button(root, text=symbol, bg="pale green", command=btn_ticker_click)
btn_ticker.place(x=30, y=8)

lbl_price = Label(root, text=response)
lbl_price.place(x=130, y=13)

price_update()

root.mainloop()
