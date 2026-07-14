from knowledge_graph.graph import CareerGraph


class GraphBuilder:

    def __init__(self):

        self.graph = CareerGraph()

    def build(self, resume):

     self.graph.add_node(resume.name)

    # Skills
     for category in resume.skills.model_dump().values():

        for skill in category:

            self.graph.add_node(skill)

            self.graph.add_edge(

                resume.name,

                "HAS_SKILL",

                skill

            )

    # Projects
     for project in resume.projects:

        self.graph.add_node(project.name)

        self.graph.add_edge(

            resume.name,

            "BUILT",

            project.name

        )

     return self.graph

    