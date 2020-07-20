link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button_basket(browser):

    browser.get(link)
    add_button = browser.find_element_by_class_name("btn-add-to-basket")
    assert add_button, "No such element"
