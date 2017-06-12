import setuptools

setuptools.setup(
    name="distraction_logging_api",
    version="1.2",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/RUGSoftEng/distraction-logging-api',
    author="Alex Daffurn-Lewis",
    author_email="a.daffurn-lewis@student.rug.nl",
    description="The Distraction Shield's Logging Server",
    install_requires=['flask>=0.9',
                      'sqlalchemy>=1.1.9',
                      'flask-cors>=3.0.0']
)
