# Map Photos — Convo v1

**Date Started:** 2026-11-18

---

## Clarifying Questions

**Q: Scope & Tech Stack**
- Will this be a web app (HTML/CSS/JS) or a desktop app?
- Should it support PDF editing client-side, or just overlaying images onto a displayed PDF?
- Any preference for libraries (pdf.js, pdfkit, etc.) or pure vanilla?

- I'd like this to be a web app. Ideally, it's a static page with everything on local machine. It should support basic PDF editing. Once done, the new PDF file will be saved and opened up in Bluebeam for further manual endits. If not, then desktop.

**Q: MVP Definition**
- For the first MVP, should we focus on steps 0–1 (PDF viewer + region labeling + markup tools)?
- Or include photo loading and dragging (steps 2)?
    - It should work for all steps. Create folders and I'll drop some samples in.

**Q: Image & PDF Handling**
- Photos: EXIF extraction — do you want to use a library (exif.js) or manual metadata parsing?
    - automatic
- PDF output: should the final PDF be editable/reloadable, or is a one-way export acceptable?
    - PDF output - should be viewable, and then allow one way export is fine.

**Q: Offline & Data Storage**
- Should the JSON linkage file be downloadable (for reloading)? - yes
- Local storage for the current session only, or persistent localStorage? - for current session only

**Q: Regions & Filtering**
- When you say "identify regions (Building X: Building Name)" — is this manual drawing (like text labels + bounding boxes) or should regions be pre-defined?
    - manual drawing bounding boxes or closed polylines, manual text to ID
- Filter on the right panel — dropdown list of regions, checkboxes, or a visual selector?
    - check boxes
---

## Answers

(Jimmy's responses will be recorded here as we clarify.)
