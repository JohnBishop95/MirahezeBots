"""This module expands links to various websites"""
from __future__ import unicode_literals, absolute_import, print_function, division

import re
from sopel.module import rule, commands, example


@commands('github', 'gh')
@example('.github user')
def ghuser(bot, trigger):
    """Expands a link to github."""
    try:
        bot.say("https://github.com/" + trigger.group(2))
    except TypeError:
        bot.say('Syntax: .github user', trigger.sender)


@commands('redditu')
@example('.redditu example')
def redditu(bot, trigger):
    """Expands a link to reddit/u."""
    try:
        bot.say("https://reddit.com/u/" + trigger.group(2))
    except TypeError:
        bot.say('Syntax: .redditu example', trigger.sender)


@commands('subred')
@example('.subred example')
def redditr(bot, trigger):
    """Expands a link to reddit/r."""
    try:
        bot.say("https://reddit.com/r/" + trigger.group(2))
    except TypeError:
        bot.say('Syntax: .subred example', trigger.sender)


@commands('wmca')
@example('.wmca example')
def wmca(bot, trigger):
    """Expands a link to Wikimedia CentralAuth."""
    target = trigger.group(2).replace(" ", "_")
    try:
        bot.say("https://meta.wikimedia.org/wiki/Special:CentralAuth/" + target)
    except TypeError:
        bot.say('Syntax: .wmca example', trigger.sender)


@commands('mhca')
@example('.mhca example')
def mhca(bot, trigger):
    """Expands a link to Miraheze Central Auth."""
    target = trigger.group(2).replace(" ", "_")
    try:
        bot.say("https://meta.miraheze.org/wiki/Special:CentralAuth/" + target)
    except TypeError:
        bot.say('Syntax: .mhca example', trigger.sender)


@commands('tw')
@example('.tw user')
def twlink(bot, trigger):
    """Expands a link to Twitter."""
    target = trigger.group(2).replace(" ", "_")
    try:
        bot.say("https://twitter.com/" + target)
    except TypeError:
        bot.say('Syntax: .tw user', trigger.sender)


@commands('mh')
@example('.mh wiki page')
def mhwiki(bot, trigger):
    """Expands a link to Miraheze wikis."""
    try:
        options = trigger.group(2).split(" ", 1)
        if len(options) == 1:
            page = options[0]
            page = page.replace(" ", "_")
            bot.say("https://meta.miraheze.org/wiki/" + page)
        elif len(options) == 2:
            wiki = options[0]
            page = options[1]
            page = page.replace(" ", "_")
            bot.say("https://" + wiki + ".miraheze.org/wiki/" + page)
    except AttributeError:
        bot.say('Syntax: .mh wiki page', trigger.sender)
