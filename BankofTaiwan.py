# coding=UTF8
import pandas as pd


def rates():
    dfs = pd.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
    BotRates = dfs[0]
    BotRates = BotRates.iloc[:, 0:5]
    BotRates.columns = ['Currency', 'CashBuying', 'CashSelling', 'SpotBuying', 'SpotSelling']
    BotRates['Currency'] = BotRates['Currency'].str.extract('\((\w+)\)')
    BotRates = BotRates.set_index(['Currency'])
    RatesDict = BotRates.to_dict()
    # 移除價位為 - 之報價
    for key, vdict in RatesDict.items():
        for k, v in list(vdict.items()):
            if v == '-':
                print('{}: {}'.format(k, v))
                del vdict[k]
    return RatesDict
