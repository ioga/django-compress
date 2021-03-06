### Motivation
Previously, if you had some apps excluded from `INSTALLED_APPS`, 
you should remove them from `settings_compress` or whereever you store your 
settings for `django-compress` , since synccompress would fail to find this 
files, because they had not been collected by collectstatic,
which do check `INSTALLED_APPS` itself.

### Usage
This fork provides support for per-application `COMPRESS_JS` & `COMPRESS_CSS`
settings, so you can define js & css groups in `your_app/settings_compress.py`
like you did in global `settings_compress`. django-compress would collect
per-application dictionaries and `.update` them into single global.

### Why not just put this code into your project?
- celery also does such stuff
- less boilerplate code

---

### Original readme
django-compress provides an automated system for compressing CSS and 
JavaScript files. By default, it only outputs compressed files while not in 
DEBUG-mode. That means you can still debug and edit your source files while 
coding, and when going to production, the compressed files will be 
automatically generated.

Support for jsmin and CSSTidy is included and enabled by default (but can 
easily be disabled). Support for YUI Compressor is also supported out of the 
box.

django-compress includes template tags for outputting the URLs to the 
CSS/JavaScript?-files and some other goodies to improve the performance of 
serving static media.

django-compress is available at [github][1] and [Google Code][2]. You can always 
access the latest and greatest code from both git and Subversion.

The documentation is available online at [Github][3], or under docs/ in the 
source.

[1]: http://github.com/pelme/django-compress/tree/master
[2]: http://code.google.com/p/django-compress/
[3]: http://github.com/pelme/django-compress/tree/master/docs

