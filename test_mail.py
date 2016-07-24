#! /usr/bin/env python

import smtpsend

S = smtpsend.Smtpsent(SUBJECT='Test')
S.sendemail('''
this is a test!
''')
