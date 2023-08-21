from setuptools import setup, find_packages

setup(
    name="ClasseVivaAPI",
    version="0.1",
    author="Fabrizio Gasparini",
    author_email="gasparini.fabrizio@einaudicorreggio.it",
    description="Questa libreria Python permette di utlizzare l'API di ClasseViva - GruppoSpaggiariParma",
    long_description="Questa libreria Python permette di utlizzare l'API di ClasseViva - GruppoSpaggiariParma",
    long_description_content_type="text/markdown",
    url="https://github.com/MakerFaffa/ClasseVivaAPI",
    packages=find_packages(),
    keywords=[
        "classeviva",
        "api",
        "ClasseVivaAPI"
    ],
    install_requires=["requests"],
    python_requires=">=3.10"
)