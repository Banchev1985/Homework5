from functions import balance

for choice in range(1, 5):
    if choice == '1' and balance().score == '200':
        assert balance().score == '200'
    elif choice == '2' and balance().purchase_question_score == '300':
        assert balance().purchase_question_score == 'У Вас недостаточно средств на счете'
    elif choice == '2' and balance().purchase_question_score == '200':
        assert balance().score == '0'
    elif choice == '2' and balance().purchase_question == 'Банан':
        assert balance().purchase_question == 'Банан'
