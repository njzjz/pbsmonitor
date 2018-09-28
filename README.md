# CQJobMonitor
[![python3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://badge.fury.io/py/CQJobMonitor)[![pypi](https://badge.fury.io/py/CQJobMonitor.svg)](https://badge.fury.io/py/ReacNetGenerator)

A PBS job monitor powered by CoolQ, which can send states of Portable Batch System to QQ.

**Author**: Jinzhe Zeng

**Email**: jzzeng@stu.ecnu.edu.cn

## Installation
### With pip
```sh
$ pip install CQJobMonitor
```
### Build from source
```sh
$ git clone https://github.com/njzjz/CQJobMonitor.git
$ cd CQJobMonitor/
$ python3 setup.py install
```
## Simple example
You need to install [CoolQ](https://cqp.cc/) and [CoolQ HTTP API plugin](https://github.com/richardchien/coolq-http-api/). Then create a QQ group to reveive messages.
```python
>>> from CQJobMonitor import CQJobMonitor
>>> CQJobMonitor(command="qstat",cqroot='http://219.228.63.56:5700/',group_id=312676525,keywords=['jzzeng'],timeinterval=300).loopmonitor()
```
