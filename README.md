###Python-PlantUML

[Plantuml](http://plantuml.sourceforge.net/index.html) is a library for
generating UML diagrams from a simple text markup language.

This is a simple python remote client interface to a
[plantuml](http://plantuml.sourceforge.net/index.html) server using the
same custom encoding used by most other plantuml
[clients](http://plantuml.sourceforge.net/running.html). Python was
missing from the list, and while there are other plantuml python
libraries, like
[sphinxcontrib-plantuml](https://pypi.python.org/pypi/sphinxcontrib-plantuml),
they require downloading and installing the java executable and spawning
a shell subprocesses.

This client defaults to the public [plantuml server](http://www.plantuml.com/plantuml/),
but can be used against any server.

###Install

    pip install git+https://github.com/SamuelMarks/python-plantuml#egg=plantuml

PS: At some point this newer version will be uploaded to PyPi, at which point you can do:

    pip install plantuml

Or by cloning it locally and running `python setup install`.

###Command line help:

To quick test it, you can run `python plantuml.py test.wsd`

To see all the command line options run `python plantuml.py --help`


###Project Links:

-   [Documentation](http://pythonhosted.org/plantuml/)
-   [PyPi](https://pypi.python.org/pypi/plantuml)
-   [GitHub](https://github.com/dougn/python-plantuml/)
