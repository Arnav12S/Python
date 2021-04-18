#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import requests


def run_emails():
    filepath = '/Users/arnav/Downloads/simple-email-scraper-master 2/domains.txt'
    with open(filepath) as fp:
        for line in fp:
            try:
                r = requests.get("http://%s" % line)
                r.encoding = 'ISO-8859-1'
                page_1 = r.text
                match = re.findall(
                    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b', page_1)
                with open('/Users/arnav/Downloads/simple-email-scraper-master 2/emails.txt', "a") as f:
                    for s in match:
                        f.write(str(s) + "\n")
                print('\n'
                      'Thanks for using this Script! If you enjoyed this script, start the repo http://github.com/luisramirez-m/simple-email-scraper')
                quit()
            except:
                quit()

def main():
    print("==============")
    print("What option do you want?")
    print("")
    print("1.- I have txt with domains to extract")
    print("0.- Exit")
    print("")
    print("==============")
    input_main = input("Select an option: ")

    if input_main == '1':
        run_emails()
    if input_main == '0':
        print('\n'
              'Thanks for using this Script! If you enjoyed this script, start the repo http://github.com/luisramirez-m/simple-email-scraper')
        quit()
    else:
        pass


main()
