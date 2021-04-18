import csv
from time import sleep
from selenium import webdriver

username = 'arnav.sudhansh12@gmail.com'
password = 'SHAshaNK@1'

login_url = 'https://www.linkedin.com/uas/login'
customMessage = "Hello, I have found mutual interest in your area of work and I would be more than happy to connect with you. Kindly, accept my invitation. Also, congrats on being features in top 50 europes most influential women in the startup and venture capital space 2021 by EU Startups, Thanks!"


def init():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome('/Users/arnav/Downloads/chromedriver', options=chrome_options)
    return wd


def login(wd):
    global username
    global password
    global login_url

    wd.get(login_url)

    elementID = wd.find_element_by_id('username')
    elementID.send_keys(username)
    sleep(5)

    elementID = wd.find_element_by_id('password')
    elementID.send_keys(password)

    elementID.submit()


def visit_profile(wd, url):
    global customMessage
    # fullLink = 'https://www.linkedin.com/' + visitingProfileID
    fullLink = url
    wd.get(fullLink)
    wd.find_element_by_class_name('pv-s-profile-actions').click()
    wd.find_element_by_class_name('mr1').click()
    elementID = wd.find_element_by_id('custom-message')
    elementID.send_keys(customMessage)
    wd.find_element_by_class_name('ml1').click()
    print("Done:")


def read_csv(fname, wd):
    fd = open(fname, "r")
    csvreader = csv.DictReader(fd)
    login(wd)
    for row in csvreader:
        linkedin_url = row['URL']
        print("Visiting {}".format(linkedin_url))
        visit_profile(wd, linkedin_url)
        print("Sleeping 30 seconds..")
        sleep(30)


if __name__ == "__main__":
    ChromeDriver = init()
    fname = '/Users/arnav/Downloads/connections.csv'
    read_csv(fname, ChromeDriver)