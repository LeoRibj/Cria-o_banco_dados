from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect, select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class Clientes(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    fullname = Column(String,nullable=False)
    cpf = Column(String(11), unique=True,nullable=False)
    banco = relationship(
        'Contas',back_populates='clientes',cascade='all,delete-orphan'
    )

    def __repr__(self):
        return f"Clientes(id={self.id},fullname={self.fullname},cpf={self.cpf})"

class Contas(Base):
    __tablename__ = 'banco'
    id = Column(Integer,primary_key=True)
    num_conta = Column(String(60), unique=True,nullable=False)
    agencia = Column(String(60),nullable=False)
    user_id = Column(Integer,ForeignKey("cliente.id"),nullable=False)
    clientes = relationship("Clientes",back_populates="banco")

    def __repr__(self):
        return f"Contas(id={self.id},num_conta={self.num_conta},agencia={self.agencia})"


engine = create_engine('sqlite://')

Base.metadata.create_all(engine)


with Session(engine) as session:
    Leo = Clientes(
        cpf="00022288825",
        fullname="leonardo martins",
        banco=[Contas(num_conta='00001', agencia='00002'),
                Contas(num_conta='00002', agencia='000003')]

    )

    Duda = Clientes(
        cpf="66655544452",
        fullname="Maria Eduarda",
        banco=[Contas(num_conta='55500', agencia='99666')]
    )
    session.add_all([Leo, Duda])

    session.commit()

stmt = select(Clientes).where(Clientes.fullname.in_(['Maria Eduarda']))

for cliente in session.scalars(stmt):
    print(cliente)