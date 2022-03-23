from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SelectField, TextAreaField, PasswordField, SubmitField, IntegerField, SelectMultipleField
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
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confpassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class ArtistRegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confpassword = PasswordField('confpassword', validators=[DataRequired()])
    #email = StringField('email', validators=[DataRequired(), Email()])
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

