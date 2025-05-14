
import streamlit as st

def calculate_bmi(weight, height):
  """Calculates BMI based on weight (kg) and height (m)."""
  try:
    bmi = weight / (height ** 2)
    return bmi
  except ZeroDivisionError:
    return "Invalid height"


st.title("BMI Calculator")

st.write("Enter your weight and height to calculate your BMI.")

weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)
height = st.number_input("Height (m)", min_value=0.0, step=0.01)


if st.button("Calculate BMI"):
  bmi = calculate_bmi(weight, height)
  st.write(f"Your BMI is: {bmi:.2f}")

  if isinstance(bmi, float): # Check if the BMI is a number
      if bmi < 18.5:
          st.write("You are underweight.")
      elif bmi < 25:
          st.write("You are in a healthy weight range.")
      elif bmi < 30:
          st.write("You are overweight.")
      else:
          st.write("You are obese.")
