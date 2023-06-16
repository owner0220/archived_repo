#웹브라우져 실행하기
import webbrowser


q_list = ["a","b","c","d"]
url="https://www.google.com/search?q="

for q in q_list:
    webbrowser.open(url+q)

#webbrowser.open(url)          ����â�� �� URL�� ������
#webbrowser.open_new(url)      ???
#webbrowser.open_new_tab(url)  �� �ǿ� �� URL�� ������