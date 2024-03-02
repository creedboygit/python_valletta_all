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

        # print("======= self.brands:\n" + str(self.brands), len(self.brands))
        # print("======= self.partners:\n" + str(self.partners), len(self.partners))
        #
        # print(self.brands[0], self.partners[0])
        # print(self.order_list.head())
        # print(self.order_list['상품명'].head())

    def classify(self):
        # for i, row, in self.order_list.iterrows():
        for i, row, in self.order_list.head(5).iterrows():
            brand_name = ""
            idx_partner = 0
            for j in range(len(self.brands)):
                # print(self.brands[j])
                if self.brands[j] in row['상품명']:
                    # print(f"{self.brands[j]}이(가) {j}번째에 포함되어 있습니다.")
                    brand_name = self.brands[j]
                    idx_partner = j
                    break
            print(f"{row['상품명']} 은 {brand_name} 브랜드입니다. {j}번째")
            print(f"업체명: {self.partners[idx_partner]}")

            # print("-----------------")
            # print(row)
            # print(row['상품명'])

        print("======= self.brands:\n" + str(self.brands), len(self.brands))
        print("======= self.partners:\n" + str(self.partners), len(self.partners))


if __name__ == '__main__':
    ce = ClassificatinoExcel("주문목록20221112.xlsx", "파트너목록.xlsx")
    ce.classify()
