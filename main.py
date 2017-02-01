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

class Index(webapp2.RequestHandler):

    def get(self):
        # display any errors
        bfe = self.request.get("error1")
        une = self.request.get("error2")
        pwve = self.request.get("error3")
        pwme = self.request.get("error4")

        # basic signup form
        # includes tables and error messages
        signup_form = "<form action='/signup' method='post'>"
        username_form = "<table><tr><td><label>Username: </td></label><td><input type='text' name='username'/></td> <td><span class='error'>" + une + "</span></td></tr><br"
        password_form = "<tr><td><label>Password: </td></label><td><input type='password' name='password1'/></td> <td><span class='error'>" + pwve + "</span></td></tr>"
        password_conf_form = "<tr><td><label>Password again: </td></label><td><input type='password' name='password2'/></td> <td><span class='error'>" + pwme + "</span></td></tr>"
        email_form = "<tr><td><label>Email (optional): </td></label><td><input type='text' name='email'/></td></tr></table>"
        form_end = """
        <input type="submit">
            </form>
            """

        content = page_header + signup_form + username_form + password_form + password_conf_form + email_form + form_end + page_footer

        self.response.write(content)

class Signup(webapp2.RequestHandler):

    def post(self):
        # get user elements from form
        user = self.request.get("username")
        pass1 = self.request.get("password1")
        pass2 = self.request.get("password2")
        email_add = self.request.get("email")

        # error messages
        blank_form_error = "You must fill out the form"
        username_error = "That isn't a valid username"
        password_blank_error = "You must enter a password"
        password_match_error = "Your passwords do not match"
        email_error = "That isn't a valid email address"

        success_message = page_header + "<h1>You successfully signed up, " + user + "!</h1>" + page_footer

        # error handling
        if user == "" or " " in user:
            self.redirect("/?error2=" + username_error)
        if pass1 == "":
            self.redirect("/?error3=" + password_blank_error)
        if pass1 != pass2:
            self.redirect("/?error4=" + password_match_error)

        # if email_add: REQUIRES REGEX, HOLD OFF UNTIL TODO 4

        self.response.write(success_message)



# COMPLETED TODO 1: Create form with all fields  COMPLETED

# COMPLETED TODO 2: Create handler for successful form COMPLETED

# COMPLETED TODO 3: Create error handler COMPLETED

# TODO 4: Add regex to validate

# TODO 5: Connect validation to error handling

# TODO 6: Create correct styling for errors

# TODO 7: Refactor code

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/signup', Signup)
], debug=True)
