# Map Photos — To-do (reviewed 2026-11-18 against schematic.md)

Legend: [x] built and checked in headless Edge · [ ] not built · [?] built, needs Jimmy's real files

## Step 0: Homepage
- [ ] Homepage with basic instructions (only a "Load a PDF" hint exists)

## Step 1: Site plan viewer + regions
- [x] Load PDF, zoom in/out, Fit, Pan (drag to scroll)
- [x] Regions: polyline (double-click to close) and box (any drag direction), text label
- [x] Regions stay put when zooming (stored in plan units)
- [x] Save-as with time suffix: Download PDF gives `<name>_photos_YYYYMMDD-HHMMSS.pdf`
- [ ] Notes (text) tool
- [ ] Arrow tool
- [ ] Cloud tool
- [ ] Multi-page PDFs (page navigation; only page 1 is used)
- [ ] Rotated PDF pages (export refuses with a message)

## Step 2: Photos
- [x] Load jpg / jpeg / png in batches; same file can be re-added
- [x] EXIF: time taken, GPS, camera; shown on card (time, pin) and in hover popup; "(file date)" when no EXIF time
- [x] Chronological order
- [x] Small thumbnails in the side panel
- [x] Drag a photo anywhere on the plan (no region needed); drag the marker to move; double-click to remove
- [x] Marker size scales with zoom; ⚙️ Settings (toolbar button or corner gear) has a live size slider for all photos, even after they are placed, plus Reset. Saved in the project JSON
- [x] Load a folder of photos (keeps relative paths) as well as individual files; each load is recorded as an import batch
- [x] Region tag comes from where the photo sits (shown as the region name, "on plan", or "not placed")
- [x] Region filter checkboxes hide cards and plan markers
- [ ] View-angle arrow on a photo (toggleable)
- [x] HEIC/HEIF: converted to JPEG in the page (heic2any); time, GPS and camera are read from the HEIC itself
- [?] HEIC from a real iPhone (Live Photos, HDR, very large files) and conversion speed with 100+ photos
- [?] Real phone photos: orientation, EXIF on large files, performance with 100+ photos

## Step 3: Hover and linkage
- [x] Hover (~0.25 s) shows an enlarged photo with metadata
- [ ] Zoom further inside the hover popup
- [x] 💾 Save JSON: one small `.mapphotos.json` listing the plan and photos by name/path/size/dates, import batches, EXIF time/GPS/camera, regions, positions and photo size. No pixels. Chrome/Edge open a Save dialog at the Desktop and later saves overwrite the same file; other browsers download it
- [x] 📂 Open JSON + link dialog: choose the folder (or files); matched by path, then name+size, then unique name. Works in a fresh browser profile
- [x] Missing photos stay on the plan as "file missing" tiles; 🔗 Link files supplies them later
- [x] Template and field guide: `templates/project.template.json`, `templates/project.fields.md`
- [x] Auto-save to the browser's local cache (keeps the pixels so Resume needs no linking); "Resume" offered on the next visit; switch off or clear in Settings
- [x] Every save/export reports its result in the toolbar: verified (read back), cancelled, or failed with the reason and an automatic download fallback; "unsaved changes" flag; Settings switch for plain downloads
- [?] The real Save/folder dialogs on Jimmy's machine: tested with real file handles (browser private file system) plus failure cases, but the earlier "didn't save" report was never reproduced. Ask what the status line says next time
- [x] Works over http(s) from a sub-path (GitHub Pages style): real PDF worker, HEIC, exports, Resume
- [?] Safari/iPad and Firefox (fallback downloads only), "Load a folder" on iPad
- [ ] Publish: own repo + GitHub Pages (index.html + libs/)
- [ ] Browsers hide real disk paths, so `path` is a name or folder-relative path. If you want true absolute paths in the JSON, they would have to be typed in or the app moved to a desktop shell
- [ ] Warn when a linked file's size differs from the JSON (file edited since)

## Step 4: PDF with photos
- [x] Download PDF with photos embedded at their locations, plus region outlines/labels and a "Region | time" caption
- [x] Round-trip checked: exported PDF reopens with 3 images in the right place
- [ ] Option for full-size photos (currently re-encoded to max 1600 px to keep the file a sensible size)
- [x] 🖼️ Download photos: every photo on the plan, renamed `RegionName_##` (numbered by time taken within each region; `NoRegion_##` outside any region), plus `_manifest.csv` mapping new name to original name, region, time, GPS and plan position. Chrome/Edge: pick a folder (a new timestamped sub-folder is made, nothing overwritten); otherwise, or via Settings, a ZIP
- [?] HEIC photos download as the converted JPEG (EXIF is not carried into the JPEG; the manifest keeps time/GPS)
- [?] Open exported PDF in Bluebeam and confirm it edits cleanly

## Design
- [x] Restyled to ARCHIVE / DRAFT v1.0: paper/ink palette, IBM Plex Mono + Newsreader + Barlow Condensed (self-hosted), square 1px-border controls, Lucide line icons (1.5px) instead of emoji, header title block / tool rail / inspector / status footer layout
- [x] Reusable `archive-draft/` folder (CSS tokens + components + fonts) to copy into other sites
- [?] Touch size: buttons are 32px and tool buttons 38px per the system, below the 48px touch targets used for kids' iPad apps. Check on the iPad; bump `--btn-h`/tool size there if needed
- [ ] PDF export still uses Helvetica for labels and captions (could embed IBM Plex Mono)
- [ ] Custom icons (French curve etc.) not needed yet; Lucide only

## Housekeeping
- [x] pdf.js, pdf-lib, heic2any and JSZip are vendored in `libs/` (no network needed; verified zero requests)
- [x] Photos/PDFs/exports git-ignored
- [ ] Add `/04 AI/patterns.md` entry for the headless Playwright + Edge test recipe
- [ ] Commit (nothing since the last commit is committed)
