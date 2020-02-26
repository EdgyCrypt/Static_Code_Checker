def prepHTML(text: str, expression: bool ):
    """
    Returns the match or miss for each character while already moving it to html
    text: the actual character
    expression: matching status
    """
    if expression:
        return f'<div class="__g__"> {text} </div>'
    else:
        return f'<div class="__r__"> {text} </div>'


def compare(original_text: string, generated_text: string):
    """
    Compares 2 strings and returns html to be served to the models
    original_text - The text from the example
    generated_text - The text from the 
    """
    comparison = ""

    # we will assume that this is the actual text
    for i in range(len(generated_text)):
        try:
            comparison += prepHTML(generated_text[i], generated_text[i] == original_text[i])
        except IndexError:
                comparison += prepHTML(generated_text[i], False)

    if len(original_text) > len(generated_text):
        comparison += prepHTML(original_text[len(generated_text):len(original_text)], False)

    percent_match = comparison.count("__g__") / (comparison.count("__g__") + comparison.count("__r__"))

    return comparison, percent_match