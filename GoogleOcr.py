import io
from google.cloud import vision
from PIL import Image, ImageDraw


def draw_boxes(image, bounds, color):
    """Draw a border around the image using the hints in the vector list."""
    draw = ImageDraw.Draw(image)

    for bound in bounds:
        draw.polygon([
            bound.vertices[0].x, bound.vertices[0].y,
            bound.vertices[1].x, bound.vertices[1].y,
            bound.vertices[2].x, bound.vertices[2].y,
            bound.vertices[3].x, bound.vertices[3].y], None, color)
    return image


def get_document_bounds(image_file):
    """Returns document bounds given an image."""
    client = vision.ImageAnnotatorClient()

    bbSym = []
    bbWord = []
    bbPara = []
    bbBlock = []

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    # Collect specified feature bounds by enumerating all document features
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        bbSym.append(symbol.bounding_box)
                    bbWord.append(word.bounding_box)
                bbPara.append(paragraph.bounding_box)
            bbBlock.append(block.bounding_box)

    return (bbWord, bbPara, bbBlock, document.text)


def extract_text(filein, fileout):
    image = Image.open(filein)
    bbWord, bbPara, bbBlock, text = get_document_bounds(filein)
    draw_boxes(image, bbBlock, 'blue')
    draw_boxes(image, bbPara, 'red')
    draw_boxes(image, bbWord, 'yellow')

    if fileout != 0:
        image.save(fileout)
    else:
        image.show()

    return text

# Below section for testing purpose
# detect_file = 'line1.png'
# out_file = 'result.jpg'
# render_doc_text(detect_file, out_file)