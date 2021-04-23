# Faraday Agent Parameters Types

The [faraday agents][dispatcher] run code remotely to ensure your domains. This info is triggered and published to a
[faraday server][faraday] instance, which had set the parameters of the code. This repository sets the models to
be used by both sides.


Features
--------

* Set the models of parameters types for the agents:
    * How to pass them by identifier strings
    * How to encode/decode them to pass data between the [Faraday server][faraday], and the [agents][dispatcher]

Credits
-------

This package was created with [Cookiecutter][cookiecutter] and the
[`audreyr/cookiecutter-pypackage`][cookiecutter-pypackage] project template.

[cookiecutter]: https://github.com/audreyr/cookiecutter
[cookiecutter-pypackage]: https://github.com/audreyr/cookiecutter-pypackage
[faraday]: https://github.com/infobyte/faraday
[dispatcher]: https://github.com/infobyte/faraday_agent_dispatcher
