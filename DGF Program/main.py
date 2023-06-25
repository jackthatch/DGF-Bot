import time
import smtplib
import discord
import asyncio
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Browser:

    # global client
    # client = discord.Client()

    TOKEN = "MTA3NzM4OTcwNDgyMDk1MzE5OA.GN2UYM.DHZiUvEnTxDu6NoCfLBmcj3ECtFHexD63U6p24"

    global found
    found = []

    browser, service = None, None

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service = self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(0.5)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(0.5)    

    def login_linkedin(self, username: str, password: str):
        self.add_input(by=By.ID, value="session_key", text=username)
        self.add_input(by=By.ID, value="session_password", text=password)
        self.click_button(by=By.CLASS_NAME, value='sign-in-form__submit-button')

    def login_dgf(self, username: str, password: str):
        
        self.add_input(by=By.ID, value="user_login", text=username)
        self.add_input(by=By.ID, value="user_pass", text=password)
        self.click_button(by=By.ID, value="wp-submit")
        time.sleep(0.2)
        

    def login_underdog(self, username: str, password: str):

        browser.open_page("https://underdogfantasy.com/login")
        time.sleep(1)
        
        self.add_input(by=By.XPATH, value="//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/label[1]/div[2]/input[1]", text=username)
        self.add_input(by=By.XPATH, value="//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/label[1]/div[2]/input[1]", text=password)
        self.click_button(by=By.XPATH, value="//button[contains(text(),'Sign in')]")
        
        
        time.sleep(200)

    def pp_login(self, username: str, password: str):

        browser.open_page("https://app.prizepicks.com/login")       ## Open the prizepicks login website
        time.sleep(0.5)


        self.add_input(by=By.ID, value="email-input", text = username)
        self.add_input(by=By.XPATH, value="//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[3]/input[1]", text = password)     ##Login to prizepicks
        self.click_button(by=By.ID, value="submit-btn")
        time.sleep(0.2)
        # browser.open_page("https://app.prizepicks.com/")        ##open the main page of prizepicks
 

    # async def send_message(client, channel_id, message):        ##Pass in our SMS message
    #     channel = client.get_channel(channel_id)
    #     await channel.send(message)

        

    def email_alert (self, subject, body, to):
        msg = EmailMessage()
        msg.set_content(body)
        msg["subject"] = subject
        msg["to"] = to
        
        user = "jthatcher128@gmail.com"
        password = "wthijsqxhpiafasr"
        msg["from"] = user


        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()





    def pp_search(self, fullname: str, over_under: str, number: str, prop: str, league: str, iteration: int):

        time.sleep(0.2)

        self.browser.find_element(by=By.XPATH, value = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[16]").click()
        time.sleep(0.2)
        
        ##Select the correct sport
        if league == "NBA":
            self.browser.find_element(by=By.XPATH, value = "//div[contains(text(), 'NBA')]").click()
        elif league == "NCAAB":
            self.browser.find_element(by=By.XPATH, value = "//div[contains(text(), 'CBB')]").click()
        elif league == "NHL":
            self.browser.find_element(by=By.XPATH, value = "//div[contains(text(), 'NHL')]").click()
        

        

        ##Add the fullname to the player search bar
        self.add_input(by=By.XPATH, value="//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/main[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]", text=fullname)
        time.sleep(0.2)

        if self.browser.find_element(by=By.XPATH, value = "//div[contains(text(),'" + number + "')]").size != 0:
            self.browser.find_element(by=By.XPATH, value = "//div[contains(text(),'" + number + "')]").click()
            time.sleep(0.2)
        else:
            print("Pick taken off of board")
            return


        
        ##Click the button within the subwindow on the side

        if iteration == 1:
            if over_under == "OVER":
                self.browser.find_element(by=By.XPATH, value = "//div[contains(text(),'MORE')]").click()
                time.sleep(0.1)
                self.browser.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(0.1)
                self.browser.find_element(by=By.XPATH, value = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[16]").click()        ##Change to COD page
                time.sleep(0.1)
            else:
                self.browser.find_element(by=By.XPATH, value = "//div[contains(text(),'LESS')]").click()
                time.sleep(0.1)
                self.browser.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(0.1)
                self.browser.find_element(by=By.XPATH, value = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[16]").click()        ##Change to COD page
                time.sleep(0.1)

            # time.sleep(1)

        if iteration == 2:
            if over_under == "OVER":
                self.browser.find_element(by=By.XPATH, value = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/main[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/div[1]").click()
            else:
                self.browser.find_element(by=By.XPATH, value = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/main[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/div[2]").click()
            
            time.sleep(0.5)




    def pp_submit_pick(self):

        self.browser.find_element(by=By.XPATH, value="//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/main[1]/div[1]/div[3]/div[2]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").clear()
        self.add_input(by=By.XPATH, value="//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/main[1]/div[1]/div[3]/div[2]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]", text="5")
        time.sleep(0.2)


        self.browser.find_element(by=By.XPATH, value = "//button[contains(text(),'Place Entry')]").click()
        time.sleep(1)

        
        
    def underdog_search(self, fullname: str, over_under: str, number: str, prop: str, league: str, iteration: int):

        if iteration == 1:
            self.browser.switch_to.window(self.browser.window_handles[3])       ##If this is the first ud search then switch to the UD page
        
        time.sleep(0.3)

        self.add_input(by=By.XPATH, value = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/div[1]/input[1]", text = fullname)


        if iteration == 1 and over_under == "OVER":
            # if self.browser.find_element(by=By.XPATH, value = "//div[contains(text(),'" + number + "')]").size != 0:
            self.browser.find_element(by=By.XPATH, value = "//div[contains(text(),'" + number + "')]/button[.=Higher]").click()
            time.sleep(0.2)
        elif iteration == 1 and over_under == "UNDER":
            self.browser.find_element(by=By.XPATH, value = "//div[contains(text(),'" + number + "')]/button[.=Lower]").click()
            time.sleep(0.2)


        elif iteration >= 2 and over_under == "OVER":
            self.browser.find_element(by=By.XPATH, value = "//div[contains(text(),'" + number + "')]/button[.=Higher]").click()
            time.sleep(0.2)
        elif iteration >= 2 and over_under == "Under":
            self.browser.find_element(by=By.XPATH, value = "//div[contains(text(),'" + number + "')]/button[.=Lower]").click()
            time.sleep(0.2)
      


    def underdog_submit(self):

        self.add_input(by=By.XPATH, value = "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/label[1]/div[2]/input[1]", text = "5")     ##Add bet amount
        time.sleep(0.3)

        self.browser.find_element(by=By.XPATH, value = "//button[contains(text(),'Submit')]").click()
        time.sleep(1)

        self.browser.switch_to.window(self.browser.window_handles[1])       ##Swap back to underdog optimizer window


    def refresh_page(self):
        self.browser.refresh()


    def get_values_pp(self, iteration: int):
            
            self.browser.switch_to.window(self.browser.window_handles[0])
        
            time.sleep(2)

            found = []
            
            i = 1
            k = 3

            while i < k:

                if i == 1:

                    firstname = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[1]").text
                    lastname = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[2]").text
                    league = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[3]").text
                    # team = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[4]").text
                    over_under = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[5]").text
                    number = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[7]").text
                    prop = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[6]").text
                    percent = float(self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[21]").text) 

                    output = (str(percent) + "% Chance: " + firstname + " " + lastname + " " + over_under + " "  + number + " " + prop + "\n" + league)
                    found.append(output)

                elif i >= 2:

                    firstname2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[1]").text
                    # team2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[4]").text
                    
                    # if firstname2 == firstname:     ##If the 1 and 2 pick are the same person check the 3rd and pair it with the first 
                    #     k +=1
                    #     continues

                    lastname2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[2]").text
                    league2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[3]").text
                    over_under2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[5]").text
                    number2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[7]").text
                    prop2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[6]").text
                    percent2 = float(self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[21]").text) 

                    output2 = (str(percent2) + "% Chance: " + firstname2 + " " + lastname2 + " " + over_under2 + " "  + number2 + " " + prop2 + "\n" + league2)
                    found.append(output2)


                i += 1

            fullname = firstname + " " + lastname
            fullname2 = firstname2 + " " + lastname2


            if (percent + percent2) / 2 >= 58:               ##If average odds is 58% + 

                self.browser.switch_to.window(self.browser.window_handles[2]) 
                time.sleep(0.5)

                browser.pp_search(fullname, over_under, number, prop, league, 1)
                time.sleep(0.2)
                browser.pp_search(fullname2, over_under2, number2, prop2, league2, 2)
                time.sleep(0.2)

                browser.pp_submit_pick()

                sms_message = output +  "\n\n" + output2 + "\n\n Has been submitted on PrizePicks!"


                time.sleep(0.2)
                self.browser.switch_to.window(self.browser.window_handles[0])
                time.sleep(10)
                
                return sms_message
            else:
                # self.browser.switch_to.window(self.browser.window_handles[1]) 
                self.browser.refresh()
                time.sleep(0.5)
                return None
            
    
    def get_values_UD(self, iteration: int):

        self.browser.switch_to.window(self.browser.window_handles[1])
        
        time.sleep(1)

        found = []
        
        i = 1
        k = 3

        while i < k:

            if i == 1:

                firstname = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[1]").text
                lastname = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[2]").text
                league = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[3]").text
                team = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[4]").text
                over_under = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[5]").text
                number = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[7]").text
                prop = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[6]").text
                percent = float(self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[20]").text) 

                output = (str(percent) + "% Chance: " + firstname + " " + lastname + " " + over_under + " "  + number + " " + prop + "\n" + league)
                found.append(output)

            elif i >= 2:

                firstname2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[1]").text
                team2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[4]").text
                
                if firstname2 == firstname:     ##If the 1 and 2 pick are the same person check the 3rd and pair it with the first 
                    k +=1
                    continue

                lastname2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[2]").text
                league2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[3]").text
                over_under2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[5]").text
                number2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[7]").text
                prop2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[6]").text
                percent2 = float(self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[20]").text) 

                output2 = (str(percent2) + "% Chance: " + firstname2 + " " + lastname2 + " " + over_under2 + " "  + number2 + " " + prop2 + "\n" + league2)
                found.append(output2)


            i += 1

        fullname = firstname + " " + lastname
        fullname2 = firstname2 + " " + lastname2


        if percent2 >= 58:               ##If both percents are > 58 submit the pick 

            self.browser.switch_to.window(self.browser.window_handles[1]) 
            

            browser.underdog_search(fullname, over_under, number, prop, league, 1)
            time.sleep(0.2)
            browser.underdog_search(fullname2, over_under2, number2, prop2, league2, 2)
            time.sleep(0.2)
            
            browser.pp_submit_pick()
            time.sleep(0.2)

            sms_message = output +  "\n\n" + output2 + "\n\n Has been submitted on Underdogs!"

            
            self.browser.switch_to.window(self.browser.window_handles[0])
            time.sleep(10)
            
            return sms_message
        
        else:

            self.browser.refresh()
            time.sleep(0.5)
            return None


    ##same function as above but this one is for the notification aspect
    def get_values_noti_pp(self, iteration: int):
            
            self.browser.switch_to.window(self.browser.window_handles[0])

        
            time.sleep(2)


            new_found = []
            sms_message = ""
            
            i = 1
            k = 3

            while i < k:

                if i == 1:

                    firstname = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[1]").text
                    lastname = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[2]").text
                    league = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[3]").text
                    # team = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[4]").text
                    over_under = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[5]").text
                    number = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[7]").text
                    prop = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[6]").text
                    percent = float(self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[21]").text) 

                    output = (str(percent) + "% Chance: " + firstname + " " + lastname + " " + over_under + " "  + number + " " + prop + "\n" + league)
                    
                    if output not in found:
                        found.append(output)       ##Add to total library of picks
                        new_found.append(output)      ##Add to library of picks for current iteration of the function



                elif i >= 2:

                    firstname2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[1]").text
                    # team2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[4]").text
                    
                    # if firstname2 == firstname:     ##If the 1 and 2 pick are the same person check the 3rd and pair it with the first 
                    #     k +=1
                    #     continues

                    lastname2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[2]").text
                    league2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[3]").text
                    over_under2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[5]").text
                    number2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[7]").text
                    prop2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[6]").text
                    percent2 = float(self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[21]").text) 

                    output2 = (str(percent2) + "% Chance: " + firstname2 + " " + lastname2 + " " + over_under2 + " "  + number2 + " " + prop2 + "\n" + league2)
                    
                    if output2 not in found:
                        found.append(output2)            ##Add to total library of picks
                        new_found.append(output2)       ##Add to library of picks for current iteration of the function
                        


                i += 1

            fullname = firstname + " " + lastname
            fullname2 = firstname2 + " " + lastname2


            if percent >= 60 or (percent + percent2) / 2 >= 58.5:               ##If percent1 is >59 or if +EV pair


                for ele in new_found:
                    sms_message += ele + "\n\n"

                time.sleep(0.5)

                sms_message += "Is available on PrizePicks!"

                self.browser.refresh()

                time.sleep(2)

                if sms_message == "Is available on PrizePicks!":
                    return None
                else:
                    # asyncio.run(send_message(topPick))
                    return sms_message

            else:
                # self.browser.switch_to.window(self.browser.window_handles[1]) 
                self.browser.refresh()
                time.sleep(0.5)

                return None
            


    def get_values_noti_ud(self, iteration: int):
            
            self.browser.switch_to.window(self.browser.window_handles[1])

        
            time.sleep(2)


            new_found = []
            sms_message = ""
            
            i = 1
            k = 3

            while i < k:

                if i == 1:

                    firstname = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[1]").text
                    lastname = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[2]").text
                    league = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[3]").text
                    # team = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[4]").text
                    over_under = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[5]").text
                    number = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[7]").text
                    prop = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[6]").text
                    percent = float(self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[20]").text) 

                    output = (str(percent) + "% Chance: " + firstname + " " + lastname + " " + over_under + " "  + number + " " + prop + "\n" + league)
                    
                    if output not in found:
                        found.append(output)       ##Add to total library of picks
                        new_found.append(output)      ##Add to library of picks for current iteration of the function



                elif i >= 2:

                    firstname2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[1]").text
                    # team2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[4]").text
                    
                    # if firstname2 == firstname:     ##If the 1 and 2 pick are the same person check the 3rd and pair it with the first 
                    #     k +=1
                    #     continues

                    lastname2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[2]").text
                    league2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[3]").text
                    over_under2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[5]").text
                    number2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[7]").text
                    prop2 = self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[6]").text
                    percent2 = float(self.browser.find_element(by=By.XPATH, value="//tbody/tr[" + str(i) + "]/td[20]").text) 

                    output2 = (str(percent2) + "% Chance: " + firstname2 + " " + lastname2 + " " + over_under2 + " "  + number2 + " " + prop2 + "\n" + league2)
                    
                    if output2 not in found:
                        found.append(output2)            ##Add to total library of picks
                        new_found.append(output2)       ##Add to library of picks for current iteration of the function
                        


                i += 1

            fullname = firstname + " " + lastname
            fullname2 = firstname2 + " " + lastname2


            if percent >= 60 or (percent + percent2) / 2 >= 58.5:               ##If percent1 is >59 or if +EV pair


                for ele in new_found:
                    sms_message += ele + "\n\n"

                time.sleep(0.5)

                sms_message += "Is available on Underdogs!"

                self.browser.refresh()

                time.sleep(2)

                if sms_message == "Is available on Underdogs!":
                    return None
                else:
                    # asyncio.run(send_message(topPick))
                    return sms_message

            else:
                # self.browser.switch_to.window(self.browser.window_handles[1]) 
                self.browser.refresh()
                time.sleep(0.5)

                return None


    
        

        
    
    
    def initial_setup(self, dg_user: str, pass1: str, pp_user: str, pass2: str):
        
        self.browser.maximize_window()
        browser.open_page("https://dgfantasy.com/login/")
        browser.login_dgf(dg_user, pass1)
        browser.pp_login(pp_user, pass2)
        browser.open_page("https://dgfantasy.com/all-sports-prizepicks-optimizer/")
        time.sleep(1)
        self.browser.execute_script("window.open('https://dgfantasy.com/underdog-fantasy-all-sports-optimizer/');")     ##Open DGF Underdogs
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.execute_script("window.open('https://app.prizepicks.com/board');")     ##Open prize picks in a second window  
        self.browser.switch_to.window(self.browser.window_handles[2])
        self.browser.execute_script("window.open('https://underdogfantasy.com/pick-em/higher-lower');")
        self.browser.switch_to.window(self.browser.window_handles[3])
        time.sleep(0.5)

        # self.browser.switch_to.window(self.browser.window_handles[0])                   ##self.browser.window_handles[0] == DGF Prizepicks   [1] == DGF UD   [2] == Prizepicks Board   [3] == UD Board
        
        time.sleep(0.5)





if __name__ == '__main__':

    picksLibrary = []
    i = 1

    balance = 10
    
    browser = Browser(r"C:\Users\Thatcher\Desktop\DGF Program\chromedriver.exe")
    
    # browser.login_underdog("jthatcher128@gmail.com", "Odyssey!12UD")

    browser.initial_setup("jackthatch", "Odyssey!12DGF", "jthatcher128@gmail.com", "Odyssey!12PP")


    ## self.browser.execute_script("window.open('https://underdogfantasy.com/pick-em/higher-lower');")  ##Run this before executing underdog_search


    time.sleep(1)

    while i <= 10000 and balance != 0:                  ## Loop to refresh page and send notification if theres is a new good pick

        picksLibrary = []
        topPick = browser.get_values_noti_pp(i)  ##passing in the iteration
        topPick2 = browser.get_values_noti_ud(i)

        ##ALL email alerts that need to be sent
        if topPick != None:
            browser.email_alert("", topPick, "2567911250@vtext.com")        ## ME
            # browser.email_alert("", topPick, "2563091406@tmomail.net")    ## Jackson Boyer
            # browser.email_alert("", topPick, "2563033821@vtext.com")        ## landon
            # browser.email_alert("", topPick, "2566063511@txt.att.net")        ## Myles 21
            print(picksLibrary)

            # break

        if topPick2 != None:
            browser.email_alert("", topPick2, "2567911250@vtext.com")       ## ME
            print(picksLibrary)

        else:
            time.sleep(7)



        i += 1
        
    

    
    time.sleep(150)

    browser.close_browser()


