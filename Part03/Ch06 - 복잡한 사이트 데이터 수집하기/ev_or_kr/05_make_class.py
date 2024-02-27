from bs4 import BeautifulSoup
import pprint
import pandas as pd
import openpyxl

if __name__ == '__main__':
    f = open("local_info.html", encoding="utf-8")
    page_string = f.read()

    ev_or_kr_parser = EvGoKrSubsidyParser(page_string)
    # collected_list = ev_or_kr_parser.parse()
    # pprint.pprint("======= collected_list:" + str(collected_list), width=400)
    ev_or_kr_parser.save_to_excel("all_sido.xlsx")
    # pprint.pprint(m, width=400)
