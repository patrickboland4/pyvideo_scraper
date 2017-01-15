from lxml import html
import requests
import urllib
from bs4 import BeautifulSoup, SoupStrainer
import requests
import pytube


vld = {'https://www.youtube.com/watch?v=UJdPBKCPDnw': ['What happened at aaronswhack', 'Nov 18, 2013'], 'https://www.youtube.com/watch?v=jMgRUI7V_mk': ['Asynchronous IO in Python 3', 'Jul 12, 2013'], 'https://www.youtube.com/watch?v=Peww9AUH6yM': ['Ultimate Language Shootout IV - QUASI', 'Jun 17, 2013'], 'https://www.youtube.com/watch?v=-PbcJjr_SFE': ['CivicLab and Between the Bars', 'Nov 18, 2013'], 'https://www.youtube.com/watch?v=kXoSASlq7zU': ['In-project virtualenvs', 'Jun 26, 2013'], 'https://www.youtube.com/watch?v=a7Oon2Bo8tE': ['Intro to Marmir - Spreadsheets on steroids', 'Jan 11, 2013'], 'https://www.youtube.com/watch?v=MN1y5lvSHQ8': ['There were 986 roadway fatalities in Illinois in 2013 Wheres the data', 'Apr 3, 2014'], 'https://www.youtube.com/watch?v=-0P5EvYI0Rk': ['Set it and forget it! Auto Scale on Rackspace', 'Sep 14, 2013'], 'https://www.youtube.com/watch?v=A_C4Z4RDDgI': ['Measure It', 'Apr 3, 2014'], 'https://www.youtube.com/watch?v=GiUPv2Q01lw': ['Lidless -  A Video Analyzer and IRC Bot', 'Nov 11, 2011'], 'https://www.youtube.com/watch?v=fbQvWcrOwUw': ['Python 330 Release', 'Oct 12, 2012'], 'https://www.youtube.com/watch?v=I7B2BtgjfgY': ['PyData Recap Lightning Talk', 'Oct 16, 2015'], 'https://www.youtube.com/watch?v=Qu6MVLnt2D8': ['Whats Love Got to do with It  Love - for techies', 'Sep 14, 2013'], 'https://www.youtube.com/watch?v=EEwufSsx4O8': ['November 2014 Chipy - Hidden Markov Models & Innate learning - Chicago Python User Group', 'Dec 6, 2014'], 'http://www.youtube.com/watch?v=bpZS9ehw98k': ['Python For Humans', 'Dec 13, 2014'], 'https://www.youtube.com/watch?v=lX1tFs6mtvk': ['Matplotlib Examples Uses', 'Sep 17, 2012'], 'https://www.youtube.com/watch?v=ja-iZG610o8': ['Storm (with python (and a side of clojure))', 'Apr 3, 2014'], 'https://www.youtube.com/watch?v=MrEoE0Py5ZY': ['MediaGoblin Update', 'Oct 12, 2012'], 'https://www.youtube.com/watch?v=cj-DTFmIUjE': ['Lexical Graphs with Natural Language Processing using NLTK', 'Oct 16, 2015'], 'https://www.youtube.com/watch?v=oH_cEl2SMr8': ['Ultimate Language Shootout IV - CoffeeScript', 'Jun 14, 2013'], 'https://www.youtube.com/watch?v=u2ujTHH40nw': ['open science', 'Feb 19, 2013'], 'https://www.youtube.com/watch?v=SB9TWabor1k': ['Hy - A Lisp that transforms itself into the Python AST', 'Oct 16, 2015'], 'https://www.youtube.com/watch?v=f1FoYwe_DT4': ['Post djangocon - An overview of edX', 'Sep 14, 2013'], 'https://www.youtube.com/watch?v=wNRb2P9bjTc': ['Open Government Data Movement', 'Jun 17, 2012'], 'https://www.youtube.com/watch?v=c5MPg88mdgc': ['Ultimate Language Shootout IV - Haskell or - How a List Comprehension Is Like a Burrito', 'Jun 17, 2013'], 'https://www.youtube.com/watch?v=50qhv8C3s9I': ['Monoids in Python', 'Nov 18, 2013'], 'https://www.youtube.com/watch?v=bWk0P7w2aZg': ['Scraping with Python', 'Feb 19, 2013'], 'https://www.youtube.com/watch?v=AxM9Qe6shoU': ['Python powered search', 'Jun 15, 2012'], 'https://www.youtube.com/watch?v=dFyD8--zs84': ['Genie', 'Jan 11, 2013'], 'https://www.youtube.com/watch?v=RLRDnC9SQWk': ['How Open Source Hardware Will Change the World', 'Apr 3, 2014'], 'https://www.youtube.com/watch?v=VCeENPxyZJw': ['Garbage Collection w Ref Cycles', 'Oct 16, 2015'], 'https://www.youtube.com/watch?v=NP0-Df2tISA': ['Ultimate Language Shootout IV - Ruby', 'Jun 17, 2013'], 'https://www.youtube.com/watch?v=Aec6HTVv5EM': ['Ultimate Language Shootout IV - Go - come drink the delicious kool-aid', 'Jun 17, 2013'], 'https://www.youtube.com/watch?v=fByR4ghTOS8': ['Ultimate Language Shootout IV - C is slightly better than you might imagine', 'Jun 17, 2013'], 'https://www.youtube.com/watch?v=eBTRRVr3AIQ': ['The Chicago Process - How Braintree Develops Software', 'Apr 3, 2014'], 'https://www.youtube.com/watch?v=oy57f4evyO4': ['SQLAlchemy - As She is Code an opinionated Intro', 'Dec 15, 2012'], 'https://www.youtube.com/watch?v=7Lwlo42j6aA': ['Big Data De-Duping', 'Jun 15, 2012'], 'https://www.youtube.com/watch?v=upw-AIzWcfQ': ['ipython  notebook demo', 'Jul 12, 2013'], 'https://www.youtube.com/watch?v=2gcrTsQ7yi4': ['Event Driven Concurrency', 'Sep 17, 2012']}



############ start point - collect links from pyvideo-chipy ############
url = 'http://pyvideo.org/events/chipy.html'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'lxml')
all_links = soup.find_all('a')
################################################


########### grab additional embedded links ###########
'''
for link in all_links:
    if link redirects to youtube:
        Does the video exist in vdl.keys()?
'''

#all_links carries every link with 'a' tag from the url
#   'a' tags will correspond to href references in next iteration
for link in all_links:
    print('\n')
    e0 = link.get('href')
    print('Found the URL in all_links:', e0)

    '''
    link =
    http://pyvideo.org/pages/thanks-will-and-sheila.html
    http://pyvideo.org/
    http://pyvideo.org/chipy/chipy-python-mentorship.html
    http://pyvideo.org/chipy/chipy-python-mentorship.html
    http://pyvideo.org/events/chipy.html

    within these, must generate a new page
        within these, if youtube href, grab link
    '''

    try:
        #open an embedded link
        e0_page = urllib.request.urlopen(e0)

        #make soup out of the embedded page
        e0_soup = BeautifulSoup(e0_page, 'lxml')

        #get all 'a' tags from the embedded page
        e0_all_links = soup.find_all('a')


        for e1_page in e0_all_links:
            href = e1_page.get('href')
            #chipy py video all links
            #   all hrefs inside of all those links
            # print(href)

            # for yt_link in href:
            #     print(yt_link)
            print("Working on the %s in embedded1 inside of %s in embedded0" % (e1_page, link.get('href')))
            # if 'yout' in href.string:
            #     print('Found YouTube at %s' % e_link)
            #     print('\n')
            # else:
            #     pass
    except:
        pass


############################################
