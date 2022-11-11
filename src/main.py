from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship


graph_attr = {
    "splines": "spline",
}

with Diagram("Portfolio", direction="TB", graph_attr=graph_attr, show=False):
    
    developer = Person(
        name="Developer", description="Update portfolio data on Github"
    )
    github_gist_input = System(name="Github Gist storage", description="Portfolio input data", external=True)

    preprocessing = Container(
        name="PreProcessing",
        technology="Python - Pandas/GeoPandas, SqlAlchemy/GeoAlchmey",
        description="Fill and/or update portfolio database",
    )
    github_ation_portfolio = System(name="Github Gist storage", description="Portfolio input data", external=True)

    #with SystemBoundary("PreProcessing"):


    developer >> Relationship("Update manually") >> github_gist_input
    developer >> Relationship("event send") >> preprocessing >> github_ation_portfolio
