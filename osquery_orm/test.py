from pathlib import Path
from osquery_orm import OsQueryDatabase, Compatibility


if __name__ == '__main__':
    db = OsQueryDatabase(f'{Path.home()}/.osquery/osqueryd.sock', Compatibility.MacOS)
    db.connect()
    print(f"DB: {db}")

    r_qry = db.raw_query("SELECT * FROM os_version")
    print(f"\nRaw Query: {r_qry}")

    c_qry = db.tables.cross_platform.OS_Version.select()
    print(f'\nCode Qry: {c_qry}')
    for itm in c_qry:
        print(f'-- {type(itm)}\n')

    tables = db.get_tables()
    print(f"\nTables: {len(tables):,}\n{tables}\n")

    rslt = db.tables.cross_platform.OS_Version.select()
    print(f"\nOS Version: {list(rslt)}\n")
