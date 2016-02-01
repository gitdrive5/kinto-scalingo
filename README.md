# Kinto for Scalingo

`kinto-scalingo` is an example on how to use [Kinto](http://kinto-storage.org) and [Scalingo](https://scalingo.com) together.
Following the installation you should have a Kinto server available for you to use.

## Installation for Scalingo

```
$ git clone http://github.com/Kinto/kinto-heroku.git --depth=1 kinto-instance && cd kinto-instance
$ scalingo create my-kinto && git push scalingo master
```

[![Deploy to Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.scalingo.com/deploy)
