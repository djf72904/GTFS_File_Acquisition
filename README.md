## GTFS File Acquisition
- - -
### What is this?
The background for this is that it is part of a larger project that involves making a service that helps with multimodal
transportation in the PA, NJ, NY, and CT region. The gist of that project is to help users who are looking to live in 
that area with planning on the best place to settle down based on transit networks and where they would be working.  

Therefore, a big part of that project is being able to map the transit networks accurately, with info including but not
limited to: stops/stations, fare information, schedules, transfers, etc. The best way to do this is through the 
[General Transit Feed Specification (GTFS)](https://gtfs.org/). This is a standardized way to make transit agencies' 
information available to the programming community so they can make a service such as the one mentioned before.  

These transit agencies make this information available and update it quite regularly, making it available to download on the 
[TransitLand Database](https://www.transit.land/) will be the main source of the data used in this project.
However, the main issue with this is that while all agencies follow the GTFS standard, they do not follow it equally.
Therefore, this project's goal is to make sure that when compiling information from many agencies, they can work together
seamlessly with the needed information.

- - -

### File Acquisition Process
1. The first thing done is that all the files are obtained from the mobility database in the form of the agencies.
2. Next is to check the fares data on all the files that were obtained. They must be updated not only to their current
   pricing model, but also some agencies don't include them at all, so it must be added.
3. After that, the goal is to make sure that all agencies are unique so that when aggregated together, there is no mix-up of 
   routes
4. Lastly, we use the built-in [Mobility Database Validator](https://github.com/MobilityData/gtfs-validator) to make 
   sure there are no major errors in the standard with our edited files.

- - -

### Agencies Involved
- MTA Subway
- MTA Bus
- Long Island Rail Road (LIRR)
- NYC Ferry
- Metro North
- NY Waterway
- PATH
- New Jersey Transit Rail
- New Jersey Transit Bus
- PATCO
- Septa Bus
- Septa Rail

