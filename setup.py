from setuptools import setup, find_packages

readme = open('README.rst', 'r')
README_TEXT = readme.read()
readme.close()

setup(
    name='text_template',
    version='0.1.0',
    url='https://github.com/sarcoma/Python_Terminal_Text_Templates',
    license='MIT',
    author='sarcoma',
    author_email='sean@orderandchaoscreative.com',
    description='Very simple text templating view for Python',
    long_description=README_TEXT,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    project_urls={
        'Order & Chaos Creative': 'https://orderandchaoscreative.com',
    }
)
