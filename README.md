# Animalia

```
 (`-')  _ <-. (`-')_  _     <-. (`-')   (`-')  _            _     (`-')  _  
 (OO ).-/    \( OO) )(_)       \(OO )_  (OO ).-/    <-.    (_)    (OO ).-/  
 / ,---.  ,--./ ,--/ ,-(`-'),--./  ,-.) / ,---.   ,--. )   ,-(`-')/ ,---.   
 | \ /`.\ |   \ |  | | ( OO)|   `.'   | | \ /`.\  |  (`-') | ( OO)| \ /`.\  
 '-'|_.' ||  . '|  |)|  |  )|  |'.'|  | '-'|_.' | |  |OO ) |  |  )'-'|_.' |
(|  .-.  ||  |\    |(|  |_/ |  |   |  |(|  .-.  |(|  '__ |(|  |_/(|  .-.  |
 |  | |  ||  | \   | |  |'->|  |   |  | |  | |  | |     |' |  |'->|  | |  |
 `--' `--'`--'  `--' `--'   `--'   `--' `--' `--' `-----'  `--'   `--' `--'
 ______   ______  _____  _________   ______   _       _____  ______  
```

## About
Explore the Animal Kingdom


## Setup
### Requirements
Python 3.9 with pip
```sh
pip install animalia
```

## Usage
### Generate a new species name
*new in 0.0.23*

```sh
animalia generate-species-name
```
you will receive a name such as
```
Chamber Mouse
```

### Generate multiple species names
*new in 0.0.23*

```sh
animalia generate-species-name --count 5
```
and similarly, you will receive a batch list of generated species names
```txt
Cream-coloured giant plunderfish
Little blue pheasant
David's root
Mountain ark
Trinidad chevron mushroom
```


## Data Sources

### species.txt
Data for generating species names uses the Swiss-Prot Protein Knowledgebase, provided by the UniProt Consortium, and distributed under the Creative Commons Attribution (CC BY 4.0) License.  

You can read more about it in the provided data source located in `animalia/data/species.txt`


## Contributors

- Jeff Doss <notdsk@gmail.com>
- Daniel Gabriele <dg0offset@gmail.com>

## License
animalia is released under the MIT License. See the bundled LICENSE file for details.
