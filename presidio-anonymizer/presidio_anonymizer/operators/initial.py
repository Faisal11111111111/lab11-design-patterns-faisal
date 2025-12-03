"""Converts PII text to initials."""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Initial operator - currently minimal, logic will be improved later."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """
        For now, just return the text unchanged.
        We will implement the real initials logic in later tasks.
        """
        return text

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters, so no validation is needed for now."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
