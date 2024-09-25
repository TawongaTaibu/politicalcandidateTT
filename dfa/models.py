from django.db import models

class News(models.Model):
    """
    Model representing a news article.

    Attributes:
        title (str): The title of the news article.
        content (str): The content or body of the news article.
        date (date): The publication date of the news article.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        """
        String representation of the News object.

        Returns:
            str: The title of the news article.
        """
        return self.title
