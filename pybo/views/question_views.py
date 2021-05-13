from datetime import datetime
from flask import Blueprint, render_template, request, url_for, g
from werkzeug.utils import redirect
#질문 라우트
from .. import db
from ..forms import QuestionForm, AnswerForm
from ..models import Question
from ..views.auth_views import login_required

bp = Blueprint('question', __name__, url_prefix='/question')

#질문 목록
@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list)

#질문 디테일
@bp.route('detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

#질문 등록 라우트에 GET과 POST 방식을 포함하는 methods 속성을 추가
@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    #데이터를 저장하기 위한 코드
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)