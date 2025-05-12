from Agents import decision_expert , market_research_expert, financial_expert,risk_expert,strategy_expert
from Tasks import decision_task,market_task, financial_task, risk_task,strategy_task

from crewai import Crew, Process
import streamlit as st

# Streamlit App Title
st.title("📊 AI-Powered Strategic Decision      Support System")

st.markdown("""
💡 **Make informed business decisions with AI!**  S
Enter your business decision topic below, and our AI-powered expert system will generate:
- Market research 📈  
- Financial analysis 💰  
- Risk assessment ⚠️  
- Strategic plan 🧭  
- Final decision recommendation ✅
""")

# User Inputs
decision_topic = st.text_input("📌 Enter the Business Decision Topic", "Launch a new product in the European market")

# Button to run CrewAI
if st.button("🚀 Generate Strategic Report"):
    if not decision_topic.strip():
        st.error("⚠️ Please enter a valid business decision topic.")
    else:
        st.write("⏳ AI is analyzing your decision... Please wait.")

        # Initialize Tasks
        market = market_task(market_research_expert, decision_topic)
        finance = financial_task(financial_expert, decision_topic)
        risk = risk_task(risk_expert, decision_topic)
        strategy = strategy_task(strategy_expert, decision_topic, dependencies=[market, finance, risk])
        decision = decision_task(decision_expert, decision_topic, dependencies=[strategy])


        # Define the Crew
        crew = Crew(
            agents=[
                market_research_expert,
                financial_expert,
                risk_expert,
                strategy_expert,
                decision_expert
            ],
            tasks=[market, finance, risk, strategy, decision],
            process=Process.sequential,
            full_output=True,
            verbose=True
        )

        # Run Crew AI
        result = crew.kickoff()

        # Display Results
        st.subheader("✅ Your Strategic Decision Report")
        st.markdown(result)

        # Download Option
        strategic_report = str(result)
        st.download_button(
            label="📥 Download Full Report",
            data=strategic_report,
            file_name="Strategic_Decision_Report.txt",
            mime="text/plain"
        )
        