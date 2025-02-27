fork of pygobject-stubs with gst-python overrides included in Gst.pyi
Upstream project is missing the gi overrides provided by gst-python package.

learning drawbacks of current implementation:
 - Gst.init not called if using Gst overrides resulting in fake_function (solved by calling Gst.init() in generate.py)
 - Errors: (IteratorError, IteratorError, MapError, AddError) missing Exception class
 - Event.new_buffer_size when generated has a async param which is a python keyword: must be manually renamed to _async (force positional argument via "/"?)
 - Iterator(GObject.GBoxed) with overrides create bogus elements (duplicate copy, next, resync, free), whys is this happening? now manually fixed
 - Missing GstBase (added in this repo)
 - Missing GstVideo (added in this repo)

# Typing Stubs for PyGObject

[![PyPI](https://img.shields.io/pypi/v/pygobject-stubs)](https://pypi.org/project/PyGObject-stubs)

## Installation
```
$ pip install pygobject-stubs
```

### Configuration

Some libraries exist in multiple versions like Gtk3/4. As both libraries are
currently imported under the namespace `Gtk` only stubs for one can be installed.

You need to decide this at install time either by using the `--config-settings` option
with pip

    $ pip install pygobject-stubs --no-cache-dir --config-settings=config=Gtk3,Gdk3,Soup2

or by setting the `PYGOBJECT_STUB_CONFIG` env variable

    $ PYGOBJECT_STUB_CONFIG=Gtk3,Gdk3,Soup2 pip install --no-cache-dir pygobject-stubs

If no configuration is set, the most recent version of each library is installed.

`--no-cache-dir` is only necessary on subsequent reinstalls, otherwise the stubs will not
be rebuild and a cache of a previous installation is used.

### Project Integration

Usually you want the stubs to be installed as part of the development dependencies.
`pyproject.toml` does not allow to pass `config-settings` to requirements.
If you need specific versions of some libraries you can use a `requirements.txt` file instead, which
allows to pass `config-settings` per requirement as of pip >= 23.1.0.

    $ pip install . -r dev.txt

## Contributing

[Guide](./CONTRIBUTING.md)
