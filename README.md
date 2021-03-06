# BlogHub
#### By Mary Njenga
## Table of Content
+ [Description](#description)
+ [Installation Requirement](#Installation)
+ [Behaviour Driven Development](#Behaviour-Driven-Development)
+ [Technology Used](#technology-used)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

****
## Description
Personal blogging website where you can create and share your opinions and other users can read and comment on them.Additionally, the website has a feature that displays random quotes to inspire users.

## Site image
![Site Image](app/static/photos/site.png)

## Live link
`https://bloghublite.herokuapp.com/`
## Installation
### Requirements
* python3.6
* pip 

### Installation process
* Open terminal
* run `git clone https://github.com/mary-wan/BlogSite.git`

### Dependancy Installation process
```
$ pip install -r requirements.txt

```

### Running the Application
To view the website run the command
```
$ chmod a+x start.sh
$ ./start.sh

```
To run the tests run the command
```
$ python3.6 manage.py test

```
## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|  Form validation    | User submits empty or invalid data on form | An error is message is displayed    |
|  Sign up   | User enters a input for all fields and submits    | User is redirected to log in page|
|  Log in   | User enters valid details  | User is logged in and redirected to main page|
|  New blog   | User enters submits a new blog  | Blog is added to list |
|  Comment   | User clicks on comment link | All comments are displayed and user can submit a new comment|
|  Profile   | User clicks on account link | Account details and posts made by the user are displayed |
|  Log out   | User logs out |Redirected to main page and a message shown |

****

[Go Back to the top](#BlogHub)
## Technology Used
* Python
* Html
* css

****
[Go Back to the top](#BlogHub)
## Licence
MIT License

Copyright (c) 2021 Mary Njenga

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


****
[Go Back to the top](#BlogHub)
## Authors Info
* Slack Profile - [Mary Njenga](https://app.slack.com/client/T077KKCG6/GLRQR61NW/user_profile/U027VKL1WLT?cdn_fallback=1)
* Email - [Mary Njenga](mary.njenga@student.moringaschool.com)

[Go Back to the top](#BlogHub)
