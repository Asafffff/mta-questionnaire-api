Extensible Database Schema
Tables:

Users

Stores user information.
Columns:
id (Primary Key, UUID): Unique identifier for each user.
username (VARCHAR): Username of the user.
email (VARCHAR): Email address of the user.
password_hash (VARCHAR): Hashed password for authentication.
created_at (TIMESTAMP): Timestamp when the user was created.
updated_at (TIMESTAMP): Timestamp when the user information was last updated.
Questionnaires

Stores information about each questionnaire.
Columns:
id (Primary Key, UUID): Unique identifier for each questionnaire.
name (VARCHAR): Name of the questionnaire (e.g., Sleep, Mood, Diet).
description (TEXT): Description of the questionnaire.
created_at (TIMESTAMP): Timestamp when the questionnaire was created.
updated_at (TIMESTAMP): Timestamp when the questionnaire was last updated.
Questions

Stores information about each question.
Columns:
id (Primary Key, UUID): Unique identifier for each question.
questionnaire_id (Foreign Key, UUID): References Questionnaires(id).
text (TEXT): The text of the question.
type (VARCHAR): The type of the question (e.g., integer, string, date-time).
created_at (TIMESTAMP): Timestamp when the question was created.
updated_at (TIMESTAMP): Timestamp when the question was last updated.
Answers

Stores responses to each question.
Columns:
id (Primary Key, UUID): Unique identifier for each answer.
user_id (Foreign Key, UUID): References Users(id).
question_id (Foreign Key, UUID): References Questions(id).
answer (TEXT): The answer provided by the user.
created_at (TIMESTAMP): Timestamp when the answer was created.

```sql
CREATE TABLE Users (
  id UUID PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Questionnaires (
  id UUID PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Questions (
  id UUID PRIMARY KEY,
  questionnaire_id UUID REFERENCES Questionnaires(id) ON DELETE CASCADE,
  text TEXT NOT NULL,
  type VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Answers (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES Users(id) ON DELETE CASCADE,
  question_id UUID REFERENCES Questions(id) ON DELETE CASCADE,
  answer TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Example Data
```sql
-- Inserting questionnaires
INSERT INTO Questionnaires (id, name, description) VALUES
  (uuid_generate_v4(), 'Sleep', 'Questions about sleep patterns and quality'),
  (uuid_generate_v4(), 'Mood', 'Questions about mood rating'),
  (uuid_generate_v4(), 'Diet', 'Questions about dietary habits');

-- Inserting questions for Sleep Questionnaire
INSERT INTO Questions (id, questionnaire_id, text, type) VALUES
  (uuid_generate_v4(), (SELECT id FROM Questionnaires WHERE name = 'Sleep'), 'When did you go to sleep?', 'date-time'),
  (uuid_generate_v4(), (SELECT id FROM Questionnaires WHERE name = 'Sleep'), 'When did you wake up?', 'date-time'),
  (uuid_generate_v4(), (SELECT id FROM Questionnaires WHERE name = 'Sleep'), 'Rate your sleep quality from 1-10', 'integer');

-- Inserting questions for Mood Questionnaire
INSERT INTO Questions (id, questionnaire_id, text, type) VALUES
  (uuid_generate_v4(), (SELECT id FROM Questionnaires WHERE name = 'Mood'), 'Rate your mood from 1-10', 'integer');

-- Inserting questions for Diet Questionnaire
INSERT INTO Questions (id, questionnaire_id, text, type) VALUES
  (uuid_generate_v4(), (SELECT id FROM Questionnaires WHERE name = 'Diet'), 'When did you eat your first meal?', 'date-time'),
  (uuid_generate_v4(), (SELECT id FROM Questionnaires WHERE name = 'Diet'), 'When did you eat your last meal?', 'date-time'),
  (uuid_generate_v4(), (SELECT id FROM Questionnaires WHERE name = 'Diet'), 'Describe your meals', 'text'),
  (uuid_generate_v4(), (SELECT id FROM Questionnaires WHERE name = 'Diet'), 'Meal category (e.g., Vegetarian, Non-Vegetarian, Vegan, Pescatarian)', 'string');
```
