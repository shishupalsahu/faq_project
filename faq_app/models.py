from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Language-specific translations
    question_hi = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)
    # Add more languages as needed

    def save(self, *args, **kwargs):  # ✅ Correct indentation
        translator = Translator()
        try:
            # Translation code...
            pass  # Replace with actual translation logic
        except Exception as e:
            # Fallback to English if translation fails
            self.question_hi = self.question
            self.answer_hi = self.answer
            self.question_bn = self.question
            self.answer_bn = self.answer

        super(FAQ, self).save(*args, **kwargs)  # ✅ Correct indentation

    def get_question(self, lang='en'):  # ✅ Correct indentation
        return getattr(self, f'question_{lang}', self.question)

    def get_answer(self, lang='en'):  # ✅ Correct indentation
        return getattr(self, f'answer_{lang}', self.answer)

    def __str__(self):  # ✅ Correct indentation
        return self.question
