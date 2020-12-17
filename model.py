def setup():
    name = "P2-Platypodes"
    source = {"name": name}

proj1 = Model(project1, projlinks1)
proj2 = Model(project2, projlinks2)
# HTML Data
projects = Model(source, [proj1, proj2])
return model

class Model():
    # HTML data with source and projects
    def init(self, source, model):
        self.source = source
        self.model = model

    # source data
    def get_source(self):
        return self.source

    # projects data
    def get_model(self):
        return self.model

