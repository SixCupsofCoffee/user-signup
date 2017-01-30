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

class MainHandler(webapp2.RequestHandler):



    def get(self):
        signup_form = """
            <form action="/signup" method="post">
                <label>Username: </label><input type="text" name="username"/><br>
                <label>Password: </label><input type="password" name="password1"/><br>
                <label>Password again: </label><input type="password" name="password2"/><br>
                <label>Email (optional): </label><input type="text" name="email"/><br>
                <input type="submit">
            </form>
            """

        content = page_header + signup_form + page_footer

        self.response.write(content)



# TODO 1: Create form with all fields

# TODO 2: Create handler for successful form

# TODO 3: Create error handler

# TODO 4: Add regex to validate

# TODO 5: Connect validation to error handling

# TODO 6: Create correct styling for errors

# TODO 7: Refactor code

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
