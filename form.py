from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SelectField, TextAreaField, PasswordField, SubmitField, \
    IntegerField, SelectMultipleField, validators
from wtforms.validators import DataRequired, InputRequired, EqualTo, NumberRange, Email, Length
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class CustomerRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20, message="Username must be between 3 and 20 characters")])
    email = StringField('Email', validators=[DataRequired(), Email(message="Email is not valid")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30, message="Password must be between 6 and 30 characters")])
    confpassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class ArtistRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=20, message="Username must be between 3 and 20 characters")])
    name = StringField('Name', validators=[InputRequired()])
    surname = StringField('Surname', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=30, message="Password must be between 6 and 30 characters")])
    confpassword = PasswordField('Confirm password', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email(message="Email is not valid")])
    category = StringField('Category', [validators.optional()])

    instauser = StringField('Instagram', [validators.optional()])
    instafollowers = IntegerField('Instagram followers', [validators.optional()])
    faceuser = StringField('Facebook', [validators.optional()])
    facefollowers = IntegerField('Facebook followers', [validators.optional()])
    twitteruser = StringField('Twitter', [validators.optional()])
    twitterfollowers = IntegerField('Twitter followers', [validators.optional()])
    ytuser = StringField('YouTube', [validators.optional()])
    ytfollowers = IntegerField('YouTube followers', [validators.optional()])
    tiktokuser = StringField('TikTok', [validators.optional()])
    tiktokfollowers = IntegerField('TikTok followers', [validators.optional()])
    twitchuser = StringField('Twitch', [validators.optional()])
    twitchfollowers = IntegerField('Twitch followers', [validators.optional()])
    applemusicuser = StringField('Apple Music', [validators.optional()])
    applemusicfollowers = IntegerField('Apple Music followers', [validators.optional()])
    spotifyuser = StringField('Spotify', [validators.optional()])
    spotifyfollowers = IntegerField('Spotify followers', [validators.optional()])
    soundclouduser = StringField('SoundCloud', [validators.optional()])
    soundcloudfollowers = IntegerField('SoundCloud followers', [validators.optional()])
    sales = IntegerField('Sales', [validators.optional()])

    submit = SubmitField('Create Account')


class EditArtistForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message="Email is not valid")])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=30, message="Password must be between 6 and 30 characters")])
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

