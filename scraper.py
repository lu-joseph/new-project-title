from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import json

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
            # print(component)
            # print()
            if (len(description) > 500):
                break
            description += component.text

            description = description

        dataDict = {"title": title, "subtitle": subtitle,
                    "description": description.strip(), "builtWith": tags}
        projects.append(dataDict)
    return projects


# getProjectData(3, "https://devpost.com/software/search?query=is%3Afeatured")
