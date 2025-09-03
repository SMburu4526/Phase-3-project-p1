from models import SessionLocal, Base, engine
from models import Team
from models import Locker

Base.metadata.create_all(bind=engine)

def create_team():
    name = input("Enter team name: ")
    session = SessionLocal()
    if session.query(Team).filter_by(name=name).first():
        print("Team already exists.")
    else:
        team = Team(name=name)
        session.add(team)
        session.commit()
        print(f"Created {team}")
    session.close()

def list_teams():
    session = SessionLocal()
    teams = session.query(Team).all()
    if teams:
        for t in teams:
            print(t)
    else:
        print("No teams found.")
    session.close()

def delete_team():
    name = input("Enter team name to delete: ")
    session = SessionLocal()
    team = session.query(Team).filter_by(name=name).first()
    if team:
        session.delete(team)
        session.commit()
        print(f"Deleted team {name}")
    else:
        print("Team not found.")
    session.close()


def create_locker():
    player = input("Player name: ")
    sport = input("Sport: ")
    equip = input("Equipment: ")
    team_name = input("Team name: ")

    session = SessionLocal()
    team = session.query(Team).filter_by(name=team_name).first()
    if not team:
        print("Team not found. Please create team first.")
    else:
        locker = Locker(player_name=player, sport=sport, equipment=equip, team=team)
        session.add(locker)
        session.commit()
        print(f"Created {locker}")
    session.close()

def list_lockers():
    session = SessionLocal()
    lockers = session.query(Locker).all()
    for l in lockers:
        print(l, "-> Team:", l.team.name if l.team else "None")
    session.close()

def search_locker():
    name = input("Enter player name: ")
    session = SessionLocal()
    locker = session.query(Locker).filter_by(player_name=name).first()
    print(locker if locker else "Not found.")
    session.close()

def update_locker():
    name = input("Enter player name to update: ")
    session = SessionLocal()
    locker = session.query(Locker).filter_by(player_name=name).first()
    if not locker:
        print("Locker not found.")
    else:
        new_sport = input(f"New sport (leave blank to keep {locker.sport}): ") or locker.sport
        new_equipment = input(f"New equipment (leave blank to keep {locker.equipment}): ") or locker.equipment
        locker.sport = new_sport
        locker.equipment = new_equipment
        session.commit()
        print("Updated:", locker)
    session.close()

def delete_locker():
    name = input("Enter player name to delete: ")
    session = SessionLocal()
    locker = session.query(Locker).filter_by(player_name=name).first()
    if locker:
        session.delete(locker)
        session.commit()
        print("Deleted:", locker)
    else:
        print("Locker not found.")
    session.close()

def exit_program():
    print("Goodbye!")
    exit()
