#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2015 Jolla Ltd.
#  Contact: Jussi Pakkanen <jussi.pakkanen@jolla.com>
#  All rights reserved.
#
#  You may use this file under the terms of BSD license as follows:
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Jolla Ltd nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR CONTRIBUTORS BE LIABLE FOR
#  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# This file demonstrates how to write a class that downloads data from the
# net, does heavy processing or some other operation that takes a long time.
# To keep the UI responsive we do the operations in a separate thread and
# send status updates via signals.

import pyotherside
import threading
import time
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

def slow_function():
    for i in range(11):
        pyotherside.send('progress', i/10.0)
        time.sleep(0.5)
    pyotherside.send('finished', random.choice(colors))

class Downloader:
    def __init__(self):
        # Set bgthread to a finished thread so we never
        # have to check if it is None.
        self.bgthread = threading.Thread()
        self.bgthread.start()

    def download(self):
        if self.bgthread.is_alive():
            return
        self.bgthread = threading.Thread(target=slow_function)
        self.bgthread.start()


downloader = Downloader()

