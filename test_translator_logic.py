from translator_logic import TranslatorLogic

def test_integration():
    logic = TranslatorLogic()
    text = "hello"
    translated_text = logic.translate(text)
    assert translated_text is not None
    print(f"Translated text: {translated_text}")

test_integration()
