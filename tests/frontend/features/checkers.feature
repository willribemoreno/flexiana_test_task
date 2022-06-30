@checker_front
Feature:
  As a player of the checkers game
  I want to perform some actions in order to validate if it's working properly

@scenario1
Scenario: Start a new game by restarting
  Given the user is in the home page
  When he starts a new game by clicking on restart button
  Then all pieces must return to default position

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
  Then the users piece must be moved correctly

@scenario5
Scenario: Let computer take your piece and make sure your piece is taken
  Given the user is in the home page
  And he starts a new game by clicking on restart button
  And he performs two movements
  When the computer take his piece
  Then the piece must no longer exist in the board

@scenario6
Scenario: Make movements and start a new game
  Given the user is in the home page
  And he starts a new game by clicking on restart button
  And he performs some movements
  When he starts a new game
  Then all pieces must return to default position