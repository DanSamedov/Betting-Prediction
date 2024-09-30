import requests
import time
import openpyxl as xl
from tqdm import tqdm


wb = xl.load_workbook('csfail_database_reverse.xlsx')
sheet = wb['Arkusz1']


rows_count = sheet.max_row
start_game = 2750000 
end_game = 5676636 - rows_count


for i in tqdm(range(end_game, start_game, -1)):
    time.sleep(1)
    api = requests.get(f'https://3cs.fail/api/crash/games/{i}')
    api = api.json()

    rows_count += 1
    items = ["crashedAt", "totalBankUsd", "usersCount", "itemsCount"]

    for item in items:
        value = api["data"]["game"][item]
        cell_print = sheet.cell(row=rows_count, column=items.index(item) + 1, value=value)

    wb.save('csfail_database_reverse.xlsx')