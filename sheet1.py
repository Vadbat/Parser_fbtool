import gspread
from oauth2client.service_account import ServiceAccountCredentials
from parserFB import Parser_fb

# Замените 'path/to/your/credentials.json' путем к вашему файлу JSON с учетными данными
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# Замените 'Your Spreadsheet Name' на имя вашей таблицы
spreadsheet = client.open('CR 2.0')

for data in Parser_fb.db_fb:
    # print(data)
    # if data[0] in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"}:
        # sheet_number = int(data[0][0])
    sheet_index = int(data[0])
    sheet_index1 =sheet_index - 1
    worksheet = spreadsheet.get_worksheet(sheet_index1)
    # worksheet = spreadsheet.sheet1  # Or use another sheet as needed
    all_values = worksheet.get_all_values()

    column_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

    column_key = data[2]

    if column_key in column_mapping:
        empty_row_index = len(all_values) + 1
        for i, row in enumerate(all_values):
            if not any(row[:6]):  # If columns A-F are empty
                empty_row_index = i + 1
                break

        worksheet.update_cell(empty_row_index, column_mapping[column_key], data[3])
        worksheet.update_cell(empty_row_index, 7, data[1])
    else:
        print('Такого значения нет')
    # else:
    #     print(f'Некорректное значение для {data[0]}')