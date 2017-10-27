def create_tag(item, tag="a"):
    """ some function to wrapp HTML-tag with data-attributes around a string"""
    try:
        item_text = item.text
    except AttributeError:
        item_text = "no text provided"
    try:
        item_lang = item.language
    except AttributeError:
        item_lang = "no lang provided"
    try:
        item_id = item.id
    except AttributeError:
        item_id = "no ID"
    try:
        item_url = item.get_absolute_url()
    except AttributeError:
        item_url = "#"
    #item_url = item
    return "<{} data-lang='{}' data-id='{}' href='{}'>{}</{}>".format(
        tag, item_lang, item_id, item_url, item_text, tag
    )
