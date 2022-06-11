import pytest
from marshmallow import ValidationError

from src.dto.credentials import CredentialsSchema


def test_missing_fields():
    # given
    schema = CredentialsSchema()
    data = {
        "username": "sergio",
    }

    # when / then
    with pytest.raises(ValidationError):
        schema.load(data)