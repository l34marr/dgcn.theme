dgcn.theme Installation
-----------------------

To install dgcn.theme using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``dgcn.theme`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        dgcn.theme
       
* Re-run buildout, e.g. with:

    $ ./bin/buildout
