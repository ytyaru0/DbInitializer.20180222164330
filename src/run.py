import ApisDbInitializer
import GnuLicensesDbInitializer
for dbiniter in [ApisDbInitializer.ApisDbInitializer(), GnuLicensesDbInitializer.GnuLicensesDbInitializer()]:
    dbiniter.CreateDb()
    print(dbiniter.CreateDbFileName())
    print(dbiniter.DbFileName)
    dbiniter.CreateTable()
