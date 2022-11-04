import pandas as pd
from IPython.display import Image, HTML


def path_to_image_html(path):
    '''
     This function essentially convert the image url to
     '<img src="'+ path + '"/>' format. And one can put any
     formatting adjustments to control the height, aspect ratio, size etc.
     within as in the below example.
    '''

    return '<img src="' + path + '" style=max-height:124px;"/>'


HTML(df.to_html(escape=False, formatters=dict(column_name_with_image_links=path_to_image_html)))
