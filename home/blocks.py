from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList


class LimitedRichTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=250)
    body = blocks.RichTextBlock(features=["bold", "italic", "ol"])
    another_page = blocks.PageChooserBlock()
    external_url = blocks.URLBlock()

    def clean(self, value):
        errors = {}

        if "the" in value.get("title"):
            errors["title"] = ErrorList(['Your title must not include the word "the".'])

        title_words = value.get("title").split()
        if any(word in str(value.get("body")) for word in title_words):
            errors["body"] = ErrorList(
                ["Body should not include any words used in the title."]
            )

        if errors:
            raise ValidationError("Validation error in StructBlock", params=errors)

        return super().clean(value)

    class Meta:
        template = "home/blocks/limited_richtext_block.html"
        label = "Limited RichText"


class ImageGallery(blocks.StructBlock):
    images = blocks.ListBlock(
        blocks.StructBlock(
            [("image", ImageChooserBlock()), ("description", blocks.TextBlock())]
        )
    )

    class Meta:
        template = "home/blocks/image_gallery.html"
        label = "Image Gallery"
