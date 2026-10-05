# Auto Job Applier for LinkedIn

from modules.helpers import get_default_temp_profile, make_directories
from config.settings import run_in_background, stealth_mode, disable_extensions, safe_mode, file_name, failed_file_name, logs_folder_path, generated_resume_path
from config.questions import default_resume_path
if stealth_mode:
    import undetected_chromedriver as uc
else: 
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    # from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from modules.helpers import find_default_profile_directory, critical_error_log, print_lg
from selenium.common.exceptions import SessionNotCreatedException

def get_local_chrome_major_version() -> int | None:
    '''
    Detects the major version number of the locally installed Google Chrome
    (e.g. 151), so ChromeDriver downloads can be pinned to a matching build
    instead of always grabbing the latest driver, which can be ahead of the
    installed browser and cause "session not created" errors.
    '''
    import re, subprocess, platform
    try:
        system = platform.system()
        if system == "Darwin":
            cmd = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"]
        elif system == "Windows":
            cmd = ["reg", "query", "HKCU\\Software\\Google\\Chrome\\BLBeacon", "/v", "version"]
        else:
            cmd = ["google-chrome", "--version"]
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode(errors="ignore")
        match = re.search(r"(\d+)\.\d+\.\d+\.\d+", output)
        if match:
            return int(match.group(1))
    except Exception:
        pass
    return None

def createChromeSession(isRetry: bool = False):
    make_directories([file_name,failed_file_name,logs_folder_path+"/screenshots",default_resume_path,generated_resume_path+"/temp"])
    # Set up WebDriver with Chrome Profile
    options = uc.ChromeOptions() if stealth_mode else Options()
    if run_in_background:   options.add_argument("--headless")
    if disable_extensions:  options.add_argument("--disable-extensions")

    print_lg("IF YOU HAVE MORE THAN 10 TABS OPENED, PLEASE CLOSE OR BOOKMARK THEM! Or it's highly likely that application will just open browser and not do anything!")
    profile_dir = find_default_profile_directory()
    if isRetry:
        print_lg("Will login with a guest profile, browsing history will not be saved in the browser!")
    elif profile_dir and not safe_mode:
        options.add_argument(f"--user-data-dir={profile_dir}")
    else:
        print_lg("Logging in with a guest profile, Web history will not be saved!")
        options.add_argument(f"--user-data-dir={get_default_temp_profile()}")
    if stealth_mode:
        # try:
        #     driver = uc.Chrome(driver_executable_path="C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe", options=options)
        # except (FileNotFoundError, PermissionError) as e:
        #     print_lg("(Undetected Mode) Got '{}' when using pre-installed ChromeDriver.".format(type(e).__name__))
            print_lg("Downloading Chrome Driver... This may take some time. Undetected mode requires download every run!")
            # Pin the ChromeDriver download to the locally installed Chrome's major
            # version. Without this, undetected_chromedriver can grab the newest
            # driver build (e.g. 152) even though the installed browser is still on
            # an older version (e.g. 151), causing "session not created: This
            # version of ChromeDriver only supports Chrome version X" errors.
            local_chrome_major_version = get_local_chrome_major_version()
            if local_chrome_major_version:
                driver = uc.Chrome(options=options, version_main=local_chrome_major_version)
            else:
                driver = uc.Chrome(options=options)
    else: driver = webdriver.Chrome(options=options) #, service=Service(executable_path="C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe"))
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
    return options, driver, actions, wait

try:
    options, driver, actions, wait = None, None, None, None
    options, driver, actions, wait = createChromeSession()
except SessionNotCreatedException as e:
    critical_error_log("Failed to create Chrome Session, retrying with guest profile", e)
    options, driver, actions, wait = createChromeSession(True)
except Exception as e:
    msg = 'Seems like Google Chrome is out dated. Update browser and try again! \n\n\nIf issue persists, try Safe Mode. Set, safe_mode = True in config.py'
    if isinstance(e,TimeoutError): msg = "Couldn't download Chrome-driver. Set stealth_mode = False in config!"
    print_lg(msg)
    critical_error_log("In Opening Chrome", e)
    from pyautogui import alert
    alert(msg, "Error in opening chrome")
    try: driver.quit()
    except NameError: exit()
    
