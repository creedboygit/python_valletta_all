import pandas as pd


class ClassificatinoExcel:
    def __init__(self, order_xlsx_filename, partner_info_xlsx_filename):
        # 주문 목록
        df = pd.read_excel(order_xlsx_filename)
        df = df.rename(columns=df.iloc[1])  # 열 제목으로 1번째를 지정
        df = df.drop([df.index[0], df.index[1]])
        # print("======= df.count():\n" + str(df.count()))
        # print(df['상품명'])

        df = df.reset_index(drop=True)
        self.order_list = df
        # print(df)

        # 파트너 목록
        df_partners = pd.read_excel(partner_info_xlsx_filename)
        # print(df_partners)
        self.brands = df_partners['브랜드'].to_list()
        self.partners = df_partners['업체명'].to_list()

        print("======= self.brands:\n" + str(self.brands), len(self.brands))
        print("======= self.partners:\n" + str(self.partners), len(self.partners))

        print(self.brands[0], self.partners[0])
        print(self.order_list.head())
        print(self.order_list['상품명'].head())

    def classify(self):
        for i, row, in self.order_list.iterrows():
            print(i)


if __name__ == '__main__':
    ce = ClassificatinoExcel("주문목록20221112.xlsx", "파트너목록.xlsx")
    ce.classify()
