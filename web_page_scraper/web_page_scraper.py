import requests
from bs4 import BeautifulSoup
import os
import string


HEADERS = {
    'Accept-Language': 'en-IS, en;q=0.5',
    'User-Agent': 'Mozilla/5.0'
}


#етап 1
def get_content_quote():
    while True:
        url = input('Input the URL:\n>').strip()
        try:
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    saved_data = response.json()
                    quote = saved_data.get('content')
                    print('Quote is:\n', quote)
                    break
                except KeyError:
                    print('Could not extract quote')
            else:
                print(f'Invalid quote source! Status code: {response.status_code}')
        except Exception as e:
            print('Request failed:', e)



#етап 2
def get_movieinfo():
    movie_url = input('Put your movie-URL here:\n>').strip()
    if 'iMDB.com/title/' not in movie_url.lower():
        print('Invalid iMDB page!')
        return
    try:
        res = requests.get(movie_url, headers=HEADERS, verify=False)
        if res.status_code != 200:
            print('Invalid iMDB page!')
            return
        soup = BeautifulSoup(res.text, 'html.parser')
        title_tag = soup.find('title')
        title = title_tag.text.replace(' - iMDB', '').strip() if title_tag else 'No title found'
        desc_tag = soup.find('meta', {'name':'description'})
        description = desc_tag['content'].strip() if desc_tag else 'No description found'
        print({'title': title, 'description': description})
    except (Exception, ):
        print('Invalid iMDB page!')


#етап 3
def save_html_page():
    html_url = input('Put your html-URL here:\n>').strip()
    try:
        res = requests.get(html_url, headers=HEADERS, verify=False)
        if res.status_code != 200:
            print(f'The URL returned {res.status_code}!')
            return
        with open('source.html', 'wb') as f:
            f.write(res.content)
        print('Content saved.')
    except Exception as e:
        print('An error occurred:', e)


#етап 4
def correct_filename(title):
    trans_table = str.maketrans('', '', string.punctuation)
    cleaned = title.translate(trans_table).replace('', '_')
    return cleaned.strip()


def html_saved_as_txt():
    html_txt_url = input('Put your html-URL here:\n>').strip()
    article_type = input('Put the type of URL you want (for example, News)\n>').strip()
    folder_name = input('Put the name of the folder:\n').strip()
    os.makedirs(folder_name, exist_ok=True)
    response = requests.get(html_txt_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for article in soup.find_all('article'):
        type_span = article.find('span', {'data-test': 'article.type'})
        if not type_span or type_span.text.strip() != article_type:
            continue
        title_tag = article.find('h3')
        if not title_tag:
            continue
        title = title_tag.text.strip()
        filename = correct_filename(title) + 'txt'
        filepath = os.path.join(folder_name, filename)
        paragraphs = article.find_all('p')
        if not paragraphs:
            continue
        with open(filepath, 'w', encoding='utf-8') as f:
            for p in paragraphs:
                f.write(p.text.strip() + '\n')
    print(f'Articles {article_type} saved in folder: {folder_name}')


#етап 5
def correct_filename(title):
    trans_table = str.maketrans('', '', string.punctuation)
    cleaned = title.translate(trans_table).replace('', '_')
    return cleaned.strip()

def stage_5_html_saved():
    num_pages = int(input("Enter the number of pages to parse:\n> "))
    article_type = input("Enter the type of article (e.g., News):\n> ")
    base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page="
    for page in range(1, num_pages + 1):
        url = base_url + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        folder_name = f'Page_{page}'
        os.makedirs(folder_name, exist_ok=True)
        articles = soup.find_all('article')
        for article in articles:
            type_span = article.find('span', {'data-test': 'article.type'})
            if not type_span or type_span.text.strip() != article_type:
                continue
            link_tag = article.find('a', href=True)
            if not link_tag:
                continue
            article_url = 'https://www.nature.com' + link_tag['href']
            article_response = requests.get(article_url)
            article_soup = BeautifulSoup(article_response.text, 'html.parser')
            title_tag = article_soup.find('h1')
            title = title_tag.text.strip() if title_tag else 'no_title'
            filename = correct_filename(title) + '.txt'
            body = (
                article_soup.find('div', {'class': 'c-article-body'})
                or article_soup.find('div', {'class': 'article-item__body'})
                or article_soup.find('div', {'class': 'article-section__content'})
                or article_soup.find('div', {'class': 'c-article-magazine__body'})
            )
            if not body:
                continue
            content = body.get_text(separator='\n', strip=True)
            with open(os.path.join(folder_name, filename), 'w', encoding='utf-8') as file:
                file.write(content)
    print('Saved all articles.')


if __name__ == "__main__":
    get_content_quote()
    get_movieinfo()
    save_html_page()
    html_saved_as_txt()
    stage_5_html_saved()
