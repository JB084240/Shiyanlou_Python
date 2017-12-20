# -*- coding: utf-8 -*-
import sys
import csv
from collections import namedtuple

IncomeTaxQuickLookupItem = namedtuple(
    'IncomeTaxQuickLookupItem',
    ['start_point', 'tax_rate', 'quick_subtractor']
)

INCOME_TAX_START_POINT = 3500

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    IncomeTaxQuickLookupItem(55000, 0.35, 5505),
    IncomeTaxQuickLookupItem(35000, 0.30, 2755),
    IncomeTaxQuickLookupItem(9000, 0.25, 1005),
    IncomeTaxQuickLookupItem(4500, 0.2, 555),
    IncomeTaxQuickLookupItem(1500, 0.1, 105),
    IncomeTaxQuickLookupItem(0, 0.03, 0)
]

class Args(object):
    
    def __init__(self):
        self.args = sys.args[1:]

    def _value-after_option(self, option):
        try:
            index = self.args.index(option)
            return self.args[index +1]
        except (ValueError, IndexError):
            print('Parameter Error')
            exit()

    @property
    def config_path(self):
        return self._value_after_option('-c')

    @property
    def userdata_path(self):
        return self._value_after_option('-d')

    @property
    def export_path(self):
        return self._value_after_option('-o')

args = Args()

class Config(object):
    
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config_path = args.config_path
        config = {}
        with open(config_path) as f:
            for line in f.readlines():
                key, value = line.strip().split('=')
                try:
                    config[key.strip()] = float(value.strip())
                except ValueError:
                    print('Parameter Error')
                    exit()
        return config

    def _get_config(self, key):
        try:
            return self.config[key]
        except KeyError:
            print('Config Error')
            exit()

    @property
    def social_insurance_baseline_low(self):
        return self._get_config('JiShuL')

    @property
    def social_insurance_baseline_high(self):
        return self._get_config('JiShuH')

    @property
    def social_insurance_total_rate(self):
        return sum([
            self._get_config('YangLao'),
            self._get_config('YiLiao'),
            self._get_config('ShiYe'),
            self._get_config('GongShang'),
            self._get_config('ShengYu'),
            self._get_config('GongJiJin')
        ])

config = Config()


class UserData(object):
    
    def __init__(self):
        self.userdata = self._read_user_data()

    def _read_user_data(self):
        userdata_path = args.userdata_path
        uerdata = []
        with open(userdata_path) as f:
            for line in f.readlines():
                employee_id, income_string = line.strip().split(',')
                try:
                    income = int(income_string)
                except ValueError:
                    print('Parameter Error')
                    exit()
                userdata.append((employee_id, income))
        return userdata

    def __iter__(self):
        return iter(self.userdata)

