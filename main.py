import logging
import os
from datetime import timedelta
import pandas as pd
import numpy as np
from decimal import Decimal
from utils import utils

PATH = './data'
INTERVAL = 5
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

def main():

    # прочитать имена файлов в PATH и отсортировать
    files = os.listdir(PATH)
    files.sort()

    dataframe = pd.DataFrame
    prev_symbol = ''

    # обработка каждого файла
    for file in files:
        # получаем символ (APEUSDT, DOTUSDT и тд) и дату начала файла
        (symbol, date_start) = utils.get_file_data(file)

        # добавляем к набору данных новый файл (если предыдущий был с таким же символом)
        if symbol == prev_symbol:
            dataframe = pd.concat([dataframe, pd.read_csv('/'.join([PATH, file]))], ignore_index = True)
            continue

        # в DataFrame уже содержатся элементы (подгруженные по предыдущему символу)
        if isinstance(dataframe.size, np.int64):
            # количество знаков после запятой
            prescision = utils.get_precision(dataframe['price'][0])

            # первый интервал выборки
            (timestamp_start, timestamp_end, timestamp_file_finish) = utils.get_interval(date_start, INTERVAL)

            while timestamp_end <= timestamp_file_finish:
                # фильтруем по time, выбираем кусок данных за интервал
                filtered_df = dataframe[(dataframe.time >= timestamp_start) & (dataframe.time < timestamp_end)] 
                [['price', 'time', 'qty', 'is_buyer_maker']]


        
        
        # читаем csv как DataFrame
        dataframe = pd.read_csv('/'.join([PATH, file]))
        prev_symbol = symbol
        
        # # количество знаков после запятой
        # prescision = utils.get_precision(dataframe['price'][0])

        

        # # первый интервал выборки
        # (timestamp_start, timestamp_end, timestamp_file_finish) = utils.get_interval(date_start, INTERVAL)

        # while timestamp_end <= timestamp_file_finish:
        #     # фильтруем по time, выбираем кусок данных за интервал
        #     filtered_df = dataframe[(dataframe.time >= timestamp_start) & (dataframe.time < timestamp_end)] 
        #     [['price', 'time', 'qty', 'is_buyer_maker']]

        #     # посмотреть min и max и разметить массив
        #     min = Decimal(str(filtered_df['price'].min()))
        #     max = Decimal(str(filtered_df['price'].max()))
        #     string_step = '0.' + '0' * (prescision - 1) + '1'
        #     step = Decimal(string_step)

        #     array_length = int((max - min) / step)
            

        #     print(array_length)
        

if __name__ == "__main__":
    main()
