PYTHON ?= python3

.PHONY: validate test check

validate:
	$(PYTHON) scripts/validate_skills.py .

test:
	$(PYTHON) -m unittest discover -s tests -v

check: validate test
