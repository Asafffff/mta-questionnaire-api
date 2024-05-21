from openapi_server.models.question import Question


sleepQuestionnaireQuestions = [
    Question(
        questionnaire_id="664b2c642691e903bc07344e",
        text="באיזה שעה הלכת לישון?",
    ).model_dump(by_alias=True),
    Question(
        questionnaire_id="664b2c642691e903bc07344e", text="באיזה שעה התעוררת?"
    ).model_dump(by_alias=True),
    Question(
        questionnaire_id="664b2c642691e903bc07344e",
        text="איך היית מדרג את איכות השינה שלך?",
    ).model_dump(by_alias=True),
]

moodQuestionnaireQuestions = [
    Question(
        questionnaire_id="664b2c642691e903bc073450",
        text="איך היית מדרג את מצב הרוח שלך?",
    ).model_dump(by_alias=True),
]

dietQuestionnaireQuestions = [
    Question(
        questionnaire_id="664b2c642691e903bc07344f",
        text="באיזה שעה אכלת את הארוחה הראשונה שלך (אתמול)?",
    ).model_dump(by_alias=True),
    Question(
        questionnaire_id="664b2c642691e903bc07344f",
        text="באיזה שעה אכלת את הארוחה האחרונה שלך (אתמול)?",
    ).model_dump(by_alias=True),
    Question(
        questionnaire_id="664b2c642691e903bc07344f",
        text="מה אכלת בארוחה האחרונה שלך אתמול?",
    ).model_dump(by_alias=True),
]
