# PBSMonitor

[![python version](https://img.shields.io/pypi/pyversions/pbsmonitor.svg?logo=python&logoColor=white)](https://pypi.org/project/pbsmonitor)
[![PyPI](https://img.shields.io/pypi/v/pbsmonitor.svg)](https://pypi.org/project/pbsmonitor)
[![Build Status](https://travis-ci.com/njzjz/pbsmonitor.svg?branch=master)](https://travis-ci.com/njzjz/pbsmonitor)
[![Coverage Status](https://coveralls.io/repos/github/njzjz/pbsmonitor/badge.svg?branch=master)](https://coveralls.io/github/njzjz/pbsmonitor?branch=master)
[![codecov](https://codecov.io/gh/njzjz/pbsmonitor/branch/master/graph/badge.svg)](https://codecov.io/gh/njzjz/pbsmonitor)

A PBS job monitor powered by CoolQ, which can send states of Portable Batch System to QQ.

**Author**: Jinzhe Zeng

**Email**: jzzeng@stu.ecnu.edu.cn

## Installation
### With pip
```sh
pip install pbsmonitor
```
### Build from source
```sh
git clone https://github.com/njzjz/pbsmonitor
cd pbsmonitor/
pip install .
```

## Simple example

You need to install [CoolQ](https://cqp.cc/) and [CoolQ HTTP API plugin](https://github.com/richardchien/coolq-http-api/). Then create a QQ group to reveive messages.

```sh
pbsmonitor -c bjobs -k jzzeng -r http://192.168.1.1:6000 -g 123456789
```
