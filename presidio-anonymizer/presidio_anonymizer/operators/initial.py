"""Converts PII text to initials."""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Initial operator - currently minimal, logic will be improved later."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """
        Convert a string like 'John Smith' into 'J. S.'.
        This is a basic version; we'll improve it in later tasks.
        """
        if text is None:
            return ""

        # 1. Strip leading/trailing whitespace
        stripped = text.strip()

        if not stripped:
            return stripped

        # 2. Split on whitespace to get words
        words = stripped.split()

        # 3. Take the first character of each word and format as "X."
        initials_parts = []
        for w in words:
            if not w:
                continue
            first_char = w[0]
            initials_parts.append(f"{first_char.upper()}.")

        # 4. Join with spaces: "J." "S." -> "J. S."
        return " ".join(initials_parts)
    def operate(self, text: str = None, params: Dict = None) -> str:
        """
        Convert a string like 'John Smith' into 'J. S.'.
        This is a basic version; we'll improve it in later tasks.
        """
        if text is None:
            return ""

        # 1. Strip leading/trailing whitespace
        stripped = text.strip()

        if not stripped:
            return stripped

        # 2. Split on whitespace to get words
        words = stripped.split()

        # 3. Take the first character of each word and format as "X."
        initials_parts = []
        for w in words:
            if not w:
                continue
            first_char = w[0]
            initials_parts.append(f"{first_char.upper()}.")

        # 4. Join with spaces: "J." "S." -> "J. S."
        return " ".join(initials_parts)


    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters, so no validation is needed for now."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
