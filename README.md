
<br />
<div align="center">
  <h3 align="center">Automation Testing</h3>
  <p align="center"> 5 acceptance test cases </p>
</div>
<br />


<!-- ABOUT THE PROJECT -->
## :open_file_folder: About The Project

The following project contains the development of five Selenium-based acceptance test cases with Python.
These five test cases were analysed theoretically in the root directory of the repository.


### Built With

* [Selenium](https://www.selenium.dev/)
* [Python](https://www.python.org/), in this case i used Python 3.10
* [Pytest](https://docs.pytest.org/)




<!-- GETTING STARTED -->
## :white_check_mark: Getting Started

### Installation

_To prepare the necessary environment for the execution of the process you can follow the steps below: ._

1. **Access** to [my repository](https://github.com/jsilvalu/FiveAcceptanceTestCases)
2. **Clone** the repo
   ```sh
   git clone https://github.com/jsilvalu/FiveAcceptanceTestCases
   ```
   
3. Install **Python** from the official site:
[Download Python](https://www.python.org/downloads/)

4. Install **Selenium Webdriver** packages:
   Via **pip**:
   ```sh
   pip install selenium
   ```

5. Install **webdriver_manager**:

Via **pypi**:
[Download webdriver_manager](https://pypi.org/project/webdriver-manager/)

Via **pip**:
   ```sh
   pip install webdriver-manager
   ```



## Improvements & Personal note:

There are some improvements that I would have liked to develop that could be interesting:

- The solution has been developed on MAC OS as there is no version of    Voicemod for MAC OS, I have not been able to verify the download of      the file. The perfect assertion in this verification would be to       check if Selenium has correctly downloaded the executable file, we       could check the binaries, size, metadata... However, in my       environment I use MAC OS and I have seen that there is no version       available to download voicemod on MAC. We can check it with       os.path.isfile (). 
- The correct way to verify the creation of a user    would be to use an email service with which emails can be generated    and make use of    an API with which the verification code can be obtained.
- To use the solution in CI/CD pipelines I would use a user    agent configuration similar to the following:

        chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["window-size"])
        chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["ignore-errors:"])
        chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["allow-running"])
        chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["disable-extensions"])
        chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["proxy-server"])
        chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["proxy-bypass"])
        chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["maximized"])
        chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["disable-gpu"])
        chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["disable-dev"])
        chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["no-sandbox"])
- It would be possible to customize the resolution with a code like this:

       def config_resolution(driver, resolucion):
            if resolucion == 'default':
                driver.maximize_window()
            else:
                ancho_alto = resolucion.split('x')
                ancho, alto = ancho_alto[0], ancho_alto[1]
                driver.set_window_size(ancho, alto)
