import csv
data = list(csv.reader(open("Stock Market Dataset.csv")))
def Nvidia_growth(data):
    #The percent growth of NVidia from 2019-2024
    top = float(data[1][27])
    last = float(data[-1][27])
    return(((top-last)/last)*100)
def Amazon_growth(data):
    #The percent growth of Amazon from 2019-2024
    top = float(data[1][33])
    last = float(data[-1][33])
    return(((top-last)/last)*100)
def NVidiaAmazonCompare(NVidiaGrowth,AmazonGrowth):
    #Compares the growth of NVidia and Amazon from 2019-2024
    if NVidiaGrowth > AmazonGrowth:
        return "Nvidia was better investment from 2019-2024"
    else:
        return "Amazon was a better investment from 2019-2024"
def AverageTechStock2022(data):
    #average stock price of the top 7 stocks at the end of 2022
    sum = 0
    for i in range(274,275):
        sum += (float(data[i][25]) + float(data[i][27]) + float(data[i][21]) + float(data[i][19]) + float(data[i][17]) + float(data[i][33]) + float(data[i][35]))
    return sum/(7)
def AverageTechStock2019(data):
    #average stock price of the top 7 stocks at the end of 2019
    sum = 0
    for i in range(1198,1199):
        sum += (float(data[i][25]) + float(data[i][27]) + float(data[i][21]) + float(data[i][19]) + float(data[i][17]) + float(data[i][33]) + float(data[i][35]))
    return sum/(7)
def TechStockpriceComparison(Average2022, Average2019):
    #Compares the average stock price of the top 7 tech stocks from 2019-2022
    if Average2022 > Average2019:
        return "The Technology sector performed well during covid (end of 2019 to end of 2022)"
    else:
        return "The Technology sector performed bad during covid (end of 2019 to end of 2022)"
def Commodities_growth(data):
    #The percent growth of the top 3 commodity stocks from 2022-2024
    top = (float(data[1][2]) + float(data[1][4]) + float(data[1][6]))/3
    last = (float(data[518][2]) + float(data[518][4]) + float(data[518][6]))/3
    return(((top-last)/last)*100)
def Crypto_growth(data):
    #The percent growth of the top 3 crypto stocks from 2022-2024
    top = (float(data[1][8].replace(",","")) + float(data[1][10].replace(",","")) + float(data[1][12].replace(",","")))/3
    last = (float(data[518][8].replace(",","")) + float(data[518][10].replace(",","")) + float(data[518][12].replace(",","")))/3
    return(((top-last)/last)*100)
def CommoditiesCryptoCompare(CommoditiesGrowth, CryptoGrowth):
    #Compares the growth of the commodities and crypto market from 2022-2024
    if dict["Percent commodity stock growth"] > dict["Percent crypto stock growth"]:
        return "The commodities market performed better from the begging of 2022 to the end of 2024"
    else:
        return "The crypto market performed better from the begging of 2022 to the end of 2024"
dict = {}
#Stores the results of the commodity and crypto growth functions
dict["Percent commodity stock growth"] = float(Commodities_growth(data))
dict["Percent crypto stock growth"] = float(Crypto_growth(data))
#Question 1:
print("Question 1:")
print("What was a better investment from 2019-2024, NVidia or Amazon?")
print("Nvidia growth from 2019 to 2024 is","%", Nvidia_growth(data))
print("Amazon growth from 2019 to 2024 is","%", Amazon_growth(data))
print(NVidiaAmazonCompare(Nvidia_growth(data),Amazon_growth(data)))
#Question 2:
print("Question 2:")
print("How did the Technology sector perform during covid (end of 2019 to end of 2022)?")
print("The average stock price in the Tech sector at the end of 2022 was:", AverageTechStock2022(data))
print("The average stock price in the Technology sector at the end of 2019 was:", AverageTechStock2019(data))
print(TechStockpriceComparison(AverageTechStock2022(data),AverageTechStock2019(data)))
#Question 3:
print("Question 3:")
print("From the beginning of 2022 to the end of 2024 how has the growth of the commodities market compared to that of the crypto market?")
print("The percent growth of the top 3 commodity stocks from 2022-2024 is","%",Commodities_growth(data))
print("The percent growth of the top 3 crypto stocks from 2022-2024 is","%",Crypto_growth(data))
print(CommoditiesCryptoCompare(dict["Percent commodity stock growth"],dict["Percent crypto stock growth"]))