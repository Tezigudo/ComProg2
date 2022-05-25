## BMI Calculator

Create a Tkinter app for a BMI calculator.

The important things to achieve are:

- events are handled correctly
- results are correct and displayed correctly (not: BMI 21.3333333333)
- invalid input is handled so app does not print exception messages on console
- layout is similar to the example
- write clean code, don't create extra attributes you don't need

Less important but good if you can them

- fields resize when window is resized
- padding between fields

Not important are

- font size
- text color and alignment

Plan your time. Work on the most important parts first.


## Formula for BMI

`BMICalculator.bmi()` computes the BMI from a person's weight (w) and height (h).
The formula depends on the units used

| Units                      | Formula     |
|----------------------------|-------------|
| English units (inch, lb)   | 703.071 * w / h^2 |
| Metric units (cm, kg)      | 10,000 * w / h^2 |
| Metric units (meter, kg)   | w / h^2     |

in this exam, we only allow the first 2 unit (in-lb and cm-kg).


## For Your Info: ABSI is a Better Metric

BMI is not a good predictor of weight-related health problems.  One reason is that it cannot account for differences in muscle mass.

A much better predictor is A Body Shape Index (ABSI).  There are some excellent online ABSI calculators that also show relative risk, using age and sex. Two worth looking at are:

* <https://www.absicalculator.eu/> has graph of relative risk
* <https://www.mytecbits.com/tools/medical/absi-calculator> has details of how ABSI is calculated and risk tables, useful if you want to write your own app.


part2 document is **here**

<https://docs.google.com/document/d/19KTeVeLOTVaf9RQF85971mgYK9vp3_teCSu-h17_HZ0/edit>
