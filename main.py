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

# -*- coding: utf-8 -*-

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
une=""
pwve=""
pwme=""

# basic signup form
# includes tables and error messages
signup_form = """
<form action="/" method="post">
<table>
    <tr><td><label>Username: </td></label><td><input type="text" name="username"/></td> <td><span class="error">%s</span></td></tr>
    <tr><td><label>Password: </td></label><td><input type="password" name="password1"/></td> <td><span class="error">%s</span></td></tr>
    <tr><td><label>Password again: </td></label><td><input type="password" name="password2"/></td> <td><span class="error">%s</span></td></tr>
    <tr><td><label>Email (optional): </td></label><td><input type="text" name="email"/></td></tr>
</table>
<input type="submit">
    </form>
    """ % (une, pwve, pwme)

class Index(webapp2.RequestHandler):

    def write_form(self, une="", pwve="", pwme=""):
        self.response.write(page_header + signup_form % {"une":une, "pwve":pwve, "pwme":pwme} + page_footer)

    def get(self):
        self.write_form()

    def post(self):

        def valid_username(usern):
            if usern == "" or " " in usern:
                return "That is not a valid username"
            else:
                return ""

        def valid_password(pw1):
            if pw1 == "":
                return "That is not a valid password"
            else:
                return ""

        def valid_password_match(pw1, pw2):
            if pw1 != pw2:
                return "Your passwords do not match"
            else:
                return ""

        une = valid_username(self.request.get("username"))
        pwve = valid_password(self.request.get("password1"))
        pwme = valid_password_match(self.request.get("password1"), self.request.get("password2"))

        if (une != "" and pwve != "" and pwme != ""):
            self.write_form(une,pwve,pwme)
        else:
            success_message = page_header + "<h1>You successfully signed up, " + self.request.get("username") + "!</h1>" + page_footer

            self.response.write(success_message)



# COMPLETED TODO 1: Create form with all fields  COMPLETED

# COMPLETED TODO 2: Create handler for successful form COMPLETED

# TODO 3: Create error handler

# TODO 4: Add regex to validate

# TODO 5: Connect validation to error handling

# TODO 6: Create correct styling for errors

# TODO 7: Refactor code

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
