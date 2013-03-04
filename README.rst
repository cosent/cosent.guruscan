.. contents::

Introduction
============

GuruScan_ is a knowledge management application that enables your employees
to quickly locate collegues that have specific expertise. 
Unlike other applications that rely on self-certification, GuruScan
crowdsources expertise profiles by asking each employee who their
"go-to person" is for a specific area of expertise.

Plone_ is an open source enterprise content management system
suitable for building large intranets. 

This package, cosent.guruscan, provides single-signon integration
of the GuruScan webservice into a Plone installation. You need
to obtain a GuruScan client id for this to work.

After installation, cosent.guruscan adds a global tab 'Knowledge Center'
that integrates the GuruScan expert locator service. Users only have to log into their
Plone account; they're then automatically logged into GuruScan as well.

For site administrators, a user export view is available at @@guruscan-exportusers
that exports the Plone user database in a format suitable for import
by GuruScan.

Credits
=======

Companies
---------

|Cosent|_

This package was created by Cosent_.

Authors
-------

- Guido Stevens aka gyst <guido.stevens@cosent.net>

.. _GuruScan: http://www.guruscan.nl
.. _Plone: http://www.plone.com
.. _Cosent: http://cosent.nl
.. |Cosent| image:: http://cosent.nl/images/logo-external.png 
                    :alt: Cosent

