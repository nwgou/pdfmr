import openpyxl

def merge_excel(book,result_list,temp_file):
    try:
        #書き込み対象シート選択
        sheet = book['請求書一覧']
        index = 6
        for i in range(len(result_list)):
            allText = result_list[i].split("\n\n")
            _, seikyu_no = allText[3].split()
            company_name = allText[4]
            _, bill = allText[7].split(" ")
            _, meigi = allText[24].split("：")
            kouza = allText[25]

        #値をセルにセット
        cell_b = 'B' + str(index+i)
        cell_c = 'C' + str(index+i)
        cell_d = 'D' + str(index+i)
        cell_e = 'E' + str(index+i)
        cell_f = 'F' + str(index+i)

        sheet[cell_b] = seikyu_no
        sheet[cell_c] = company_name
        sheet[cell_d] = bill
        sheet[cell_e] = meigi
        sheet[cell_f] = kouza

        #保存
        book.save(temp_file)
    except Exseption as e:
        err_message = "Excelファイルへのデータ転記処理でエラーが発生しました。<br>\
        アップロードしたPDFファイルが正しいフォーマットか確認してください。<br>\
        エラーメッセージ：" + str(e)
        return err_message