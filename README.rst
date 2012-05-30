====================
kotti_sharethis
====================

This is an extension to the Kotti CMS that allows you to add ShareThis
widget to your Kotti site.

`Find out more about Kotti`_

Setting up the widget
=====================

To set up the profile widget to display on every page in Kotti on the
right hand side, add ``kotti_sharethis.include_sharethis_widget`` to the
``kotti.includes`` setting in your Paste Deploy config::

  kotti.includes = kotti_sharethis.include_sharethis_widget

There is an option to have this widget show above your content. To initiate
that, changed the above code to the following::

  kotti.includes = kotti_sharethis.include_sharethis_widget_above

To set what website options are shown, set the
``kotti_sharethis.sharethis_widget.{}`` variables.  An example of these
variables::

  kotti_sharethis.sharethis_widget.sharethis = False,
  kotti_sharethis.sharethis_widget.facebook = True,
  kotti_sharethis.sharethis_widget.twitter = True
  kotti_sharethis.sharethis_widget.linkedin = True,
  kotti_sharethis.sharethis_widget.gplus = True,
  kotti_sharethis.sharethis_widget.pinterest = False,
  kotti_sharethis.sharethis_widget.email = True,

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti