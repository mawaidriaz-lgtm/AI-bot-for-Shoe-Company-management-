#!/usr/bin/env python3
"""
Shoes Company Administration and Marketing AI System
CLI-based Expert System using If-Else Rule Based AI
Author : Mohammad Awaid Riaz | Roll No: 37 | BS-AI Semester 4
Course : Artificial Intelligence
Instructor: Engr. Naveed
University: Emerson University Multan
"""

import sys
import datetime

# Knowledge Base — 15 questions per category (6 categories = 90 total)
KNOWLEDGE_BASE = {

    # ── Administration ──────────────────────────────────────────────
    "what is your name":
        "I am ShoesAI, an intelligent assistant for shoes company "
        "administration and marketing.",
    "what do you do":
        "I assist in managing shoe company operations including marketing "
        "strategies, inventory, staff, and customer relations.",
    "how to register a new employee":
        "Collect CNIC, fill HR-01 form, assign department, set salary "
        "grade, issue ID card, and enroll in payroll system.",
    "what is the leave policy":
        "Employees get 14 annual leaves, 10 casual leaves, and 8 sick "
        "leaves per year as per company HR policy.",
    "how to handle employee resignation":
        "Receive resignation letter, serve 1-month notice, complete "
        "clearance form, process final settlement.",
    "how to open a new branch":
        "Conduct market survey, register with SECP, obtain trade license, "
        "hire local staff, install POS system, do soft launch.",
    "what documents are needed for company registration":
        "NTN certificate, CNIC of directors, Memorandum of Association, "
        "Articles of Association, and bank account proof.",
    "how to manage petty cash":
        "Maintain petty cash register, set daily limit (e.g. Rs. 5000), "
        "get vouchers signed, reconcile weekly.",
    "what is the appraisal process":
        "Annual appraisal in December: supervisor rates performance on "
        "KPIs, HR reviews, increment decided by management.",
    "how to handle customer complaints":
        "Log complaint in CRM, assign to relevant dept, resolve within "
        "48 hrs, follow up with customer, close ticket.",
    "how to archive company documents":
        "Label files by department and year, store in fireproof cabinet, "
        "scan to digital backup, restrict access by role.",
    "how to manage vendor contracts":
        "Draft contract with payment terms, delivery schedule, and penalty "
        "clauses. Review annually and renew or renegotiate.",
    "what is the compliance reporting process":
        "Prepare monthly compliance report covering tax filings, labor law "
        "adherence, and safety checks. Submit to director.",
    "how to conduct a company audit":
        "Schedule internal audit quarterly. Cross-check invoices, payroll, "
        "and inventory records. Report discrepancies to management.",
    "how to manage office IT assets":
        "Maintain asset register with serial numbers. Assign to employees "
        "with sign-off. Audit assets every 6 months.",

    # ── Marketing  ───────────────────────────────────────────────────
    "how to increase shoe sales":
        "Run seasonal discounts, loyalty programs, social media campaigns, "
        "and collaborate with influencers.",
    "what marketing strategy works best for shoes":
        "Combine digital marketing (Instagram, TikTok), in-store "
        "promotions, and local events sponsorships.",
    "how to launch a new shoe collection":
        "Teaser campaign 2 weeks before, influencer seeding, launch event, "
        "paid ads, and PR coverage.",
    "what is the target market for premium shoes":
        "Urban professionals aged 25-45 with disposable income, "
        "fashion-conscious, prefer quality over price.",
    "how to compete with imported brands":
        "Emphasize local craftsmanship, offer better after-sales service, "
        "competitive pricing, and custom options.",
    "how to use social media for shoe marketing":
        "Post daily on Instagram/Facebook, use Reels, run contests, "
        "collaborate with micro-influencers, use hashtags.",
    "what is brand positioning":
        "How your brand is perceived vs competitors. For shoes: comfort, "
        "style, durability, and price value.",
    "how to price shoes competitively":
        "Calculate cost (material + labor + overhead), add 30-40% margin, "
        "compare with competitors, set final price.",
    "how to run a discount campaign":
        "Set discount % (e.g., 20%), define duration, advertise on all "
        "channels, train staff, monitor sales daily.",
    "what is customer lifetime value":
        "Total revenue a customer generates over their relationship with "
        "you. Increase via loyalty programs.",
    "how to conduct market research for shoes":
        "Survey customers on style preferences, analyze competitor product "
        "lines, study seasonal trends and social media buzz.",
    "how to run an email marketing campaign":
        "Build subscriber list, segment by purchase history, send "
        "personalized offers monthly, track open and click rates.",
    "what is influencer marketing for shoes":
        "Partner with fashion or lifestyle influencers to showcase products "
        "via unboxing videos, Reels, or styled photos.",
    "how to measure marketing campaign success":
        "Track KPIs: reach, clicks, conversion rate, cost per acquisition, "
        "and ROI. Review weekly and adjust strategy.",
    "how to plan a seasonal promotion":
        "Identify peak season (Eid, back-to-school), set budget, design "
        "offers, brief staff, and launch 2 weeks early.",

    # ── Inventory Management  ────────────────────────────────────────
    "how to manage shoe inventory":
        "Use barcode system, track stock by SKU, set reorder level, "
        "do monthly physical count.",
    "what is the reorder level":
        "When stock falls to 20% of max capacity, trigger a purchase "
        "order automatically.",
    "how to handle excess inventory":
        "Run clearance sales, offer bundle deals, transfer to other "
        "branches, or donate for tax benefit.",
    "how to track shoe sizes in inventory":
        "Maintain size-wise SKU codes (e.g., UK6=SK001-6), update in "
        "ERP after each sale.",
    "what causes inventory shrinkage":
        "Theft, damage, miscounting, and supplier short deliveries. "
        "Use CCTV and regular audits to reduce it.",
    "how to do a stock cycle count":
        "Count a portion of inventory weekly on rotation so the full "
        "stock is verified monthly without full shutdown.",
    "how to handle damaged goods in inventory":
        "Separate damaged stock, log in system, assess repair cost, "
        "sell as seconds or write off with management approval.",
    "how to integrate barcode system with inventory":
        "Assign unique barcode to each SKU, use scanner at point of sale "
        "and receiving, sync with ERP in real time.",
    "what is FIFO in inventory management":
        "First In First Out: sell oldest stock first to prevent product "
        "aging and keep inventory fresh.",
    "how to manage inter-branch stock transfers":
        "Raise transfer request in ERP, pack and dispatch with delivery "
        "note, receiving branch confirms in system.",
    "how to handle supplier short deliveries":
        "Compare delivery note with purchase order, log discrepancy, "
        "notify supplier, and raise debit note for shortage.",
    "what is dead stock and how to handle it":
        "Unsold stock for 6+ months. Bundle with fast movers, offer "
        "heavy discount, or return to supplier if possible.",
    "how to set up a warehouse layout for shoes":
        "Organize by category and size. Place fast-moving styles near "
        "dispatch. Use labeled racks and clear aisle paths.",
    "how to reduce inventory errors":
        "Train staff on system entry, do dual-verification at receiving, "
        "run weekly system vs physical count checks.",
    "what ERP features are useful for shoe inventory":
        "Stock alerts, SKU tracking, supplier PO management, sales "
        "reporting, and inter-branch transfer modules.",

    # ── Finance & Accounting  ────────────────────────────────────────
    "how to prepare monthly sales report":
        "Compile daily sales data, categorize by product line, compare "
        "with last month, highlight variances.",
    "what are typical shoe company expenses":
        "Rent, salaries, raw materials (leather/rubber), utilities, "
        "marketing, packaging, and logistics.",
    "how to calculate profit margin":
        "Profit Margin = ((Selling Price - Cost Price) / Selling Price) "
        "x 100.",
    "how to reduce operating costs":
        "Negotiate bulk material discounts, automate payroll, use "
        "energy-efficient lighting, reduce returns.",
    "what is break even point":
        "Break-even = Fixed Costs / (Selling Price - Variable Cost "
        "per unit).",
    "how to prepare annual budget for shoe company":
        "Review last year's actuals, forecast sales by season, estimate "
        "costs per department, get director approval.",
    "how to process payroll":
        "Collect attendance data, calculate basic + allowances - "
        "deductions, transfer to bank by 30th of each month.",
    "how to file GST for shoe sales":
        "Register on FBR portal, collect GST on each invoice, submit "
        "monthly return by 15th with payment.",
    "what is accounts receivable management":
        "Track all credit sales, send payment reminders at 30/60/90 days, "
        "escalate overdue accounts to management.",
    "how to do bank reconciliation":
        "Match bank statement with company cash book, identify outstanding "
        "cheques and deposits, reconcile differences.",
    "what is cost of goods sold":
        "COGS = Opening Stock + Purchases - Closing Stock. Reflects direct "
        "cost of shoes sold in a period.",
    "how to manage invoice processing":
        "Receive supplier invoice, match with purchase order and delivery "
        "note (3-way match), approve and post in ERP.",
    "how to track daily cash flow":
        "Record all receipts and payments daily. Prepare weekly cash flow "
        "statement to ensure liquidity.",
    "how to handle tax filing for shoe company":
        "File income tax return annually via IRIS portal. Keep records of "
        "sales, expenses, and depreciation.",
    "what is working capital management":
        "Balance current assets vs liabilities. Ensure enough cash to pay "
        "suppliers and staff without idle excess funds.",

    # ── Manufacturing ──────────────────────────────────────────
    "what materials are used in shoe manufacturing":
        "Upper: leather/synthetic. Sole: rubber/PU. Lining: fabric/foam. "
        "Adhesive: solvent-based glue.",
    "how to ensure shoe quality":
        "QC at each stage: cutting, stitching, sole attachment, finishing. "
        "Use durability and flex tests.",
    "what is the production process of shoes":
        "Design -> Pattern making -> Cutting -> Stitching -> Lasting -> "
        "Sole Attachment -> Finishing -> QC -> Packaging.",
    "how to reduce manufacturing defects":
        "Train workers on SOPs, maintain machines, use quality raw "
        "materials, implement Six Sigma.",
    "what certifications are needed for shoe export":
        "ISO 9001, CE marking (for EU), GSP Form A, Chamber of Commerce "
        "certificate.",
    "how to maintain cutting machines":
        "Clean blades daily, lubricate moving parts weekly, calibrate "
        "pressure monthly, replace worn blades promptly.",
    "what is lasting in shoe manufacturing":
        "Lasting is stretching the upper over the last (mold) and securing "
        "it before sole attachment for proper shape.",
    "how to conduct a flex test on shoes":
        "Bend the shoe 10,000 times on a flex tester. Check for sole "
        "separation, upper cracking, or stitch failure.",
    "what is a supplier quality audit":
        "Visit supplier facility, inspect raw material quality, check "
        "certifications, review defect rates and delivery history.",
    "how to implement Six Sigma in shoe production":
        "Define defect metrics, measure current defect rate, analyze root "
        "causes, improve processes, and control via SOPs.",
    "how to reduce material wastage in cutting":
        "Use computer-aided cutting (CAD), nest patterns efficiently, "
        "reuse offcuts for lining or small components.",
    "how to manage production schedule":
        "Set daily output targets per line, track actual vs target hourly, "
        "adjust staff allocation for bottleneck stages.",
    "what is sole attachment process":
        "Roughen mating surfaces, apply adhesive to both, let it tack, "
        "press sole onto lasted upper, cure under pressure.",
    "how to handle production rejects":
        "Tag rejected units, log defect type, return to rework if fixable, "
        "write off irreparable units with supervisor approval.",
    "what is ISO 9001 and why does it matter for shoe export":
        "ISO 9001 certifies your quality management system meets "
        "international standards, required by most export buyers.",

    # ── Human Resourcesne ─────────────────────────────────────────────
    "how many staff needed for a shoe outlet":
        "Minimum: 1 manager, 2 sales staff, 1 cashier, 1 stock keeper "
        "per outlet.",
    "how to train sales staff":
        "Product knowledge training, role-play selling scenarios, customer "
        "service workshops, weekly briefings.",
    "what is the salary structure":
        "Sales staff: Rs. 25,000-35,000. Supervisors: Rs. 40,000-55,000. "
        "Managers: Rs. 60,000-90,000.",
    "how to motivate staff":
        "Commission on sales, monthly bonuses for top performers, annual "
        "trips, and recognition awards.",
    "how to handle staff conflict":
        "Mediate privately, listen to both sides, document resolution, "
        "involve HR if unresolved.",
    "how to recruit staff for a shoe company":
        "Post on LinkedIn and local job boards, screen CVs for retail "
        "experience, conduct structured interviews, verify CNICs.",
    "what is the onboarding process for new hires":
        "Induction on day 1 covering company policies, product training "
        "in week 1, buddy assignment, 3-month probation review.",
    "how to handle overtime policy":
        "Overtime beyond 8 hours requires supervisor approval. Compensate "
        "at 1.5x hourly rate or give compensatory off.",
    "what is the harassment policy":
        "Zero tolerance for harassment. Complaint to HR, independent "
        "inquiry within 7 days, action per PESHA 2010.",
    "how to conduct an exit interview":
        "HR meets departing employee privately. Ask about reasons for "
        "leaving, experience, and improvement suggestions.",
    "how to set up commission plan for sales staff":
        "Base salary + 1-2% commission on monthly sales above target. "
        "Pay commission with next month's salary.",
    "how to do staff performance appraisal":
        "Set KPIs at start of year, mid-year review, annual rating on "
        "1-5 scale, link to increment and promotion decisions.",
    "what are payroll grades in shoe company":
        "Grade 1: support staff. Grade 2: sales/floor staff. "
        "Grade 3: supervisors. Grade 4: managers. Grade 5: directors.",
    "how to handle staff attendance":
        "Use biometric machine at entry, export daily report, flag "
        "absences to supervisor by 10 AM for follow-up.",
    "how to plan staff requirements for peak season":
        "Forecast sales volume, calculate staff-to-sales ratio, hire "
        "temporary staff 4 weeks before Eid or back-to-school.",
}

GREETINGS = ["hello", "hi", "hey", "salam", "assalam",
             "good morning", "good evening"]
FAREWELLS = ["bye", "exit", "quit", "goodbye",
             "thank you", "thanks"]


# ── AI Engine (If-Else Rule Based) ───────────────────────────────────────────
class ShoesAI:
    def __init__(self):
        self.session_start = datetime.datetime.now()
        self.query_count = 0
        self.name = "ShoesAI"

    def preprocess(self, text: str) -> str:
        return text.lower().strip().rstrip("?!.")

    def find_answer(self, query: str) -> str:
        cleaned = self.preprocess(query)

        # Rule 1: Greeting detection
        if any(g in cleaned for g in GREETINGS):
            return (f"Welcome to {self.name}! I assist with Shoes Company "
                    "Administration and Marketing. How can I help you today?")

        # Rule 2: Farewell detection
        if any(f in cleaned for f in FAREWELLS):
            return f"Thank you for using {self.name}. Goodbye!"

        # Rule 3: Help / menu command
        if cleaned in ("help", "menu", "options", "what can you do"):
            topics = [
                "Administration (HR, branches, policies)",
                "Marketing (campaigns, social media, pricing)",
                "Inventory (stock, SKU, reorder levels)",
                "Finance (reports, margins, break-even)",
                "Manufacturing (materials, QC, process)",
                "Staff Management (salaries, training, conflict)",
            ]
            return ("I can answer questions on:\n"
                    + "\n".join(f"  - {t}" for t in topics))

        # Rule 4: Exact match lookup
        if cleaned in KNOWLEDGE_BASE:
            return KNOWLEDGE_BASE[cleaned]

        # Rule 5: Partial keyword match (>= 50% word overlap)
        for key, answer in KNOWLEDGE_BASE.items():
            key_words = set(key.split())
            query_words = set(cleaned.split())
            overlap = key_words & query_words
            if len(overlap) >= max(2, len(key_words) // 2):
                return answer

        # Rule 6: Single significant keyword fallback
        for key, answer in KNOWLEDGE_BASE.items():
            if any(w in cleaned for w in key.split() if len(w) > 4):
                return f"(Related answer) {answer}"

        # Rule 7: Default fallback
        return ("I don't have a specific answer for that. "
                "Please ask about administration, marketing, inventory, "
                "finance, manufacturing, or staff management.")

    def get_stats(self) -> str:
        elapsed = datetime.datetime.now() - self.session_start
        mins = int(elapsed.total_seconds() // 60)
        return (f"Session: {mins} min | Queries answered: "
                f"{self.query_count} | Knowledge base: "
                f"{len(KNOWLEDGE_BASE)} rules")


# ── CLI Interface ─────────────────────────────────────────────────────────────
def print_banner():
    print("=" * 62)
    print("  SHOES COMPANY ADMINISTRATION & MARKETING AI SYSTEM")
    print("  CLI Expert System | If-Else Rule Based AI")
    print("  Developer : Mohammad Awaid Riaz | Roll No: 37")
    print("  Program   : BS-AI Semester 4 | Section A")
    print("  University: Emerson University Multan")
    print("=" * 62)
    print("Type your question. 'help' for topics. 'exit' to quit.")
    print("-" * 62)


def main():
    ai = ShoesAI()
    print_banner()

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            sys.exit(0)

        if not user_input:
            continue

        ai.query_count += 1

        if user_input.lower() == "stats":
            print(f"\nShoesAI: {ai.get_stats()}")
            continue

        response = ai.find_answer(user_input)
        print(f"\nShoesAI: {response}")

        if any(f in user_input.lower() for f in FAREWELLS):
            sys.exit(0)


if __name__ == "__main__":
    main()
