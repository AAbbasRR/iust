from django.core.exceptions import ValidationError

from Abrat.settings import MAX_DOCUMENTS_SIZE

from utils.base_errors import BaseErrors

from PIL import Image


def validate_image_file(value):
    if not value:
        return

    image = Image.open(value)
    image.verify()

    allowed_formats = ['JPEG', 'PNG', 'JPG', 'PDF']
    if image.format not in allowed_formats:
        raise ValidationError(BaseErrors._change_error_variable("invalid_file_formats", formats=', '.join(allowed_formats)))

    if len(value) > MAX_DOCUMENTS_SIZE:
        raise ValidationError(BaseErrors._change_error_variable("invalid_file_formats", size=MAX_DOCUMENTS_SIZE))
