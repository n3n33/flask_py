from bs4 import BeautifulSoup
import requests

def remote_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    # write your ✨magical✨ code here
    table = soup.find('table',id='jobsboard')
    rows = [x for x in table.find_all('tr')]
    for row in rows[2:]:
      for column in row.find_all('td')[:2]:
        text =', '.join(x.strip() for x in column.text.split('\n') if x.strip()).strip()
        print(text)
    return text
  else:
    text_log = "Can't get jobs."
    return text_log
    
    
def wework_job(term):
  url = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={term}"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    # write your ✨magical✨ code here
    rows = soup.find_all('div',attrs={"class" : "jobs-container"})
    for row in rows:
      text ='\n '.join(x.strip() for x in row.text.split('\n') if x.strip()).strip()
      print(text)
    return text
  else:
    text_log = "Can't get jobs."
    return text_log
