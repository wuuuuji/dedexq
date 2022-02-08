import hashlib

month_dict: dict = {'january': '一月', 'february': '二月', 'march': '三月',
                    'april': '四月', 'may': '五月', 'june': '六月',
                    'july': '七月', 'august': '八月', 'september': '九月',
                    'october': '十月', 'november': '十一月', 'december': '十二月'}
mon = input('请输入月份: ').lower()
if mon in month_dict:
    print('{} 的中文是 {}'.format(mon, month_dict[mon]).title())
else:
    print('{} 拼写错误 '.format(mon))