import xlrd

# 参照情報(フォルダパス、参照期間)
folderPath = []
startDay = []
endDay = []

preferenceFile = open('reference.txt', 'r')
textLines = preferenceFile.readlines()   

# 1つ目の参照情報取得
folderPath.append(textLines[1])
startDay.append(textLines[4])
endDay.append(textLines[5])

# 2つ目の参照情報取得
if not textLines[8]:
    folderPath.append(textLines[8])
    startDay.append(textLines[11])
    endDay.append(textLines[12])



preferenceFile.close