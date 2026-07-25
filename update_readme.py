import datetime
import random
import re
import pytz

# List of inspiring developer quotes
QUOTES = [
    "“First, solve the problem. Then, write the code.” – John Johnson",
    "“Experience is the name everyone gives to their mistakes.” – Oscar Wilde",
    "“Code is like humor. When you have to explain it, it’s bad.” – Cory House",
    "“Before software can be reusable it first has to be usable.” – Ralph Johnson",
    "“Make it work, make it right, make it fast.” – Kent Beck",
    "“Simplicity is the soul of efficiency.” – Austin Freeman",
    "“Fix the cause, not the symptom.” – Steve Maguire",
    "“Programs must be written for people to read, and only incidentally for machines to execute.” – Harold Abelson",
    "“Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” – Martin Fowler",
    "“Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.” – Antoine de Saint-Exupéry",
    "“In order to be irreplaceable one must always be different.” – Coco Chanel",
    "“Java is to JavaScript what car is to Carpet.” – Chris Heilmann",
    "“Knowledge is power.” – Francis Bacon",
    "“Optimism is an occupational hazard of programming: feedback is the treatment.” – Kent Beck",
    "“Talk is cheap. Show me the code.” – Linus Torvalds"
]

def get_live_data():
    # Set timezone to Indian Standard Time (IST)
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(tz)
    
    # 1. Format Time/Date
    time_str = now.strftime('%A, %d %B %Y, %I:%M %p IST')
    
    # 2. Calculate Year Progress
    start_of_year = datetime.datetime(now.year, 1, 1, tzinfo=tz)
    end_of_year = datetime.datetime(now.year + 1, 1, 1, tzinfo=tz)
    total_seconds = (end_of_year - start_of_year).total_seconds()
    elapsed_seconds = (now - start_of_year).total_seconds()
    progress = (elapsed_seconds / total_seconds) * 100
    
    # Generate progress bar
    bar_length = 20
    filled_length = int(bar_length * progress // 100)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    progress_str = f"{bar} {progress:.2f}%"
    
    # 3. Select Quote
    quote = random.choice(QUOTES)
    
    return time_str, progress_str, quote

def update_readme():
    time_str, progress_str, quote = get_live_data()
    
    # Read the current README file
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Construct the replacement content block
    live_content = (
        f"> ### 🕒 Live Status & Update\n"
        f">\n"
        f"> | Metric | Value |\n"
        f"> | :--- | :--- |\n"
        f"> | 📅 **Current Date/Time** | `{time_str}` |\n"
        f"> | ⏳ **Year Progress** | `{progress_str}` |\n"
        f"> | 💬 **Quote of the Day** | *{quote}* |\n"
    )
    
    # Pattern to search for placeholder markers
    start_marker = "<!-- START_SECTION:live_info -->"
    end_marker = "<!-- END_SECTION:live_info -->"
    pattern = f"{start_marker}.*?{end_marker}"
    
    # Replace content between markers
    new_content = re.sub(pattern, f"{start_marker}\n{live_content}{end_marker}", content, flags=re.DOTALL)
    
    # Write back to README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
