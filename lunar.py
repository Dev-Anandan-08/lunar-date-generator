import streamlit as st
import datetime
import lunardate


def gregorian_to_lunar(year, month, day):
    lunar_date = lunardate.LunarDate.fromSolarDate(year, month, day)
    return lunar_date.year, lunar_date.month, lunar_date.day


def main():
    st.title("Lunar Date of Birth Generator")

    st.write("Enter your date of birth to find the corresponding lunar date.")

    dob = st.date_input("Select your date of birth", datetime.date(2000, 1, 1))

    if st.button("Convert to Lunar Date"):
        lunar_date = gregorian_to_lunar(dob.year, dob.month, dob.day)
        st.success(
            f"Your Lunar Date of Birth: Year {lunar_date[0]}, Month {lunar_date[1]}, Day {lunar_date[2]}"
        )


if __name__ == "__main__":
    main()
