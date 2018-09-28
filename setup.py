from setuptools import setup
setup(name='CQJobMonitor',
      version='1.0.2',
      description='A PBS job monitor powered by CoolQ.',
      keywords="coolq",
      url='https://github.com/njzjz/CQJobMonitor',
      author='Jinzhe Zeng',
      author_email='jzzeng@stu.ecnu.edu.cn',
      packages=['CQJobMonitor'],
      install_requires=['cqhttp'])
