# Map Photos project file (JSON)

`project.template.json` in this folder is a complete example. A real project is saved by **💾 Save JSON** and opened with **📂 Open JSON**. It lists the plan and photos by name and path; it does **not** contain any pixels. Real project files hold family/site data (GPS, dates), so `*.mapphotos.json` is git-ignored. The template is the only JSON that belongs in git.

## How files are found when you open a project

Browsers never reveal a file's real location, so `path` is only what the app could see at import time:

- Photos from **📁 Load a folder** have a path relative to the folder you picked (`Trip/morning/IMG_1.jpg`).
- Photos or a plan chosen with the file picker only have their name, so `path` equals `file_name`.

On **Open JSON** the app asks you to choose the folder (or files). Each asset is matched in this order: path, then name + size, then name if only one file has it. Missing photos stay on the plan as "file missing" tiles with their positions kept; use **🔗 Link files** later to supply them. You can edit `path` by hand in the JSON if you keep files in sub-folders.

## Fields

| Field | Meaning |
|---|---|
| `format`, `version` | Must be `mapphotos-project` and `1`. |
| `name` | Project name (defaults to the plan's file name). |
| `saved_at` | When this file was written (UTC ISO 8601). |
| `coordinate_units` | Note on units. All `x`, `y`, `width`, `height` are in PDF points at 100% zoom, origin top-left, y down. They do not change when you zoom. |
| `plan.file_name`, `plan.path` | The PDF site plan. |
| `plan.size_bytes`, `plan.modified` | Size and last-modified date of the plan file when imported. |
| `plan.page`, `plan.page_width`, `plan.page_height` | Page used (only page 1 so far) and its size in points. |
| `settings.photo_size_percent_of_page_width` | Size of every photo on the plan (1 to 20). All photos share one size. |
| `regions[]` | The active scheme's regions (kept for older readers; `schemes[]` is the full list). Drawn regions. `type` is `box` (`x`, `y`, `width`, `height`) or `polyline` (`closed`, `points[{x,y}]`). `label` is the name you typed. |
| `schemes[]` | Region schemes (semantic layers): `id`, `name`, `regions[]` (same shape as `regions[]`). Each scheme is its own set of regions on the plan. Older files without it load as one scheme named Areas. |
| `active_scheme` | `id` of the scheme shown on the plan and used for photo locations. |
| `tags[]` | Tags: `id`, `name`, `color` (`#rrggbb`), `tab` (true = shown as a tab above the plan). |
| `annotations[]` | Markup. `type` is `note` (`x`, `y`, `text`), `arrow` (`x1`, `y1` tail, `x2`, `y2` point) or `cloud` (`x`, `y`, `width`, `height`). Optional; older files without it open fine. |
| `embedded` | Optional. Makes the file self-contained: `plan` is a data URI for the plan (PDF, JPG or PNG; an image becomes a one-page PDF) and `photos[]` has one data URI per entry in `photos[]`, same order. Files with `embedded` open directly, with no link step. The app never writes this field itself. |
| `import_batches[]` | Each time photos were loaded: `batch` number, `imported_at`, `source` (`files` or `folder`), `photo_count`. |
| `photos[].id` | Stable number for the photo within this project. |
| `photos[].tags` | Tag `id`s on the photo. Its first tag's colour frames it on the plan and in the PDF. |
| `photos[].file_name`, `path` | Original file. HEIC photos keep their `.HEIC` name; they are converted in the page when loaded. |
| `photos[].size_bytes`, `modified` | Size and last-modified date of the original file. |
| `photos[].format` | `jpeg`, `png`, `heic`, etc. |
| `photos[].import_batch`, `imported_at` | Which batch brought it in, and when. |
| `photos[].taken_at` | Time taken. |
| `photos[].taken_at_source` | `exif` (read from the photo) or `file_date` (no EXIF time, so the file's modified date is used). |
| `photos[].gps` | `{lat, lon}` from EXIF, or `null`. |
| `photos[].camera` | Camera make/model from EXIF, or `null`. |
| `photos[].aspect_ratio` | Width / height after rotation. Keeps the marker shape if the file is missing. |
| `photos[].placed`, `position` | Whether it is on the plan, and its centre `{x, y}`. |
| `photos[].region`, `region_id` | Informational: the region its position falls inside, or `null`. Recomputed on open from `position`, so editing these has no effect. |
