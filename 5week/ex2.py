import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

data = {
    'name': ['여자친구', '소녀시대', '레드벨벳', '에이핑크', '마마무', '트와이스', '블랙핑크', '오마이걸', '있지', '우주소녀'],
    'address': ['경기', '서울', '경북', '경기', '전남', '서울', '경남', '서울', '경남', '서울'],
    'youtube_count': [800, 1114600, 44500, 2900, 6900, 3334500, 443700, 3500, 21300, 350]
}

df = pd.DataFrame(data)


def addtext(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] + 0.5, y[i], ha='center')

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font',family=font_name)


plt.figure(figsize=(15, 10))
plt.bar(df['name'], df['youtube_count'], color=('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple', 'cyan', 'magenta', 'gray'))
plt.title('singer_youtube.csv')
plt.xlabel('그룹 이름')
plt.ylabel('유튜브 구독자 수')


addtext(df['name'], df['youtube_count'])


plt.show()
