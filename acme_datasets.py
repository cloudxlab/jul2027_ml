"""
acme_datasets.py
================
All datasets used across the RAG and Agentic AI curriculum.
Import what you need:

    from acme_datasets import DOCUMENTS, CHUNKS, MINI_CORPUS, QA_EVAL_SET

No external libraries required for this file.
"""

# ---------------------------------------------------------------------------
# Module 1 — The Knowledge Gap
# Three short policy documents used in Exercises 1.1 and 1.2
# ---------------------------------------------------------------------------

DOC_A = """ACME CORP — TRAVEL EXPENSE POLICY (Updated Q3 2024)
Employees may claim up to $250 per night for hotel accommodation.
All flights must be booked at least 14 days in advance to qualify for reimbursement.
Meal allowance is $60 per day. Receipts are required for all individual claims over $25.
Business class flights are permitted only for journeys exceeding 6 hours.
Alcohol is not reimbursable under any circumstances.
Last-minute flight bookings require written VP approval before purchase."""

DOC_B = """ACME CORP — REMOTE WORK GUIDELINES (Updated Q2 2024)
Employees may work remotely up to 3 days per week.
A minimum of 2 days of in-office attendance per week is required for all staff.
Remote work requests covering a full calendar week require advance manager approval.
Employees working remotely must be reachable during core hours: 10am–3pm local time.
Home office equipment (monitor, keyboard, chair) is reimbursable up to $500 per year."""

DOC_C = """ACME CORP — ONBOARDING CHECKLIST (Updated Q1 2024)
Week 1: Complete mandatory compliance training. Set up laptop, accounts, and email signature.
Week 2: Schedule a 1-on-1 with your team lead. Review and agree on your 90-day goals.
Week 3: Shadow a senior colleague for at least one full day. Attend the monthly all-hands meeting.
Week 4: Submit your first progress self-review via the HR portal. Request access to any remaining tools."""

DOC_D = """ACME CORP — IT SECURITY POLICY (Updated Q3 2024)
All company devices must have full-disk encryption enabled at all times.
Employees must use the company VPN when accessing internal systems remotely.
Passwords must be at least 14 characters and changed every 90 days.
Sharing credentials with colleagues is strictly prohibited, even temporarily.
Any suspected security breach must be reported to security@acme.corp within 1 hour of discovery.
Personal USB drives may not be connected to company equipment."""

DOC_E = """ACME CORP — PERFORMANCE REVIEW PROCESS (Updated Q4 2024)
Performance reviews are conducted twice per year: in June and December.
Each employee submits a self-assessment at least one week before their review meeting.
Managers rate performance on four dimensions: delivery, collaboration, growth, and impact.
Ratings of 'Exceeds Expectations' require written justification and skip-level approval.
Employees rated 'Needs Improvement' are placed on a 60-day improvement plan.
Compensation adjustments linked to reviews take effect on the first of the following quarter."""

DOC_F = """ACME CORP — PARENTAL LEAVE POLICY (Updated Q1 2024)
Primary caregivers are entitled to 16 weeks of fully paid parental leave.
Secondary caregivers are entitled to 4 weeks of fully paid parental leave.
Leave must begin within 12 months of the child's birth or adoption date.
Employees must provide at least 8 weeks notice before planned leave starts.
Benefits (health, dental, pension contributions) continue in full during parental leave.
Unused parental leave cannot be carried over or paid out — it must be taken."""

# Convenience list used in Exercise 1.2
DOCUMENTS = [DOC_A, DOC_B, DOC_C, DOC_D, DOC_E, DOC_F]

# ---------------------------------------------------------------------------
# Module 2 — The Search Problem
# Mini corpus used in Exercise 2.1 to demonstrate keyword vs semantic search
# ---------------------------------------------------------------------------

MINI_CORPUS = [
    # Three ways of saying the same thing (hotel rate cap)
    "The hotel rate is capped at $250 per night.",
    "Accommodation costs must not exceed two hundred and fifty dollars per night.",
    "Lodging expenses are reimbursable up to the standard nightly limit of $250.",
    # Unrelated decoy
    "Python is a high-level programming language widely used in data science.",
    # More policy sentences (mixed topics)
    "Employees working from home must be available during core hours.",
    "All passwords must be changed every ninety days.",
    "Performance reviews happen in June and December each year.",
    "Meal receipts are required for individual claims above twenty-five dollars.",
]

# ---------------------------------------------------------------------------
# Module 3 — Inventing RAG
# Longer single document used in Exercise 3.2 for chunking experiments
# ---------------------------------------------------------------------------

LONG_TRAVEL_POLICY = """ACME CORP TRAVEL EXPENSE POLICY — FULL VERSION

Section 1: Flights
All domestic flights must be booked at economy class.
Business class is permitted only for flights exceeding 6 hours of total travel time.
All flights must be booked at least 14 days in advance to qualify for reimbursement.
Last-minute bookings require VP approval and a written justification submitted to finance@acme.corp.
Flights must be booked through the approved corporate travel portal (TravelDesk).
Employees may not book flights using personal rewards programs and seek reimbursement.

Section 2: Hotels
Employees are entitled to a maximum of $250 per night for hotel accommodation.
The company has negotiated preferred rates with Marriott and Hilton chains — use these where available.
Extended stays of more than 7 consecutive nights require written manager sign-off before booking.
Airbnb and similar short-term rental platforms are not approved for reimbursement.
Hotel bookings must include a business justification if the rate exceeds $200 per night.

Section 3: Meals
The daily meal allowance is $60. This is intended to cover breakfast, lunch, and dinner combined.
Alcohol is not reimbursable under any circumstances, even when consumed with clients.
Receipts are required for any single meal exceeding $25.
Team dinners with external clients may be expensed separately under the entertainment budget, up to $120 per person.
Room service is reimbursable within the daily meal allowance limit.

Section 4: Ground Transport
Taxis and rideshare (Uber, Lyft) are reimbursable for airport transfers and client meetings.
Personal vehicle use is reimbursed at $0.22 per kilometre, with a mileage log required.
Car rentals require pre-approval from a manager and must be booked through the corporate Avis account.
Parking at the office is not reimbursable. Airport parking is reimbursable for trips exceeding 2 days.
Public transit costs are fully reimbursable without a receipt for amounts under $10.

Section 5: International Travel
All international travel requires VP approval at least 3 weeks in advance.
Travel insurance is mandatory and must be purchased through the company's approved provider.
Currency exchange fees are reimbursable. ATM withdrawal fees are not.
Per diem rates for meals differ by country — consult the International Per Diem Table on the intranet.
Employees must notify HR of any travel to countries with active travel advisories."""

# ---------------------------------------------------------------------------
# Structured document set — used in Exercise 2.2 and Module 3/5
# Each entry is a dict with id, text, and source fields
# ---------------------------------------------------------------------------

STRUCTURED_DOCUMENTS = [
    # Travel policy
    {"id": 1,  "text": "Hotel accommodation is capped at $250 per night.", "source": "travel_policy.txt"},
    {"id": 2,  "text": "All flights must be booked at least 14 days in advance.", "source": "travel_policy.txt"},
    {"id": 3,  "text": "Business class is only permitted for flights exceeding 6 hours.", "source": "travel_policy.txt"},
    {"id": 4,  "text": "Meal allowance is $60 per day. Receipts required for claims over $25.", "source": "travel_policy.txt"},
    {"id": 5,  "text": "Alcohol is not reimbursable under any circumstances.", "source": "travel_policy.txt"},
    {"id": 6,  "text": "Airbnb and similar platforms are not approved for reimbursement.", "source": "travel_policy.txt"},
    {"id": 7,  "text": "Personal vehicle use is reimbursed at $0.22 per kilometre.", "source": "travel_policy.txt"},
    {"id": 8,  "text": "Team dinners with clients may be expensed up to $120 per person.", "source": "travel_policy.txt"},
    # Remote work
    {"id": 9,  "text": "Employees may work remotely up to 3 days per week.", "source": "remote_policy.txt"},
    {"id": 10, "text": "A minimum of 2 in-office days per week is required.", "source": "remote_policy.txt"},
    {"id": 11, "text": "Full-week remote requests require advance manager approval.", "source": "remote_policy.txt"},
    {"id": 12, "text": "Home office equipment is reimbursable up to $500 per year.", "source": "remote_policy.txt"},
    # IT security
    {"id": 13, "text": "All company devices must have full-disk encryption enabled.", "source": "it_security.txt"},
    {"id": 14, "text": "Employees must use the company VPN when accessing internal systems remotely.", "source": "it_security.txt"},
    {"id": 15, "text": "Passwords must be at least 14 characters and changed every 90 days.", "source": "it_security.txt"},
    {"id": 16, "text": "Any suspected security breach must be reported within 1 hour.", "source": "it_security.txt"},
    # Performance
    {"id": 17, "text": "Performance reviews are conducted in June and December each year.", "source": "performance.txt"},
    {"id": 18, "text": "Employees rated Needs Improvement are placed on a 60-day improvement plan.", "source": "performance.txt"},
    # Parental leave
    {"id": 19, "text": "Primary caregivers are entitled to 16 weeks of fully paid parental leave.", "source": "parental_leave.txt"},
    {"id": 20, "text": "Secondary caregivers are entitled to 4 weeks of fully paid parental leave.", "source": "parental_leave.txt"},
    {"id": 21, "text": "Leave must begin within 12 months of the child's birth or adoption date.", "source": "parental_leave.txt"},
    {"id": 22, "text": "Employees must give at least 8 weeks notice before planned parental leave.", "source": "parental_leave.txt"},
]

# ---------------------------------------------------------------------------
# Module 5 — Evaluation set
# 15 question-answer pairs for testing your completed RAG agent
# Use these to measure accuracy: how many does your agent get right?
# ---------------------------------------------------------------------------

QA_EVAL_SET = [
    {
        "question": "What is the maximum hotel rate per night?",
        "expected_answer": "$250",
        "source": "travel_policy.txt",
        "difficulty": "easy",
    },
    {
        "question": "Can I fly business class on a 4-hour domestic flight?",
        "expected_answer": "No. Business class is only permitted for flights exceeding 6 hours.",
        "source": "travel_policy.txt",
        "difficulty": "easy",
    },
    {
        "question": "Is alcohol reimbursable at a client dinner?",
        "expected_answer": "No. Alcohol is not reimbursable under any circumstances.",
        "source": "travel_policy.txt",
        "difficulty": "easy",
    },
    {
        "question": "How many days in advance must flights be booked?",
        "expected_answer": "At least 14 days in advance.",
        "source": "travel_policy.txt",
        "difficulty": "easy",
    },
    {
        "question": "Can I book accommodation through Airbnb?",
        "expected_answer": "No. Airbnb and similar platforms are not approved.",
        "source": "travel_policy.txt",
        "difficulty": "easy",
    },
    {
        "question": "What is the reimbursement rate for using my personal car?",
        "expected_answer": "$0.22 per kilometre.",
        "source": "travel_policy.txt",
        "difficulty": "medium",
    },
    {
        "question": "I am working from home today. Do I need to be available all day?",
        "expected_answer": "You must be reachable during core hours: 10am to 3pm local time.",
        "source": "remote_policy.txt",
        "difficulty": "medium",
    },
    {
        "question": "How long is parental leave for a primary caregiver?",
        "expected_answer": "16 weeks of fully paid parental leave.",
        "source": "parental_leave.txt",
        "difficulty": "medium",
    },
    {
        "question": "What happens if I am rated Needs Improvement in my review?",
        "expected_answer": "You are placed on a 60-day improvement plan.",
        "source": "performance.txt",
        "difficulty": "medium",
    },
    {
        "question": "How long does a password need to be?",
        "expected_answer": "At least 14 characters.",
        "source": "it_security.txt",
        "difficulty": "medium",
    },
    {
        "question": "I have a 3-day business trip. What is the maximum I can claim for meals in total?",
        "expected_answer": "$180 (3 days × $60 per day).",
        "source": "travel_policy.txt",
        "difficulty": "hard — requires retrieval + calculation",
    },
    {
        "question": "I drove 120 kilometres to a client site. How much can I claim?",
        "expected_answer": "$26.40 (120 km × $0.22).",
        "source": "travel_policy.txt",
        "difficulty": "hard — requires retrieval + calculation",
    },
    {
        "question": "Can I use Airbnb and also claim the $250 hotel rate?",
        "expected_answer": "No. Airbnb is not approved, so no reimbursement applies.",
        "source": "travel_policy.txt",
        "difficulty": "hard — requires reasoning",
    },
    {
        "question": "I found out about a security breach. When do I need to report it?",
        "expected_answer": "Within 1 hour of discovery.",
        "source": "it_security.txt",
        "difficulty": "hard — requires precise retrieval",
    },
    {
        "question": "My partner is having a baby. We are both Acme employees. How much total paid leave can our household take?",
        "expected_answer": "20 weeks total: 16 weeks for the primary caregiver and 4 weeks for the secondary caregiver.",
        "source": "parental_leave.txt",
        "difficulty": "hard — requires reasoning across one document",
    },
]


# ---------------------------------------------------------------------------
# Utility — quick sanity check
# Run this file directly to verify it loads correctly:
#   python acme_datasets.py
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print(f"DOCUMENTS: {len(DOCUMENTS)} policy documents")
    print(f"MINI_CORPUS: {len(MINI_CORPUS)} sentences")
    print(f"STRUCTURED_DOCUMENTS: {len(STRUCTURED_DOCUMENTS)} chunks")
    print(f"QA_EVAL_SET: {len(QA_EVAL_SET)} question-answer pairs")
    print(f"LONG_TRAVEL_POLICY: {len(LONG_TRAVEL_POLICY.split())} words")
    print("\nAll datasets loaded successfully.")