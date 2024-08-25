from django.db import models

# Create your models here.

class Questions(models.Model):
    QUESTON_TYPE = (("Text", "Text"),( "BigText", "BigText"), ("Radio", "Radio"),
                    ("Checkbox", "Checkboz"))
    question = models.CharField(max_length=100)
    question_type = models.CharField(choices=QUESTON_TYPE, max_length=100, default="Text")

    def __str__(self) -> str:
        return self.question + " " + self.question_type

class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="options")
    option_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.option_name 

class CustomerFeedback(models.Model):
    question = models.ManyToManyField(Questions)


class CustomerResponse(models.Model):
    feedback = models.ForeignKey(CustomerFeedback, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    response_text = models.TextField(null=True, blank=True)
    selected_options = models.ManyToManyField(Options, blank=True)

    def __str__(self):
        return f"Response to {self.question}"