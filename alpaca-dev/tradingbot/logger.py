#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging as lg
import os
from datetime import datetime as dt

# Create a log folder for logs

logs_path = './logs'

try:
    os.mkdir(logs_path)
except OSError:
    print('Creation of the logs directory %s failed, folder already exists!' %logs_path)
else:
    print('Successfully created log directory.')


# Rename each log depending on the time
log_name = dt.now().strftime('%Y-%m-%d_%H:%M%S')

lg.basicConfig(
    filename=f'{logs_path}/bot.log.{log_name}',
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=lg.DEBUG
)

# If you should want to print those messages to the console. Use->lg.getLogger().addHandler(lg.StreamHandler())

# lg Levels: DEBUG|INFO|WARNING|ERROR|Critical

lg.info('This is a info message.')
lg.error('This is a error message.')
lg.critical('This is a critical message.')


