from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from sqlalchemy import or_
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# Create engine and session ===================================================
# engine = create_engine('sqlite:///:memory:')
# engine = create_engine('sqlite:///test.db', echo=True)
engine = create_engine('sqlite:///test.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
# Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


# Create mapped class =========================================================
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


# Session and adding rows =====================================================

# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
# session.add(ed_user)
#
# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', password='foobar'),
#     User(name='mary', fullname='Mary Contrary', password='xxg527'),
#     User(name='fred', fullname='Fred Flinstone', password='blah')])

# session.commit()
# ed_user.name = 'Edwardo'
# fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
# session.add(fake_user)

# print(session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all())

session.rollback()

# session.commit()

# QUERY =======================================================================

print()
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)
print()

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)
print()

for row in session.query(User, User.name).all():
    print(row.User, row.name)
print()

for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)
print()

user_alias = aliased(User, name='derp')
for row in session.query(user_alias, user_alias.name).all():
    print(row.derp)
print()

for u in session.query(User).order_by(User.id)[1:3]:
    print(u)
print()

for name, in session.query(User.name).filter_by(fullname='Ed Jones'):
    print(name)
print()

for user in session.query(User).filter(User.name == 'ed'). \
        filter(User.fullname == 'Ed Jones'):
    print(user)
print()

query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
print(query.all())
print(query.first())
# ERROR with multiple results found
# user = query.one()
# print(user)
# ERROR with no results found
# user = query.filter(User.id == 99).one()
# No ERROR for one or none results but will for multiple
user = query.filter(User.id == 99).one_or_none()
print(user)
print()

query = session.query(User).filter(
    or_(User.name == 'ed', User.name == 'wendy'))
# print(query.scalar())
print(query.all())
print()


# BUILDING AND WORKING WITH RELATIONSHIPS =====================================

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship(
    "Address", order_by=Address.id, back_populates="user")

Base.metadata.create_all(engine)

jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
print(jack.addresses)
jack.addresses = [
    Address(email_address='jack@google.com'),
    Address(email_address='j25@yahoo.com')]
print(jack.addresses)
print(jack.addresses[1])
print(jack.addresses[1].user)
print()

# session.add(jack)
# session.commit()

jack = session.query(User).filter_by(name='jack').one()
print(jack)

# QUERY WITH JOINS ============================================================
