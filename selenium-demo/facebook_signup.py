from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FacebookSignup:
    def __init__(self):
        self.driver = self.setup_driver()
        self.wait = WebDriverWait(self.driver, 10)

    def setup_driver(self):
        """Set up Chrome WebDriver with options."""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        return webdriver.Chrome(options=chrome_options)

    def navigate_to_signup(self):
        """Navigate to Facebook login and click 'Create new account'."""
        self.driver.get("https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F")
        create_account = self.driver.find_element(by=By.LINK_TEXT, value='Create new account')
        create_account.click()

    def fill_personal_info(self, first_name, last_name):
        """Fill in first and last name fields."""
        self.driver.find_element(by=By.ID, value="_R_1cl2p4jikacppb6amH1_").send_keys(first_name)
        self.driver.find_element(by=By.ID, value="_R_1kl2p4jikacppb6amH1_").send_keys(last_name)

    def select_custom_dob(self, label, value):
        """Select an option from a custom dropdown (e.g., day, month, year)."""
        combobox = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[@aria-label='{label}']")
        ))
        combobox.click()

        option_xpath = f"//div[@role='option'][normalize-space()='{value}']"
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option.click()

    def select_dob(self, day, month, year):
        """Select date of birth."""
        self.select_custom_dob("Select day", day)
        self.select_custom_dob("Select month", month)
        self.select_custom_dob("Select year", year)

    def select_gender(self, gender_value):
        """Select gender from dropdown."""
        gender_trigger_xpath = "//div[@role='combobox'][.//span[contains(text(), 'Select your gender')]]"
        gender_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, gender_trigger_xpath)))
        gender_menu.click()

        option_xpath = f"//div[@role='option'][normalize-space()='{gender_value}']"
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option.click()

    def fill_credentials(self, email, password):
        """Fill in email and password fields."""
        email_field_xpath = "//input[..//label[contains(text(), 'Mobile number or email address')]]"
        email_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, email_field_xpath)))
        email_input.clear()
        email_input.send_keys(email)

        password_xpath = "//input[@type='password'][..//label[text()='Password']]"
        password_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
        password_input.clear()
        password_input.send_keys(password)

    def submit_form(self):
        """Submit the signup form."""
        submit_xpath = "//div[@role='button'][.//span[text()='Submit']]"
        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, submit_xpath)))
        submit_button.click()

    def run_signup(self, first_name, last_name, day, month, year, gender, email, password):
        """Run the complete signup process."""
        self.navigate_to_signup()
        self.fill_personal_info(first_name, last_name)
        self.select_dob(day, month, year)
        self.select_gender(gender)
        self.fill_credentials(email, password)
        self.submit_form()


if __name__ == "__main__":
    signup = FacebookSignup()
    signup.run_signup(
        first_name="John",
        last_name="Doe",
        day="25",
        month="May",
        year="1995",
        gender="Male",
        email="your_email@example.com",
        password="YourStrongPassword123!"
    )
