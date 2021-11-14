from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment
from .forms import UpdateProfile,BlogForm,CommentForm,UpdateBlog
from .. import db,photos
from ..request import get_quotes


@main.route('/')
def index():
    pitches = Pitch.query.all()
    quotes = get_quotes()
    return render_template('index.html', pitches = pitches,quotes =quotes,user=current_user)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data         
        new_pitch = Pitch(title = title,post=post,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))
        
    return render_template('new_blog.html', form = form,titl = "Create Blog"   )

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        new_comment = Comment(comment = comment,pitch_id = pitch_id,user=current_user)
        new_comment.save_comment()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    
    return render_template('comment.html', form =form, pitch = pitch,comments=comments)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    posts = Pitch.query.filter_by(user = current_user).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data  
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route("/pitch/<int:pitch_id>/delete",methods= ['POST'])
@login_required
def delete_post(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    db.session.delete(pitch)
    db.session.commit()
    flash('Your blog has been deleted!')
    return redirect(url_for('main.index'))

@main.route("/delete_comment/<int:pitch_id>/<int:comment_id>",methods= ['POST'])
@login_required
def delete_comment(comment_id,pitch_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    flash('Comment has been deleted!')
    return redirect(url_for('.comment', pitch_id = pitch_id))

@main.route("/update_post/<int:pitch_id>",methods= ['POST','GET'])
@login_required
def update_post(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    form = UpdateBlog()
    if form.validate_on_submit():
        pitch.title =form.title.data
        pitch.post = form.post.data
        db.session.commit()
        flash('Your post has been updated!',)
        return redirect(url_for('main.index',pitch_id=pitch_id))
    elif request.method == 'GET':
        form.title.data = pitch.title
        form.post.data = pitch.post
    return render_template('new_blog.html',form=form, titl='Update Blog')
    