FROM python:3.8

# Prep
ADD bot.py /
RUN pip install -r requirements.txt

# Run
CMD ["python", "./bot.py"]
