Feature:
  As a player of the checkers game
  I want to perform some actions in order to validate if it's working properly

@scenario1
Scenario: Start a new game by restarting
  Given the user is in the home page
  When he starts a new game by clicking on restart button
  Then all pieces must be returned to original place

@scenario2
Scenario: Make your first move
  Given the user is in the home page
  And he starts a new game by clicking on restart button
  When he makes his first move
  Then the users piece must be moved properly

@scenario3
Scenario: Let computer move
  Given the user is in the home page
  And he starts a new game by clicking on restart button
  And he makes his first move
  When the computer makes his move
  Then the computer piece must be moved properly

@scenario4
Scenario: Make your second move
  Given the user is in the home page
  And he starts a new game by clicking on restart button
  And he makes his first move
  When he makes his second move
  Then the users piece must be moved properly