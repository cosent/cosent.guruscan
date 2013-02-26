.. contents::

Introduction
============

Guruscan_ is a knowledge management application that enables your employees
to quickly locate collegues that have specific expertise. 
Unlike other applications that rely on self-certification, Guruscan
crowdsources expertise profiles by asking each employee who their
"go-to person" is for a specific area of expertise.

Plone_ is an open source enterprise content management system
suitable for building large intranets. 

This package, cosent.guruscan, provides single-signon integration
of the Guruscan webservice into a Plone installation. You need
to obtain a Guruscan client id for this to work.

After installation, cosent.guruscan adds a global tab 'Knowledge Center'
that integrates the Guruscan service. Users only have to log into their
Plone account; they're then automatically logged into Guruscan as well.

For site administrators, a user export view is available at @@guruscan-exportusers
that exports the Plone user database in a format suitable for import
by Guruscan.

Credits
=======

Companies
---------

|Cosent|_

Cosent_ provides social intranets and knowledge management solutions using Plone.

Authors
-------

- Guido Stevens aka gyst <guido.stevens@cosent.net>

.. _Guruscan: http://www.guruscan.nl
.. _Plone: http://www.plone.com
.. _Cosent: http://cosent.nl
.. |Cosent| image:: http://cosent.nl/images/logo-external.png 
                    :alt: Cosent

