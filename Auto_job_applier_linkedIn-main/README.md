# LinkedIn AI Auto Job Applier 🤖
This is an web scraping bot that automates the process of job applications on LinkedIn. It searches for jobs relevant to you, answers all questions in application form, customizes your resume based on the collected job information, such as skills required, description, about company, etc. and applies to the job. Can apply 100+ jobs in less than 1 hour. 


## ✨ Content
- [Introduction](#linkedin-ai-auto-job-applier-)
- [Install](#%EF%B8%8F-how-to-install)
- [Configure](#-how-to-configure)
- [Updates](#%EF%B8%8F-major-updates-history)
- [Disclaimer](#-disclaimer)
- [Terms and Conditions](#%EF%B8%8F-terms-and-conditions)
- [License](#%EF%B8%8F-license)

<br>

## ⚙️ How to install

1. [Python 3.10](https://www.python.org/) or above. Visit https://www.python.org/downloads/ to download and install Python, or for windows you could visit Microsoft Store and search for "Python". **Please make sure Python is added to Path in System Environment Variables**.
2. Install necessary [Undetected Chromedriver](https://pypi.org/project/undetected-chromedriver/), [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) and [Setuptools](https://pypi.org/project/setuptools/) packages. After Python is installed, OPEN a console/terminal or shell, Use below command that uses the [pip](https://pip.pypa.io/en/stable) command-line tool to install these 3 package.
  ```
  pip install undetected-chromedriver pyautogui setuptools openai flask-cors flask
  ```
3. Download and install latest version of [Google Chrome](https://www.google.com/chrome) in it's default location, visit https://www.google.com/chrome to download it's installer.
4. (Not needed if you set `stealth_mode = True` in `config/settings.py` ) Download and install the appropriate [Chrome Driver](https://googlechromelabs.github.io/chrome-for-testing/) for Google Chrome and paste it in the location Chrome was installed, visit https://googlechromelabs.github.io/chrome-for-testing/ to download.
  <br> <br>
  ***OR*** 
  <br> <br>
  If you are using Windows, click on `windows-setup.bat` available in the `/setup` folder, this will install the latest chromedriver automatically.

[back to index](#-content)

<br>

## 🔧 How to configure
1. Open `personals.py` file in `/config` folder and enter your details like name, phone number, address, etc. Whatever you want to fill in your applications.
2. Open `questions.py` file in `/config` folder and enter your answers for application questions, configure wether you want the bot to pause before submission or pause if it can't answer unknown questions.
3. Open `search.py` file in `/config` folder and enter your search preferences, job filters, configure the bot as per your needs (these settings decide which jobs to apply for or skip).
4. Open `secrets.py` file in `/config` folder and enter your LinkedIn username, password to login and OpenAI API Key for generation of job tailored resumes and cover letters (This entire step is optional). If you do not provide username or password or leave them as default, it will login with saved profile in browser, if failed will ask you to login manually.
5. Open `settings.py` file in `/config` folder to configure the bot settings like, keep screen awake, click intervals (click intervals are randomized to seem like human behavior), run in background, stealth mode (to avoid bot detection), etc. as per your needs.
6. (Optional) Don't forget to add you default resume in the location you mentioned in `default_resume_path = "all resumes/default/resume.pdf"` given in `/config/questions.py`. If one is not provided, it will use your previous resume submitted in LinkedIn or (In Development) generate custom resume if OpenAI APT key is provided!
7. Run `runAiBot.py` and see the magic happen.
8. To run the Applied Jobs history UI, run `app.py` and open web browser on `http://localhost:5000`.

[back to index](#-content)

<br>

## 🗓️ Major Updates History:
### Jan 20, 2026
- You can now simultaneously use chrome, while bot continues applying in a new window

### Jul 20, 2024
- Contributions from community have been added
- Better AI support, minor bug fixes

### Nov 28, 2024
- Patched to work for latest changes in Linkedin.
- Users can now select to follow or not follow companies when submitting application.
- Frameworks for future AI Developments have been added.
- AI can now be used to extract skills from job description. 

### Oct 16, 2024
- Framework for OpenAI API and Local LLMs
- Framework for RAG

### Sep 09, 2024
- Smarter Auto-fill for salaries and notice periods
- Robust Search location filter, will work in window mode (No need for full screen)
- Better logic for Select and Radio type questions
- Proper functioning of Decline to answer questions in Equal Employment opportunity questions
- Checkbox questions select fail bug fixed
- Annotations are clearer in instructions for setup

### Sep 07, 2024
- Annotations for developers
- Robust input validations
- Restructured config file
- Fixed pagination bug

### Aug 21, 2024
- Performance improvements (skip clicking on applied jobs and blacklisted companies)
- Stop when easy apply application limit is reached
- Added ability to discard from pause at submission dialogue box
- Added support for address input
- Bug fixed radio questions, added support for physical disability questions
- Added framework for future config file updates

### June 19, 2024
- Major Bug fixes (Text Area type questions)
- Made uploading default resume as not required

### May 15, 2024
- Added functionality for textarea type questions `summary`, `cover_letter`(Summary, Cover letter); checkbox type questions (acknowledgements)
- Added feature to skip irrelevant jobs based on `bad_words` 
- Improved performance for answering questions
- Logic change for masters students skipping
- Change variable names `blacklist_exceptions` -> `about_company_good_words` and `blacklist_words` -> `about_company_bad_words`
- Added session summary for logs
- Added option to turn off "Pause before Submit" until next run

### May 05, 2024
- For questions similar to "What is your current location?", City posted in Job description will be posted as the answer if `current_city` is left empty in the configuration
- Added option to over write previously saved answers for a question `overwrite_previous_answers`
- Tool will now save previous answer of a question
- Tool will now collect all available options for a Radio type or Select type question
- Major update in answering logic for Easy Apply Application questions
- Added Safe mode option for quick stable launches `safe_mode`

### May 04, 2024
- Added option to fill in "City, state, or zip code" search box `search_location`
- Bug fixes in answering City or location question


[back to index](#-content)

<br>

## 📜 Disclaimer

**This program is for educational purposes only. By downloading, using, copying, replicating, or interacting with this program or its code, you acknowledge and agree to abide by all the Terms, Conditions, Policies, and Licenses mentioned, which are subject to modification without prior notice. The responsibility of staying informed of any changes or updates bears upon yourself. Additionally, kindly adhere to and comply with LinkedIn's terms of service and policies pertaining to web scraping. Usage is at your own risk. The creators and contributors of this program emphasize that they bear no responsibility or liability for any misuse, damages, or legal consequences resulting from its usage.**


## 🏛️ Terms and Conditions

Please consider the following:

- **LinkedIn Policies**: LinkedIn has specific policies regarding web scraping and data collection. The responsibility to review and comply with these policies before engaging, interacting, or undertaking any actions with this program bears upon yourself. Be aware of the limitations and restrictions imposed by LinkedIn to avoid any potential violation(s).

- **No Warranties or Guarantees**: This program is provided as-is, without any warranties or guarantees of any kind. The accuracy, reliability, and effectiveness of the program cannot be guaranteed. Use it at your own risk.

- **Disclaimer of Liability**: The creators and contributors of this program shall not be held responsible or liable for any damages or consequences arising from the direct or indirect use, interaction, or actions performed with this program. This includes but is not limited to any legal issues, loss of data, or other damages incurred.

- **Use at Your Own Risk**: It is important to exercise caution and ensure that your usage, interactions, and actions with this program comply with the applicable laws and regulations. Understand the potential risks and consequences associated with web scraping and data collection activities.

- **Chrome Driver**: This program utilizes the Chrome Driver for web scraping. Please review and comply with the terms and conditions specified for [Chrome Driver](https://chromedriver.chromium.org/home).


## ⚖️ License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

See [AGPLv3 LICENSE](LICENSE) for more info.


<br>

[back to index](#-content)
