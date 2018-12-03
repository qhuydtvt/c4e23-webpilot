from urllib.request import urlopen
from bs4 import BeautifulSoup

from collections import OrderedDict
import pyexcel

#1. Connect to the page
url = "https://dantri.com.vn"
conn = urlopen(url)

#2. Download the page content
raw_data = conn.read()
page_content = raw_data.decode("utf8")

# with open("dantri.html", "wb") as f:
#   f.write(raw_data)

#3. Find ROI region
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew") # href="", id=""

#4. Extract data

li_list = ul.find_all("li")
news_list = []
for li in li_list:
  a = li.h4.a
  title = a.string
  link = url + a["href"]

  news = OrderedDict({
    "title": title,
    "link": link,
  })
  news_list.append(news)

#5. Save data
pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")