import requests # This needs to be installed with pip
# DO NOT UPLOAD A VIRTUAL ENVIRONMENT TO GIT

class CurrencyConverter:
    def __init__(self, url):
        self.data= requests.get(url).json()
        self.currecies= self.data['rates']
        """
        When a currency converter is created it should first try to load currency data from JSON (using the load_currency_data-method)
        If it doesn't find any json-data, it should try to get the data from the exchangerates API (using the fetch_currency_data-method)
        """

    def fetch_currency_data(self):
        """
        This method should fetch new currency data using the openexchangerate API
        It has some boilerplate code you can use.
        """
        # Use this code to fetch currency data from openexchangerates.org.
        app_id = "YOUR_APP_ID" # Add your own app_id from openexchangerates.org here
        url = f"https://openexchangerates.org/api/latest.json?app_id={e51b35554f8443ac9929f62fe6239e10}"
        headers = {"accept": "application/json"} # This needs to be added, it tells the API that they should return JSON
        response = requests.get(url, headers=headers)
    
    def convert_from_usd(self, to_currency, amount):

        """
        This method should convert from USD to a currency of choice
        You should not use an additional endpoint, the latest currencies are enough.
        """
        pass
            
    def convert_any_currency(self, from_currency, to_currency, amount):
        initial_amount = amount
        #fisrt convert it to USD if it is not in USD since USD is the base currency for conversion rate
        #this method takes arguments the currency you wan to convets from, the currency in which you wan tot convert, and the amount you wan to convert
        
        if from_currency != 'USD':
            amount = amount / self.currecies[from_currency]

        #limiting the precision to 4 decimal places
        amount = round(amount * self.currecies[to_currency], 4)

        """
        This method is not required for Godkänt (G) grade
                
        # # # # # # FÖR VÄL GODKÄND - VG REQUIREMENT # # #
        This method converts from any currency, to any currency
        This should not require any more requests (e.g you do not need to make another request with a different base currency)
        """
    
    def list_currencies(self):
        """
        This method lists available currencies in alphabetical order
        """
        pass
    
    def load_currency_data(self):
        """
        # # # # # FÖR GODKÄND - G REQUIREMENT # # # # #:
        This method should attempt to load currency data from a json-file.
        
        # # # # # FÖR ATT FÅ VÄL GODKÄNT - VG REQUIREMENT # # # # # #
        The function should look at the current time using the python datetime module (https://docs.python.org/3/library/datetime.html).
        If the saved data is older than more hour, it should automatically update the data being used and save it.
        This is possible by looking at the timestamp of the fetched data. You need to figure out yourself how this can be done.
        """
        pass

    def export_to_json(self):
        """
        This should export to JSON so that the application can be run again without the need to fetch new data
        """
        pass
    
def main():
    """
    This function should contain a menu allowing the user to
    [0] - (G) List all currencies
    [1] - (G) Convert USD to a currency of choice
    [2] - (G) Refresh the data (fetch new currency data, this is because the API updates new currency rates every hour)
    [3] - (G) Export the data to JSON
    [4] - (VG) Convert from any currency to any currency that is available on the API
    """
    pass
    
if __name__ == "__main__":
    #this is the main function
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    
    App(converter)
    main()
    #sync my chages to github
    
