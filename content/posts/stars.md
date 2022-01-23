Title: We Name The Stars
Date: 2016-03-20 10:40
Status: published

New Project! [We Name The Stars](http://wenamethestars.inkleby.com/) is a way to explore the database place names in outer space. It lets you explore maps and gives context on what the names *mean*.

Essentially it’s a demonstration of how a dataset can be transformed by highlighting connections and bringing context to the information. So there’s a crater at blah coordinates - but where is that? Can we see it on a map? What’s nearby? How long would it take to get somewhere else? It’s named after someone, but who is that person? Where can I found out more? It combines data from eight different datasets to reveal new information that wasn't visible in any of the component parts. 

There's also a companion robot, [@WNTS_Rover](http://wenamethestars.inkleby.com/rover/) that's visiting every crater on the moon and tweeting elevation maps as it goes. 

As an extra fun thing, I [wrote something](http://www.citymetric.com/horizons/titans-doom-mons-mercurys-pourquoi-pas-how-did-landscape-space-get-its-names-1930) for CityMetric about the history of naming things in space I picked up while putting this together.

And for coders, this yielded three fun new things for our github:

[moon_elevation_reader](https://github.com/inkleby/moon_elevation_reader) - the code needed to extract elevation data from ISIS Cube files given lat and long. This is used to get the height information to generate the elevation maps the rover produces. 

[google_maps_tile_converter](https://github.com/inkleby/google_maps_tile_converter) - this is a basic script to process an image and carve it into tiles at different zoom levels for use in mapping interfaces like google maps. 

[world_tiles](https://github.com/inkleby/world_tiles) - The collection of tiles the above spit out  for planets other than the Earth, Moon and Mars. Can be used to create your own maps.

