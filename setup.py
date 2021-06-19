from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

setup(name='openaipylite',
      version='0.1.0',
      description='OpenAI API Python bindings without any dependencies.',
      long_description=long_description,
      keywords="openai python",
      url='https://github.com/argosopentech/openai-api-py-lite',
      classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        ],
      packages=find_packages()
)
