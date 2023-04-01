This library performs "deskewing" on scanned text documents. Deskewing is a term used for fixing the scans to get the lines of text straight. That means rotating the image of the scanned page a little to compensate for the misalignment of the paper in the scanner.

For multi-page formats like TIF and PDF, this library performs the operation on every page, not just on the first page. The input file gets disassembled into individual pages and then, after performing the operation on each page, they all get assembled back to a single file, preserving the original page order.

This library utilizes the Windows binary from **Galfar's Deskew Tools**.

  https://galfar.vevb.net/wp/projects/deskew/  

This library requires the following prerequisites on the robot machine:

* .NET 5.0.17 DesktopRuntime  
  https://dotnet.microsoft.com/en-us/download/dotnet/5.0

* Python 3.10 x64  
  pip install **pillow**==9.4.0  
  pip install **tifftools**==1.3.9  

Supported file formats:

* Input:  BMP, JPG, PNG, JNG, GIF, DDS, TGA, PBM, PGM, PPM, PAM, PFM, TIF, PSD, PDF  
* Output: BMP, JPG, PNG, JNG, GIF, DDS, TGA, PGM, PPM, PAM, PFM, TIF, PSD, PDF  

Limitations:

* All the paths provided to this library must be absolute. Relative path leads to exceptions.
* PDF text layer gets removed. The resulting PDF will have images only.
* DOS windows will open and close while the deskew is in progress.
