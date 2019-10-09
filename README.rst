===================
Django Funky Sheets
===================

Django implementation of Handsontable spreadsheets for CRUD actions. This
is a fork of version 0.1.3. It is now compatible with Django 1.11.x.

Live Demo
=========

Demo_

.. _Demo: https://trco.si/dfs/create/

Installation
============

Install ``django-funky-sheets``::

  $ pip install django-funky-sheets

Add ``funky_sheets`` to your INSTALLED_APPS::

  # settings.py

  INSTALLED_APPS = [
      ...
      'funky_sheets',
      ...
  ]

Quick Start
===========

URL
---

Define URLs for Create and Update views.

.. code-block:: python

  # urls.py

  from django.conf.urls import url

  from . import views

  urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.CreateMovieView.as_view(), name='create'),
    url(r'^update/', views.UpdateMovieView.as_view(), name='update'),
  ]

View
----

Define Create and Update views which inherit from ``HotView`` and render the Handsontable spreadsheet based on selected model fields.

.. code-block:: python

  # views.py

  from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput
  from django.urls import reverse_lazy

  from funky_sheets.formsets import HotView

  from .models import Movie

  class CreateMovieView(HotView):
      # Define model to be used by the view
      model = Movie
      # Define template
      template_name = 'examples/create.html'
      # Define prefix for the formset which is constructed from Handsontable spreadsheet on submission
      prefix = 'table'
      # Define success URL
      success_url = reverse_lazy('update')
      # Define fields to be included as columns into the Handsontable spreadsheet
      fields = (
          'id',
          'title',
          'director',
          'release_date',
          'parents_guide',
          'imdb_rating',
          'genre',
          'imdb_link',
      )
      # Define extra formset factory kwargs
      factory_kwargs = {
          'widgets': {
              'release_date': DateInput(attrs={'type': 'date'}),
              'genre': CheckboxSelectMultiple(),
              'parents_guide': CheckboxInput(),
          }
      }
      # Define Handsontable settings as defined in Handsontable docs
      hot_settings = {
          'contextMenu': 'true',
          'autoWrapRow': 'true',
          'rowHeaders': 'true',
          'contextMenu': 'true',
          'search': 'true'
      }

  class UpdateMovieView(CreateMovieView):
    template_name = 'examples/update.html'
    # Define 'update' action
    action = 'update'
    # Define 'update' button
    button_text = 'Update'

Template
--------

Define templates which include ``hot_template`` in place where you want to render Handsontable spreadsheet.

.. code-block:: html+django

  examples/create.html

  ...
  {% include hot_template %}
  ...

  examples/update.html

  ...
  {% include hot_template %}
  ...

Contribute
==========

This is an Open Source project and any contribution is appreciated.

License
=======

This project is licensed under the MIT License.

Changes
=======

2019-10-09
  - backported to Django 1.11.x
