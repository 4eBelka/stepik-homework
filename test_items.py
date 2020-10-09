link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_cart_button(browser):
    browser.get(link)
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(button) > 0, "Cart button not found"
