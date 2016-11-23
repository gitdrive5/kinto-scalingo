# Kinto for Scalingo

`kinto-scalingo` is an example on how to use [Kinto](http://kinto-storage.org) and [Scalingo](https://scalingo.com) together.
Following the installation you should have a Kinto server available for you to use.

## Installation for Scalingo

To deploy Kinto on Scalingo, just click on this button:

[![Deploy to Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.scalingo.com/deploy)

or using CLI:

```
$ git clone http://github.com/Scalingo/kinto-scalingo.git --depth=1 my-kinto && cd my-kinto
$ scalingo create my-kinto
$ scalingo --app my-kinto addons-add scalingo-postgresql free
$ git push scalingo master
```

## How to upgrade / change configuration?

First of all use the [Scalingo command](http://cli.scalingo.com/) to login:

Clone this repository and link it to your Scalingo app (here named `my-kinto`):

```
$ git clone http://github.com/Scalingo/kinto-scalingo.git --depth=1 my-kinto
$ cd my-kinto
```

If you did not create the app on the Scalingo dashboard yet:

```
$ scalingo create my-kinto
$ scalingo --app my-kinto addons-add scalingo-postgresql free
```

otherwise, if the app is already created:

```
$ git remote add scalingo git@scalingo.com:my-kinto.git
```

(*optional*) Edit your configuration:

```
$ <Edit kinto.ini with your new settings>
$ git commit -am "New setting"
```

> Note: You can also edit the `requirements.txt` to add new dependencies / plugins.

Deploy your modification:

```
$ git push scalingo master

 <-- Start deployment of my-kinto -->
-------> Buildpack version 1.3.3
Use locally cached dependencies where possible
-----> Installing runtime (python-2.7.10)
-----> Installing dependencies with pip
       Collecting cliquet==2.15.0 (from -r requirements.txt (line 1))
         Downloading cliquet-2.15.0-cp2.cp3-none-any.whl (315kB)

[...]

-----> Running post-compile hook
/app/.scalingo/python/lib/python2.7/site-packages/kinto/core/storage/postgresql/client.py:88: UserWarning: Reuse existing PostgreSQL connection. Parameters permission_* will be ignored.
  warnings.warn(msg)
/app/.scalingo/python/lib/python2.7/site-packages/kinto/core/storage/postgresql/client.py:88: UserWarning: Reuse existing PostgreSQL connection. Parameters cache_* will be ignored.
  warnings.warn(msg)
INFO   Running kinto 5.0.0. 
INFO   Created PostgreSQL cache tables 
INFO   Create PostgreSQL storage schema at version 14 from /app/.scalingo/python/lib/python2.7/site-packages/kinto/core/storage/postgresql/schema.sql 
INFO   Created PostgreSQL storage schema (version 14). 
INFO   Created PostgreSQL permission tables 
----- Procfile declares types -> web
 Build complete, shipping your container...
 Waiting for your application to boot... 
 <-- https://my-kinto.scalingo.io -->
```

Done!
