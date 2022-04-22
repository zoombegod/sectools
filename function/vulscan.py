#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : vulscan.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:46
# @Software: PyCharm
import sys

from main import begin
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mDescription\033[0m']
table.add_row(['1', '\033[0;33mSingle\033[0m'])
table.add_row(['2', '\033[0;33mAll\033[0m'])


class Vulnerability:
    @staticmethod
    def scan():
        print(table)
        while True:
            try:
                vuln_choices = input('\033[0;32mNorah C.IV\033[0m > ')
                if vuln_choices == '1':
                    print(1)

                elif vuln_choices == '0':
                    begin()

                else:
                    print('\033[0;31m[-] Error: Invalid Brute Type!Please Retype It!\033[0m')

            except KeyboardInterrupt:
                print('')
                print('[-] Exited By User')
                sys.exit(0)
