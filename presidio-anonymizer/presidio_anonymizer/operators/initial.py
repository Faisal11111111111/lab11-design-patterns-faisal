"""Converts PII text to initials."""

from typing import Dict
import re

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Initial operator - currently minimal, logic will be improved later."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """
        Convert text to initials.

        Examples:
        - "John Smith" -> "J. S."
        - "     Eastern    Michigan   University " -> "E. M. U."
        - "@abc" -> "@A."
        - "@843A" -> "@8."
        - "--**abc" -> "--**A."
        """
        if text is None:
            return ""

        stripped = text.strip()
        if not stripped:
            return stripped

        # Split into chunks separated by whitespace
        chunks = stripped.split()
        result_chunks = []

        for chunk in chunks:
            # Match optional non-word prefix and then a word part
            match = re.match(r"(\W*)(\w+)", chunk)
            if match:
                prefix = match.group(1)
                word_part = match.group(2)
                first_char = word_part[0].upper()
                result_chunks.append(f"{prefix}{first_char}.")
            else:
                # No alphanumeric content, keep chunk as-is
                result_chunks.append(chunk)

        return " ".join(result_chunks)


    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters, so no validation is needed for now."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
