from selenium import webdriver
from time import sleep
from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(4)
        mo_btn= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        mo_btn.click()
        sleep(3)
        """ fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
        fb_btn.click()
        sleep(3) """
        

        #switching to login tab
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        ps_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        ps_in.send_keys(password)
        login_btn=self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        self.driver.switch_to_window(base_window)


        pop1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        pop1.click()
        pop2= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        pop2.click() 

        
        try:
            emailconpop= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/button[2]')
            emailconpop.click()

        


    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn= self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def autolike(self):
        while True:
            sleep(1)
            self.like()
'''bot= TinderBot()
bot.login()'''
