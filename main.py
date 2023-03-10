from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random, csv, pyautogui, pdb, traceback, os, sys
import json
from personal_info import *


class Wfajobs_apply:

    def __init__(self, data):

        self.email = data["email"]
        self.password = data["password"]
        self.positions = data["keyword"]
        self.locations = data["location"]
        self.driver = webdriver.Chrome(data["driver_path"])
        '''LOGS IN'''

    def login(self):

        self.driver.get("https://www.indeed.com/account/login")
        time.sleep(10)
        users = self.driver.find_element(By.NAME, "__email")
        users.send_keys(self.email)
        time.sleep(30)
        users.send_keys(Keys.ENTER)
        time.sleep(10)
        self.driver.find_element(By.ID, "auth-page-google-password-fallback").click()
        time.sleep(8)
        password = self.driver.find_element(By.NAME, "__password")
        password.send_keys(self.password, Keys.ENTER)
        time.sleep(30)

    def security_check(self):
        current_url = self.driver.current_url
        page_source = self.driver.page_source
        if '/checkpoint/challenge/' in current_url or 'security check' in page_source:
            input("Please complete the security check and press enter in this console when it is done.")
            time.sleep(random.uniform(5.5, 10.5))

        '''KEYWORD SEARCH FOR JOBS'''

    def search_jobs(self):
        self.driver.find_element(By.ID, "text-input-what").send_keys(self.positions)
        time.sleep(2)
        where = self.driver.find_element(By.ID, "text-input-where")
        where.send_keys(Keys.CLEAR)
        where.send_keys(Keys.ENTER)
        time.sleep(2)

        '''CLICKS APPLY ON BTN ON EACH'''

    def click_jobs(self):
        total_results = self.driver.find_element(By.CLASS_NAME, "jobsearch-JobCountAndSortPane-jobCount")
        total_results_int = int(total_results.text.split(' ', 1)[0].replace(",", ""))
        print(total_results_int)
        results = self.driver.find_elements(By.CSS_SELECTOR, ".mosaic-provider-jobcards .tapItem")
        items_per_page = 15
        num_of_pages = total_results_int // items_per_page
        applied = len(results)
        apply_btn = self.driver.find_element(By.CLASS_NAME, "ia-IndeedApplyButton")
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((results)))

        for i in range(0, total_results_int, items_per_page):
            results_to_click = results[i:i + items_per_page]
            if applied > items_per_page:
                self.driver.find_element(By.XPATH, "//a[@data-testid='pagination-page-next']").click()
                time.sleep(5)
                current_url = self.driver.current_url
                self.driver.get(current_url)
                element(results)
            for result in results_to_click:
                hover = ActionChains(self.driver).move_to_element(result).click()
                time.sleep(2)
                hover.perform()
                if apply_btn:
                    time.sleep(5)
                    apply_btn.click()
                    time.sleep(15)
                    self.operation()
                else:
                    time.sleep(2)
                    continue

    def operation(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.questionnaire()
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    def questionnaire(self):
        while True:
            questions_title_el = self.driver.find_element(By.CLASS_NAME, "ia-BasePage-heading").text
            questions_title = self.driver.find_element(By.CLASS_NAME, "ia-BasePage-heading").text.lower()
            questions_continue_btn = self.driver.find_element(By.CSS_SELECTOR, '.css-vw73h2')
            qualifications_continue_btn = self.driver.find_element(By.CSS_SELECTOR, ".css-1rpq9wt")
            resume_continue_btn = self.driver.find_element(By.CSS_SELECTOR, ".css-vw73h2")
            experience_continue_btn = self.driver.find_element(By.CSS_SELECTOR, ".css-vw73h2")
            submit_application_btn = self.driver.find_element(By.CSS_SELECTOR, ".css-10eonrg")
            random_questions = False

            if 'questions' in questions_title:
                questions = self.driver.find_elements(By.CLASS_NAME, "ia-Questions-item")
                for question in questions:
                    question_text = self.driver.find_element(By.CSS_SELECTOR, ".css-dtssv9").text.lower()
                    # written response
                    if 'experience' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR,
                                                                                            add_default_experience)
                        time.sleep(1)
                    elif 'python experience' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_python)
                        time.sleep(1)
                    elif 'javascript experience' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_javascript)
                        time.sleep(1)
                    elif 'analysis experience' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_analysis)
                        time.sleep(1)
                    elif 'address' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_address)
                        time.sleep(1)
                    elif 'city' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_city)
                        time.sleep(1)
                    elif 'github url' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_github)
                        time.sleep(1)
                    elif 'aws experience' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_aws)
                        time.sleep(1)
                    elif 'django experience' or 'selenium experience' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_django)
                        time.sleep(1)
                    elif 'leadership experience' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_leadershipdevelopment)
                        time.sleep(1)
                    elif 'programming experience' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_programming)
                        time.sleep(1)
                    elif 'salary' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_salary)
                        time.sleep(1)
                    elif 'gender' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_gender)
                        time.sleep(1)
                    elif 'postal' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_postal)
                        time.sleep(1)
                    elif 'state' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_state)
                        time.sleep(1)
                    elif 'linkedin url' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_linkedin)
                        time.sleep(1)
                    elif 'college' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_university)
                        time.sleep(1)
                    elif 'java experience' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_java)
                        time.sleep(1)
                    elif 'city' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, '[id^="input-q"]').send_keys(Keys.CLEAR, add_city)
                        time.sleep(1)

                    # Multiple choice response
                    elif 'authorization' or 'authorized to work' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, f".css-d0lawn:contains{add_workauthorized}").click()
                        time.sleep(1)
                    elif 'level of education' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, f".css-d0lawn:contains{add_education}").click()
                        time.sleep(1)
                    elif 'sponsorship' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, f".css-d0lawn:contains{add_valid_cert}").click()
                        time.sleep(1)
                    elif 'commute' or 'travel' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, f".css-d0lawn:contains{add_commute}").click()
                        time.sleep(1)
                    elif 'veteran' or 'disability' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, f".css-d0lawn:contains{add_disability}").click()
                        time.sleep(1)
                    elif 'valid' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, f".css-d0lawn:contains{add_sponsorship}").click()
                        time.sleep(1)
                    elif 'gender' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, f".css-d0lawn:contains{add_sponsorship}").click()
                        time.sleep(1)
                    elif 'authorization' or 'authorized' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, f".css-d0lawn:contains{add_sponsorship}").click()
                        time.sleep(1)
                    elif 'hear about this position' in question_text.lower():
                        question.find_element(By.CSS_SELECTOR, f".css-81omu8:contains{add_sponsorship}").click()
                        time.sleep(1)
                    else:
                        unknown_multi_questions = question.find_element(By.CSS_SELECTOR, 'css-81omu8')
                        unknown_written_question = question.find_element(By.CSS_SELECTOR, '[id^="input-q"]')
                        if unknown_written_question:
                            unknown_written_question.send_keys(add_default_experience)
                        if unknown_multi_questions:
                            question.find_element(By.CSS_SELECTOR, f".css-81omu8:contains{default_unknown_multi}").click()

            # clicks the submit or contiune btn
            if questions_continue_btn:
                questions_continue_btn.click()
                time.sleep(5)
            elif qualifications_continue_btn:
                qualifications_continue_btn.click()
                time.sleep(5)
            elif resume_continue_btn:
                resume_continue_btn.click()
                time.sleep(5)
            elif experience_continue_btn:
                experience_continue_btn.click()
                time.sleep(5)
            elif submit_application_btn:
                submit_application_btn.click()
                time.sleep(5)

    # Clicks apply now btn if valid
    def apply_btn_func(self):
        apply_btn = self.driver.find_element(By.CLASS_NAME, "ia-IndeedApplyButton")
        if apply_btn:
            time.sleep(5)
            apply_btn.click()
            time.sleep(15)
        else:
            self.click_jobs()
            time.sleep(2)


if __name__ == '__main__':
    with open('config.json') as config_file:
        data = json.load(config_file)

    bot = Wfajobs_apply(data)
    bot.login()
    bot.search_jobs()
    bot.click_jobs()