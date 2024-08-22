import requests

class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 2)
        print(f"{initial_amount} {from_currency} ={ amount} {to_currency}")

def main():
    url = "https://open.er-api.com/v6/latest/USD"
    converter = CurrencyConverter(url)

    print("---Döviz Çevirici---")
    try:
        from_currency = input("Çevirmek İstediğiniz Para Birimi : ").upper()
        to_currency = input("Hangi Para Birimine Çevirmek İstiyorsunuz : ").upper()
        amount = float(input("Çevirmek İstediğiniz Miktar : "))
    except Exception as e:
        print("Lütfen String ve İnteger istenen yerlere dikkat edelim! ")
    converter.convert(from_currency, to_currency, amount)

if __name__ == "__main__":
    main()