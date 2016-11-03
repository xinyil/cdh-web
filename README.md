# CDH Website Repo

## Overview
The purpose of this repo is to house the development files for the current version of the CDH Website,
including static files used in templates (**not** static/media).

Initial development of the site in 09/16 and 10/16 used [Mezzanine 4.2.0](mezzanine.jupo.org/docs/) running on [django 1.10](https://docs.djangoproject.com/en/1.10).

Mezzanine's "Mezzanine is just django" approach allowed the project to be easily created with a series of interlocking
applications developed to serve custom page types, as well as to add iCal support and feeds.

The website lives on the server cdh-web.princeton.edu (publicly aliased as digitalhumanities.princeton.edu).

+ cdhWebsite
  + Primary settings, local_settings.py held on server
+ eventspages
  + This app includes models for events, their publication pages, and the overall events page_processor
+ icalevents
  + This app provides an ical feed at /ical/<event number>
+ index
  + This app provides a page_processor for index.html and the base home page
+ projectpages
  + This app provides models for projects, project pages, and the project page boxes at /projects/
+ staffprofiles
	+ This app provides models for staff, their individual pages (not complete), and the staff director page_processor
+ static
	+ Static files included here, including copies of jQuery, fonts, and modified Bootstrap3 CSS
+ stocktemplate
	+ This app provides models for stockpages.
+ subscribe
  + This app provides models and views for subscribing to the listserv (which must still be approved with an OK email from
digitalhumanities@princeton.edu
+ templates
  + All template files, including blog/ includes/ and pages/, as well as templates in the main directory for displaybles, primarily project and event individual pages (staff pages to be added)


## Tests

Unit tests are written with py.test but use Django fixture loading and convenience
testing methods when that makes things easier.  To run them, first install
development requirements:

  pip install -r dev-requirements.txt

Run tests using py.test:

  py.test
