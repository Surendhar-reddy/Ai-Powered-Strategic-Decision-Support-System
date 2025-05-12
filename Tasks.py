from crewai import Task

def market_task(agent,decision_topic: str):
    return Task(
    description=(
        f"Conduct a comprehensive market analysis for the business decision: '{decision_topic}'. "
        f"Your report must include:\n"
        f"- Current market trends and growth projections\n"
        f"- Detailed competitor analysis (top 3 competitors with strengths/weaknesses)\n"
        f"- Target customer demographics and behavior\n"
        f"- Regional market variations (if any)\n"
        f"- Insights backed by recent data, studies, or reputable sources"
),
    expected_output=(
        "A well-structured market research report with data points, competitor comparisons, customer insights, and regional analysis. "
        "Use bullet points, subheadings, and include web links or references if possible."
    ),

        agent=agent,
        verbose=True,
        output_file='market_task.md'
    )

def financial_task(agent,decision_topic: str):
    return Task(
        description=(
    f"Analyze the financial feasibility of the business decision: '{decision_topic}'. "
    f"Include:\n"
    f"- Initial investment breakdown and assumptions\n"
    f"- Projected revenue over 1, 3, and 5 years\n"
    f"- Expected ROI and payback period\n"
    f"- Cost-benefit analysis (quantitative)\n"
    f"- Financial risks and contingencies"
),
expected_output=(
    "A detailed financial report with tables or clear bullet points, including ROI metrics, forecasts, and scenario comparisons. "
    "Make it easy to interpret with labels and justifications."
),
        agent=agent,
        verbose=True,
        output_file='financial_task.md'
    )

def risk_task(agent,decision_topic: str):
    return Task(
        description=(
    f"Identify, categorize, and evaluate key risks associated with the decision: '{decision_topic}'. "
    f"Cover:\n"
    f"- Strategic risks (e.g., market misalignment)\n"
    f"- Operational risks (e.g., supply chain issues)\n"
    f"- Financial risks (e.g., currency or cost fluctuation)\n"
    f"- Regulatory or compliance risks (if relevant)\n"
    f"For each risk, assess likelihood, impact, and propose at least one mitigation strategy."
),
expected_output=(
    "A structured risk matrix or report with clear sections for each risk type, ranked by severity. "
    "Include actionable mitigations and explanations for prioritization."
),
        agent=agent,
        verbose=True,
        output_file='risk_task.md'
    )

def strategy_task(agent,decision_topic: str, dependencies):
    return Task(
        description=(
    f"Using insights from market, financial, and risk analysis, formulate a complete strategic plan for the decision: '{decision_topic}'. "
    f"Include:\n"
    f"- Recommended strategy (e.g., entry mode, targeting approach)\n"
    f"- Timeline with key phases or milestones\n"
    f"- Resource requirements (human, financial, technological)\n"
    f"- KPIs to track success\n"
    f"- Potential obstacles and fallback plans"
),
expected_output=(
    "A concise and actionable strategic roadmap with timelines, priorities, and measurable objectives. "
    "Structure the output as an executive summary followed by implementation details."
),
        agent=agent,
        depends_on=dependencies,
        verbose=True,
        output_file='strategy_task'
    )

def decision_task(agent,decision_topic: str, dependencies):
    return Task(
       description=(
    f"Based on the findings from all previous reports, evaluate whether to proceed with the business decision: '{decision_topic}'. "
    f"Provide a clear 'Go', 'No-Go', or 'Conditional' recommendation. "
    f"Support your conclusion with:\n"
    f"- A short summary of key insights from each report\n"
    f"- A reasoning chain explaining trade-offs and priorities\n"
    f"- A confidence score (e.g., 80%) and why\n"
    f"- Suggested next steps if the decision is approved"
),
expected_output=(
    "A final decision recommendation report with a justified verdict, confidence score, concise summary of analyses, and action suggestions. "
    "Keep it clear and professional as if reporting to a board."
),
        agent=agent,
        depends_on=dependencies,
        verbose=True,
        output_file='decision_task.md'
    )
