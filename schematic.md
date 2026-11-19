Map Photos

Context:
Walked with a group of people around a campus. 
Took a series of photographs.
Want to be able to retrace steps via photographs on a site plan.
Sensitive data, everything to be offline - will borrow AI to create a framework. All input/ output should be inside git.ignore

Purpose:
To map photos onto a PDF


How it works:
0 - Homepage with basic instructions
1 - Load site plan/ reference document. Identify regions (Building X: Building Name)
    - Create a "viewer" that allows basic PDF controls, zoom in/ out, add notes, add arrows, add clouds, add images (in preparation for next step)
    - Create a save as feature for the siteplan with time suffix
2 - Load photos (in background)
    - Create a matrix of the photos, extracting EXIF data (timestamp, GPS if available) to sort them chronologically.
    - Create small versions of each photo
    - In side panel, display photos, have them dragged and dropable to the siteplan. 
    - If clicked, allow there be an arrow to indicate view angle... This should be toggleable
    - Depending on where the image is drawn, it should be linked to the region. On the right side, there should be a filter that allows for showing only certain regions and their related images.
3 - Create a Json file for the linkage. When viewing in the browser, hovering over the image for a while will create a popup showing a larger image, with ability to further zoom in. When saved and reloaded, this allows for compositing of the PDF for loading with other viewers
4 - Create a high res PDF with the full sized photos
    - Allow for save as into a new file with suffix

Next Steps:
A - Review scope of work
B - Create MVP
C - I will drop in assets in designated folder and test