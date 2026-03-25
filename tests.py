import pytest
from model import Question

def test_create_question(): 
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title(): 
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct
    
def test_create_choice_with_invalid_text():
    question = Question(title='q1')
    
    with pytest.raises(Exception):
        question.add_choice('', False)
    with pytest.raises(Exception):
        question.add_choice('a'*101, False) 

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points=0)
    with pytest.raises(Exception):
        Question(title='q1', points=101)
        
def test_remove_choice_by_id():
    question = Question(title='q1')
    
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', True)

    assert len(question.choices) == 2

    question.remove_choice_by_id(choice1.id)

    assert len(question.choices) == 1
    assert question.choices[0].id == choice2.id
    
def test_remove_choice_with_invalid_id():
    question = Question(title='q1')
    
    choice1 = question.add_choice('a', False)

    with pytest.raises(Exception):
        question.remove_choice('invalido')

def test_remove_all_choices():
    question = Question(title='q1')
    
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', True)

    assert len(question.choices) == 2

    question.remove_all_choices()

    assert len(question.choices) == 0

def test_set_correct_choices():
    question = Question(title='q1', max_selections=2)
    
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', False)
    choice3 = question.add_choice('c', False)

    assert not choice1.is_correct
    assert not choice2.is_correct
    assert not choice3.is_correct

    question.set_correct_choices([choice2.id, choice3.id])

    assert not choice1.is_correct
    assert choice2.is_correct
    assert choice3.is_correct
    
def test_set_correct_choices_with_invalid_id():
    question = Question(title='q1', max_selections=2)
    
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', False)

    with pytest.raises(Exception):
        question.set_correct_choices(['invalido'])
        
def test_correct_selected_choices():
    question = Question(title='q1', max_selections=1)
    
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', False)

    question.set_correct_choices([choice1.id])
    
    result = question.correct_selected_choices([choice1.id])
    
    assert result == [choice1.id]
    
def test_incorrect_selected_choices():
    question = Question(title='q1', max_selections=1)
    
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', False)

    question.set_correct_choices([choice1.id])
    
    result = question.correct_selected_choices([choice2.id])
    
    assert result == []
    
def test_correct_selected_choices_more_than_max_selections():
    question = Question(title='q1', max_selections=1)
    
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', False)

    question.set_correct_choices([choice1.id])
    
    with pytest.raises(Exception):
        question.correct_selected_choices([choice1.id, choice2.id])