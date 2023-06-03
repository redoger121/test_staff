import requests
import codecs
from bs4 import BeautifulSoup as BS

# __all__ = ('',)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           }


def hh_ru(url, theme):
    errors = []
    jobs = []
    if url:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:

            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='a11y-main-content')
            if main_div:
                div_list = main_div.find_all('div', attrs={'class': 'serp-item'})
                for div in div_list:
                    title = div.find('a', attrs={'class': 'serp-item__title'})
                    href = title['href']
                    img = div.find('img', attrs={'class': 'vacancy-serp-item-logo'})


                    # content = div.find('div', attrs={'class': 'g-user-content'})
                    # print(content)
                    true_content = div.find('a', attrs={'class': "bloko-link"})
                    print(true_content.text)

                    company = div.find('div', attrs={'class': 'vacancy-serp-item__meta-info-company'})


                    pay = div.find('div', attrs={'class': 'vacancy-serp-item-body__main-info'})
                    real_pay = pay.find('span', attrs={'class': 'bloko-header-section-3'})

                    if img != None:
                        real_img=(img['src'])
                    else:
                        real_img=''

                    if hasattr(real_pay, 'text'):
                        true_pay = real_pay.text
                    else:
                        true_pay = 'Зарплата не указана'
                    jobs.append({'title': title.text,
                                 'href': href,
                                 'content': true_content.text,
                                 'company': company.text,
                                 'pay': true_pay, 'theme': theme,
                                 'img_href': real_img,})


        else:
            errors.append({'url': url, 'title': 'Page not response'})

        print(jobs)
    return jobs, errors


# def job_ru(url, theme):
#     errors = []
#     jobs = []
#     if url:
#
#         resp = requests.get(url, headers=headers)
#         if resp.status_code == 200:
#
#             soup = BS(resp.content, 'html.parser')
#             main_div = soup.find('div', attrs={'class':'span-mr-wrap vac-list'})
#
#             if main_div:
#
#                 div_list = main_div.find_all('section', attrs={'data-test': 'vacancies-list-item'})
#
#                 for div in div_list:
#                     span=div.find('span')
#                     span.decompose()
#                     title = div.find('a', attrs={'data-test': 'vacancy-item-header'})
#                     real_title=title.text
#                     pay=div.find('div', attrs={'class': 'span-m'})
#                     href = title['href']
#                     true_pay=pay.find('h3')
#                     true_pay2=true_pay.find('a')
#                     true_pay2.decompose()
#
#
#                     real_pay = pay.find('h3')
#
#                     content = div.find('div', attrs={'itemprop': 'description'})
#                     company = div.find('div', attrs={'class': 'company'})
#                     a_img=div.find('a', attrs={'class': 'logo'})
#
#
#                     if a_img!=None:
#                         img=a_img.find('img')
#                         real_img=(img['src'])
#                     else:
#                         real_img=''
#                     print(real_img)
#
#
#                     if hasattr(real_pay, 'text'):
#                         true_pay = real_pay.text
#                     else:
#
#                         true_pay = 'Зарплата не указана'
#                     jobs.append({'title':real_title,
#                                  'href': href,
#                                  'content': content.text,
#                                  'company': company.text,
#                                  'pay':true_pay,
#                                  'theme': theme,
#                                  'img_href': real_img,
#                                  })
#
#
#         else:
#             errors.append({'url': url, 'title': 'Page not response'})
#     return jobs, errors




# if __name__ == '__main__':
#     url = 'https://djinni.co/jobs/?keywords=Python'
#     h = codecs.open('../work.txt', 'w', 'utf-8')
#     h.write(str(jobs))
#     h.close()
