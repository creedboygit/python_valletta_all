from bs4 import BeautifulSoup
import pprint
import pandas as pd
import openpyxl


def is_list(l, i):
    if not l:
        res = ""
    else:
        res = int(l[i])

    return res


def form(a, b, c, d, e):
    # print("======= len(e): " + str(len(e)))
    return {"sido": a, "region": b, "sep1": c, "sep2": d, "value": e}


# tr을 넘기면 [{}, {}, {}]
def parse_tr(tr):
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


if __name__ == '__main__':
    f = open("local_info.html", encoding="utf-8")
    page_string = f.read()
    soup = BeautifulSoup(page_string, "html.parser")
    table = soup.find("table", {"class": "table01 fz15"})
    trs = table.find("tbody").find_all("tr")

    # print("======= trs: " + str(trs))

    # for tr in trs[3:4]:
    # for tr in trs[:30]:
    # for tr in trs:

    m = []
    # for tr in trs[3:4]:
    for tr in trs:
        # print("======= tr: " + str(tr))

        row = parse_tr(tr)
        # pprint.pprint(row)
        # print("======= row: " + str(row))
        m += row

    # pprint.pprint(m, width=400)

    df = pd.DataFrame(m)
    print("======= df:\n" + str(df))
    df.to_excel("all_sido.xlsx")
