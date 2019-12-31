.. _issues: https://github.com/leaprovenzano/collectionish/issues

============
Contributing
============

Step 1 : File an issue
----------------------

All contributions (with the possible exception of minor documentation changes) should start in `issues`_ .
Hashing out changes and discussion an issue means no ones time is wasted writing PRs that are not accepted.

If you'd like to work on your issue please be sure and mention that when you create it.
That way we can assign it to you once the work is accepted.

Report Bugs:
~~~~~~~~~~~~

Report bugs in our `issues`_. If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting. This must include your version of python and collectionish
* A minimal example that will reproduce the bug.


Suggest featues:
~~~~~~~~~~~~~~~~

Suggest features in our `issues`_. PRs for new features will not be accepted without some discussion in an issue.
Feature suggestions should include details of the feature and why you think it would be useful.

A really nice way of outlining a bit of new functionality is to write a little type-hinted stub with a (preferably google style) docstring including
doctest examples. Contributors are encouraged to suggest features in this way.

For example lets say i want to suggest a function ``depth`` which will give me the max depth of a nested mapping,
I might include a stub like this when i create my issue:

.. code:: python

    from typing import Collection

    def depth(thing: Collection) -> int:
        """Get the max depth of a given Collection.

        Depth here is defined as the maximum degree of nestedness of a collection type.
        you can think of it as how many times `__getitem__` would need to be called to
        get to the deepest object.

        Example:

            >>> from collectionish.ops import depth
            >>>
            >>> thing = {'a': 1, 'b': {'ba': 1, 'bb': 2}}
            >>> depth(thing)
            2

            flat mappings have a depth of 1

            >>> depth({'a': 1, 'b': 2})
            1

            arrays work just as well

            >>> depth([ 1, 2, [1, [ 1, 2]]])
            3

            but note that strings are containers and so will count towards depth!

            >>> depth(['list', 'of', 'strings'])
            2

        """
        ...



Existing Issues:
~~~~~~~~~~~~~~~~

If you see a "help wanted" tag and want to work on it just give us a shout and we will assign it to you.


Pull Requests:
--------------

If you've been assigned an issue and you'd like to get started here's how to go about making a PR:


Setting up for local development:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Fork the `collectionish` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/collectionish.git

3. Install your local copy into a virtualenv::

    $ python3 -m collectionish/env
    $ cd collectionish
    $ source env/bin/activate
    $ pip install -e .

4. You'll also want to install some dev dependencies.
   We seperate in the requirements directory into test, docs, & dev for the sake of CI.
   To install all the dependencies you can simply::

    $ pip install -r requirements/all.txt

3. Install the pre-commit hooks. These will reformat your code using lea's special version of black
   do mypy and pep8 checks and generally complain at you if you try and commit something they hate. Doing
   This means that stuff will be formatted correctly and will not set off linting errors in your PR::

   $ pip install pre-commit
   $ pre-commit install

PR Guidelines:
~~~~~~~~~~~~~~

* PR's should contain one and only one logical change. It's perfectly fine to open multiple PRs (or multiple issues) for a large bit of work.

* PR's should not change or add anything not referenced in the original Issue

* PR's should usually contain a little description of the changes for reviewers to read
  and should always link to the original issue.

* All features and bug fixes must have a user friendly high level description of the changes
  entered into the /HISTORY.rst.If a new version will be created make it in the same format
  you see below. This is currently a bit annoying but we will work out a better solution soon.

* All new public functions and classes code must have docstrings in the google style. Most docstrings should
  include examples.

* All new features must have tests and all bug fixes must provide regression tests.

* Type hints should be added wherever possible.

* New Contributors should update the AUTHORS.rst with their name in the contributors section.

* All features and bugfixes must have a user friendly high level description of the changes
  entered into the HISTORY.rst

* Make a sensible branch name. it's also encouraged to use the following prefixes::

    feature/
    bugfix/

* Make decent descriptive commit messages.

* Try and keep commits small. This is particularly true when pre-commit hooks in place.

* Documentation updates may not need several of the above requirements and can PRS can be opened without an issue.
