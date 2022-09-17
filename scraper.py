import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

# numProjects = 5
# pageToParse = "https://devpost.com/software/search?query=is%3Afeatured"


def getPageSoup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    reqPage = urlopen(req).read()
    reqPageSoup = soup(reqPage, "html.parser")
    return reqPageSoup


def getProjectData(numProjects, pageToParse):

    staffPicksPageSoup = getPageSoup(pageToParse)

    projectPageURLs = staffPicksPageSoup.select(
        '#container > div.row > div.columns > div.portfolio-row > div > a')

    projectJsons = []

    for i in range(numProjects):
        projectURL = projectPageURLs[i].attrs["href"]
        projectPageSoup = getPageSoup(projectURL)
        title = projectPageSoup.select_one('#app-title').text
        subtitle = projectPageSoup.select_one(
            '#software-header > div.row > div.columns > p.large').text
        builtWith = projectPageSoup.select('#built-with > ul > li')
        tags = []
        for tag in builtWith:
            tags.append(tag.text)
        dataDict = {"title": title, "subtitle": subtitle, "builtWith": tags}
        ProjectJsonString = json.dumps(dataDict)
        projectJsons.append(ProjectJsonString)

    totalJson = "{" + str(projectJsons) + "}"
    return json.dumps(totalJson)
