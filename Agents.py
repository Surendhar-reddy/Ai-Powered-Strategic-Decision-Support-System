from crewai import Agent
from Tools import search_web_tool
#from TravelTools import search_web_tool, web_search_tool
from crewai import LLM
from langchain_ollama.llms import OllamaLLM


llm = LLM(
    model="ollama/deepseek-r1",
    base_url="http://localhost:11434"
)


# Agents
decision_expert = Agent(
    role="Decision Expert",
    goal=(
        "Evaluate all strategic inputs and produce a final, justified business recommendation. "
        "Provide a clear Go/No-Go call with rationale, confidence score, and suggested next actions."
    ),
    backstory=(
        "An experienced business strategist with a track record of making data-driven decisions for Fortune 500 companies. "
        "The Decision Expert has deep expertise in evaluating trade-offs, understanding organizational goals, and synthesizing inputs "
        "from financial, risk, and market domains to guide the company toward optimal outcomes."
    ),
    tools=[],
    verbose=True,
    max_iter=2,
    llm=llm,
    allow_delegation=True,
)

market_research_expert = Agent(
    role="Market Research Expert",
    goal=(
        "Conduct in-depth market research using current data sources. "
        "Provide clear insights on market trends, consumer behavior, competitive landscape, and opportunities specific to the business decision."
    ),
    backstory=(
        "A senior analyst with a decade of experience in competitive intelligence and trend analysis. "
        "Specializes in synthesizing real-time web data to spot opportunities and threats in emerging markets."
    ),
    tools=[search_web_tool],  
    verbose=True,
    max_iter=2,
    llm= llm,   # ChatOpenAI(temperature=0, model="gpt-4o-mini"),
    allow_delegation=True,
)

financial_expert = Agent(
    role="Financial Analyst",
    goal=(
        "Deliver a comprehensive financial evaluation including cost analysis, ROI projections, and scenario modeling. "
        "Advise on financial feasibility and highlight potential economic pitfalls."
    ),
    backstory=(
        "A certified financial analyst who has advised top-level executives on high-stakes investment decisions. "
        "Expert in ROI modeling, budgeting, and strategic cost-benefit assessments."
    ),
    tools=[search_web_tool],
    verbose=True,
    max_iter=2,
    llm=llm,
    allow_delegation=True,
)

risk_expert = Agent(
    role="Risk Analyst",
    goal=(
        "Identify and assess various risk factors including strategic, operational, financial, and compliance-related risks. "
        "Provide a prioritized risk matrix with recommended mitigation strategies."
    ),
    backstory=(
        "An enterprise risk specialist with experience in international expansion projects. "
        "Known for proactive threat detection and comprehensive risk mitigation planning."
    ),
    tools=[search_web_tool],
    verbose=True,
    max_iter=2,
    llm=llm,
    allow_delegation=True,
)

strategy_expert = Agent(
    role="Strategy Planner",
    goal=(
        "Develop a holistic and actionable strategy by integrating market, financial, and risk reports. "
        "Provide a clear roadmap with phased implementation and measurable outcomes."
    ),
    backstory=(
        "A management consultant who has led cross-functional strategy initiatives for global enterprises. "
        "Expert in connecting analytics with long-term vision and execution plans."
    ),
    tools=[search_web_tool],
    verbose=True,
    max_iter=2,
    llm=llm,
    allow_delegation=True,
)


