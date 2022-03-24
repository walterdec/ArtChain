from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SelectField, TextAreaField, PasswordField, SubmitField,\
    IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, InputRequired, EqualTo, NumberRange, Email, Length
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('login')


class EditArtistForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confpassword = PasswordField('confpassword', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    category = StringField('category', validators=[DataRequired()])

    instauser = StringField('instauser')
    instafollowers = IntegerField('instafollowers')
    faceuser = StringField('faceuser')
    facefollowers = IntegerField('facefollowers')
    twitteruser = StringField('twitteruser')
    twitterfollowers = IntegerField('twitterfollowers')
    ytuser = StringField('ytuser')
    ytfollowers = IntegerField('ytfollowers')
    tiktokuser = StringField('tiktokuser')
    tiktokfollowers = IntegerField('tiktokfollowers')
    twitchuser = StringField('twitchuser')
    twitchfollowers = IntegerField('twitchfollowers')
    applemusicuser = StringField('applemusicuser')
    applemusicfollowers = IntegerField('applemusicfollowers')
    spotifyuser = StringField('spotifyuser')
    spotifyfollowers = IntegerField('spotifyfollowers')
    soundclouduser = StringField('soundclouduser')
    soundcloudfollowers = IntegerField('soundcloudfollowers')
    sales = IntegerField('sales')

    submit = SubmitField('Create Account')


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

