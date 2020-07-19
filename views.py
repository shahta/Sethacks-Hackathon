from django.shortcuts import render
from django.views.generic import ListView
from .models import SDG
import requests
from bs4 import BeautifulSoup


class SDGListView(ListView):
    model = SDG
    template_name = 'product/base.html'
    context_object_name = 'SDG'


def poverty_detail(request):
    numbers = ['1.2.3.4.5.6.7.8.9.10.']
    empty = []
    response = requests.get('https://www.globalcitizen.org/en/content/10-things-to-do-to-end-extreme-poverty-by-2030/')
    soup = BeautifulSoup(response.text, 'html.parser')

    header = soup.find('section', class_='article-content__main article-content')
    title = header.h1.text

    article_div = header.find('div', class_='cms-placeholder-wrapper')
    paragraphs = article_div.find_all('p')

    tips = paragraphs[2:24]
    all = [item.text for item in tips]

    context = {'title': title, 'paragraphs': all}

    return render(request, 'product/poverty_scrape.html', context)


def hunger_detail(request):
    response = requests.get('https://www.worldvision.ca/stories/food/world-hunger-facts-how-to-help')
    soup = BeautifulSoup(response.text, 'html.parser')

    header = soup.find('div', class_='news-title')
    title = header.h1.text

    article = soup.find('div', class_='col-md-8 col-md-offset-2 news-story margin-bottom-lg')
    text = article.text
    split = text.split('?')

    context = {'title': title, 'split': split}

    return render(request, 'product/hunger_scrape.html', context)


def business_detail(request):
    response = requests.get('https://thrivehive.com/how-and-why-to-make-your-business-more-eco-friendly/#:~:text=Businesses%20across%20the%20country%20are,the%20image%20of%20your%20brand.')
    soup = BeautifulSoup(response.text, 'html.parser')

    div = soup.find('div', class_='the_content_wrapper')
    header = div.find_all('h2')[2].text
    intro = div.find_all('p')[3].text

    h3 = div.find_all('h3')
    para = div.find_all('p')
    li = div.find_all('li')

    recycle = h3[0].text
    recycle_p = [item.text for item in para[4:7]]

    ink = h3[1].text
    ink_p = para[7].text

    chemicals = h3[2].text
    chemicals_p = para[8].text

    energy = h3[3].text
    energy_p = para[9].text

    electronics = h3[4].text
    electronics_p = para[10].text

    audit = h3[5].text
    audit_p = para[11].text

    transportation = h3[6].text
    transportation_p = para[12].text

    marketing = h3[7].text
    marketing_p = para[13].text
    marketing_li = [item.text for item in li[:5]]
    another_marketing_p = para[14].text

    solar = h3[8].text
    solar_p = [item.text for item in para[15:19]]

    context = {'header': header, 'intro': intro, 'recycle': recycle, 'recycle_p': recycle_p,
               'ink': ink, 'ink_p': ink_p, 'chemicals': chemicals, 'chemicals_p': chemicals_p,
               'energy': energy, 'energy_p': energy_p, 'electronics': electronics, 'electronics_p': electronics_p,
               'audit': audit, 'audit_p': audit_p, 'transportation': transportation,
               'transportation_p': transportation_p, 'marketing': marketing, 'marketing_p':marketing_p,
               'marketing_li': marketing_li, 'marketing_p2': another_marketing_p, 'solar': solar,
               'solar_p': solar_p}

    return render(request, 'product/business_scrape.html', context)
