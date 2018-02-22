#!/usr/bin/env python
# -*- coding: utf-8 -*-
import DbInitializer
class ApisDbInitializer(DbInitializer.DbInitializer): pass

if __name__ == "__main__":
    assert issubclass(ApisDbInitializer().__class__, DbInitializer.DbInitializer)
    assert isinstance(ApisDbInitializer(), DbInitializer.DbInitializer)
    ApisDbInitializer().CreateDb()
