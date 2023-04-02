from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def find_element_by_xpath(element):


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.set_window_size(1920, 1080)

    url = 'https://www.inmuebles24.com/departamentos-en-renta-en-ciudad-de-mexico-con-mascotas-mas-de-2-recamaras-mas-de-1-estacionamiento-mas-de-80-metros-cuadrados-cubiertos-hasta-18000-pesos.html'

    driver.get(url)

    bedroom_button = driver.find_element(By.XPATH, '//div[@data-qa="filters-environmentBedroom"][1]')
    bedroom_button.click()

    min_bedrooms_select = driver.find_element(By.XPATH, '//div[@data-qa="filters-recámaras-from"][1]')
    max_bedrooms_select = driver.find_element(By.XPATH, '//div[@data-qa="filters-recámaras-until"][1]')

    min_bedrooms_select.click()

    min_2_bedrooms = driver.find_element(By.XPATH, '//div[@data-qa="filters-from-2recámaras"][1]')
    min_2_bedrooms.click()

    # postings = driver.find_element(By.CLASS_NAME, 'postings-container')
    # postings_html = postings.get_attribute("outerHTML")
    #
    # soup = BeautifulSoup(postings_html, "html.parser")
    #
    # with open('index.html', 'w') as file:
    #     file.write(soup.prettify())
