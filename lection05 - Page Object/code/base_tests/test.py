import pytest
from base_tests.base import BaseCase


class TestOne(BaseCase):
    @pytest.mark.skip("SKIP")
    def test_title(self):
        assert "Python" in self.driver.title

    @pytest.mark.parametrize(
        'query',
        [
            pytest.param(
                'pycon'
            ),
            pytest.param(
                'python'
            ),
        ]
    )
    @pytest.mark.skip("SKIP")
    def test_search(self, query):
        self.base_page.search(query)
        assert "No results found." not in self.driver.page_source

    @pytest.mark.skip("SKIP")
    def test_search_negative(self):
        self.search_page.search("dasdasdasdasdasdasdasdasdasdas")
        assert "No results found." in self.driver.page_source

    @pytest.mark.skip("SKIP")
    def test_carousel(self):
        self.main_page.click(self.main_page.locators.COMPREHENSIONS, timeout=17)
