import time
import MostActiveRun
import DataFinder
import FileFormatting
import Tabulation

MostActiveRun.most_active_run()
time.sleep(15)
FileFormatting.file_formatting()
time.sleep(5)
comparison_dict = {}
tickers = open("FILE_COMPANY_NAME_Main.txt","r")
for ticker in tickers:
    time.sleep(5)
    open, prev_close, current_stock_price = DataFinder.stock_data_finder(ticker)
    print(open,prev_close,current_stock_price)
    print(f"ticekr symbol is {ticker[:-1]}")
    final_score = Tabulation.tabulation_output(open,prev_close,current_stock_price)
    if final_score > 0:
        comparison_dict.update({ticker[:-1]:final_score})

comparison_dict_keys = list(comparison_dict.keys())
comparison_dict_keys.sort()
sorted_dict = {i : comparison_dict[i] for i in comparison_dict_keys}
print(sorted_dict)