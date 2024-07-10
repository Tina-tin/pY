import streamlit as st

def main():
    st.title("Goal Calculator")

    st.header("Team A")
    goals_performed_a = st.number_input("Goals Performed by Team A", min_value=0, step=1)
    goals_reached_a = st.number_input("Goals Reached by Team A", min_value=0, step=1)

    st.header("Team B")
    goals_performed_b = st.number_input("Goals Performed by Team B", min_value=0, step=1)
    goals_reached_b = st.number_input("Goals Reached by Team B", min_value=0, step=1)

    if st.button("Calculate"):
        total_goals_a = goals_performed_a + goals_reached_a
        total_goals_b = goals_performed_b + goals_reached_b

        st.subheader(f"Total Goals for Team A: {total_goals_a}")
        st.subheader(f"Total Goals for Team B: {total_goals_b}")

        if total_goals_a > total_goals_b:
            st.subheader("Winner: Team A advances to the next game")
        elif total_goals_a < total_goals_b:
            st.subheader("Winner: Team B advances to the next game")
        else:
            st.subheader("It's a tie! Both teams advance to the next game")

if _name_ == "_main_":
    main()
