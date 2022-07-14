#the goal is to test the quiz function on the LessLikely website
#step 1: open https://www.albany.edu/~BP754362/tips.html
#step 2: locate the quiz page and complete the quiz
#step 3: check if the url is the correct url

class Pg_Locators(object):
    #quiz page locators
    page_link_txt = "Stress Quiz"
    calc_btn_xpath = "/html/body/div/div[2]/div[2]/div[2]/div[1]/button"

    #id locator for each question in the quiz
    q1 = "input_q1"
    q2 = "input_q2"
    q3 = "input_q3"
    q4 = "input_q4"
    q5 = "input_q5"
