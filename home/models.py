from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from .blocks import LimitedRichTextBlock, ImageGallery


class HomePage(Page):
    content = StreamField(
        [
            ("text", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("body", LimitedRichTextBlock()),
            ("image_gallery", ImageGallery())
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    templates = "home/home_page.html"
