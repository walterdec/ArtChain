from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SelectField, TextAreaField, PasswordField, SubmitField,\
    IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, InputRequired, EqualTo, NumberRange, Email, Length
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class CustomerRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20, message="Username must be between 3 and 20 characters")])
    email = StringField('Email', validators=[DataRequired(), Email(message="Email is not valid")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=16, message="Password must be between 8 and 16 characters")])
    confpassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class ArtistRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=20, message="Username must be between 3 and 20 characters")])
    name = StringField('Name', validators=[InputRequired()])
    surname = StringField('Surname', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=16, message="Password must be between 8 and 16 characters")])
    confpassword = PasswordField('Confirm password', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email(message="Email is not valid")])
#   category = StringField('Category', validators=[DataRequired()])

    instauser = StringField('Instagram')
    instafollowers = IntegerField()
    faceuser = StringField('Facebook')
    facefollowers = IntegerField()
    twitteruser = StringField('Twitter')
    twitterfollowers = IntegerField()
    ytuser = StringField('YouTube')
    ytfollowers = IntegerField()
    tiktokuser = StringField('TikTok')
    tiktokfollowers = IntegerField()
    twitchuser = StringField('Twitch')
    twitchfollowers = IntegerField()
    applemusicuser = StringField('Apple Music')
    applemusicfollowers = IntegerField()
    spotifyuser = StringField('Spotify')
    spotifyfollowers = IntegerField()
    soundclouduser = StringField('SoundCloud')
    soundcloudfollowers = IntegerField()
    sales = IntegerField('Sales')

    submit = SubmitField('Create Account')


class EditArtistForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message="Email is not valid")])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=16, message="Password must be between 8 and 16 characters")])
    confpassword = PasswordField('Confirm password', validators=[InputRequired()])

    #   category = StringField('Category', validators=[DataRequired()])

    instauser = StringField('Instagram')
    instafollowers = IntegerField()
    faceuser = StringField('Facebook')
    facefollowers = IntegerField()
    twitteruser = StringField('Twitter')
    twitterfollowers = IntegerField()
    ytuser = StringField('YouTube')
    ytfollowers = IntegerField()
    tiktokuser = StringField('TikTok')
    tiktokfollowers = IntegerField()
    twitchuser = StringField('Twitch')
    twitchfollowers = IntegerField()
    applemusicuser = StringField('Apple Music')
    applemusicfollowers = IntegerField()
    spotifyuser = StringField('Spotify')
    spotifyfollowers = IntegerField()
    soundclouduser = StringField('SoundCloud')
    soundcloudfollowers = IntegerField()
    sales = IntegerField('Sales')

    submit = SubmitField('Create Account')


class ForgotPasswordForm(FlaskForm):
    email = StringField('Type your email', validators=[InputRequired(), Email(message="Email is not valid")])
    submit = SubmitField('Send Email')

