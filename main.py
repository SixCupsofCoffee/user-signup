#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import cgi
import re

page_header = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
    <h1>User Signup</h1>
</head>
<body>
"""

# html boilerplate for bottom of page
page_footer = """
</body>
</html>
"""

# basic signup form
# includes tables and error message substitution
signup_form = """
<form action="/" method="post">
<table>
    <tr><td><label>Username: </td></label><td><input type="text" name="username" value="%(usern)s"/></td> <td><span class="error">%(une)s</span></td></tr>
    <tr><td><label>Password: </td></label><td><input type="password" name="password1"/></td> <td><span class="error">%(pwve)s</span></td></tr>
    <tr><td><label>Password again: </td></label><td><input type="password" name="password2"/></td> <td><span class="error">%(pwme)s</span></td></tr>
    <tr><td><label>Email (optional): </td></label><td><input type="text" name="email"/></td> <td><span class="error">%(eme)s</tr>
</table>
<input type="submit">
    </form>
    """

class Index(webapp2.RequestHandler):

    def write_form(self, usern="", une="", pwve="", pwme="", eme=""):
        usern = self.request.get("username")

        if une == None:
            une = ""
        if pwve == None:
            pwve = ""
        if pwme == None:
            pwme = ""
        if eme == None:
            eme = ""
        self.response.write(page_header + signup_form % {"usern":usern, "une":une, "pwve":pwve, "pwme":pwme, "eme":eme} + page_footer)

    def get(self):
        self.write_form()

    def post(self):

        def valid_username(usern):
            user_regex = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
            if user_regex.match(usern) == None:
                return "That is not a valid username"
            else:
                return None

        def valid_password(pw1):
            user_password_regex = re.compile(r"^.{3,20}$")
            if user_password_regex.match(pw1) == None:
                return "That is not a valid password"
            else:
                return None

        def valid_password_match(pw1, pw2):
            if pw1 != pw2:
                return "Your passwords do not match"
            else:
                return None

        def valid_email(ema):
            user_email_regex = re.compile(r"^[\S]+@[\S]+.[\S]+$")
            if ema == "":
                return None
            elif user_email_regex.match(ema) == None:
                return "That is not a valid email address"
            else:
                return None


        une = valid_username(self.request.get("username"))
        pwve = valid_password(self.request.get("password1"))
        pwme = valid_password_match(self.request.get("password1"), self.request.get("password2"))
        eme = valid_email(self.request.get("email"))

        success_message = page_header + "<h1>You successfully signed up, " + self.request.get("username") + "!</h1>" + page_footer

        if (une == None and pwve == None and pwme == None and eme == None):
            self.redirect("/success?username=" + self.request.get("username"))
        else:
            self.write_form(une,pwve,pwme,eme)

class Success(webapp2.RequestHandler):

    def get(self):
        success_message = page_header + "<h1>You successfully signed up, " + self.request.get("username") + "!</h1>" + page_footer

        self.response.write(success_message)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/success', Success)
], debug=True)
