ENGLISH = "in-lb"
METRIC = "cm-kg"


class BMICalculator:

    def bmi(self, height, weight, units):
        """Compute the BMI from weight and height.

        :param height: the person's height
        :param weight: the person's weight
        :param units:  is either ENGLISH ('in-lb') or METRIC ('cm-kg')
        :returns: the BMI (of course)
        :raises ValueError: if units has an invalid value or height is 0
        """
        constants = {ENGLISH: 703.071, METRIC: 10000}
        if units not in constants:
            raise ValueError(f"Invalid units {units}")
        if height == 0:
            raise ValueError("height cannot be zero")
        return constants[units]*weight/(height*height)

    def health_assessment(self, bmi: float):
        """A health assessment based on BMI value, which is probably useless.

        :param bmi: the BMI value to assess
        :returns:  health assessment based on the bmi value
        """
        if bmi < 15:
            return "Emaciated"
        if bmi < 18.5:
            return "Underweight"
        if bmi <= 25:
            return "Likely a healthy weight"
        if bmi <= 30:
            return "Muscular or overweight"
        return "Likely obese"
