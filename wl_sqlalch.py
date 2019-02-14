from sqlalchemy import create_engine,MetaData, Table, insert
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.exc import IntegrityError
from WeatherLinkScrape import get_soup

def db_insert(url):
    engine = create_engine('sqlite:///ws.sqlite')
    connection = engine.connect()
    metadata = MetaData()

    observation = Table('observation',metadata,
        Column('observation_time',String(255),unique=True),
        Column('station_name', String(255),unique=False),
        Column('dewpoint_c', Float(), unique=False),
        Column('dewpoint_f', Float(), unique=False),
        Column('heat_index_c', Float(), unique=False),
        Column('heat_index_f', Float(), unique=False),
        Column('location', String(255), unique=False),
        Column('latitude', Float(), unique=False),
        Column('longitude', Float(), unique=False),
        Column('pressure_in', Float(), unique=False),
        Column('pressure_mb', Float(), unique=False),
        Column('relative_humidity', Integer(),unique=False),
        Column('solar_radiation', Integer(), unique=False),
        Column('sunrise', String(255), unique=False),
        Column('sunset', String(255), unique=False),
        Column('temp_c', Float(), unique=False),
        Column('temp_f', Float(), unique=False),
        Column('uv_index', Float(), unique=False),
        Column('wind_degrees', Integer(), unique=False),
        Column('wind_dir', String(255), unique=False),
        Column('wind_kt', Float(), unique=False),
        Column('wind_mph', Float(), unique=False),
        Column('windchill_c', Float(), unique=False),
        Column('windchill_f', Float(), unique=False)
    )

    metadata.create_all(engine)

    soup = get_soup(url)
    query = insert(observation).values(soup)
    try:
        ResultProxy = connection.execute(query)
        print('Observation Successfully recorded to Database')
    except IntegrityError:
        print('New Observation Not Found')
