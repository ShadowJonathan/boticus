FROM python:3.8

# Prep
ADD bot.py /
RUN pip install discord

# Run
CMD ["python", "./bot.py"]
