# collective.folderishcollection

Replaces the Plone "Collection" content-type with a "folderish" version.

Until now we have been creating Folders and inside them adding Collections to create
news or events listing.

Remember the `news/aggregator` and `events/aggregator` that Plone creates adding a new site?

That's exactly what we were doing.

But, setting the Collection as default page, creates other problems, such as creating additional URLs
that Google and other search engines crawl.

Although Plone tries to solve that creating canonical URLs, trying to hide the `aggregator` part from the URL
sometimes search engines find a minimal way to crawl your site.

Using this product, you can create a Collection that holds all the configuration bells and whistles, and also add the content
inside it.

This way you can have your `news` collection, with news items inside it (`news/my-newsitem`) and the folder can have
a configurable search providing the results of the search.

## Installation

add collective.folderishcollection to your project's dependencies.

## Contribute

- [Issue tracker](https://github.com/collective/collective.folderishcollection/issues)
- [Source code](https://github.com/collective/collective.folderishcollection/)

### Prerequisites ✅

- An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
- [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
- [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
- [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
- [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:collective/collective.folderishcollection.git
    cd collective.folderishcollection
    ```

2.  Install this code base.

    ```shell
    make install
    ```

## License

The project is licensed under GPLv2.

## Credits and acknowledgements 🙏

The idea of this product came after having used [collective.folderishtypes](https://github.com/collective/collective.folderishtypes) that adds folderish behavior to News Items, Events and Documents.

Generated using [Cookieplone (0.9.7)](https://github.com/plone/cookieplone) and [cookieplone-templates (4d55553)](https://github.com/plone/cookieplone-templates/commit/4d55553d61416df56b3360914b398d675b3f72a6) on 2025-07-22 12:20:18.861060. A special thanks to all contributors and supporters!
