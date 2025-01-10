from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.python.org/events/")

event_names = driver.find_elements(By.CLASS_NAME, "event-title")
event_times = driver.find_elements(By.TAG_NAME, "time")
event_locations = driver.find_elements(By.CLASS_NAME, "event-location")


event_names_list = []
event_times_list = []
event_locations_list = []

for x in event_names:
    event_names_list.append(x.text)

for x in event_times:
    event_times_list.append(x.text)

    
for x in event_locations:
    event_locations_list.append(x.text)



events = [
    {"name":name,
     "time": time,
     "location":location
     }
    for name, time, location in zip(event_names_list, event_times_list, event_locations_list)
]

print(events[1])

driver.quit()