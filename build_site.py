#!/usr/bin/env python3
"""Build the Dlucs — The New Era of Barbering swipe site. Run: python3 build_site.py"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/DLUCS_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/**/*.mp4"), recursive=True)):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     ROLES.get(os.path.basename(p), "")))
    return rows


ROLES = {}

CONFIG = {
 "SITE": "Dlucs — The New Era of Barbering",
 "CREATOR": "Dlucs",
 "ADS_KEY": "dlucs",
 "FUNNEL_IDS": ["F042"],
 "CAPTURED": "18 August 2026",
 "REPO": REPO,
 "PACKAGE": "~/Downloads/Swipes/DLUCS_Swipe",
 "BLURB": "Coaching barbers to $20k&ndash;$30k months. There is <b>no VSL</b>. The application page "
          "is <b>6.2 hours of long-form customer interviews</b> and a Calendly.",
 "PAGES": [("index.html","Overview"),("analysis.html","Analysis"),
              ("transcripts.html","Transcripts"),("videos.html","Video library")],
 "STATS": [("Niche","Barbers"),("Promise","$20k &ndash; $30k+ months"),("Operator","Michael De Jesus"),
           ("VSL","<b>none</b>"),("Proof videos","12"),("Total proof runtime","<b>6h 09m</b>"),
           ("Longest single video","87 min"),("Booking","Calendly")],
 "OFFER": [("Product","Coaching / mentorship for working barbers"),
   ("Promise","&ldquo;How we grow and scale barbers to <b>$20k &ndash; $30k+ months</b>&rdquo;"),
   ("Positioning","&ldquo;We are revolutionizing the barbering industry&rdquo;"),
   ("Structure","Explicit <b>&ldquo;Step 1 of 2: Watch Video · Step 2 of 2: Book Your Call&rdquo;</b>"),
   ("Proof","12 named-barber interview videos, 23 to 87 minutes each"),
   ("Path","Main page &rarr; video + application &rarr; Calendly &rarr; pre-call confirmation"),
   ("Price","<b>Never stated</b>")],
 "FINDINGS": [
  ("There is no VSL. The proof <i>is</i> the pitch",
   "Every video embedded across the funnel is a <b>customer interview</b> &mdash; 12 of them, "
   "totalling <b>6 hours 9 minutes</b>, the longest running 87 minutes. There is no presenter-led "
   "sales video anywhere. He has replaced the argument with the evidence and let the prospect "
   "choose how much of it to consume."),
  ("Every title is a name, a number and a place",
   "&ldquo;@nguyensteadycutting makes <b>$20k/m</b> as a barber in <b>Richmond Virginia</b>&rdquo;. "
   "&ldquo;Barber makes $20k/m cutting in <b>parents garage</b>&rdquo;. &ldquo;@terrance90_ went "
   "from $1.6k to <b>$6.9k/m in 60 days</b>&rdquo;. Handle, figure, and a specific humble setting. "
   "For a barber earning $2k in a rented chair, the garage detail is the proof &mdash; not the "
   "$20k. <b>The setting does the identification work the number cannot.</b>"),
  ("Long-form proof is a filter, not just proof",
   "Nobody watches 87 minutes of another barber's interview unless they are seriously considering "
   "this. The runtime pre-qualifies intent before the call, at zero cost to him. Compare Viral "
   "Coach, which uses <i>twelve shallow</i> proof cards to kill a breadth objection &mdash; "
   "opposite tactic, opposite problem. <b>Dlucs sells one niche deeply; Viral Coach sells every "
   "niche shallowly. Each built the proof shape their objection required.</b>"),
  ("The two-step is labelled on the page",
   "&ldquo;<b>Step 1 of 2:</b> Watch Video&rdquo; and &ldquo;<b>Step 2 of 2:</b> Book Your Call&rdquo;. "
   "Naming the number of steps caps the perceived commitment. A prospect who knows there are "
   "exactly two will start; one who cannot see the end of the process often will not."),
  ("Browser push notifications are installed",
   "<b>PushCrew</b> runs alongside ClickFunnels, Calendly, Wistia, Intercom, Hyros, Meta Pixel and "
   "GTM. A retargeting channel that survives ad-blockers and does not need an email address. "
   "Nobody else in this file runs it."),
 ],
 "FUNNEL": [
  ("Main page","theneweraofbarbering.com","&ldquo;We are revolutionizing the barbering industry.&rdquo; Michael De Jesus. Links to a full YouTube success-story playlist."),
  ("Video + application","go.theneweraofbarbering.com/nec-video",'<span class="tag good">the mechanic</span> &ldquo;Step 1 of 2 / Step 2 of 2.&rdquo; 12 interview videos. ClickFunnels + Calendly + Wistia + Hyros + PushCrew.'),
  ("Pre-call confirmation","go.theneweraofbarbering.com/pre-call-congrats","&ldquo;Congratulations! We received your application.&rdquo; Step 1 watch, Step 2 inside look."),
 ],
 "TRANSCRIPT_GROUPS": [("Customer interviews", sorted(glob.glob(os.path.join(PKG,"Transcript/*.md"))))],
 "SLIDE_PAGES": [],
 "ANALYSIS": """
<div class="note"><b>This funnel has no sales video at all.</b> Six hours of other barbers talking,
a Calendly, and a two-step label. It is the most extreme proof-over-pitch structure in the swipe
file, and it is working in a niche where the buyer distrusts polish.</div>

<h2 class="sec">The twelve videos</h2>
<div class="tablewrap"><table>
<tr><th>Runtime</th><th>Title</th></tr>
<tr><td>87 min</td><td>The TRUTH Behind How We Scaled Henry Hoang To $24k/m</td></tr>
<tr><td>40 min</td><td>Barber LEAVES $10k/m Business To Start From Zero</td></tr>
<tr><td>33 min</td><td>Barber Makes $20k/m Cutting In Parents Garage</td></tr>
<tr><td>30 min</td><td>How @Joelthompsoncoach scaled to $200 a cut and $20k months</td></tr>
<tr><td>27 min</td><td>Customer review: @ryan2fresh makes $13k/m in his parents spare room</td></tr>
<tr><td>26 min</td><td>Dlucs Customer Review: Barbershop Owner SCALES His Income</td></tr>
<tr><td>24 min</td><td>@barberxrios Barber Made $34k Doing Hair Replacement Units</td></tr>
<tr><td>24 min</td><td>@nguyensteadycutting makes $20k/m in Richmond Virginia</td></tr>
<tr><td>23 min</td><td>@tristan.escobedo Makes $9k Cutting From His Garage</td></tr>
<tr><td>22 min</td><td>Barbers INSANE Journey From $2K to $13K Per Month</td></tr>
<tr><td>19 min</td><td>@terrance90_ Went from $1.6k to $6.9k/m in 60 days</td></tr>
<tr><td>16 min</td><td>@legacyluis22 Added $27k To His Yearly Income In 60 Days</td></tr>
</table></div>
<p style="margin-top:12px"><b>Total: 6 hours 9 minutes.</b> Every one is a real handle a prospect
can go and check on Instagram. That is the part that cannot be faked and is the reason the format
survives without a pitch wrapped around it.</p>

<h2 class="sec">Two opposite proof strategies, both correct</h2>
<div class="tablewrap"><table>
<tr><th></th><th>Dlucs</th><th>Viral Coach</th></tr>
<tr><td>Proof shape</td><td>12 deep, 6+ hours</td><td>12 shallow cards</td></tr>
<tr><td>Market</td><td>One niche (barbers)</td><td>Every local niche</td></tr>
<tr><td>Objection killed</td><td>&ldquo;Can someone <i>like me</i> really do this?&rdquo;</td><td>&ldquo;Would this work in <i>my industry</i>?&rdquo;</td></tr>
</table></div>
<p style="margin-top:12px"><span class="tag">READ</span> We are closer to Dlucs than to Viral Coach
&mdash; one avatar, one promise. Our proof is still formatted like Viral Coach's: short, many,
shallow. <b>Worth testing one 30-minute unedited student interview against the current highlight
reels.</b></p>

<h2 class="sec">The stack</h2>
<p>ClickFunnels, Calendly, Wistia, Intercom, Hyros, Meta Pixel, GTM, GA and <b>PushCrew</b> for
browser push. The push channel is the outlier &mdash; a retargeting surface that needs no email
and ignores ad-blockers.</p>

<h2 class="sec">What is missing, honestly</h2>
<ul><li><b>The 12 videos are identified and catalogued but not yet downloaded.</b> YouTube
rate-limited this IP mid-capture (HTTP 403 on every format after the first ~10 MB per file). The
IDs, titles and runtimes are all recorded above; the pull needs a retry.</li>
<li><b>No transcripts yet</b>, for the same reason. This is the highest-value outstanding item in
this swipe &mdash; 6 hours of barbers describing, in their own words, what they were stuck on and
what changed. That is objection and desire language we cannot get anywhere else.</li>
<li><b>No price</b> anywhere in the funnel.</li>
<li><b>No emails</b> &mdash; opt-in never submitted.</li></ul>
""",
}
CONFIG["VIDEOS"] = video_library()

if __name__ == "__main__":
    build(CONFIG)
