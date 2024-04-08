# QA3

## Each File's purpose 

1. categSelection.py : Creates the inital gui displaying the categories and then closes said window. Opens new window based on category selection of user's previous input and displays 10 questions. User clicks sumbit when he's done to see the correct answer. I find it more meaniful to make the user to scroll and look at each question they either got wrong or right so they retain the infromation better. Which is why I didn't display a score at the top when user submitted.

2. business_questions.py : Inserts a list of 10 question for five different categories into a table. Which is then used for the user in his gui, is the reason he is able to see what he sees on his end. Creates display for all 10 questions.

3. businessQuestions.db : This database stores all the important imformation behind the scenes. Is the support beam for the user's experience. Holds all 50 questions for dispol at any time. 
