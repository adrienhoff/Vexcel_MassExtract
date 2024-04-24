# Vexcel_MassExtract
ArcPro tool for mass imagery extract from Colorado Vexcel services.
Created by Adrien Hoff, Senior GIS Analyst at Jeffcom911

The collaboration between the CDOT Division of Transportation Development and the Colorado Office of Information Technology (OIT) has resulted in the acquisition of statewide high-resolution imagery from Vexcel®, offering a significant enhancement in data resources for the region. This initiative provides local agencies with access to a variety of imagery, including statewide coverage at 15-20 cm (5.9-7.8 in.) resolution collected biannually, annual urban area coverage at 7.5 cm (3 in.) resolution, and specialized coverage like "Gray Sky" imagery captured at 3 in. resolution immediately following major disasters. To ensure accessibility, the data is distributed through various channels, including a high-performance Web Map Tile Streaming (WMTS) service and an online map viewer. Agencies who take part in the initial training are granted access to the Vexcel server via provided logins and access tokens.

The script here allows for mass extraction of TIFFs by iterating through a tessellation grid, replacing polygon values with minimum and maximum coordinates generated from the grid. The size of tessellation squares is determined using an initial TIFF extraction as a reference. By dynamically constructing API URLs for each polygon, the script downloads imagery from the Vexcel API, providing public safety agencies with offline access to high-resolution imagery spanning large geographic areas.

USER MUST GENERATE OWN TESSELLATION. It is recommended that the user generate a SQUARE grid of 1500 sq ft in GCS. The API utilizes lat/long of GCS, not projections. User can extract single TIFF from Vexcel viewer to get exact size of grid squares.

The flexibility of the script allows users to specify the type of imagery (e.g., bluesky-high, greysky, or urban-r) they wish to extract, catering to diverse needs across different scenarios.

Once retrieved, agencies can create raster mosaics or datasets with the new imagery. The Hexagon ECW “compression algorithm achieves 15:1 compression ratios at a visually lossless quality level” (https://hexagon.com/products/ecw-compression) and is highly recommended. Agencies can purchase a short term license for GeoCompressor for under $1k.

This comprehensive approach streamlines the process of accessing and utilizing high-resolution imagery, empowering public safety agencies with valuable resources to support their operations effectively.
