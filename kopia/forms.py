"""
kopia.forms
===========

Handle all forms.
"""
from flask import current_app as app
from flask_wtf import FlaskForm
from wtforms.widgets.core import Input
from wtforms.validators import (
    DataRequired,
    ValidationError,
)
from wtforms import (
    DateField,
    IntegerField,
    StringField,
    PasswordField,
)

from tinydb import Query

from .database import get_db


class IntegerInput(Input):
    """
    Render a single-line integer input.
    """

    input_type = 'number'


class DateInput(Input):
    """
    Render a single-line date input.
    """
    input_type = 'date'


class IntField(IntegerField):
    def process_formdata(self, valuelist):
        try:
            super(IntField, self).process_formdata(valuelist)
        except ValueError:
            pass


class UserLoginForm(FlaskForm):
    ID = IntField('Nomerao',
                  widget=IntegerInput(),
                  validators=[DataRequired()])
    name = StringField('Anarana feno',
                       validators=[DataRequired()])
    birth = DateField('Teraka',
                      widget=DateInput(),
                      validators=[DataRequired()])

    def validate_ID(self, field):
        db = get_db()
        q = Query()

        result = db.get(q.ID == field.data)

        if result is None:
            raise ValidationError('Tsy misy io Nomerao io')
        return True

    def validate_name(self, field):
        try:
            self.validate_ID(self.ID)
        except ValidationError:
            return False

        db = get_db()
        q = Query()

        result = db.get(q.ID == self.ID.data)['full_name']
        if field.data != result:
            raise ValidationError("Tsy mifanaraka amin'ny anarana ny nomerao")
        return True

    def validate_birth(self, field):
        try:
            self.validate_name(self.name)
        except ValidationError:
            return

        if not self.validate_name(self.name):
            return

        db = get_db()
        q = Query()

        result = db.get(q.ID == self.ID.data)['birth_date']
        app.logger.info(result)
        app.logger.info(field.data)
        if field.data != result:
            raise ValidationError(f"Tsy tamin'io no teraka i {self.name.data}")


class ModeratorLoginForm(FlaskForm):
    nickname = StringField("Solon'anarana")
    password = PasswordField('Tenimiafina')

    def validate_nickname(self, field):
        pass

    def validate_password(self, field):
        pass
