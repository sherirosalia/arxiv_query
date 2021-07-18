
from encodings import utf_8
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import quote
# from pprint import pprint
import pandas as pd
import time
# import data

#establish global variable to be utilized by both functions
arxiv_results=None

def arxiv_reload(search_terms):
    # "remind" python of global variable
    global arxiv_results

    # search_terms = data.open_json('data.json')

    # print(search_terms)
    # api parameters:
    # key terms to search
    # search_terms=['fungus', 'mushroom']
    # search_terms=['homeopathic','diabetes treatment', 'diabetic', 'herbal remedies', 'insulin', 'metabolic syndrome', 'fluffernuttter', 'plant medicine', 'blood sugar']
    # search_terms=['homeopathic','diabetes treatment', 'herbal remedies', 'insulin', 'metabolic syndrome', 'fluffernuttter']
    # range of results
    start_num=0
    max_results=10
    # master list of results
    arxiv_results=[]
    # count to be used as an identity index for all results
    results_count=0
    wait_time=3
    # master loop allowing each search term to be appended 
    for search_term in search_terms:
        # assign search term as a string
        key_search = search_term
        # increment results count
        results_count += 1
        # encode parameters for interpretability for the api
        search_term=quote(search_term)
        # url with parameters
        url= f'http://export.arxiv.org/api/query?search_query=all:{search_term}&start={start_num}&max_results={max_results}'
        # request url response
        response = requests.get(url)
        # verify 200 response
        # print(response)

        # xml beautiful soup text parse
        arxiv_xml =(bs(response.text, 'lxml'))
        # pprint(arxiv_xml)
        # create variables to hold extracted information from xml in list form for debugging
        # titles_list = []
        # authors_list = []

        # counter to serve as an ID indext type column
        entry_counter = 0
        # polite pause and print statement
        wait_time=1
        # print('Sleeping for %i seconds' % wait_time)
        time.sleep(wait_time)
        # loop through entries in response
        for entries in arxiv_xml:
            # response includes all entries in range - xml format
            entries=arxiv_xml.find_all('entry')
            # print(entries)
            # isolate individual entries to extract individual data points 
            for entry in entries:
                
                if entry is not None:
                    #index
                    entry_counter += 1
                    #extract title text
                    title = entry.find('title').text
                    # titles_list.append(title)

                    # url link 
                    link = entry.find('id').text
                    # multiple authors within multiple author tags
                    authors_string = ''
                    authors = entry.find_all('author')
                    for author in authors:
                        author = author.text.replace('\n',' ')
                        author = f'{author.strip()}, '
                        authors_string += ''.join(author)
                    #list option / debugging
                    # authors_list.append(authors_string)

                    # abstract held in summary tags
                    summary=entry.find('summary')
                    if summary is not None:
                        summary = summary.text
                        summary = summary.replace('\n', ' ')
                    # print(f'ENTRY number: {entry_counter}------------title: {title} ------author: {authors_string} -----key search = {key_search}')
                    authors_string = authors_string.rstrip(', ","')
                    arxiv_dict= {
                        'id' : entry_counter,
                        'search_term' : key_search,
                        'title' : title,
                        'url'  : link,
                        'author' : authors_string, 
                        'abstract' : summary,
                    }
                    # print(arxiv_dict)
                
                    arxiv_results.append(arxiv_dict)


                
    # print(arxiv_results)
    df=pd.DataFrame(arxiv_results,) 
    # data=df.to_html(classes='table') 
    # df.to_csv('arxiv.csv', index=None)

                


       
            
arxiv_reload(['fungus', 'mushroom'])           
             
def data_frame():
    # remind python of global
    global arxiv_results
    df=pd.DataFrame(arxiv_results)
    return df
                    
# print(data_frame())



    # json style dictionary
    # arxiv_dict= {
    #     'id' : results_count,
    #     'search_term' : key_search,
        
        

    # }

    # append to master list outside of loop
    # arxiv_results.append(arxiv_dict)

# print list of results
# print(arxiv_results)


# results_list=[]
# search_number=0
# # print(url_list)
# for link in url_list:
#     search_number+=1
#     response = requests.get(link)
#     soup=(bs(response.text, 'lxml'))
#     # print(soup)
#     print(len(soup))



    

    # for terms in soup:
    #     entry=terms.find('entry')
    #     entry=entry.text

    #     print(terms)
        # author=term.find('author')
        # if author is not None:
        #     author = author.text
        #     author = author.strip('\n')
        #     print(author)


        # for author in authors:
        #     if author is not None:
        #         author = author.text
        #         author = author.strip('\n')
        # for summary in summaries:
        #     if summary is not None:
        #         summary = summary.text
        #         summary = summary.replace('\n', ' ') 
        
    
    # for author in authors:
    #     if author is not None:
    #         author = author.text
    #         author = author.strip('\n')  
    # for summary in summaries:
    #     if summary is not None:
    #         summary = summary.text
    #         summary = summary.replace('\n', ' ') 
        
    # summaries = soup.find_all('summary')
    # for summary in summaries:
    #     if summary is not None:
    #         summary = summary.text
    #         summary = summary.replace('\n', ' ')
#     arxiv_dict={'author': author,
#                 'abstract':summary,
                    
#         }
#     results_list.append(arxiv_dict)
# print(results_list)
# df=pd.DataFrame(results_list)
# df.to_csv('test.csv')
#     summaries = soup.find_all('summary')
#     for summary in summaries:
#         if summary is not None:
#             summary = summary.text
#             summary = summary.replace('\n', ' ')

#     # result_urls = soup.find_all('id')
#     updates = soup.find_all('updated')
#     publishings = soup.find_all('published')
#     entries = soup.find_all('entry')


#     for entry in entries:
#         if entry is not None:
#             split_up=entry.text.split('\n')
#             title=split_up[4]
#             result_url=split_up[1]
        
#     # for result_url in result_urls:
#     #     if result_url is not None:
#     #         result_url = result_url.text
#     for update in updates:
#         if update is not None:
#             update= update.text
#     for published in publishings:
#         if published is not None:
#             published= published.text

#         results_dictionary = {
#                 'title' : title,
#                 'author' : author,
#                 'search term': search_number,
#                 'url' : result_url,
#                 'published' : published,
#                 'update' : update,
#                 'abstract' : summary,
#             }
#         results_list.append(results_dictionary)
# df=pd.DataFrame(results_list)
# print(df)


# # pprint(results_list)
# keys=results_list[0].keys()
# # print(keys)
# # with open('diabetes_treatment_6_24.csv', 'w', encoding='utf8', newline='') as output_file:
# #     csv_rows= csv.DictWriter(
# #         output_file, fieldnames=results_list[0].keys(),
# #     )
# #     csv_rows.writeheader()
# #     csv_rows.writerows(results_list)


    
#     # print(soup)
# #     archive_results.append(soup)


# #     for data in soup:
# #         # entry=data.find('entry')
            
# #         author=data.find('author')
# #         print(author)
# #         # archive_results.append(author)
# #         # split_up=entry.text.split('\n')
# #         # url_id=split_up[1]
# #         # publishing_date=split_up[3]
# #         # title=split_up[4]
# #         # summary=data.find('summary')
# #         # print(summary.text)
# #         # print(author.text)
# print(results_count)
    





    