from os import getenv

database_user    :str = getenv('PGUSER',     'postgres')
database_name    :str = getenv('PGDATABASE', 'ghelephant')
database_password:str = getenv('PGPASSWORD', 'postgres')
database_host    :str = getenv('PGHOST',     'localhost')
database_port    :str = getenv('PGPORT',     '5432')
data_path        :str = getenv('DATA_PATH',  '/tmp/ghelephant')
# TODO autodetect default option
sed_name         :str = getenv('SED',        'sed') # gsed for mac, sed for linux
