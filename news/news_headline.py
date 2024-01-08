import requests 
from bs4 import BeautifulSoup 

# # 경제 분야 제목 크롤링
# URL = "https://www.ytn.co.kr/news/list.php?mcd=0102" 
# response = requests.get(URL) 
# soup = BeautifulSoup(response.text, 'html.parser') 

# til_contents = soup.find_all('span', class_='til')  # 'til' 클래스를 가진 'span' 태그를 모두 찾음

# for content in til_contents:
#     print(content.text)  # 각각의 내용을 출력

# 최신 분야 제목 크롤링
URL = "https://www.ytn.co.kr/news/list.php?mcd=recentnews" 
response = requests.get(URL) 
soup = BeautifulSoup(response.text, 'html.parser') 

til_contents = soup.find_all('span', class_='til')  # 'til' 클래스를 가진 'span' 태그를 모두 찾음

for content in til_contents:
    print(content.text)  # 각각의 내용을 출력