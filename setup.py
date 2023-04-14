from setuptools import setup, find_packages

setup(
    
    name = "Census-Income_project",
    version = "0.0.1",
    author = "Farshid Hesami",
    author_email = "farshidhesami@gmail.com",
    description =("An demonstration of how to create,Census Bureau publishes population estimates" 
                                     "and demographic components of change, such as births, deaths, and migration."),           
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn','matplotlib','scikit-learn','scipy','flask'],
    
)


