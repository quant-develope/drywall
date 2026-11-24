"""English pages: same keys and structure as pages_el.py."""
from pages_el import boards, svc_grid

NAV = [("ceilings", "Ceilings"), ("partitions", "Partitions"), ("insulation", "Insulation"), ("cost", "Cost"),
       ("areas", "Areas"), ("contact", "Contact")]

MENU = [
    ("Services", [("ceilings", "Drywall suspended ceilings"), ("partitions", "Partitions & new rooms"), ("linings", "Wall linings"),
                  ("insulation", "Thermal & sound insulation"), ("bathroom", "Drywall in bathrooms & kitchens"),
                  ("decor", "Hidden lighting & features"), ("hotels", "Hotels & shops"), ("repairs", "Repairs")]),
    ("Before you start", [("cost", "What drives the cost"), ("areas", "Areas we cover"), ("faq", "Frequently asked questions")]),
    ("Gypsos Loutraki", [("home", "Home"), ("contact", "Contact"), ("privacy", "Privacy")]),
]

FORM = dict(eb="Free site visit", h="Tell us what you want to build. We come and measure it.",
            card="Site visit & written quote",
            p="Leave your name and phone and pick the type of work. The installer who will take the measurements calls you to arrange a day and time.",
            perks=["We talk on the phone, WhatsApp or Viber", "Site visit and measurement at no charge", "Written quote per job and per square metre"],
            name="Name", phone="Phone", area="Area", type="Work",
            areas=["Loutraki", "Corinth", "Perachora / Pisia / Lake Vouliagmeni", "Other area"],
            opts=["Suspended ceiling", "Partition / new room", "Wall lining", "Thermal or sound insulation", "Bathroom or kitchen",
                  "Hidden lighting / feature", "Hotel or shop", "Repair", "Not sure yet, I need advice"],
            msg="A few words about the space (optional)", ph="e.g. living room 30 m², 3 m high, I want a ceiling with hidden lighting",
            send="Get a quote", alt="Or send the same message via",
            note="Your details are used only to reply to you.", privt="Privacy")

ILL = {
    "hero-saloni": "Living room in progress: metal frame with mineral wool on the left, drywall and a lit niche on the right",
    "psevdorofi": "Suspended drywall ceiling with spotlights and perimeter hidden lighting",
    "chorisma": "Partition with CW studs, a door frame and mineral wool before the boards go on",
    "ependysi": "Lining an old cracked wall: drywall on a metal frame",
    "monosi": "Frame filled with mineral wool for sound and thermal insulation",
    "bano": "Bathroom with green moisture-resistant board behind the tiles and a lit niche",
    "diakosmitika": "Drywall TV wall with shelves, hidden lighting and a lit shelf",
    "xenodocheia": "Hotel corridor with a suspended ceiling, lighting and a room door",
    "episkeves": "Repairing a hole in drywall: cut out, new piece, filler",
    "chartis-perioxis": "Map: Loutraki, Corinth, Perachora, Pisia and Lake Vouliagmeni",
    "saloni-kryfos-fotismos": "Living room with a suspended ceiling, perimeter hidden lighting and a TV wall with lit shelves",
    "diadromos-kryfos-fotismos": "Hallway with a suspended ceiling and LED cove lighting on both sides",
    "orthostates-chorismatos": "Metal partition studs in place, before the boards go on",
    "skeletos-chorismaton-diadromos": "Partition and ceiling framing with insulation above, boards ready on the floor",
    "ependysi-toichou-provoleas": "Wall being prepared for lining, with site floodlights",
    "kogchi-ntous": "Tiled niche in a shower wall",
    "kogches-rafia-saloni": "Living-room wall with drywall recesses and shelves",
    "diadromos-xenodocheiou": "Hotel corridor with a suspended ceiling, spotlights and straight walls",
    "stokarisma-armon": "Filling drywall joints with a taping knife",
    "tavani-me-tainies-stoko": "Large room with drywall ceiling and walls, first coat of filler on the joints",
    "ergotaxio-gypsosanides": "Shop space with drywall walls and ceiling before finishing",
    "orofi-gypsosanida-ktirio": "Drywall ceiling and walls in a commercial space, with plumbing outlets ready",
}

SVC = [("ceilings", "diadromos-kryfos-fotismos", "Suspended ceilings", "A level ceiling, spotlights, hidden lighting and room for cables and air-conditioning ducts."),
       ("partitions", "orthostates-chorismatos", "Partitions & new rooms", "One room becomes two in two days, with no bricks, rubble or damp."),
       ("linings", "tavani-me-tainies-stoko", "Wall linings", "Crooked or cracked walls become straight and ready to paint."),
       ("insulation", "skeletos-chorismaton-diadromos", "Thermal & sound insulation", "Less noise from next door and lower electricity bills."),
       ("bathroom", "kogchi-ntous", "Bathrooms & kitchens", "Moisture-resistant board behind tiles, shower niches, boxing-in for pipes."),
       ("decor", "kogches-rafia-saloni", "Hidden lighting & features", "TV walls, shelves, niches, arches and LED lighting.")]

BOARDS = [("#e9e4d8", "White · type A", "Standard board", "For ceilings, partitions and linings in dry rooms. 12.5 mm thick."),
          ("#9fc58f", "Green · type H", "Moisture-resistant", "For bathrooms, kitchens, laundry rooms and storerooms. Goes behind tiles."),
          ("#e79a9a", "Pink / red · type F", "Fire-resistant", "For boiler rooms, stairwells, hotels and shops with fire-protection requirements."),
          ("#8fb0d8", "Blue · acoustic", "Sound-insulating", "Heavier board for partitions between bedrooms, offices and hotel rooms.")]


def _home(p, B):
    L = lambda k: B.path_of("en", k)  # noqa: E731
    return """<section class="hero"><div class="w">
 <div class="hero-in">
  <div>
   <p class="eyebrow">Drywall in Loutraki, Corinth and Perachora</p>
   <h1>Drywall installation in Loutraki, <em>clean and on time</em></h1>
   <p class="lead">Suspended ceilings, partitions, wall linings and insulation with dry construction, in homes, holiday houses, hotels and shops in Loutraki, Corinth and Perachora. We measure, give you a written price and finish when we said we would.</p>
   <ul class="ok"><li>Free site visit and quote</li><li>Framing and boards from well-known manufacturers, CE marked</li><li>We hand over the space swept clean and ready to paint</li></ul>
   <p class="hero-alt">Want to talk now? <a href="tel:{tel}">{phone}</a> · <a href="https://wa.me/{wa}">WhatsApp</a> · Viber · we speak English</p>
  </div>
  <figure class="hero-ph">{hero}<span class="badge"><b>1–2</b>days for a<br>20 m² partition</span><figcaption>{hero_cap}</figcaption></figure>
 </div>
 {form}
</div></section>
{trust}
<section class="sec"><div class="w">
 <div class="sec-h"><div><p class="eyebrow">What we build</p><h2>Every kind of drywall work from one crew</h2></div><a class="more" href="{hotels}">For hotels and shops {arrow}</a></div>
 {svc}
</div></section>
<section class="sec sec-stone"><div class="w split">
 <div><p class="eyebrow">Why drywall</p><h2>A wall in one day, not in two weeks</h2>
  <p>A brick partition needs laying, plastering, weeks to dry and buckets of rubble. With drywall we set up a metal frame, run cables and insulation inside and screw on the boards. The next day we fill the joints and the wall is ready to paint.</p>
  <ul class="ok"><li>Light construction that does not load the slab and copes well with earthquakes</li><li>Cables, pipes and mineral wool fit inside the wall</li><li>Straight surfaces, no cracks from damp or settlement</li><li>Easy to change if you want a different layout later</li></ul>
  <p><a class="more" href="{cost}">What drives the cost {arrow}</a></p></div>
 <div>{lining}</div>
</div></section>
<section class="sec sec-dark"><div class="w">
 <div class="sec-h"><div><p class="eyebrow">How we work</p><h2>From the first call to the last coat of filler</h2></div></div>
 <ol class="line"><li><b>Contact</b>You send photos and rough dimensions.</li><li><b>Site visit</b>We measure and check heights, wiring and plumbing.</li><li><b>Quote</b>In writing, with every job and the materials listed.</li><li><b>Build</b>Framing, insulation, boards, corner beads, tape.</li><li><b>Finish</b>Filling to level Q2–Q4, sanding, cleaning.</li></ol>
</div></section>
<section class="sec"><div class="w">
 <div class="sec-h"><div><p class="eyebrow">Materials</p><h2>The right board for every room</h2></div><a class="more" href="{bathroom}">Drywall in bathrooms and kitchens {arrow}</a></div>
 {boards}
</div></section>
<section class="sec sec-stone"><div class="w split">
 <div>{map}</div>
 <div><p class="eyebrow">Where we work</p><h2>Loutraki, Corinth and Perachora</h2>
  <p>We are based in Loutraki. Every day we work in apartments and hotels in town, in houses, offices and shops in Corinth, and in holiday homes in Perachora, Pisia and around Lake Vouliagmeni.</p>
  <ul class="chips"><li class="on">Loutraki</li><li>Corinth</li><li>Perachora</li><li>Pisia</li><li>Lake Vouliagmeni</li></ul>
  <p style="margin-top:20px"><a class="more" href="{areas}">More about the areas {arrow}</a></p></div>
</div></section>
""".format(tel=B.PHONE_TEL, phone=B.PHONE, wa=B.WA, arrow=B.ARROW,
           form=B.lead_form("en", "Ask for a free site visit and quote", wide=True), trust=B.trust("en"),
           hero=B.ill("saloni-kryfos-fotismos", "en", eager=True, sizes="(min-width: 1000px) 46vw, 100vw"), hero_cap=ILL["saloni-kryfos-fotismos"],
           svc=svc_grid(B, "en", SVC), lining=B.fig("ependysi", "en"), boards=boards(BOARDS), map=B.fig("chartis-perioxis", "en", "ph map"),
           hotels=L("hotels"), cost=L("cost"), bathroom=L("bathroom"), areas=L("areas"))


HOME_FAQ = [
    ("How soon can you come for a site visit?", "In Loutraki usually within 2–3 working days. If you send photos on WhatsApp first, we come to the appointment with a first idea of the solution and the price."),
    ("Do you price per square metre?", "Yes, the quote shows a price per m² for each type of work, with extras such as hidden lighting, mineral wool or doors listed separately. The final price depends on height, board type and finish level, so we give it after measuring."),
    ("Do you also paint?", "We hand over the wall filled and sanded, ready for primer. If you like, we arrange the painting with a partner painter, so you have one person for the whole job."),
    ("Do you work in occupied homes?", "Yes. We cover floors and furniture, cut boards outside or in one spot as far as possible, and clean up every afternoon. Drywall has none of the mortar and rubble of brickwork."),
    ("Do I need a permit for a drywall partition?", "Interior layout changes that do not touch the load-bearing structure usually need a small-scale works approval or nothing at all, depending on the case. In an apartment block, let the building manager know. Check with your engineer to be sure."),
]

PAGES = {
    "home": dict(
        title="Drywall installers in Loutraki · ceilings, partitions, insulation",
        desc="Drywall installation in Loutraki, Corinth and Perachora: suspended ceilings, partitions, wall linings, insulation. Free site visit and written quote.",
        h1="Drywall installation in Loutraki", short="Home", ill="saloni-kryfos-fotismos", cls="home", body=_home, faq=HOME_FAQ),

    "ceilings": dict(
        slug="drywall-ceilings-loutraki", ill="diadromos-kryfos-fotismos", service=True, stype="Drywall suspended ceiling",
        title="Drywall suspended ceilings in Loutraki · spots & hidden lighting",
        desc="Drywall suspended ceilings in Loutraki, Corinth and Perachora: a level ceiling, spotlights, hidden LED lighting, room for air conditioning. Free site visit.",
        h1="Drywall suspended ceilings in Loutraki", short="Ceilings", kicker="Ceilings",
        card="A level ceiling with spots, hidden lighting and room for the AC.",
        lead="A suspended ceiling hides cables and pipes, levels a crooked or cracked ceiling and gives you a place for spotlights, LED strips and air-conditioning vents. We hang it from the slab on adjustable hangers, as low as it needs to be.",
        ticks=["From 5–6 cm below the slab for simple levelling", "Steps, recesses and perimeter hidden lighting", "Access hatches for AC units and manifolds"],
        answer="For a 25–30 m² living room, the ceiling is framed and boarded in 2–3 days and filled in another 1–2. The price depends mostly on the design: a flat ceiling costs much less than one with steps and hidden lighting. See {{k:cost|what drives the cost}}.",
        secs=[
            ("How a suspended ceiling is built", "<p>First we mark the final height on every wall with a laser and fix the UD perimeter track. From the slab we hang rods every 80–100 cm and attach the CD 60×27 main channels to them. The frame is levelled, and only then do we screw on the boards across the channels, staggering the joints so they never line up.</p><p>The joints get tape and filler in two or three coats. Corners get corner beads so they stay straight and do not chip.</p>{{ill:psevdorofi}}"),
            ("Hidden lighting and spotlights", "<p>Hidden (cove) lighting is an LED strip inside a channel along the perimeter or around a recess. The light falls on the ceiling and the room feels taller. We design the channel together with the electrician, so the driver fits and the strip is easy to replace.</p><p>Recessed spots need at least 8–10 cm of space below the slab. If you want recessed spots across the whole living room, tell us at the site visit, because that sets how far the ceiling drops. More on the {{k:decor|hidden lighting}} page.</p>{{ill:saloni-kryfos-fotismos}}"),
            ("Air conditioning, ventilation and hatches", "<p>In new homes and in Loutraki's hotels, AC ducts or ducted indoor units often go inside the ceiling. We leave openings for the vents and hinged access hatches, so filters can be cleaned and the technician can reach the unit without breaking anything.</p>"),
            ("Ceilings in bathrooms, balconies or under a roof", "<p>In bathrooms we use green moisture-resistant board, and the room must be ventilated. Under a roof or in an attic we first add insulation and a vapour barrier. For outdoor areas such as balcony soffits there are cement boards that withstand rain and sea salt. Ask us about your case.</p>{{note|If the slab shows damp or flaking plaster, we tell you before we start. A ceiling hides the problem, it does not solve it. Waterproofing first, drywall second.}}"),
        ],
        faq=[("How much lower will the ceiling be?", "5–6 cm for simple levelling, 8–12 cm if you want recessed spots, and more if AC ducts run through. On a 2.70 m ceiling a simple suspended ceiling does not change the feel of the room."),
             ("Will the ceiling crack over time?", "Not if the frame is hung correctly and the joints are taped. Cracks usually come from too few hangers or filler without tape, and we do neither."),
             ("Can I hang a light fitting?", "Yes. For heavy fittings we add a reinforcement in the frame beforehand, or fix directly to the slab. Tell us in advance where they will go.")],
        rel=["decor", "insulation", "cost"]),

    "partitions": dict(
        slug="drywall-partitions-loutraki", ill="orthostates-chorismatos", service=True, stype="Drywall partition",
        title="Drywall partitions in Loutraki · a new room in 2 days",
        desc="Drywall partitions in Loutraki: a new bedroom, office or walk-in wardrobe with sound insulation, a door and electrics. Free site visit, written quote.",
        h1="Drywall partitions in Loutraki", short="Partitions", kicker="New rooms",
        card="One room becomes two, with sound insulation, a door and sockets.",
        lead="Want a second bedroom for the children, a home office, or to split a studio for letting? With drywall the partition goes up in one or two days, with no bricks, plaster or waiting for it to dry.",
        ticks=["50, 75 or 100 mm frame, depending on the thickness you want", "Mineral wool inside for sound insulation", "Door frame, sockets and switches before the wall is closed"],
        answer="A typical 4-metre partition with a door and sound insulation is framed and closed in 1–2 days. Filling takes another 2, then it is painted. The finished thickness is 10–12.5 cm, about the same as a brick wall.",
        secs=[
            ("What a partition is made of", "<p>UW tracks are fixed to the floor and the ceiling. CW studs go into them every 60 cm, closer if wall cabinets will hang there. At the door we double the studs and add timber or a reinforced profile, so the frame does not shake.</p><p>The electrician runs cables and boxes before we close the second side. We fill the frame with mineral wool and screw one or two layers of board to each side.</p>{{ill:chorisma}}"),
            ("How much sound insulation you need", "<p>A simple partition with one board per side and no insulation stops speech, but not the TV. For bedrooms we recommend 50–70 mm mineral wool and double board on each side. That brings the partition to about 50 dB of sound reduction according to manufacturer data, enough that conversation next door is not heard.</p><p>Sealing the gaps matters as much as the insulation: a sealing tape under the tracks and acrylic sealant at the edges. See also {{k:insulation|sound insulation}}.</p>"),
            ("Wardrobes, shelves and heavy items", "<p>Drywall holds shelves, mirrors and a TV with the right anchors. For kitchen wall units, a water heater or a heavy wardrobe we add reinforcement inside the wall before closing it. That is why we ask at the site visit what goes on each wall.</p>"),
            ("Partitions in apartments for letting", "<p>Many apartments in Loutraki are let in the summer. A partition that turns a studio into a one-bedroom flat raises the value for short-term letting. We work fast from October to April, so the flat is ready before the season.</p>{{note|If the partition cuts a window or leaves a room without daylight, we say so from the start. Sometimes a glass strip above the door solves it.}}"),
        ],
        faq=[("Is a drywall partition sturdy?", "Yes. With studs at the right spacing and two boards per side, the wall does not shake when the door closes and stands up to normal household use."),
             ("Can I remove it later?", "Yes, it unscrews and comes out in a day, without touching the floor or ceiling beyond a few holes to fill."),
             ("Do you fit the door?", "We prepare the opening and fit the frame. The door itself can be hung by your carpenter or ours, whichever you prefer.")],
        rel=["insulation", "linings", "cost"]),

    "linings": dict(
        slug="drywall-wall-lining", ill="ependysi-toichou-provoleas", service=True, stype="Drywall wall lining",
        title="Drywall wall lining in Loutraki · straight walls, ready to paint",
        desc="Drywall wall lining in Loutraki: crooked, cracked or old walls become straight and ready to paint, with or without thermal insulation.",
        h1="Drywall wall lining", short="Wall linings", kicker="Walls",
        card="Crooked or cracked walls become straight, with or without insulation.",
        lead="An old house in Loutraki or Perachora often has crooked walls, plaster that bubbles and cracks that come back after every repaint. Drywall lining gives a new, straight surface in front of the old wall, without tearing anything out.",
        ticks=["On a frame or bonded, depending on the wall", "With thermal insulation on outside walls", "Cables and sockets run inside"],
        answer="If the wall is dry and fairly straight, we bond the board directly with plaster adhesive and you lose only 2 cm. If it is crooked or you want insulation, we build a frame and you lose 5–8 cm.",
        secs=[
            ("Bonded lining or on a frame", "<p><b>Bonded lining</b> uses dabs of plaster adhesive, directly on the plaster or brick. It is quick and cheap, but needs a dry wall without large hollows.</p><p><b>Framed lining</b> is built on CD or CW profiles a little in front of the wall. It corrects any unevenness, leaves room for cables and insulation, and is not affected by the old plaster.</p>{{ill:ependysi}}"),
            ("Thermal insulation from inside", "<p>On outside walls, especially north-facing ones, lining is a chance to add insulation. We fill the frame with stone wool or bond ready-made insulated plasterboard with expanded polystyrene. More on the {{k:insulation|insulation}} page.</p>"),
            ("When lining is not the answer", "<p>If the wall has active damp from rising water or a leak, lining will hide the problem and go mouldy behind. In that case the cause is fixed first and the drywall goes on afterwards.</p>{{note|In ground floors near the sea we often see damp at the bottom of walls. We measure it with a moisture meter at the site visit before suggesting a solution.}}"),
        ],
        faq=[("How much space do I lose?", "About 2 cm with bonded lining, 5–8 cm with a frame, and a little more with thick insulation."),
             ("Do I need to strip the old plaster?", "No, unless it is falling off. With a frame the board does not touch the old plaster at all."),
             ("Can you line just one wall of a room?", "Yes. We often line only the outside wall or only the TV wall.")],
        rel=["insulation", "repairs", "decor"]),

    "insulation": dict(
        slug="thermal-sound-insulation", ill="skeletos-chorismaton-diadromos", service=True, stype="Thermal and sound insulation with drywall",
        title="Thermal & sound insulation with drywall in Loutraki",
        desc="Thermal and sound insulation with drywall and mineral wool in Loutraki, Corinth and Perachora: walls, ceilings, attics and hotel rooms.",
        h1="Thermal and sound insulation with drywall", short="Insulation", kicker="Heat, cold, noise",
        card="Less noise and lower electricity bills.",
        lead="Noise from the neighbours, cold from the north wall and summer heat under the roof can often be solved from inside, with a drywall frame full of mineral wool. No scaffolding, and the outside of the building does not change.",
        ticks=["Stone wool or glass wool inside the frame", "Acoustic boards and resilient profiles for noise", "Vapour barrier where needed"],
        answer="For noise from the next apartment, the most effective solution is an independent lining with mineral wool and double acoustic board that does not touch the old wall. For cold or heat, insulation goes on the outside walls or on the ceiling under the roof.",
        secs=[
            ("Sound insulation: what really helps", "<p>Sound passes through the wall and through every gap. Good sound insulation has three parts: <b>mass</b> (double or acoustic board), <b>absorption</b> (mineral wool inside the frame) and <b>decoupling</b> (the new wall does not touch the old one, and resilient tape goes at the edges).</p><p>Egg-box foam and thin polystyrene do not insulate against sound. They absorb a little echo inside the room, but do not stop noise from next door.</p>{{ill:monosi}}"),
            ("Thermal insulation from inside", "<p>When external insulation is not possible, for example in an apartment block, insulating from inside is the practical answer. With 5–8 cm of stone wool and drywall, the wall stops feeling cold to the touch and the air conditioner works less.</p><p>On ceilings under a tiled roof or in attics, insulation above the suspended ceiling makes the biggest difference in summer.</p>"),
            ("Damp and vapour barriers", "<p>With insulation on the inside, warm indoor air must not reach the cold wall, or it condenses. Where needed we add a vapour-barrier membrane or boards with a built-in barrier. In Loutraki, with the humidity from the sea, this matters.</p>"),
            ("Sound insulation in hotels and holiday lets", "<p>Guest reviews often mention noise from the next room. A sound-insulating lining on the party wall takes a few days per room, out of season. See the {{k:hotels|hotels}} page.</p>{{ill:ergotaxio-gypsosanides}}"),
        ],
        faq=[("How much noise will it cut?", "It depends on the existing wall and on the gaps. A proper independent lining with double board and mineral wool makes normal conversation next door inaudible. We do not promise total silence from bass-heavy music."),
             ("Stone wool or glass wool?", "Both insulate well. Stone wool is denser, insulates sound better and resists fire longer. Glass wool is lighter and cheaper."),
             ("Can it be done only on the ceiling?", "Yes. For footsteps from the flat above we fit a suspended ceiling on resilient hangers with mineral wool above.")],
        rel=["partitions", "linings", "ceilings"]),

    "bathroom": dict(
        slug="drywall-bathroom-kitchen", ill="kogchi-ntous", service=True, stype="Moisture-resistant drywall in bathrooms and kitchens",
        title="Drywall in bathrooms and kitchens · moisture board, niches",
        desc="Moisture-resistant drywall in bathrooms and kitchens in Loutraki: walls behind tiles, shower niches, boxing for cisterns and pipes, ceilings.",
        h1="Drywall in bathrooms and kitchens", short="Bathrooms & kitchens", kicker="Wet rooms",
        card="Moisture board behind tiles, shower niches, boxing for pipes.",
        lead="In a bathroom, drywall hides pipes and concealed cisterns, creates shampoo niches in the shower and straightens walls before tiling. We use only green moisture-resistant board and waterproof before the tiles go on.",
        ticks=["Moisture-resistant type H board", "Waterproofing with tape at the shower corners", "Reinforcement for wall-hung toilets and vanities"],
        answer="Moisture-resistant board copes with bathroom humidity, but not with running water. That is why in the shower zone we always apply a liquid waterproofing membrane with tape in the corners before tiling, or use cement board for a walk-in shower.",
        secs=[
            ("What we build in a bathroom", "<ul><li>Walls for a concealed cistern and wall-hung toilet, with the steel frame inside.</li><li>Shower niches, with LED lighting if you want.</li><li>Boxing to hide vertical soil pipes.</li><li>A ceiling in moisture board with IP44 or IP65 recessed spots.</li></ul>{{ill:bano}}"),
            ("In the kitchen", "<p>In the kitchen, drywall hides the cooker hood and its duct, closes the space above the cabinets and straightens walls so units fit properly. For wall cabinets we add timber or OSB reinforcement behind the board.</p>"),
            ("Waterproofing before tiling", "<p>Tiles and grout are not waterproof. Water slowly gets through and, if it reaches plain drywall, the board swells. So the order is always: moisture board, primer, two coats of waterproofing with tape in the corners, then tiles. We work with your tiler or suggest one of ours.</p>{{note|If the bathroom has no window, it needs an extractor fan. We plan it in the ceiling with a duct to the outside.}}"),
        ],
        faq=[("Is green drywall waterproof?", "No. It is moisture-resistant, meaning it copes with humid air. In the shower it needs waterproofing on top before tiling."),
             ("Can I tile on drywall?", "Yes, with C2 tile adhesive. For large, heavy tiles we space the studs closer and use double board."),
             ("How long does it take?", "For a 5–6 m² bathroom, the drywall work is done in 2–3 days, before the tiler.")],
        rel=["ceilings", "partitions", "repairs"]),

    "decor": dict(
        slug="hidden-lighting-drywall-features", ill="kogches-rafia-saloni", service=True, stype="Decorative drywall features",
        title="Hidden lighting & drywall features · TV walls, niches, shelves",
        desc="Decorative drywall features in Loutraki: TV walls, shelves, niches, arches, and hidden LED lighting in ceilings and walls.",
        h1="Hidden lighting and drywall features", short="Hidden lighting & features", kicker="Features",
        card="TV walls, shelves, niches and hidden LED lighting.",
        lead="A TV wall with hidden cables, lit niches beside the bed, an arch in the hallway or an LED channel around the whole ceiling. Small builds that completely change how a room looks.",
        ticks=["A dimensioned sketch before we start", "Channels for LED strips and drivers", "Corners with corner bead, straight and durable"],
        answer="We first show you a simple dimensioned sketch, so you know exactly where the light falls and where the cables go. Most living-room features are finished in 2–4 days including filling.",
        secs=[
            ("TV walls", "<p>We build a lining a few centimetres in front of the wall, reinforced where the bracket goes. HDMI, power and network cables run inside and come out right behind the TV. Shelves or lit niches can go on either side.</p>{{ill:diakosmitika}}"),
            ("Hidden lighting in ceilings and walls", "<p>The LED strip sits in a channel that hides it from every point in the room. We size the channel so the light spreads evenly, without dots. We suggest warm white 2700–3000 K for living rooms and bedrooms. See also {{k:ceilings|suspended ceilings}}.</p>"),
            ("Niches, shelves and arches", "<p>Niches beside the bed instead of bedside tables, bookshelves in the hallway, arches in openings and curves in ceilings. For curves we use thin 6.5 mm flexible board.</p>"),
        ],
        faq=[("Who does the electrics?", "Your electrician or ours. We leave the channels and openings where we agreed."),
             ("Can a drywall shelf take weight?", "A drywall shelf holds ornaments and a few books. For heavy loads we put a timber or steel core inside."),
             ("Can you build something from a photo I liked?", "Yes, send us the photo on WhatsApp and we will tell you whether and how it works in your space.")],
        rel=["ceilings", "linings", "cost"]),

    "hotels": dict(
        slug="hotels-shops-drywall", ill="diadromos-xenodocheiou", service=True, stype="Dry construction for hotels and shops",
        title="Drywall for hotels and shops in Loutraki",
        desc="Dry construction for hotels, holiday lets, shops and offices in Loutraki: off-season renovations, fire-rated and sound-insulating systems.",
        h1="Drywall for hotels and shops", short="Hotels & shops", kicker="Commercial spaces",
        card="Off-season renovations, scheduled floor by floor.",
        lead="Loutraki lives on tourism, and every winter hotels and rental rooms are renovated to be ready before Easter. We work to a schedule per floor or per room, so the business knows in advance when each space closes and reopens.",
        ticks=["Suspended ceilings with hatches for AC and fire detection", "Fire-rated partitions and linings in corridors", "Sound insulation between rooms"],
        answer="For hotels we visit every room, quote per room type and give a schedule per floor. Where fire protection is required, we use certified manufacturer systems as specified in your engineer's fire-safety study.",
        secs=[
            ("Hotels and rental rooms", "<p>The most common jobs are new ceilings in rooms and corridors, sound insulation on party walls, boxing for new pipework and linings in bathrooms before new tiles. We work from November to March, and in operating hotels if needed, keeping noise down during quiet hours.</p>{{ill:xenodocheia}}"),
            ("Shops, restaurants and offices", "<p>In a shop on the seafront or in the main market, time is money. Dry construction lets the layout change in a few days: new fitting rooms, counters, a lit ceiling, partitions for a storeroom or office.</p>"),
            ("Fire protection", "<p>Stairwells, escape corridors and plant rooms often require a fire rating such as EI 60 or EI 90. We achieve it with type F fire-resistant boards and a system tested by the manufacturer, built exactly as described in the system sheet.</p>{{note|Fire protection is specified by an engineer's study. We build the system the study calls for and keep photos of every stage for the file.}}"),
            ("Scheduling and invoicing", "<p>For commercial spaces we give a price per square metre or per room, a schedule, and an invoice. We coordinate with your engineer, electrician and HVAC technician so each trade knows when it comes in.</p>{{ill:orofi-gypsosanida-ktirio}}"),
        ],
        faq=[("Do you work while the hotel is open?", "Yes, in sections that close temporarily, and we schedule noisy work at times that do not disturb guests."),
             ("Do you issue invoices?", "Yes, for all work."),
             ("How early should we book for the winter?", "The earlier the better. The schedule fills up in autumn, so for January–March work it is best to talk by October.")],
        rel=["insulation", "ceilings", "partitions"]),

    "repairs": dict(
        slug="drywall-repairs", ill="stokarisma-armon", service=True, stype="Drywall repair",
        title="Drywall repairs in Loutraki · holes, cracks, water damage",
        desc="Drywall repairs in Loutraki, Corinth and Perachora: holes, cracked joints, water damage, access hatches. Quick appointments.",
        h1="Drywall repairs", short="Repairs", kicker="Small jobs",
        card="Holes, cracked joints, water damage.",
        lead="A hole from a door handle, a joint that opened in the ceiling, a section that swelled after a leak. Small drywall damage is fixed quickly and disappears after painting, as long as it is done properly.",
        ticks=["Replacing swollen sections after a leak", "Cracked joints re-taped", "Access hatches where missing"],
        answer="Small repairs usually take two visits: on day one we cut out, fit a new piece and apply the first filler, and on day two we finish. If the damage is from water, we first make sure the leak has stopped.",
        secs=[
            ("Holes and breakage", "<p>We cut the damaged part into a clean rectangle, add a backing support, screw in a new piece of the same thickness and apply tape and filler. After sanding and painting, the repair cannot be seen.</p>{{ill:episkeves}}"),
            ("Cracked joints", "<p>If joints keep opening, tape is usually missing or the frame moves. We open the joint, check the screws and hangers, and redo it with fibreglass or paper tape.</p>{{ill:tavani-me-tainies-stoko}}"),
            ("Water damage", "<p>Drywall that got wet swells and softens. It does not dry back properly, so we replace it. We also check the insulation behind, which often needs replacing too. If needed, we coordinate with your plumber.</p>"),
        ],
        faq=[("Do you come for small jobs?", "Yes. We often group them with other work in the same area so we can come sooner."),
             ("Will the repair show?", "After sanding and painting the whole wall, no. If only the patch is painted, the colour may differ slightly."),
             ("Do you repair other crews' drywall?", "Yes, we look at what is wrong and tell you whether a repair is enough or a section needs redoing.")],
        rel=["linings", "ceilings", "bathroom"]),

    "areas": dict(
        slug="areas", ill="chartis-perioxis",
        title="Areas · Drywall in Loutraki, Corinth, Perachora",
        desc="Drywall installation in Loutraki, Corinth and Perachora, including Pisia and Lake Vouliagmeni. Free site visit.",
        h1="Loutraki, Corinth and Perachora", short="Areas", kicker="Loutraki and around",
        card="Loutraki, Corinth and Perachora.",
        lead="We are based in Loutraki. We work in town, in Corinth and in Perachora, including Pisia and Lake Vouliagmeni. All of them are a few minutes away.",
        ticks=["Free site visit", "Same prices in Loutraki, Corinth and Perachora", "For longer distances, ask us"],
        answer="We cover Loutraki, Corinth and Perachora. For work in another area, ask us: for larger projects we may travel.",
        secs=[
            ("Loutraki", "<p>Apartments in town blocks, holiday homes, rental rooms and seafront hotels. Much of our work here is renovation before the summer season: {{k:partitions|partitions}} to turn a studio into a one-bedroom flat, {{k:ceilings|suspended ceilings}} with hidden lighting and {{k:insulation|sound insulation}} between rooms.</p>"),
            ("Perachora, Pisia and Lake Vouliagmeni", "<p>Detached and holiday houses, often older, with walls that need {{k:linings|lining}} and ceilings under tiled roofs that need insulation. In houses near the sea we pay special attention to damp.</p>"),
            ("Corinth", "<p>Homes, offices and shops in the city of Corinth. Here we often do {{k:hotels|commercial spaces}}: shops, clinics and offices that change layout.</p>{{ill:chartis-perioxis}}"),
        ],
        rel=["ceilings", "partitions", "contact"]),

    "cost": dict(
        slug="drywall-cost", ill="tavani-me-tainies-stoko",
        title="Drywall cost: what raises and what lowers the price",
        desc="What drives the cost of drywall ceilings, partitions and linings: board type, insulation, height, design, finish level. Written quote after measuring.",
        h1="What drives the cost of drywall", short="Cost", kicker="Prices",
        card="Board, insulation, height, design and finish: what changes the price.",
        lead="Drywall is usually priced per square metre, but two square metres do not always cost the same. Here we explain what raises the price and what you can do to keep it down without spoiling the result.",
        answer="The biggest factors are the design (flat, or with steps and curves), the number of boards per side, insulation and the finish level. Our written quote lists every item separately, so you see what you are paying for.",
        secs=[
            ("What raises the price", "<div class=\"tw\"><table><tr><th>Factor</th><th>Why it matters</th></tr>"
             "<tr><td>Design</td><td>A flat suspended ceiling is the cheapest. Steps, LED channels, curves and niches need more framing and much more labour.</td></tr>"
             "<tr><td>Board type</td><td>Moisture-resistant, fire-resistant and acoustic boards cost more than standard board.</td></tr>"
             "<tr><td>Layers</td><td>Double board per side means twice the material and more screws, but much better sound insulation and strength.</td></tr>"
             "<tr><td>Insulation</td><td>Mineral wool is added per m², depending on thickness and density.</td></tr>"
             "<tr><td>Height</td><td>Above 3 metres you need scaffolding and more time.</td></tr>"
             "<tr><td>Finish</td><td>Level Q2 is enough for matt paint. Q4, with filler over the whole surface, is needed for grazing light and glossy paints.</td></tr>"
             "<tr><td>Access</td><td>A third floor with no lift or a narrow stairwell add time for carrying materials.</td></tr></table></div>"),
            ("How to keep the cost down", "<ul><li>Group all drywall work into one phase, so the crew does not come back several times.</li><li>Decide in advance where lights, sockets and cabinets go, to avoid cutting openings later.</li><li>Keep hidden lighting where it will really be seen, for example in the living room.</li><li>Ask for Q2 where there is no grazing light.</li></ul>"),
            ("What our quote includes", "<p>Materials (framing, boards, insulation, screws, tape, corner beads, filler), labour, transport of materials and cleaning. Anything optional, such as hidden lighting, access hatches or painting, is listed separately. No hidden charges at the end.</p>{{cta}}"),
            ("How to get a price quickly", "<p>Send us a few photos of the space on WhatsApp, rough dimensions and what you want done. We give you an indicative price on the phone and book a site visit for the final, written quote.</p>"),
        ],
        faq=[("Why don't you publish a price per m²?", "Because the same ceiling can cost very differently depending on design, height and finish. A price without measuring would be misleading. An indicative price from photos is free."),
             ("Is the site visit charged?", "No, the site visit and written quote are free in Loutraki, Corinth and Perachora."),
             ("How is payment made?", "Usually a deposit for materials and the balance on completion. For large projects, by stage.")],
        rel=["ceilings", "partitions", "insulation"]),

    "faq": dict(
        slug="faq", ill="ergotaxio-gypsosanides",
        title="Drywall FAQ · Gypsos Loutraki",
        desc="Answers about drywall: strength, damp, earthquakes, sound insulation, timing, permits and what to do before the crew arrives.",
        h1="Frequently asked questions about drywall", short="FAQ", kicker="Questions",
        card="Strength, damp, earthquakes, timing, permits.",
        lead="The questions we hear most often at site visits, with short and honest answers. If yours is not here, send us a message.",
        answer="Drywall is a proven material for interiors: light, fast and clean. It needs the right board for each room and a proper frame, and then it lasts as long as a built wall.",
        secs=[
            ("Strength and safety", "<p><b>Is drywall strong?</b> A wall with a proper frame and double board stands up to normal household use, wall cabinets with reinforcement and knocks from furniture. For busy spaces there are high-hardness boards.</p>{{ill:hero-saloni}}<p><b>How does it behave in an earthquake?</b> Because it is light, it loads the building less than a brick wall, and the metal frame absorbs small movements.</p><p><b>Does it burn?</b> Gypsum contains water and slows fire down. Type F fire-resistant boards are used where a study calls for a specific fire rating.</p>"),
            ("Damp", "<p>In wet rooms we use moisture-resistant board and waterproofing under the tiles. On walls with active damp we do not install drywall until the problem is solved. See {{k:bathroom|bathrooms and kitchens}}.</p>"),
            ("Timing and organisation", "<p><b>How long does the work take?</b> A partition 1–2 days, a living-room ceiling 2–3 days, then 1–2 days for filling. A whole apartment usually 5–10 working days.</p><p><b>What should I do before you come?</b> Clear the space as far as possible and decide where lights and sockets will go. We take care of the rest, including floor protection and cleaning.</p>"),
            ("Permits and apartment blocks", "<p>Interior layout changes in drywall, without touching the load-bearing structure, usually need a small-scale works approval or no permit at all. Every case is different, so ask your engineer. In an apartment block, let the building manager know the working hours.</p>"),
        ],
        faq=HOME_FAQ, rel=["cost", "areas", "contact"]),

    "contact": dict(
        slug="contact", ill="saloni-kryfos-fotismos",
        title="Contact · Gypsos Loutraki · phone & WhatsApp",
        desc="Contact us about drywall in Loutraki, Corinth and Perachora: phone, WhatsApp, Viber, email. Free site visit and written quote. We speak English.",
        h1="Contact", short="Contact", kicker="Talk to us",
        card="Phone, WhatsApp, Viber and email.",
        lead="The fastest way is a WhatsApp or Viber message with photos of the space. You can also call us or fill in the form at the bottom of the page.",
        ticks=["Phone, WhatsApp and Viber: +30 690 683 8669", "Monday to Saturday, 8:00–19:00", "Loutraki, Corinth and Perachora"],
        answer="Phone, WhatsApp and Viber: <a href=\"tel:+306906838669\">+30 690 683 8669</a>. We reply to messages the same day.",
        secs=[
            ("What to send us", "<ul><li>2–4 photos of the space from different angles.</li><li>Rough dimensions and ceiling height.</li><li>What you want done: ceiling, partition, lining, insulation.</li><li>The area and when you would like the work to start.</li></ul>"),
            ("Hours", "<p>Monday to Saturday, 8:00–19:00. On Sundays we reply to messages but do not work in homes.</p>"),
        ],
        rel=["cost", "areas", "faq"]),

    "privacy": dict(
        slug="privacy", ill="orofi-gypsosanida-ktirio", noindex=True, no_form=True,
        title="Privacy policy · Gypsos Loutraki",
        desc="How we use the details you send us through the form, phone, WhatsApp and email. We do not use tracking cookies.",
        h1="Privacy policy", short="Privacy", kicker="Privacy",
        lead="Short and simple: what details we keep, why and for how long.",
        secs=[
            ("What we collect", "<p>When you fill in the form, we receive by email your name, phone, area, type of work and message, and the page you sent it from. If you write to us on WhatsApp, Viber or by email, we have whatever you sent there.</p>"),
            ("Why we use it", "<p>Only to reply to you, arrange a site visit and send you a quote. We do not pass it to third parties and do not send marketing messages.</p>"),
            ("Cookies", "<p>This site does not use tracking or advertising cookies. Fonts are loaded from Google Fonts.</p>"),
            ("Photos", "<p id=\"photos\">The photos on this site come from Unsplash and are used under the Unsplash License. They show the kinds of work we do and are not projects by our crew. The drawings are our own.</p>"),
            ("Your rights", "<p>You can ask to see, correct or delete your details with a message to the phone or email at the bottom of the page.</p>"),
        ]),
}

NOT_FOUND = dict(
    title="Page not found · Gypsos Loutraki", desc="The page you asked for does not exist.", h1="Page not found",
    ill="episkeves",
    body="""<section class="intro"><div class="w" style="padding:40px 0"><p class="eyebrow">404</p><h1>This page does not exist</h1>
<p class="lead">It may have moved. Try the <a href="/en/">home page</a> or call us on <a href="tel:+306906838669">+30 690 683 8669</a>.</p></div></section>""")
