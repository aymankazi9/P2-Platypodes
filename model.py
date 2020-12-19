def setup():
    name = "P2-Platypodes"
    source = {"name": name}

    project1 = "Frontend"
    projlinks1 = [
        Link("GitHub", "https://github.com/aymankazi9/P2-Platypodes/tree/main/templates")
    ]

    project2 = "Backend"
    projlinks2 = [
        Link("GitHub", "https://github.com/aymankazi9/P2-Platypodes/blob/main/model.py")
    ]

    # Project Objects
    proj1 = Model(project1, projlinks1)

    proj2 = Model(project2, projlinks2)
    # HTML Data
    projects = Models(source, [proj1, proj2])
    return projects


# class for button label and href
class Link():
    # href is linked to button label
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href

    def get_btn(self):
        return self.btn

    def get_href(self):
        return self.href


# Project data class contain project name and links (Link class objects)
class Model():
    # project data with name and links
    def __init__(self, name, links):
        self.name = name
        self.links = links

    def get_name(self):
        return self.name

    def get_links(self):
        return self.links


# Projects class contains person (owner) and multiple projects (Project class objects)
class Models():
    # HTML data with source and projects
    def __init__(self, source, model):
        self.source = source
        self.model = model

    # source data
    def get_source(self):
        return self.source

    # projects data
    def get_model(self):
        return self.model

