def truncate_text(text):

    if len(text)>20:
        return text[:17]+'...'
    print(text)
    return text
truncate_text("Hello, world!")
truncate_text("This string should get truncated.")
truncate_text("Exactly twenty chars")
truncate_text(".....................")