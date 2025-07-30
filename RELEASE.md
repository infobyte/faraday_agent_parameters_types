1.8.1 [Jul 16th, 2025]:
---
 * [MOD] Downgrade `validators` package version to `0.20.0` to avoid nix issues in Faraday. #52

1.8.0 [May 14th, 2025]:
---
 * [ADD] Added a new domain list data type. #49

1.7.3 [Jan 6th, 2025]:
---
 * [MOD] Added a boolean field to retrieve all completed scans from Tenable SC. #47
 * [MOD] All legacy parameters for Cisco Cyber Vision were renamed. Also, new ones were added. #48

1.7.2 [Oct 24th, 2024]:
---
 * [MOD] Changed Nmap TARGET and PORT_LIST to list type. #43

1.7.1 [Sep 20th, 2024]:
---
 * [MOD] Changed Nuclei Arguments to list type. #42

1.7.0 [Jul 11th, 2024]:
---
 * [ADD] Added Microsoft Defender agent parameters. #39

1.6.0 [May 22nd, 2024]:
---
 * [ADD] Added Tenable sc manifest. #30
 * [ADD] Added Cisco Cyber Vision agent parameters. #38
 * [MOD] Modify Tenable IO agent parameters. #37

1.5.1 [Mar 7th, 2024]:
---
 * [MOD] Added hotspots option to sonarqube. #33

1.5.0 [Mar 6th, 2024]:
---
 * [MOD] Added GitHub code scanning tools manifest. #36

1.4.0 [Feb 8th, 2024]:
---
 * [MOD] Added dependabot manifest. #35

1.3.1 [Aug 3rd, 2023]:
---
 * [MOD] Added relaunch parameter and make TENABLE_SCAN_ID optional to tenableio executor #32

1.3.0 [July 7th, 2023]:
---
 * [ADD] Add AppScan manifest #31

1.2.0 [Nov 30th, 2022]:
---
 * [ADD] Added sonar manifest
 * [ADD] Added tenable.io manifest

1.1.0 [Oct 26th, 2022]:
---
 * [Add] Added Qualys manifest
 * Remove python from cmd field for python executors manifest

1.0.4 [Sep 5th, 2022]:
---
 * Add site_id optional parameter and make executive_report_id optional to insightVM manifest

 * Add timeout parameter to arachni manifest
 * Change api_key agument in Zap manifest to enviroment variables

 * Change EXECUTIVE_REPORT_ID to string
 * Nikto now uses only requieres TARGET_URL argument.

1.0.3 [Dec 13th, 2021]:
---
 * add commands --api-token and --random-user-agent
 * Add shodan's manifest

1.0.2 [Oct 19th, 2021]:
---
 * added new parameter type Script for nmap

1.0.1 [Aug 9th, 2021]:
---
 * New manifest for InsightVM agent
 * Remove HOST and API from parameters

1.0.0 [Jun 29th, 2021]:
---
 * First release of module

0.1.0 [May 14th, 2021]:
---
 * Release of first stable version, to use in multiples pipelines

0.1.0a1 [Apr 22nd, 2021]:
---
 * Encode/Decode the types, plus identifier logic
 * First release of the package, in alpha status
