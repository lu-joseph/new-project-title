# new-project-title
A hackathon idea generator that looks on Devpost for past hackathon ideas and generate a new one using the Cohere API

Scraper.getProjectData() returns a JSON with the form:
```
{
  "projectJsons": [
    {
      "title": project_title,
      "subtitle": subtitle,
      "builtWith": [built_with_tags]
    },
    {
      "title": project_title,
      "subtitle": subtitle,
      "builtWith": [built_with_tags]
    },
    {
      "title": project_title,
      "subtitle": subtitle,
      "builtWith": [built_with_tags]
    },
  ]
}
```
