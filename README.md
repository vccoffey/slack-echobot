# slack-echobot

A simple Slack bot written in Python.

## Documentation

See the tutorial, https://github.com/jackreichelt/slackbot-tutorial/blob/master/Slackbot%20Slides.pdf

### Docker

#### Build

    $ docker build -t echobot .

#### Run

    $ docker run -itd echobot

#### Tag and Push

    $ docker tag -f echobot industrieit/echobot
    $ docker push industrieit/echobot

##### Runtime Environment Variables

- `TOKEN` - the Slack token for the bot

License and Authors
-------------------

The MIT License (MIT)

Copyright (c) 2016 Jack Reichelt

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
