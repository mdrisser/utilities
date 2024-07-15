

def ipgeo_lookup(domain, ip, apiKey):
    """
    Gets the IP address associated with the domain, also gets the
    geolocation information. Prints the information to the console.
    :return: None
    """
    
    #print("Getting IP Geolocation...")
    import requests
    
    IPGEO_API_URL = "https://api.ipgeolocation.io/ipgeo"

    api_params = {"apiKey": apiKey, "ip": ip}
    geo_ip = requests.get(IPGEO_API_URL, params=api_params)

    # If we got somekind of an error in response, show what it is
    if geo_ip.status_code != 200:
        print(f"Request Status Code: {geo_ip.status_code}")
        print(f"{geo_ip.text}")
        sys.exit()

    # Get the JSON object returned by the request
    answer = geo_ip.json()
    answer['domain'] = domain

    # Show the information we want to see
    #print(f"          Domain: {domain}")
    #print(f"              IP: {answer['ip']}")
    #print(f"    Country Code: {answer['country_code2']}")
    #print(f"         Country: {answer['country_name']}")
    info = {
        'domain': domain,
        'ip': answer['ip'],
        'country_code': answer['country_code2'],
        'country': answer['country_name'],
    }

    return info


def check_blocklist(ip):
    """
    Site: blocklist.de

    :param ip: IP Address to search the blacklist for
    :return: list containing blacklist name and number of times reported
    """
    import requests
    import json
    # Check returns JSON in the format of:
    # {"attacks":0,"reports":0}
    blde_url = "http://api.blocklist.de/api.php"
    blde_params = {'ip': ip, 'start': 1, 'format': 'json'}
    r = requests.get(blde_url, params=blde_params)

    returned = json.loads(r.text)

    result = {
        'blacklist': 'blocklist.de',
        'reports': returned['reports']
    }
    
    return result

def check_stopforumspam(ip):
    """
    Site: stopforumspam.com
    :param ip: IP Address to search the blacklist for
    :return: list containing blacklist name and number of times reported
    """
    import requests
    import untangle
    # Check returns XML in the format of:
    # <response success="true">
    #     <type>ip</type>
    #     <appears>yes</appears>
    #     <lastseen>2007-09-18 05:48:53</lastseen>
    #     <frequency>2</frequency>
    # </response>
    sfs_url = "http://api.stopforumspam.org/api"
    sfs_params = {'ip': ip}

    r = requests.get(sfs_url, params=sfs_params)
    xmldom = untangle.parse(r.text)

    result = {
        'blacklist': 'Stop Forum Spam',
        'reports': xmldom.response.frequency.cdata
    }
    
    return result


def check_abuseipdb(ip, apiKey):
    """
    Site: AbuseIPDB
    :param ip: IP Address to search the blacklist for
    :return: list containing blacklist name and number of times reported
    """
    import requests
    import json
    # Check returns JSON in the format of:
    # {
    #     "data": {
    #         "ipAddress": "118.25.6.39",
    #         "isPublic": true,
    #         "ipVersion": 4,
    #         "isWhitelisted": false,
    #         "abuseConfidenceScore": 100,
    #         countryCode": "CN",
    #         "countryName": "China",
    #         "usageType": "Data Center/Web Hosting/Transit",
    #         "isp": "Tencent Cloud Computing (Beijing) Co. Ltd",
    #         "domain": "tencent.com",
    #         "hostnames": [],
    #         "totalReports": 1,
    #         "numDistinctUsers": 1,
    #         "lastReportedAt": "2018-12-20T20:55:14+00:00",
    #         "reports": [
    #             {
    #                 "reportedAt": "2018-12-20T20:55:14+00:00",
    #                 "comment": "Dec 20 20:55:14 srv206 sshd[13937]: Invalid user oracle from 118.25.6.39",
    #                 "categories": [
    #                     18,
    #                     22
    #                 ],
    #                 "reporterId": 1,
    #                 "reporterCountryCode": "US",
    #                 "reporterCountryName": "United States"
    #             }
    #         ]
    #     }
    # }
    aipdb_url = "https://api.abuseipdb.com/api/v2/check"
    aipdb_params = {'ipAddress': ip}
    aipdb_headers = {
        'Key': apiKey,
        'Accept': "application/json"
    }

    r = requests.get(aipdb_url, params=aipdb_params, headers=aipdb_headers)

    returned = json.loads(r.text)

    result = {
        'blacklist': "AbuseIPDB",
        'reports': returned['data']['totalReports']
    }

    return result


def blacklist_check(ip, abuseipdb_apikey):
    """
    Queries several different blacklist sites for the provided IP Address
    :param ip: IP Address to search the blacklists for
    :return: list of sites and number of times reported to each site
    """
    blacklist_results = []
    blacklist_results.append(check_blocklist(ip))
    blacklist_results.append(check_stopforumspam(ip))
    blacklist_results.append(check_abuseipdb(ip, abuseipdb_apikey))

    return blacklist_results
