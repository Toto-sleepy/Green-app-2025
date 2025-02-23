from flask import render_template, Blueprint

developers=Blueprint('developers',__name__)

@developers.route('/developers')
def developers_home():
  return render_template('developers.html', title='developers')