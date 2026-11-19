# Sample project: Hollywood Bowl

A ready-made project: a satellite view of the Hollywood Bowl as the plan, five regions (Stage, Seating, Parking Lot B, Ticketing, Museum), a few markup items, and nine photos waiting in the right panel for you to place.

Files:
- `hollywood_bowl.sample.json` the whole project in one file. The plan image and the photos are embedded in it, so nothing needs linking.
- `hollywood_bowl.sample.js` the same data, loaded by `index.html` so the start screen can offer it even when opened straight from disk.
- `hollywood_bowl_site_plan.jpg` (and `.pdf`) the plan image
- `photos/` the nine photos
- `project.src.json` the editable source (regions, markup, photo times); `build_sample.py` rebuilds the two `sample` files from it and the images (`python3 sample-project/build_sample.py`)

## How to use it

1. Open `index.html` in Chrome or Edge.
2. Click **Hollywood Bowl sample** on the start screen. (Or use **Open JSON** and pick `hollywood_bowl.sample.json`.) The plan appears with its regions and markup, and the photos are listed in the right panel, oldest first.
3. Scroll the right panel to **Photos**. Hover a photo to enlarge it.
4. Drag a photo from the list onto the plan where it was taken. Its card shows the region it landed in. Suggested spots:
   - 01 LA Phil marquee, 02 Tonight marquee, 03 Fountain and statue: **Ticketing**
   - 04 Side view of stage, 05 Aisle view, 06 Stage from the seats, 07 Promenade walkway: **Seating**
   - 08 Aerial of seating: above the bowl. 09 Historic aerial: **Museum**
5. Drag a placed photo to move it. Double-click it to take it off the plan.
6. Tick regions under **Filter by region** to show only their photos.

## Try the markup tools

The three tools are in the left rail under the region tools. Click the tool, then use the plan. Click the tool again to switch it off.

7. **Text note** (T icon): click on the plan, type, press **Ctrl+Enter**. Enter adds a new line.
8. **Arrow** (diagonal arrow icon): press at the tail, drag, release at the point.
9. **Revision cloud** (cloud icon): drag a rectangle around the area that changed.
10. Everything you add is listed under **Markup** in the right panel. Use **Edit** to change a note, **Delete** to remove an item, or **Clear all markup**.

## Draw your own region

11. Pick the **polyline** tool (click points, double-click to close) or the **box** tool (drag), then name the region.

## Save and export

12. **Save JSON** keeps regions, markup and photo positions (photos are listed, not copied).
13. **Download PDF** writes a PDF with the regions, markup and placed photos on the plan.
14. **Download photos** saves the placed photos renamed by region (`Ticketing_01.jpg`, and so on).
15. The app also keeps a copy in your browser, so next time the start screen offers **Resume**.

## About the times

The photos carry made-up times (17:35 to 18:30) so they sort as a walk from the Highland Ave marquee to the seats and the museum.

## Sources

The plan image and the nine photos were supplied by the project owner for this demo; their original sources and licenses were not recorded. Check them before publishing this repo publicly, and keep a license and credit with any photos you add.
