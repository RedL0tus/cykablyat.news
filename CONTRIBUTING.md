Contribution guide
==================

Bazinga~

Before submission
-----------------

You should confirm that your submission:
 - Must not because of your own opinion, it have to be really, really dumb.
 - You need to state why this is dumb in the description.

How can I submit urls?
----------------------

Article information are stored in the [news directory](news).

Structure:
```
news
└── fake (Type of the news)
    └── big-hack.yaml (Title of the article)
```

Fields in the yaml file:
```yaml
title: "The Big Hack: How China Used a Tiny Chip to Infiltrate U.S. Companies"
link: "https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies"
archive: "https://webcache.googleusercontent.com/search?q=cache:RKqi2EuG9dMJ:https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies"
description: "A chip has that kind of capability is kind of impossible right now. Customers of Supermicro like Amazon, Apple claimed they didn't find that kind of chip in their systems as well."
```

 - title: Title of the article.
 - link: Link to the source of the article.
 - archive: Link to the archive of the article.
 - description: A brief description of why this article is dumb. 

Title, description and at least one of link and archive are required.

Pull requests and issues contain the information above are OK.
