# InstagramGiveaways

Have you seen those Instagram giveaways where you have to tag your friends for a higher chance to win?
Well, there was this giveaway where you could tag 2 friends in a comment. The more comments (and pairs of friends), the higher your chances were!
This Python bot employs Selenium to do exactly that. Given a dataset of Instagram IDs and common phrases like "Let's see if we win this time!",
it grabs unique pairs of IDs and leaves as many comments as possible.

It is worth mentioning that Instagram has bot detection systems. Thus, random waiting times are performed in-between actions. Moreover,
the bot also respects Instagram's limit for comments per minute.

Testing took place months ago, around August 2020. Therefore, it is possible that some modifications to HTML tags have been made in the meantime.
It should not be hard to adapt the code.

DISCLAIMER: THIS BOT WAS TESTED ON MY OWN PRIVATE POSTS. IT HAS NEVER BEEN USED IN REAL GIVEAWAYS. USE AT YOUR OWN DISCRETION.
