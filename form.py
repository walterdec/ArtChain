from flask_wtf import FlaskForm
from markupsafe import Markup
from wtforms import StringField, SelectField, TextAreaField, PasswordField, SubmitField, IntegerField, validators,\
        FloatField
from wtforms.validators import DataRequired, InputRequired, Email, Length, NumberRange
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField(Markup('&#x1F50D;'))


class CustomerRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=3, max=20,
                                                          message="Username must be between 3 and 20 characters")])
    email = StringField('Email', validators=[DataRequired(), Email(message="Email is not valid")])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=8, max=30, message="Password must be between 8 and 30 characters")])
    confpassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class ArtistRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),
                                                   Length(min=3, max=20,
                                                          message="Username must be between 3 and 20 characters")])
    name = StringField('Name', validators=[InputRequired()])
    surname = StringField('Surname', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(),
                                                     Length(min=8, max=30,
                                                     message="Password must be between 8 and 30 characters")])
    confpassword = PasswordField('Confirm password', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email(message="Email is not valid")])
    category = SelectField('Category', choices=['Musician', 'Sketcher', 'Video Maker', 'Other'])

    crypto = StringField('Crypto Acronym', validators=[DataRequired()])

    profile_pic = FileField('Profile Picture', validators=[DataRequired(),
                                                           FileAllowed(['jpg', 'png', 'jpeg', 'webp'],
                                                                       message="File must be .jpg, .png, .jpeg or .webp")])

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

    submit = SubmitField('Create Account')


class EditArtistForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message="Email is not valid")])
    password = PasswordField('Password', validators=[validators.optional(),
                                                     Length(min=8, max=30,
                                                            message="Password must be between 8 and 30 characters")])
    confpassword = PasswordField('Confirm password', validators=[validators.optional()])

    profile_pic = FileField('Profile Picture', validators=[validators.optional(),
                                                           FileAllowed(['jpg', 'png', 'jpeg', 'webp'],
                                                                       message="File must be .jpg, .png, .jpeg or .webp")])

    instauser = StringField('Instagram', [validators.optional()])
    instafollowers = IntegerField('Instagram', [validators.optional()])
    faceuser = StringField('Facebook', [validators.optional()])
    facefollowers = IntegerField('Facebook', [validators.optional()])
    twitteruser = StringField('Twitter', [validators.optional()])
    twitterfollowers = IntegerField('Twitter', [validators.optional()])
    ytuser = StringField('YouTube', [validators.optional()])
    ytfollowers = IntegerField('YouTube', [validators.optional()])
    tiktokuser = StringField('TikTok', [validators.optional()])
    tiktokfollowers = IntegerField('TikTok', [validators.optional()])
    twitchuser = StringField('Twitch', [validators.optional()])
    twitchfollowers = IntegerField('Twitch', [validators.optional()])
    applemusicuser = StringField('Apple Music', [validators.optional()])
    applemusicfollowers = IntegerField('Apple Music', [validators.optional()])
    spotifyuser = StringField('Spotify', [validators.optional()])
    spotifyfollowers = IntegerField('Spotify', [validators.optional()])
    soundclouduser = StringField('SoundCloud', [validators.optional()])
    soundcloudfollowers = IntegerField('SoundCloud', [validators.optional()])

    submit = SubmitField('Save Profile')


class EditCustomerForm(FlaskForm):
    email = StringField('Email', validators=[Email(message="Email is not valid")])
    password = PasswordField('Password', validators=[validators.optional(),
                                                     Length(min=8, max=30, message="Password must be between 8 and 30 "
                                                                                   "characters")])
    confpassword = PasswordField('Confirm password', validators=[validators.optional()])
    submit = SubmitField('Save Profile')


class NewNFTForm(FlaskForm):
    nft_name = StringField('NFT Name', validators=[DataRequired()])
    category = SelectField('Category', choices=['Art', 'Music', 'Video Games', 'Collectible Items', 'Sport', 'Memes',
                                                'Miscellaneous'], validators=[DataRequired()])
    price = FloatField('Price', validators=[InputRequired(), NumberRange(min=0,
                                                                         message="Price must be at least 0 ACH")])
    description = TextAreaField('Description', validators=[DataRequired()])
    nft_file = FileField('File', validators=[DataRequired(),
                                             FileAllowed(['jpg', 'png', 'jpeg', 'webp'],
                                                         message="File must be .jpg, .png, .jpeg or .webp")])
    submit = SubmitField('Create NFT')


class BuySellCryptoForm(FlaskForm):
    amount_buy = FloatField('Buy/Sell', validators=[validators.optional(), NumberRange
                                                    (min=0, message="Amount must be > 0")])
    amount_sell = FloatField('Buy/Sell', validators=[validators.optional(), NumberRange
                                                     (min=0, message="Amount must be > 0")])
    submit = SubmitField('Buy/Sell')


class ResellNFTForm(FlaskForm):
    new_price = FloatField('New Price', validators=[DataRequired(),
                                                    NumberRange(min=0, message="Price must be at least 0 ACH")])
    submit = SubmitField('Put On Sale')


class SelectNFTViewForm(FlaskForm):
    select = SelectField('Choose', choices=['All', 'On Sale'], validators=[DataRequired()])
    submit = SubmitField('Select')


class BuyNFTForm(FlaskForm):
    submit = SubmitField('Buy')


class CancelNFTSaleForm(FlaskForm):
    submit = SubmitField('Keep NFT')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message="Email is not valid")])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')


class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message="Email is not valid")])
    submit = SubmitField('Recover Password')




