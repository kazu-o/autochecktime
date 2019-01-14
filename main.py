import glob
import xlrd

# 参照情報(フォルダパス、参照期間)
folderPaths = []
startDays = []
endDays = []

preferenceFile = open('reference.txt', 'r')
textLines = preferenceFile.readlines()   

# 1つ目の参照情報取得
folderPaths.append(textLines[1])
startDays.append(textLines[4])
endDays.append(textLines[5])

# 2つ目の参照情報取得
if not textLines[8]:
    folderPaths.append(textLines[8])
    startDays.append(textLines[11])
    endDays.append(textLines[12])

preferenceFile.close


# セルの値クリア

# 期間入力


# パスから勤務表ファイル名取得
for folderPath in folderPaths
    workFilesName = glob.glob(folderPath + '*.xlsx')

    # 勤務表から作業時間取得
    for workFileName in workFilesName
        workFile = xlrd.open_workbook(workFileName)
        workSheet = workFile.sheet_by_name('作業時間')


# 名前取得
    # 名前変換
# 時間取得
    # 表記変更
# 表示

# redmineでも同様

# 一括表示
# 自動チェックして不一致のみ表示