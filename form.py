from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SelectField, TextAreaField, PasswordField, SubmitField, \
    IntegerField, SelectMultipleField, validators, FloatField
from wtforms.validators import DataRequired, InputRequired, EqualTo, NumberRange, Email, Length
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class CustomerRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=3, max=20,
                                                          message="Username must be between 3 and 20 characters")])
    email = StringField('Email', validators=[DataRequired(), Email(message="Email is not valid")])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=6, max=30, message="Password must be between 6 and 30 characters")])
    confpassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class ArtistRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),
                                                   Length(min=3, max=20,
                                                          message="Username must be between 3 and 20 characters")])
    name = StringField('Name', validators=[InputRequired()])
    surname = StringField('Surname', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(),
                                                     Length(min=6, max=30,
                                                     message="Password must be between 6 and 30 characters")])
    confpassword = PasswordField('Confirm password', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email(message="Email is not valid")])
    category = SelectField('Category', choices=['Musician', 'Sketcher', 'Video Maker', 'Other'])

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
    password = PasswordField('Password', validators=[validators.optional(),
                                                     Length(min=6, max=30,
                                                            message="Password must be between 6 and 30 characters")])
    confpassword = PasswordField('Confirm password', validators=[validators.optional()])

    instafollowers = IntegerField('Instagram', [validators.optional()])
    facefollowers = IntegerField('Facebook', [validators.optional()])
    twitterfollowers = IntegerField('Twitter', [validators.optional()])
    ytfollowers = IntegerField('YouTube', [validators.optional()])
    tiktokfollowers = IntegerField('TikTok', [validators.optional()])
    twitchfollowers = IntegerField('Twitch', [validators.optional()])
    applemusicfollowers = IntegerField('Apple Music', [validators.optional()])
    spotifyfollowers = IntegerField('Spotify', [validators.optional()])
    soundcloudfollowers = IntegerField('SoundCloud', [validators.optional()])
    sales = IntegerField('Sales', [validators.optional()])

    submit = SubmitField('Save Profile')


class EditCustomerForm(FlaskForm):
    email = StringField('Email', validators=[Email(message="Email is not valid")])
    password = PasswordField('Password', validators=[validators.optional(),
                                                     Length(min=6, max=30, message="Password must be between 6 and 30 "
                                                                                   "characters")])
    confpassword = PasswordField('Confirm password', validators=[validators.optional()])
    submit = SubmitField('Save Profile')


class NewNFTForm(FlaskForm):
    nft_name = StringField('NFT Name', validators=[DataRequired()])
    category = SelectField('Category', choices=['Art', 'Music', 'Video Games', 'Collectible Items', 'Sport', 'Memes',
                                                'Miscellaneous'], validators=[DataRequired()])
    price = FloatField('Price (Euro)', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    nft_file = FileField('File', validators=[DataRequired()])
    submit = SubmitField('Create NFT')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message="Email is not valid")])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')


class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message="Email is not valid")])
    submit = SubmitField('Recover Password')




