from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path="/home/qq097/Downloads/chromedriver_linux64/chromedriver")
driver.get("https://trello.com/login")

driver.find_element_by_id("googleButton").click()

driver.find_element_by_id("identifierId").send_keys("Email")
driver.find_element_by_xpath("//div[@id='identifierNext']").click()
driver.implicitly_wait(10)

driver.find_element_by_name("password").send_keys("Password")
driver.find_element_by_id("passwordNext").click()
driver.implicitly_wait(10)

driver.find_element_by_css_selector("div.chrome.chrome-92.linux.body-tabbed-page:nth-child(1) "
                                    "div._2ffa7ex19Eoxvc:nth-child(1) div._2W6d4IdyPwMlNi main._13yPKk9EPKnvGB:nth-child(2) "
                                    "div.member-boards-view div.js-boards-page div.js-react-root div.home-container "
                                    "div.home-sticky-container div.all-boards:nth-child(2) div.content-all-boards "
                                    "div.boards-page-board-section.mod-no-sidebar:nth-child(2) "
                                   "div:nth-child(2) ul.boards-page-board-section-list li.boards-page-board-section-list-item:nth-child(5) > div.board-tile.mod-add").click()

driver.find_element_by_class_name("_2C8dwcFUoIOCYP").send_keys("Goa Trip Preparation")
driver.find_element_by_xpath("//button[contains(text(),'Create board')]").click()

driver.find_element_by_class_name("list-name-input").send_keys("To Do")
driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/form[1]/div[1]/input[1]").click()

driver.find_element_by_class_name("js-add-a-card").click()
driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/textarea[1]").send_keys("Shopping")
driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]").click()

driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/textarea[1]").send_keys("Booking Tickets")
driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]").click()

driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/textarea[1]").send_keys("Booking Hotels")
driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]").click()


driver.find_element_by_class_name("list-name-input").send_keys("Doing")
driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/form[1]/div[1]/input[1]").click()

driver.find_element_by_class_name("list-name-input").send_keys("Done")
driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[3]/form[1]/div[1]/input[1]").click()
driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[4]/form[1]/div[1]/a[1]").click()

driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]").click()
driver.find_element_by_xpath("//a[contains(text(),'Move all cards in this list…')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Doing')]").click()

driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/a[1]").click()
driver.find_element_by_xpath("//a[contains(text(),'Move all cards in this list…')]").click()
driver.find_element_by_link_text("Done").click()

driver.close()
driver.quit()
