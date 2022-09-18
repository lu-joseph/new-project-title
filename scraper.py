from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import json

# NUM_PROJECTS = 5
# pageToParse = "https://devpost.com/software/search?query=is%3Afeatured"
# QUERY = "Blockchain"


def getPageSoup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    reqPage = urlopen(req).read()
    reqPageSoup = soup(reqPage, "html.parser")
    return reqPageSoup


def getProjectData(numProjects, pageToParse):

    staffPicksPageSoup = getPageSoup(pageToParse)

    projectPageURLs = staffPicksPageSoup.select(
        '#container > div.row > div.columns > div.portfolio-row > div > a')

    projects = []

    for i in range(numProjects):
        projectURL = projectPageURLs[i].attrs["href"]
        projectPageSoup = getPageSoup(projectURL)
        title = projectPageSoup.select_one('#app-title').text.strip()
        subtitle = projectPageSoup.select_one(
            '#software-header > div.row > div.columns > p.large').text.strip()
        builtWith = projectPageSoup.select('#built-with > ul > li')
        tags = []
        for tag in builtWith:
            tags.append(tag.text)
        # print("title:" + title)
        descriptionDiv = projectPageSoup.select('#app-details-left > div')[1]
        # print(descriptionDiv.prettify())
        description = ""
        for component in descriptionDiv.children:
            if (component.name[0] == 'h'):
                continue
            if (len(description) > 500):
                break
            description += component.text
        dataDict = {"title": title, "subtitle": subtitle,
                    "description": description.strip(), "builtWith": tags}
        projects.append(dataDict)
    return projects


# getProjectData(
#     NUM_PROJECTS, "https://devpost.com/software/popular?query=" + QUERY)
