import cohere
import json
import re
from scraper import getProjectData
import threading
from os.path import exists

NUMPROJECTREFERENCES = 7
QUERY = "hardware"
# working queries so far: IoT, Blockchain, NFT,

# what we're trying to do
TASK_DESCRIPTION = "This program will generate a project title, subtitle, and description for a hackathon project."

STOP_SEQUENCE = "--"

DATA_FILE = "data.json"

RESTOCK_TO = 5

# restocks ideas until we have at least 5 ready


def restock():
    with open(DATA_FILE) as f:
        data = json.load(f)

    restock_count = 0
    while len(data) <= RESTOCK_TO:
        with open(DATA_FILE) as f:
            data = json.load(f)
        print("restocking ideas")
        generate()
        restock_count += 1
        if restock_count >= 5:
            break

# retrieves a generated idea from our store


def get_idea(category=""):
    if not exists(DATA_FILE):
        data = []
        with open(DATA_FILE, "w+") as f:
            f.write(json.dumps(data))

    with open(DATA_FILE) as f:
        data = json.load(f)

    fail_count = 0
    while len(data) == 0:
        print("no ideas ready")
        fail_count += 1
        if (fail_count >= 3):
            return {
                "message": "All out of new ideas :("
            }

        generate(category)

        with open(DATA_FILE) as f:
            data = json.load(f)

    idea = data.pop(0)

    with open(DATA_FILE, "w") as f:
        f.write(json.dumps(data))

    if (len(data) <= 5):
        thread = threading.Thread(target=restock)
        thread.start()

    return idea

# generates new ideas


def generate(category=""):
    print("generating new ideas...")
    with open('key.txt', 'r') as file:
        KEY = file.read().replace('\n', '')

    co = cohere.Client(KEY)

    data = getProjectData(
        NUMPROJECTREFERENCES, "https://devpost.com/software/popular?query=is%3Awinner+" + category)

    prompt = TASK_DESCRIPTION + "\n" + "".join(map(lambda project: (
        STOP_SEQUENCE + "\n" +
        "Project title: " + project["title"] + "\n" +
        "Project subtitle: " + project["subtitle"] + "\n" +
        "Project description: " + project["description"] + "\n"
    ), data)) + STOP_SEQUENCE + "\n"

    print("prompt:", prompt)

    response = co.generate(
        prompt=prompt,
        max_tokens=250,
        temperature=1.0
    )

    # not 100% sure about the output from the api, may try to produce more than one post
    # so we take the first one
    ideas = response.generations[0].text.strip().split("\n--\n")

    ideas_processed = []
    for idea in ideas:
        print("idea", idea)
        # print(idea.strip())
        re_results = re.search(
            "Project title: (.*)\nProject subtitle: (.*)\nProject description: ((.|\n)*)", idea.strip())
        if not re_results:
            break
        ideas_processed.append({
            "title": re_results.group(1),
            "subtitle": re_results.group(2),
            "description": re_results.group(3)
        })

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        data = data + ideas_processed
    with open(DATA_FILE, "w") as f:
        f.write(json.dumps(data))
