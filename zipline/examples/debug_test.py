from zipline.api import order, symbol

stocks = ['AAPL', 'MSFT']


def initialize(context):
    context.has_ordered = False
    context.stocks = stocks


def handle_data(context, data):
    if not context.has_ordered:
        for stock in context.stocks:
            order(symbol(stock), 100)

if __name__ == '__main__':
    pass