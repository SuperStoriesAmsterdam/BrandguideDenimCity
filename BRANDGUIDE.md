# Denim City AMS — Brand Guide

> Connecting the next generation with the forefront of the denim world towards a brighter blue.

---

## 01 Design System

### Spacing scale

Base unit: 8px. Every spacing value is a multiple of this base. No arbitrary values.

| Token     | Value  | Use                                        |
|-----------|--------|--------------------------------------------|
| `--sp-1`  | 8px    | Icon gaps, inline padding, tag padding     |
| `--sp-2`  | 16px   | Between related text elements              |
| `--sp-3`  | 24px   | Between components within a block          |
| `--sp-4`  | 32px   | Card/cell internal padding                 |
| `--sp-5`  | 48px   | Between content blocks                     |
| `--sp-6`  | 64px   | Between sections                           |
| `--sp-7`  | 96px   | Major section breaks, hero padding         |
| `--sp-8`  | 128px  | Page-level top padding                     |

### Type scale

| Token              | Size                        | Font           | Weight | Case       | Use                                      |
|--------------------|-----------------------------|----------------|--------|------------|------------------------------------------|
| `--type-display`   | clamp(72px, 10vw, 128px)    | Topol Bold     | 700    | UPPERCASE  | Wordmark, logotype only                  |
| `--type-headline`  | clamp(36px, 6vw, 80px)      | Topol Bold     | 700    | UPPERCASE  | Homepage section headlines               |
| `--type-numeric`   | clamp(48px, 7vw, 96px)      | Topol Bold     | 700    | —          | Statistics, large numbers                |
| `--type-h1`        | clamp(28px, 4vw, 48px)      | Topol Bold     | 700    | Sentence   | Inner page titles                        |
| `--type-h2`        | 24px                        | Topol Bold     | 700    | Sentence   | Subsection headings                      |
| `--type-h3`        | 18px                        | Apercu Pro     | 700    | Sentence   | Card titles, block headers               |
| `--type-intro`     | 20px                        | Apercu Pro     | 400    | Sentence   | Lead paragraphs, intro text              |
| `--type-body`      | 16px                        | Apercu Pro     | 400    | Sentence   | Body text                                |
| `--type-small`     | 14px                        | Apercu Pro     | 400    | Sentence   | Captions, secondary descriptions         |
| `--type-label`     | 11px                        | Apercu Mono    | 400    | UPPERCASE  | Category labels, metadata, navigation    |
| `--type-streamer`  | clamp(28px, 4vw, 56px)      | Apercu Pro     | mixed  | UPPERCASE  | Editorial pull quotes (Bold + Italic mix)|

Line height defaults: display/headline 0.9, h1/h2 1.1, body 1.6, label 1.2
Letter spacing: label +0.08em, headline -0.01em, display -0.02em

### Color system

| Token       | Hex       | Name          | Use                                          |
|-------------|-----------|---------------|----------------------------------------------|
| `--bg`      | #FFE0DB   | DC Pink       | Page background — always, never white        |
| `--surface` | #F5D0CB   | DC Surface    | Cards, hover states, elevated surfaces       |
| `--primary` | #0000A5   | DC Blue       | Text, borders, structural elements           |
| `--accent`  | #FF2B2B   | AMS Red       | Location name (AMS), links, emphasis         |
| `--white`   | #FFFFFF   | White         | Inverse text on dark surfaces only           |
| `--muted`   | #0000A540 | DC Blue 25%   | Disabled states, ghost elements, decorative  |
| `--border`  | #0000A5   | DC Blue       | Grid lines, card borders — always 1px        |

Color rules:
- Background is always `--bg`. Never white as page background.
- `--accent` (AMS Red) is the location identifier. Used sparingly — AMS in wordmark, active states, one emphasis per block maximum.
- The blue gradient system (Electric, Digital, Light) exists for campaign materials. Not used in the web interface.

---

## 02 Typography System

### Fonts

**Topol Bold** (`fonts/Topol-Bold.woff2`)
The structural font. Narrow, heavy, confident. Designed by Filip Matejicek.
Used for: wordmark, homepage headlines, statistics, page titles (sentence case on inner pages).
Only one weight available (Bold). Hierarchy is created through size and case, not weight variation.

**Apercu Pro** (`fonts/Apercu-Pro-Regular.woff2`, `Apercu-Pro-Bold.woff2`, `Apercu-Pro-Italic.woff2`)
The reading font. Web adaptation not in the 2018 original — added for legibility at small sizes.
Used for: body text, intro text, card descriptions, the italic/bold mix in editorial streamers.
Italic weight is used for the streamer treatment on the homepage.

**Apercu Mono** (`fonts/Apercu-Mono.woff2`)
The information font. Mono-spaced, precise, functional.
Used for: category labels, metadata, navigation items, vertical spatial labels.
Always uppercase. Always tracked out (+0.08em minimum).

### The two typographic modes

#### Homepage mode — expressive

The homepage operates as a magazine. Typography creates tension through contrast.

Headline treatment:
- Section headlines: Topol Bold, ALL CAPS, large (`--type-headline`)
- No periods after headlines

Streamer treatment (editorial pull quotes):
- Mix of Apercu Pro Bold Italic + Apercu Pro Regular Italic in the same line
- The bold/italic switch mid-sentence is the voice — emphasis lands on specific words
- ALL CAPS
- Example: *INSIDE AMSTERDAM'S DENIM* **INNOVATION HUB** *WHERE MATERIAL LITERACY REPLACES* **SUSTAINABILITY** *AS THE APPETITE*

Category labels:
- Apercu Mono, small, uppercase, tracked — always above the headline
- Example: `EDUCATION` above `MAKE YOUR OWN JEANS`

Body text on homepage:
- Apercu Pro Regular, sentence case — this is where lowercase is introduced
- The coexistence of uppercase headlines and lowercase body on the homepage is intentional
- It prepares the reader for the predominantly lowercase inner pages

Statistics:
- Topol Bold, very large (`--type-numeric`)
- Small Apercu Mono label below: `OF VISITORS WHO FIND US, BOOK`

Vertical labels:
- Apercu Mono, rotated 90° counterclockwise, left edge of grid cells
- Example: `EXPLORE`

Navigation:
- Apercu Mono, uppercase, small — not Apercu Pro
- Active item has `→` prefix in accent color

Grid:
- Full-width grid divided by 1px `--border` lines
- Cells contain one content type each
- No internal margin on cell edges — content sits against the border

#### Inner page mode — functional

Inner pages prioritize reading over expression. The typographic complexity of the homepage is absent.

Headlines: Topol Bold, sentence case (`--type-h1`) — not ALL CAPS
Subheads: Apercu Pro Bold, sentence case (`--type-h2` or `--type-h3`)
Body: Apercu Pro Regular, sentence case — dominant voice
Labels: Apercu Mono, uppercase — retained but used only for genuine metadata

No streamer treatment on inner pages.
No large numerics unless they carry content meaning.
No vertical text unless used for navigation wayfinding.

The agenda/list pattern from the Additional reference:
- Rows divided by 1px border lines
- Category label left (Apercu Mono), content right (Apercu Pro)
- Dates in Apercu Mono, event name in Apercu Pro Regular or Bold
- Generous row height — minimum 48px (`--sp-5`)

### Typography rule summary

| Element              | Font         | Weight  | Case      | Mode        |
|----------------------|--------------|---------|-----------|-------------|
| Wordmark             | Topol Bold   | 700     | UPPERCASE | Both        |
| Homepage headline    | Topol Bold   | 700     | UPPERCASE | Home only   |
| Streamer             | Apercu Pro   | 700+400 | UPPERCASE | Home only   |
| Statistics           | Topol Bold   | 700     | —         | Home only   |
| Inner page title     | Topol Bold   | 700     | Sentence  | Inner only  |
| Subheading           | Apercu Pro   | 700     | Sentence  | Inner only  |
| Body                 | Apercu Pro   | 400     | Sentence  | Both        |
| Category label       | Apercu Mono  | 400     | UPPERCASE | Both        |
| Navigation           | Apercu Mono  | 400     | UPPERCASE | Both        |
| Vertical label       | Apercu Mono  | 400     | UPPERCASE | Home only   |

---

## 03 Logo System

The logo is a communication device, not just a wordmark.

**Always two lines:**
```
DENIM
CITY AMS
```

**Three information layers (from original system):**
- Line 1–2: Brand (Topol Bold) + Location (Apercu Mono, same cap-height as Topol)
- Line 3: Area or Activity (Topol Bold, slightly smaller)
- Line 4: Detail (Apercu Mono, smaller)

**Color rules:**
- `DENIM CITY` always in `--primary` (DC Blue) or white on dark backgrounds
- `AMS` always in `--accent` (AMS Red) — the location has its own color
- On the pink background: blue wordmark, red AMS
- On dark blue background: white wordmark, red AMS

**What not to do:**
- Never distort or alter proportions
- Never use AMS in blue — the red is the location identifier
- No periods after wordmark elements

---

## 04 Color Rules

The background is always `--bg` (#FFE0DB). This is not a design choice — it is the brand.

AMS Red is used for:
1. The AMS location identifier in the wordmark
2. Maximum one emphasis per content block
3. Active navigation states

Blue borders (1px) define all structural divisions. Never use shadow or rounded corners for structure.

---

## 05 Layout Principles

**Grid:** full-width cells divided by 1px borders. No gutters between cells.

**Cell types:**
- Text cell: padding `--sp-4` on all sides
- Image cell: image fills 100% of cell, no padding
- Mixed cell: image right half, text left half with `--sp-4` padding

**Navigation:** fixed top, height 56px, `--bg` background, 1px bottom border. Logo left, nav links right (Apercu Mono).

**Max content width:** 1440px on brandguide pages. Full bleed on homepage grid.

---

## 06 Design Principles

**Specific, not generic**
Every choice has a reason. If you can swap the brand name and the text still works, it is not specific enough.

**Uppercase holds structure, lowercase carries meaning**
ALL CAPS creates tension and marks the skeleton. Sentence case is where information lives. Both must be present. The homepage introduces lowercase through body text. Inner pages expand it.

**Pink, never white**
The background is always #FFE0DB. White exists only as text color on dark surfaces and as image frames.

**The border is the system**
1px DC Blue borders divide everything. No shadows. No cards with border-radius. Structure is visible.

**Strictly offline**
The brand drives people to the physical space in De Hallen. Digital materials create urgency for the real experience.

---

## 07 Voice and Tone

Short. Direct. No corporate padding.

Topol headlines: punchy, active, declarative — but not shouting. The size does the emphasis.
Body copy: specific, factual, first-person plural where appropriate. "We" not "Denim City".
Labels: purely functional. They orient, not describe.

Do: "Make your own jeans"
Do: "The only denim laundry lab in the Netherlands"
Don't: "Explore our world-class educational offerings"
Don't: Periods after headlines

---

## 08 Assets

### Fonts in use
```
fonts/Topol-Bold.woff2           — display, headlines, wordmark
fonts/Apercu-Pro-Regular.woff2   — body text
fonts/Apercu-Pro-Bold.woff2      — subheads, bold body
fonts/Apercu-Pro-Italic.woff2    — streamer italic voice
fonts/Apercu-Pro-Bold-Italic.woff2 — streamer bold italic voice
fonts/Apercu-Mono.woff2          — labels, metadata, navigation
```

Note: Only Topol Bold is available. No Topol Regular or Topol Italic. Hierarchy within Topol is achieved through size and case only.

### File naming
- Fonts: `{family}-{weight}.woff2`
- Images: `{context}-{subject}-{number}.{ext}`
- Icons: `icon-{name}.svg`

### Image direction
Photography shows the physical reality of the space: fabric, machines, people at work, the store interior. Never staged lifestyle. The rawness of the workshop is the aesthetic.
