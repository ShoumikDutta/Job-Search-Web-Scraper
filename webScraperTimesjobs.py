from bs4 import BeautifulSoup
import requests
import pandas as pd
#keywords pattern: Keywords=python%2Cdjango%2Cjava
#each keyword sperated by %2C take user input and ask to sperate each keyword with comma than split and create a str and use f str to create the link
def main():
    df = getting_data()
    saving_data(df)

def user_input():
    inn=input("Enter keywords(please separate each keyword with comma): ")
    li=inn.strip(',')
    s=""
    for i,item in enumerate(li):
        if i == 0:
            s = s+item
        else:
            s = s+item+"%2C"
    return "Kewords="+s
def getting_data():

    df=pd.DataFrame()
    condition = True
    jobs_scaraped = 00.
    n=1
    while condition:
        html_text=requests .get(f'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence={n}&startPage=1').text
        n += 1
        #print(html_text)
        soup=BeautifulSoup(html_text,'lxml')
        total = int(soup.find('span', id="totolResultCountsId").text)
        #print(soup)
        jobs=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        jobs_scaraped+=len(jobs)
        print(jobs_scaraped)
        #dont use strong tag to get text use the tag before that
        for job in jobs:
            name=job.find('h2').text.strip()
            company=job.find('h3',class_="joblist-comp-name").text.strip()
            location=job.find('span').text.strip()
            skills=job.find('span',class_="srp-skills").text.strip()
            link = job.header.h2.a['href']
            dic = {'Position': name,
                   'Company': company,
                   'Location': location,
                   'Skills': skills,
                   'Link':link,}
            df = df.append(dic, ignore_index=True)
            df = df.reset_index(drop=True)


        if jobs_scaraped==total:
            condition=False
        else:
            condition=True

    return df

def saving_data(df):
    with pd.ExcelWriter('jobs.xlsx') as writer:
        df.to_excel(writer,sheet_name='data')

    print("writing done")


if __name__ == '__main__':
    main()


