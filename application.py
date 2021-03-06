#!/usr/bin/env python

import os
import sys
from app import create_app
from dmutils import init_manager


port = int(os.getenv('PORT', '5004'))
application = create_app(
    os.getenv('DM_ENVIRONMENT') or 'development'
)
manager = init_manager(application, port, ['./app/content/frameworks'])

application.logger.info('Command line: {}'.format(sys.argv))

if __name__ == '__main__':
    try:
        application.logger.info('Running manager')
        manager.run()
    finally:
        application.logger.info('Manager finished')
