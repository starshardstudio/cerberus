"""
Module defining declaratively SQL tables via :mod:`sqlalchemy`.
"""

import sqlalchemy as s
import sqlalchemy.orm as so
import sqlalchemy.schema as ss
import authlib.integrations.sqla_oauth2
import uuid


class Base(so.DeclarativeBase):
    """
    Declarative base of the project.
    """


class Person(Base):
    """
    A physical person who uses the service.
    """
    __tablename__ = "people"

    name: so.Mapped[str] = so.mapped_column(primary_key=True)
    avatar: so.Mapped[str] = so.mapped_column(nullable=False, default="https://raw.githubusercontent.com/starshardstudio/emblems/main/rendered/person.png")
    password: so.Mapped[bytes] = so.mapped_column()

    controls: so.Mapped["Control"] = so.relationship(back_populates="person")
    clients: so.Mapped["Client"] = so.relationship(back_populates="creator")


class Control(Base):
    """
    Bridge table connecting :class:`Person` to :class:`Identity`.
    """
    __tablename__ = "control"

    id: so.Mapped[uuid.UUID] = so.mapped_column(primary_key=True)

    person_name: so.Mapped["str"] = so.mapped_column()
    identity_name: so.Mapped["str"] = so.mapped_column()

    person: so.Mapped["Person"] = so.relationship(back_populates="controls")
    identity: so.Mapped["Identity"] = so.relationship(back_populates="controlled_by")

    __table_args__ = (
        ss.UniqueConstraint(person_name, identity_name, name="bridge_person_identity"),
    )


class Identity(Base):
    """
    An identity that the physical person decided to assume.
    """
    __tablename__ = "identities"

    name: so.Mapped[str] = so.mapped_column(primary_key=True)
    avatar: so.Mapped[str] = so.mapped_column(nullable=False, default="https://raw.githubusercontent.com/starshardstudio/emblems/main/rendered/user.png")

    controlled_by: so.Mapped["Control"] = so.relationship(back_populates="identity")
    tokens: so.Mapped["Token"] = so.relationship(back_populates="identity")

    def get_user_id(self):
        return self.name


class Token(Base, authlib.integrations.sqla_oauth2.OAuth2TokenMixin):
    """
    A OAuth2 token for an :class:`Identity`.
    """
    __tablename__ = "people_tokens"

    id: so.Mapped[uuid.UUID] = so.mapped_column(primary_key=True)
    identity_name: so.Mapped[str] = so.mapped_column(s.ForeignKey("identities.name"), nullable=False)

    identity: so.Mapped["Identity"] = so.relationship(back_populates="tokens")


class Client(Base, authlib.integrations.sqla_oauth2.OAuth2ClientMixin):
    """
    A OAuth2 client registered by a :class:`Person`.
    """
    __tablename__ = "clients"

    id: so.Mapped[uuid.UUID] = so.mapped_column(primary_key=True)
    creator_name: so.Mapped[str] = so.mapped_column(s.ForeignKey("people.name"), nullable=False)

    creator: so.Mapped["Person"] = so.relationship(back_populates="clients")


__all__ = (
    "Base",
    "Person",
    "Control",
    "Identity",
    "Token",
    "Client",
)
