

## Topics

- Welcome
- Manage index
- Manage documents 
- Manage mappings
- Queries
    - Term query
    - Match query
    - Range query
    - Bool query
    - Sorting of query results
- Summary

## Plase make sure you have - 


* Installed Docker following the instruction in https://docs.docker.com/engine/install/ (if they are not in your machine). Make sure `docker` and `docker-compose` commands are available in your terminal
* Clone the repo to your local machine from this url: https://git.realestate.com.au/asia-workshops/elastic-search-workshop-101
* In your terminal, go to the repo's root folder and run `docker-compose pull`. This will pull all the images needed by the workshop.

## Useful commands
### Start the server
Create an environment with:
```bash
docker-compose up -d
```

Elasticsearch should now be available on `http://localhost:9200`

Kibana should now be available on `http://localhost:5601`


### Stop the server
Stop the environment with:
```bash
docker-compose down
```

### Cleanup the server
Cleanup the environment and delete all data with:
```bash
docker-compose down --volumes --remove-orphans
```



# AutoComplete-Input-Elastic-Search-Python
![image](https://user-images.githubusercontent.com/39345855/88481649-ae6a4e80-cf2a-11ea-9ac7-cda7dbf1f519.png)
* remember you can use regular expression query or match phrase prefix please see youtube video for demo


#### Tutorial 
* https://www.youtube.com/watch?v=gDOu_Su1GqY

Creating  Auto Complete System Frontend Flask + Backend (Elastic Search)
