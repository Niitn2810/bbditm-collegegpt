from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(user_message: str) -> str:
    msg = user_message.lower()

    # ---- Greetings ----
    if any(w in msg for w in ["hello", "hi", "hii", "hey", "namaste"]):
        return (
            "Hello! I am BBDITM – CollegeGPT 🤖\n"
            "Ask me about admission, fees, hostel, placement, scholarships, etc."
        )

    # ---- About college ----
    if "about" in msg or ("bbditm" in msg and "college" in msg):
        return (
            "Babu Banarasi Das Institute of Technology & Management (BBDITM), "
            "Lucknow is an AICTE approved institute affiliated to Dr. A.P.J. Abdul Kalam "
            "Technical University (AKTU). The college focuses on quality education, "
            "practical learning and overall development of students."
        )

    # ---- Courses / Branches ----
    if "course" in msg or "branch" in msg or "b.tech" in msg or "btech" in msg:
        return (
            "Courses offered at BBDITM:\n"
            "- B.Tech: CSE, CSE(AI), IT, ECE, ME, CE\n"
            "- BBA, BCA\n"
            "- M.Tech (selected branches)\n"
            "CSE (Computer Science & Engineering) is one of the most popular branches."
        )

    # ---- Admission process ----
    if "admission" in msg or "how to apply" in msg or "process" in msg:
        return (
            "Admission to B.Tech at BBDITM, Lucknow is mainly through AKTU (UPTAC) counselling "
            "based on JEE (Main) / entrance rank.\n"
            "You can also contact the college admission cell with required documents for "
            "guidance about direct/management quota seats.\n"
            "For exact dates, please check aktu / bbditm official website."
        )

    # ---- Fee structure (B.Tech CSE) ----
    if "fee" in msg or "fees" in msg or "fee structure" in msg:
        return (
            "BBDITM B.Tech CSE – Approx Fee Structure (per your document):\n"
            "Year 1: ₹1,18,803\n"
            "Year 2: ₹1,10,303\n"
            "Year 3: ₹1,10,303\n"
            "Year 4: ₹1,05,303\n\n"
            "Main components: Tuition fee, welfare fund, insurance, internal exam fee, "
            "personality development & training (Learnovate) etc.\n"
            "Note: Hostel, bus and university exam fees are separate and may change year to year."
        )

    # ---- Hostel / Bus / Extra charges ----
    if "hostel" in msg or "room" in msg or "mess" in msg or "bus" in msg:
        return (
            "Yes, BBDITM provides in-campus hostel facility.\n"
            "- Hostel fee (3-seater Non-AC) ~ ₹79,000 per year + ₹1,000 medical charges\n"
            "- Annual bus fee for local conveyance ~ ₹30,000\n"
            "Hostel includes mess, Wi-Fi, security and basic facilities."
        )

    # ---- Scholarship ----
    if "scholarship" in msg or "discount" in msg or "fee concession" in msg:
        return (
            "As per fee document:\n"
            "- 25% scholarship on tuition fee is given to students taking admission in "
            "B.Tech (ECE/EE/ME/Civil) – as per college policy.\n"
            "- 25% scholarship on tuition fee is also given in some PG courses if the "
            "candidate is UG pass-out from the same college.\n"
            "For current scholarship rules, please confirm with the college admission cell."
        )

    # ---- Placement ----
    if "placement" in msg or "package" in msg or "company" in msg or "job" in msg:
        return (
            "BBDITM Lucknow has an active Training & Placement Cell for B.Tech students.\n"
            "Companies that have visited include:\n"
            "- Wipro, Infosys, TCS, HCL, Tech Mahindra, Cognizant, Byju's and others.\n\n"
            "Typical packages (approx, vary every year):\n"
            "- Average package: ₹3.5 – 5 LPA\n"
            "- Higher packages: around ₹8 – 10 LPA for some students.\n\n"
            "The T&P cell also conducts aptitude training, soft-skill sessions and mock interviews."
        )

    # ---- Facilities ----
    if "facility" in msg or "facilities" in msg or "library" in msg or "lab" in msg or "campus" in msg:
        return (
            "BBDITM campus facilities include:\n"
            "- Central library\n"
            "- Well-equipped labs for CSE and other branches\n"
            "- Wi-Fi enabled campus\n"
            "- Seminar halls & smart classrooms\n"
            "- Sports grounds and cafeteria\n"
            "- Separate hostels for boys and girls"
        )

    # ---- Location / address ----
    if "location" in msg or "address" in msg or "where" in msg:
        return (
            "BBDITM is located at:\n"
            "Sector I, Dr. Akhilesh Das Nagar, Faizabad Road, Lucknow, Uttar Pradesh – 226028.\n"
            "You can search 'BBDITM Lucknow' on Google Maps for exact location and directions."
        )

    # ---- Website / contact ----
    if "contact" in msg or "phone" in msg or "email" in msg or "website" in msg:
        return (
            "BBDITM Official Contact:\n"
            "- Website: www.bbditm.ac.in\n"
            "- Email: director@bbditm.ac.in\n"
            "- Phone: +91-522-6196222 / 6196223 / 6196349\n"
            "For admission related queries, you can also use the enquiry form on the website."
        )

    # ---- Thanks / bye ----
    if "thank" in msg or "thanks" in msg or "shukriya" in msg:
        return "You're welcome! 🙂 If you have more questions about BBDITM, feel free to ask."

    # ---- Default / fallback ----
    return (
        "Sorry, I couldn't understand your question clearly. 🙏\n"
        "You can ask me things like:\n"
        "- BBDITM CSE fee structure\n"
        "- Admission process\n"
        "- Hostel / bus fee\n"
        "- Placement details\n"
        "- College facilities, address, website, contact etc."
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_bot_reply():
    data = request.get_json()
    user_msg = data.get("message", "")
    reply = get_bot_response(user_msg)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    # debug=True sirf development ke liye
    app.run(debug=True)
