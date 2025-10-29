import unittest

from utils.regex import extract_markdown_images, extract_markdown_links

class TestRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://www.boot.dev/img/bootdev-logo-full-small.webp)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://www.boot.dev/img/bootdev-logo-full-small.webp")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            'Head over to [Wikipedia](https://www.wikipedia.org)'
        )
        self.assertListEqual([('Wikipedia', 'https://www.wikipedia.org')], matches)
        
    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            'Head over to [Wikipedia](https://www.wikipedia.org) and [Google](https://www.google.com)'
        )
        self.assertListEqual([('Wikipedia', 'https://www.wikipedia.org'), ('Google', 'https://www.google.com')], matches)
        
    def test_no_matches(self):
        matches = extract_markdown_links(
            'Head over to Wikipedia'
        )
        self.assertListEqual([], matches)

    def test_image_with_empty_alt_text(self):
        matches = extract_markdown_images(
            "Here's an image: ![](https://example.com/image.png)"
        )
        self.assertListEqual([("", "https://example.com/image.png")], matches)
    
    def test_link_is_not_detected_as_image(self):
        text = "This is a regular link: [Bootdev](https://www.boot.dev)"
        image_matches = extract_markdown_images(text)
        self.assertListEqual([], image_matches)

if __name__ == "__main__":
    unittest.main()