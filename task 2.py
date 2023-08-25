from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

desired_capabilities= {
    "platformName": "android", 
    "appActivity": "com.atg.world.activity.SplashActivity", 
    "appWaitDuration": "5000", "appExecTimeout": "50000", 
    "uiautomator2ServerLaunchTimeout": "50000", 
    "uiautomator2ServerInstallTimeout": "50000", 
    "appPackage": "com.ATG.World", 
    "deviceName": "emulator-5554", 
    "driver": "http://localhost:4723/wd/hub"
    #"app":"E:\\Courses\\Python\\BANAO\\app-chat-debug.apk"
    }

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)
wait=WebDriverWait(driver,100)


#File access permission allow
driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_button").click()
wait.until(ec.visibility_of_element_located((By.ID, "com.ATG.World:id/getStartedTv")))
#time.sleep(2)

#Get Started
driver.find_element(By.ID,"com.ATG.World:id/getStartedTv").click()
wait.until(ec.visibility_of_element_located((By.ID, "com.ATG.World:id/login_email")))
#time.sleep(2)


#Join ATG sign in 
driver.find_element(By.ID,"com.ATG.World:id/login_email").click()
time.sleep(3)

# signing in eith credentials
def test_LoginWithRightCredential():
        #Email
        wait.until(ec.visibility_of_element_located((By.ID, "com.ATG.World:id/email_phone_login")))
        email1= driver.find_element(By.ID,"com.ATG.World:id/email_phone_login")
        email1.click()
        email1.send_keys("wiz_saurabh@rediffmail.com")
        driver.find_element(By.ID,"com.ATG.World:id/signinbutton").click()

        #Password
        wait.until(ec.visibility_of_element_located((By.ID, "com.ATG.World:id/password")))
        driver.find_element(By.ID,"com.ATG.World:id/password").click()
        driver.find_element(By.ID,"com.ATG.World:id/password").send_keys("Pass@123")
        driver.find_element(By.ID,"com.ATG.World:id/passwordloginbutton").click()

        print("test_LoginWithRightCredential passed")

test_LoginWithRightCredential()

#Got IT
wait.until(ec.visibility_of_element_located((By.ID, "com.ATG.World:id/btnGotit")))
driver.find_element(By.ID,"com.ATG.World:id/btnGotit").click()


#Pen
wait.until(ec.visibility_of_element_located((By.ID, "com.ATG.World:id/fab")))
driver.find_element(By.ID,"com.ATG.World:id/fab").click()

#image fab
wait.until(ec.visibility_of_element_located((By.ID, "com.ATG.World:id/image_fab_clicked")))
driver.find_element(By.ID,"com.ATG.World:id/image_fab_clicked").click()

#post action
wait.until(ec.visibility_of_element_located((By.ID, "com.ATG.World:id/toolbar_post_action")))
driver.find_element(By.ID,"com.ATG.World:id/toolbar_post_action").click()

#caption
wait.until(ec.visibility_of_element_located((By.ID, "com.ATG.World:id/caption_edit_text")))
driver.find_element(By.ID,"com.ATG.World:id/caption_edit_text").click()

#post
wait.until(ec.visibility_of_element_located((By.ID, "com.ATG.World:id/toolbar_post_action")))
driver.find_element(By.ID,"com.ATG.World:id/toolbar_post_action").click()
