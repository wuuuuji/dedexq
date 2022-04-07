def greedy(radios, cities):
    greedy_radios = set()
    while cities:
        greedy_choose = None
        city_cover = set()
        for radio, area in radios.items():
            cover = cities & area
            if len(cover) > len(city_cover):
                greedy_choose = radio
                city_cover = cover
        cities -= city_cover
        greedy_radios.add(greedy_choose)
    return greedy_radios


cities = {'台北', '基隆', '桃园',
          '新竹', '台中', '嘉义',
          '台南', '高雄', '花莲',
          '云林', '台东', '南投', '苗粟'}
radios = {}
radios['电台 1'] = {'新竹', '台中', '嘉义'}
radios['电台 2'] = {'基隆', '新竹', '台北'}
radios['电台 3'] = {'桃园', '台中', '台南'}
radios['电台 4'] = {'台中', '南投', '嘉义'}
radios['电台 5'] = {'台南', '高雄', '屏东'}
radios['电台 6'] = {'宜兰', '花莲', '台东'}
radios['电台 7'] = {'苗粟', '云林', '嘉义', '南投'}
a = greedy(radios, cities)
print(a)
