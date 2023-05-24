from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Import your models
from sqldb.models import Base, Verbatim, Structure

def fill_db():
    # Create engine
    engine = create_engine('sqlite:///sql.db')

    # Bind the engine to the Base metadata
    Base.metadata.bind = engine

    # Start new session
    db = Session(bind=engine)

    # Create some Structure instances
    structures = [
        Structure(lib_str='Structure 1'), 
        Structure(lib_str='Structure 2'),
        Structure(lib_str='Structure 3'),
        Structure(lib_str='Structure 4'),
        Structure(lib_str='Structure 5'),
        ]

    # Add the Structure instances to the session
    db.add_all(structures)

    # Commit the transaction
    db.commit()

    # Create some Verbatim instances
    # verbatims = [
    #     Verbatim(
    #         str_id=structures[0].id,
    #         upload_date=datetime.strptime('23/05/2023', '%d/%m/%Y'),
    #         verbatim_date=datetime.strptime('23/05/2023', '%d/%m/%Y'),
    #         verbatim_content='Content 1',
    #         verbatim_sentiment='Positive',
    #         verbatim_category='Category 1',
    #     ),
    #     Verbatim(
    #         str_id=structures[1].id,
    #         upload_date=datetime.strptime('23/05/2023', '%d/%m/%Y'),
    #         verbatim_date=datetime.strptime('23/05/2023', '%d/%m/%Y'),
    #         verbatim_content='Content 2',
    #         verbatim_sentiment='Negative',
    #         verbatim_category='Category 2',
    #     ),
    # ]

    verbatims = []

    for struct in structures:
        for i in range(1, 6):
            verbatims.append(
                Verbatim(
                    str_id=struct.id,
                    upload_date=datetime.strptime('23/05/2023', '%d/%m/%Y'),
                    verbatim_date=datetime.strptime('23/05/2023', '%d/%m/%Y'),
                    verbatim_content=f'Content {i}',
                    verbatim_sentiment='Positive',
                    verbatim_category=f'Category {i}',
                )
            )

    # Add the Verbatim instances to the session
    db.add_all(verbatims)

    # Commit the transaction
    db.commit()
