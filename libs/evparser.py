from bs4 import BeautifulSoup
import pandas as pd


# import openpyxl


class EvGoKrSubsidyParser:
    trs = []

    def __init__(self, html_text):
        soup = BeautifulSoup(html_text, "html.parser")
        table = soup.find("table", {"class": "table01 fz15"})
        self.trs = table.find("tbody").find_all("tr")

    # tr을 넘기면 [{}, {}, {}]
    def parse_tr(self, tr):
        # tr = trs[2]

        tds = tr.find_all("td")

        sido = tds[0].text
        region = tds[1].text

        replace_brackets = lambda x: x.replace("(", "").replace(")", "").split(" ")[1:]
        # form = lambda a, b, c, d, e: {"sido": a, "region": b, "sep1": c, "sep2": d, "value": e}

        민간공고대수 = replace_brackets(tds[5].text)
        접수대수 = replace_brackets(tds[6].text)
        출고대수 = replace_brackets(tds[7].text)
        출고잔여대수 = replace_brackets(tds[8].text)

        # print("======= 민간공고대수: " + str(민간공고대수[0]))

        l = [
            form(sido, region, "민간공고대수", "우선순위", is_list(민간공고대수, 0)),
            form(sido, region, "민간공고대수", "법인및기관", is_list(민간공고대수, 1)),
            form(sido, region, "민간공고대수", "택시", is_list(민간공고대수, 2)),
            form(sido, region, "민간공고대수", "일반", is_list(민간공고대수, 3)),
            form(sido, region, "접수대수", "우선순위", is_list(접수대수, 0)),
            form(sido, region, "접수대수", "법인및기관", is_list(접수대수, 1)),
            form(sido, region, "접수대수", "택시", is_list(접수대수, 2)),
            form(sido, region, "접수대수", "일반", is_list(접수대수, 3)),
            form(sido, region, "출고대수", "우선순위", is_list(출고대수, 0)),
            form(sido, region, "출고대수", "법인및기관", is_list(출고대수, 1)),
            form(sido, region, "출고대수", "택시", is_list(출고대수, 2)),
            form(sido, region, "출고대수", "일반", is_list(출고대수, 3)),
            form(sido, region, "출고잔여대수", "우선순위", is_list(출고잔여대수, 0)),
            form(sido, region, "출고잔여대수", "법인및기관", is_list(출고잔여대수, 1)),
            form(sido, region, "출고잔여대수", "택시", is_list(출고잔여대수, 2)),
            form(sido, region, "출고잔여대수", "일반", is_list(출고잔여대수, 3)),
        ]

        # print("======= l: " + str(l))

        return l

    def parse(self):
        collected_list = []
        for tr in self.trs:
            row = self.parse_tr(tr)
            collected_list += row
        return collected_list

    def save_to_excel(self, excel_filename):
        collected_list = self.parse()
        df = pd.DataFrame(collected_list)
        print("======= df:\n" + str(df))
        df.to_excel(excel_filename)


def is_list(list_i, i):
    if not list_i:
        res = ""
    else:
        res = int(list_i[i])

    return res


def form(a, b, c, d, e):
    # print("======= len(e): " + str(len(e)))
    return {"sido": a, "region": b, "sep1": c, "sep2": d, "value": e}
