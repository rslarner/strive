Design:

Concepts:

 - Users, with emails

 - Test: type (Skill Evaluation), title, description
 
 - Question, child of Test: title, sequence, and time
 
 - UserTest: test_id, user_id, start_time, status
 
 - UserAnsweredQuestion: question_id, user_id, answer, start_time

 
 Apps:
  - Users
  - Tests
  
  
  Setup:
   - python 3.4.4
   - virtualenv venv
   - source venv/bin/activate
   - pip install -r requirements.txt

Admin:
 - python manage.py createsuperuser
 - http://127.0.0.1:8000/admin
 - create the test and questions
 
 Taking the test:
  - python manage makemigrations
  - python manage migrate 
  - python manage runserver
  - http://127.0.0.1/login
  - complete login, redirects to /tests
  - start test, redirects to /tests/questions
  - completing question redirects to subsequent question

Work left to do:
 - Get model form to actually save the POSTed data!
 - better test experience, e.g. present tests that can be taken on the /tests/ page based on entries in UserTests
   - comparing number of entries in UserQuestion vs Questions for given test indicate tests started by user but not completed
   - Tests without corresponding UserTests entries are unstarted
- UserQuestionView needs to take the test_id in. should go to first question in sequence for test for which no UserQuestion exists
- implement timer check
  - default start_time to now
  - validate the UserQuestion.start_time + Question.duration is not more than now
  