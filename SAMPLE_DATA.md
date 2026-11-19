# Sample Data for Testing

Put your own files here. Everything under `samples/` is git-ignored.

```
Map Photos/
├── samples/
│   ├── pdf/      site plan PDFs
│   └── photos/   jpg / jpeg / png photos
└── index.html    open directly in Chrome or Edge, no server
```

## Try it

1. **Load PDF** (the plan fits the window; use 🔍 +/− and Pan to move around).
2. **Draw regions** with Polyline (double-click to close) or Box, then name each one.
3. **Load Photos**. They sort by time taken (EXIF) and show a 📍 if they have GPS.
4. **Drag a photo anywhere on the plan.** It does not need to be inside a region. If it lands inside one, its card shows the region name.
5. **Hover** a photo (on the plan or in the list) for a larger view with time, GPS and camera.
6. Drag a placed photo to move it; double-click to take it off the plan.
7. **⬇️ Download PDF** saves `<plan>_photos_<date-time>.pdf` with the photos embedded where you put them.

The ⚙️ panel has a slider for photo size on the plan.

## Markup: notes, arrows, revision clouds

Three tools under the region tools. Click the tool, then use the plan:

- **Text note**: click, type, Ctrl+Enter.
- **Arrow**: drag from tail to point.
- **Revision cloud**: drag a rectangle.

They are listed under **Markup** (Edit a note, Delete, Clear all), are saved in the project JSON (`annotations[]`), and are drawn into the downloaded PDF.

## Sample project

`sample-project/` holds a Hollywood Bowl plan, a project JSON with regions and markup, and a `photos/` folder for your own pictures. Step-by-step instructions are in `sample-project/README.md`.

## Downloading the photos

**🖼️ Download photos (n)** saves every photo you have placed on the plan, renamed by where it sits:

- `Building_A-Admin_01.jpg`, `Building_A-Admin_02.jpg`, … The number counts up by **time taken** within each region. Illegal file-name characters in a region name become `-` and spaces become `_`.
- Photos on the plan but outside every region are `NoRegion_01`, `NoRegion_02`, …
- Photos not yet placed are left out. JPG and PNG files are saved untouched; HEIC photos are saved as the converted JPEG.
- A `_manifest.csv` comes with them: new name, original name and path, region, time taken, GPS and position on the plan.
- In Chrome/Edge you choose a folder and a new `<plan>_photos_<date-time>` sub-folder is created inside it. In other browsers (or from ⚙️ Settings, "Download renamed photos as a ZIP") you get one ZIP.

## Saving your work

- **💾 Save JSON** writes a small `<plan>.mapphotos.json` that *lists* the plan and photos (names, paths, dates, import batches, EXIF time/GPS/camera, regions, where each photo sits, photo size). It holds no pixels. In Chrome/Edge it opens a Save dialog at the Desktop the first time and then overwrites the same file.
- **📂 Open JSON** reads it, then asks you to **choose the folder** that holds the plan and photos (sub-folders are searched). Anything it can't find stays on the plan as a "file missing" tile; **🔗 Link files** lets you supply it later.
- Keep the plan and photos where you can find them again; the JSON does not copy them.
- The format is documented in `templates/project.fields.md` with an example in `templates/project.template.json`.
- The page also **auto-saves to this browser** (including the pixels), so after a refresh the start screen offers "Resume". Turn this off or clear the copy in ⚙️ Settings.
- Real project JSONs are git-ignored (`*.mapphotos.json`).

## Photo size

Open **⚙️ Settings** (toolbar, or the round button at the bottom right) and slide **Photo size**. Every photo on the plan changes together, live. Reset goes back to 5%.

## If a save doesn't seem to work

The toolbar line next to **⚙️ Settings** always says what happened: `✓ Saved …` (written and read back to confirm), `⚠ Save cancelled. Nothing was written.`, or `⚠ Could not write with the save dialog (reason). Downloaded … instead.` Failures fall back to a normal download, so nothing is lost. It also shows `unsaved changes` after you edit.

If the dialogs are troublesome (for example a folder that is being synced), tick **Always use plain browser downloads** in ⚙️ Settings, or use **Download JSON (Downloads folder, no dialog)** / **Download renamed photos as a ZIP**.

## Hosting on GitHub Pages

Works as-is: everything is static, uses relative paths (`libs/…`), loads nothing from other sites, and Pages is HTTPS, so the save/folder dialogs are available. Checked by serving it from a sub-path and exercising PDF, HEIC, exports and Resume.

- Publish `index.html`, `libs/` and `archive-draft/` (the stylesheet and its self-hosted fonts; the `templates/` folder is optional). Never commit `samples/` or real project JSONs (git-ignored here).
- Best in a **separate repo** for this app (the seed-project convention), so Pages doesn't publish the rest of this workspace.
- Free GitHub Pages sites are public. The app code is public, but plan and photos never leave your device.
- Chrome and Edge get the Desktop save dialog and folder picker. Safari and Firefox fall back to downloads (JSON to Downloads, photos as a ZIP); "Load a folder" may not work on iPad.
- The browser auto-save is per site, so a hosted copy does not see what a locally opened copy saved. Use Save JSON / Open JSON to move between them.

## Notes

- iPhone HEIC/HEIF photos are converted to JPEG when loaded (a few seconds each). Time taken, GPS and camera are read from the HEIC.
- Download PDF is separate from Save: it gives a flat PDF to open in Bluebeam, not something you reload here.
