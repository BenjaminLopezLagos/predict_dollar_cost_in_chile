import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import sys

# Dictionary to map abbreviated month names to month numbers
month_map = {
    "Ene.": "01",
    "Feb.": "02",
    "Mar.": "03",
    "Abr.": "04",
    "May.": "05",
    "Jun.": "06",
    "Jul.": "07",
    "Ago.": "08",
    "Sep.": "09",
    "Oct.": "10",
    "Nov.": "11",
    "Dic.": "12"
}

def parse_date(date_str):
    # Split the input string into month and year
    month_abbr, year = date_str.split(".")
    # Get the month number from the dictionary
    month = month_map[month_abbr + "."]
    # Create a datetime object
    date_obj = datetime.strptime(f"{year}-{month}-01", "%Y-%m-%d")
    return date_obj

def main(storage_path):
    r = requests.get(f'https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_TIPO_CAMBIO/MN_TIPO_CAMBIO4/TC_HIST/TC_HIST?cbFechaInicio={1970}&cbFechaTermino={datetime.now().year}&cbFrecuencia=MONTHLY&cbCalculo=NONE&cbFechaBase=')
    soup = BeautifulSoup(r.content,'lxml')
    print(soup)
    table = soup.find('table')
    usd_cost = table.find_all('td')
    dates = table.find_all('th')

    stored_dates = []
    stored_costs = []

    for cost, date in zip(usd_cost, dates):
        try:
            processed_cost = float(str.replace(cost.text, ',', '.'))
            processed_date = parse_date(date.text)
            stored_dates.append(processed_date)
            stored_costs.append(processed_cost)
        except:
            print('invalid row')

    df = pd.DataFrame({'periodo': stored_dates, 'pesos por dolar': stored_costs})
    df.to_csv(f'{storage_path}/data.csv', ',')

if __name__ == '__main__':
    where_to_store = sys.argv[1]
    main(where_to_store)