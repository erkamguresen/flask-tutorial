import re

from marshmallow import Schema, fields, validates, ValidationError, post_load

from src.models.user import User


class UserCreationSchema(Schema):
    username = fields.String(Required=True)
    password = fields.String(Required=True)
    email = fields.String(Required=True)

    @validates("password")
    def validates_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        if not any(c.isupper() for c in value):
            raise ValidationError("Password must contain at least one uppercase character.")

        if not any(c.islower() for c in value):
            raise ValidationError("Password must contain at least one lowercase character.")

    @validates("email")
    def validates_email(self, value):
        if not re.match("[^@]+@[^@]+\.[^@]+", value):
            raise ValidationError("Invalid email format")

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
