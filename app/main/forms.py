from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Your Blog', validators=[Required()],render_kw={'class': 'form-control', 'rows': 5})
    submit = SubmitField('Submit Blog')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Save')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment',validators=[Required()])
    submit = SubmitField('Comment')
    
