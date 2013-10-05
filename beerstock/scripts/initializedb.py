import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    Item,
    ItemType,
    Base,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        ipa = ItemType('1-2', 'IPA Zythos')
        bitter = ItemType('2-1', 'Bitter English')
        brown = ItemType('3-1', 'Brown SSD')
        dubbel = ItemType('4-1', 'Dubbel Belgian Ale')
        DBSession.add_all([ipa, bitter, brown, dubbel])
        DBSession.add_all([Item('1', ipa), Item('2', ipa), Item('3', bitter), Item('4', brown), Item('5', dubbel)])
