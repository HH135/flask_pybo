from flask import Blueprint, render_template, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from pybo.models import Question
from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    #question_list = Question.query.order_by(Question.create_date.desc())
    #return render_template('question/question_list.html', question_list=question_list)

@bp.route('detail/<int:question_id>/')
def detail(question_id):
    #----- �럹�씠吏� �삤瑜�
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)
