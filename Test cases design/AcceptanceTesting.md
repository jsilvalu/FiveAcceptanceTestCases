# :blue_book: Introduction

### What is acceptance testing?
In software engineering, acceptance testing is performed to establish the degree of confidence in a system as determined by its degree of adherence to needs and/or requirements.
The International Software Testing Qualification Board (ISTQB) defines "Acceptance" as: 

> "Formal testing with respect to user needs, requirements and business
> processes, performed to determine whether a system satisfies
> acceptance criteria that enable the user, customer or other authorised
> entity to determine whether or not to accept the system".

### Types

Some of the most important acceptance testing types are:
| Type |Description  |
|--|--|
|User Acceptance Testing (UAT)  | It helps to determine whether the system is working for the user with the given specific requirements. Sometimes, customers perform this testing. |
|Business Acceptance Testing (BAT)  | It helps to check whether the system satisfies the business requirements and specifications. The main aim of this testing is to help in increasing business profits by considering market strategies and technologies.
Contract Acceptance Testing (CAT)  |The name itself says that it helps to test the product with all acceptance test cases within the contract period of time. The contract may be like payment will be done before the product goes live or after the product goes live.  |
|Alpha Testing  |Specialized Testers will perform this testing to check any bugs have occurred. Also, they help to give suggestions to improve product usability in a controlled manner with the oficial documentation.  |
|Beta Testing  |Helps to grab the bugs or any issues of a product. End-Users will perform this testing with an uncontrolled manner as an ad-hoc.  |

## :bulb: Case analysis
The information received to date is based on performing acceptance tests on a website where the entire focus of the tester should be on the front-end. The objective is to design five critical test cases on https://www.voicemod.net/. For these test cases I will not consider the "Tuna" part of the software as it bundles a lot of functionalities and the instructions detail to focus on "Voicemod". However, some possible test cases for "Tuna" could be related to sound search, sound playback, filters, categories, tags, upload to sound...
After an exploratory testing session we can highlight several specific test cases on the website.



# :ballot_box_with_check: Test Cases Design

## <center> Test Case #1 - *Download Voicemod for free* </center>

**Description:** It is possible to download the executable by clicking on the button on the main page.



| User Story |
|--|
| **As an** end user/customer|--|
**I want** to use VOICEMOD|--|
**So I can** click on the "Download Voicemod for Free" button to download the executable |




**Desired behaviour:** Using the button "DOWNLOAD VOICEMOD FOR FREE" the user will be able to download the executable file to install the software on his computer.

**Steps to test:** 
 1. Access to https://www.voicemod.net/
 2. Click on "DOWNLOAD VOICEMOD FOR FREE"
 3. Verify that the download of the executable happens

**Feedback:** 

> This is simply one of the most critical test cases as the core
> business is in this app, all users must be able to access it.

## <center> Test Case #2 - *Create a new account* </center>

**Description:** It´s possible to create a new account 

| User Story |
|--|
| **As an** end user/customer|--|
**I want** to create a new account in VOICEMOD |--|
**So I can**  |

**Desired behaviour:** 

- Insert the email address.
- Receive the confirmation code in the email account

**Steps to test:**
 1. Access to https://www.voicemod.net/
 2. Click on "My Acount"
 3. Insert the email adress.
 4. Verify that we receive a verification code in our email.
 5. Insert the verification code on the website.
 6. Verify that we´ve finished the process.

**Feedback:** 

> The creation of a new user is a critical test case as attracting new
> users to the app should not be a problem in the production
> environment.


## <center> **Test Case #3 - *Main links*** </center>

**Description:** The banner links must redirect to the correct website.

| User Story |
|--|
| **As an** end user/customer|--|
**I want** to browse the sections of the website https://www.voicemod.net/|--|
**So I can** use the links in the banner |

**Desired behaviour:** 
By clicking on the links "Voicemod" logo, "Soundboard", "FreeSounds"... I can navigate to different sections of the front-end.

**Steps to test:**
 1. Access to https://www.voicemod.net/
 2. Click on the different links.
 3. Verify that link redirect us to another sections.
 
**Feedback:** 

> The user must be able to navigate through the different sections of
> the website, which is why the links in the banner must be accessible.
> These links are statistically the most used, since according to the UX
> the focus of a customer is on the top of the page most of the time
> during the first moments of access to the website.




## <center> Test Case #4 - *FAQ searching* </center>

**Description:** 

| User Story |
|--|
| **As an** end user/customer|--|
**I want** to search a question in FAQ section|--|
**So I can** use the search bar, write a topic and check the results |

**Desired behaviour:** 
By using the search bar, we will be able to enter a topic we wish to search for and the page will give us results relevant to our search.

**Steps to test:**
 1. Access to https://www.voicemod.net/
 2. Click on FAQ link.
 3. Write an input parameter in the search bar.
 4. Input ENTER.
 5. Verify that we have been redirected to the page "Search results".


**Feedback:** 

> All customers should be able to solve their problems themselves by
> consulting the FAQ section because if the customer can easily solve
> the problem by himself he will not overwhelm the technical support
> team.



## <center> Test Case #5 -*Feedback & Support* </center>

**Description:** Using the URL https://www.voicemod.net/support/?source=helpcenter I will be able to submit a support request.

| User Story |
|--|
| **As an** end user/customer|--|
**I want** to submit a support request|--|
**So I can** complete the form and send it|

**Desired behaviour:** 
By accessing the support form and completing it I will be able to submit my support request.

**Steps to test:**
 1. Access to https://www.voicemod.net/
 2. Click on FAQ link.
 3. Click on Submit a request.
 4. Enter a value in "Let´s talk!" among the drop-down options
 5. Enter a message
 6. Enter a name
 7. Enter a Email address
 8. Enter a Country
 9. Enter a platform
 10. Select a product  among the drop-down options
 11. Check the checkbox of the privacy policy
 12. Verify that I am human
 13. Click on "Send" buttom.

**Feedback:** 

> This is an important but not critical test case because in case of
> need, if a user cannot solve a problem in the FAQ, he/she should be
> able to contact the technical support team. This is very important
> because it gives the feeling that the brand provides all the necessary
> procedures to satisfy the customer.




## :heavy_plus_sign: Other interesting test cases:

- Of course, the page should be up as much of the time as possible according to demand.
- The brand logo can be expected to be in the top left corner according to UX standards.
- It should be possible to change languages using the most popular plugins such as in chrome using Google Translator, in this case some texts are affected by language changes "breaking" the front-end.
- Check the first login and flows like Set your name, Upload a new image, Set up a banner, Profile bio.