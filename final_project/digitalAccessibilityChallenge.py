# ---Course: Ethics
# ---Semester Fall 2022
# ---Format/IDE:Python/Colab

print("Welcome to our TEST YOUR DIGITAL ACCESSIBILITY KNOWLEDGE challenge!")
print('NOTE: Please check your spelling and punctuation to ensure that your responses are graded correctly')
score = 0
question_no = 0
playing = input(f'\nAre you ready to begin? ').lower()
if playing == 'yes':

# --1
    question_no += 1
    ques = input(f'\n{question_no}. In what year was the Americans With Disabilities Act passed? ...  ')
    if ques == '1990':
        score +=1
        print('   Well done! 1 point has been added to your digital accessibility knowledge score.')
        
    else:
        print('   Oh no...')
        print(f'   The correct challenge response is 1990.')


# --2
    question_no += 1
    ques = input(f'\n{question_no}. According to the CDC, what percentage of Americans have a disability? Select one: 25%, 50%, 75% or 100%  ...  ').lower()
    
    if ques == '25%':
        score +=1
        print('   Awesome! 1 point has been added to your digital accessibility knowledge score.')
        
    else:
        print('   Time for a little review...')
        print(f'   The correct response is 25%.')


# --3
    question_no += 1
    ques = input(f'\n{question_no}. What type of disability includes color blindness, low vision and or no vision? Enter one term: visual, auditory, speech, motor or cognitive? ...  ').lower()
    

    if ques == 'visual':
        score +=1
        print('   Great Job! 1 point has been added to your digital accessibility knowledge score.')
        
    else:
        print('   Oh no...')
        print(f'   The correct challenge response is visual.')


# --4
    question_no += 1
    ques = input(f'\n{question_no}. What type of disability includes focus or learning differences? Enter One term: visual, auditory, speech, motor or cognitive? ... ').lower()
    
    if ques == 'cognitive':
        score +=1
        print('   Excellent! 1 point has been added to your digital accessibility knowledge score.')
        
    else:
        print('   Time for a little review...')
        print(f'   The correct response is cognitive.')


# --5
    question_no += 1
    ques = input(f'\n{question_no}. What type of disability includes stuttering, apraxia, dysarthrai? Enter one term: auditory, speech, visual, motor or cognitive ...  ').lower()
    
    if ques == 'speech':
        score +=1
        print('Correct! 1 point has been added to your digital accessibility knowledge score.')
        
    else:
        print('   On no...')
        print(f'   The corect challenge response is speech.')


# --6 
    question_no += 1
    ques = input(f'\n{question_no}. What type of disability includes deafness or hard of hearing? Enter one term: cognitive, auditory, speech, motor or visual ...  ').lower()
    
    if ques == 'auditory':
        score +=1
        print('Perfect! 1 point has been added to your accessibility knowledge score.')
        
    else:
        print('   Time for a little review ...')
        print(f'   The correct response is auditory.')


# --7
    question_no += 1
    ques = input(f'\n{question_no}. What type of disability includes fine motor control or slow response time? Enter one term: motor, auditory, speech, visual or cognitive ...  ').lower()
    
    if ques == 'motor':
        score +=1
        print('Superb! 1 point has been added to your digital accessibility knowledge score.')
        
    else:
        print('   Oh no...')
        print(f'   The correct challenge response is motor.')


# --8
    question_no += 1
    ques = input(f'\n{question_no}. Can the absence of digital accessility inclusinve tools on a websites lead to lawsuits? Enter one response: yes or no ...  ').lower()
    
    if ques == 'yes':
        score +=1
        print('Great Response! 1 point has been added to your digital accessibility knowledge score.')
        
    else:
        print('   Time for a litte review...')
        print(f'   The correct answer is yes.')


# --9
    question_no += 1
    ques = input(f'\n{question_no}. The asccessibility of a website should be checked by a... Enter one response: a colleague, an accessibilty checker or a revenue checker ...  ').lower()
    
    if ques == 'an accessibility checker':
        score +=1
        print('Exceptional! 1 point has been added to your digital accessibility knowledge score.')
        
    else:
        print('   Oh no...')
        print(f'   The correct response is an accessibility checker.')


# --10
    question_no += 1
    ques = input(f'\n{question_no}.  What does WCAG stand for? ...  ')
    
    if ques == 'Web Content Accessibility Guidelines':
        score +=1
        print('Excellent Job! 1 point has been added to your digital accessibility knowledge score.correct! you got 1 point')
        
    else:
        print('     Time for a little review...')
        print(f'      The correct answer is Web Content Accessibility Guidelines.')


# --11
    question_no += 1
    ques = input(f'\n{question_no}. What percentage of website are accessible? Enter one response: 2%, 5%, 10%, 15% or 20% ...  ').lower()
    
    if ques == '2%':
        score +=1
        print('Awesome Job! 1 point has been added to your digital accessibility knowledge score.')
        
    else:
        print('    Oh no...')
        print(f'    The correct answer is --> 2%')


# --12
    question_no += 1
    ques = input(f'\n{question_no}. What does SEO stand for? ...  ').lower()
    
    if ques == 'search engine optimization':
        score +=1
        print('Awesome Job! 1 point has been added to your digital accessibility knowledge score.')
        
    else:
        print('    Time for a little review...')
        print(f'    The correct answer is search engine optimization.')


# --End

else:
    print('Thanks for taking our DIGITAL ACCESSIBILTY KNOWLEDGE challenge.')
    quit()

print(f'\nDIGITAL ACCESSIBILLITY CHALLENGE SCORE REPORT: The number of challlenge questions asked were {question_no}.')
print(f'Your DIGITAL ACCESSIBILTY KNOWLEDGE score is {score}.')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% questions were correctly answered.')

print(f'{percentage}% of digital accessible challenge questions were correctly answered.')
