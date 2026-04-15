#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from pathlib import Path
import sys

# Añadimos el directorio padre para importar el módulo operativo
sys.path.append(str(Path(__file__).resolve().parents[1]))
from merci_sitemap import update_lastmod

class TestSitemap(unittest.TestCase):
    @patch("merci_sitemap.SITEMAP_PATH")
    def test_update_lastmod_success(self, mock_path):
        content = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            '   <url><lastmod>2000-01-01</lastmod></url>\n'
            '</urlset>'
        )
        mock_path.exists.return_value = True
        mock_path.read_text.return_value = content
        
        update_lastmod()
        
        called_with = mock_path.write_text.call_args[0][0]
        self.assertNotIn("2000-01-01", called_with)
        self.assertIn("<lastmod>", called_with)

if __name__ == "__main__":
    unittest.main()