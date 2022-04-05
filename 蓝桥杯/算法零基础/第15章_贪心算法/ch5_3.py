""" 电台选择 """
def greedy(radios, cities):
    greedy_radios = set()  # 最终城市的选择
    while cities:  # 还有城市没有覆盖循环继续
        greedy_choose = None  # 最初化选择
        city_cover = set()  # 暂存
        for radio, area in radios.items():
            cover = cities & area
            if len(cover) > len(city_cover):
                greedy_choose = radio
                city_cover = cover
        cities -= city_cover
        greedy_radios.add(greedy_choose)
    return greedy_radios


cities = {'台北', '基隆', '桃园', '新竹', '台中', '嘉义', '台南', '高雄'}
radios = {}
radios['电台 1'] = {'新竹', '台中', '嘉义'}
radios['电台 2'] = {'基隆', '新竹', '台北'}
radios['电台 3'] = {'桃园', '台中', '台南'}
radios['电台 4'] = {'台中', '嘉义'}
radios['电台 5'] = {'台南', '高雄'}
a = greedy(radios, cities)
print(a)
