# Hospital Referral Network

## 1. Project Description

The Hospital Referral Network is a Python-based application that represents connections between healthcare facilities in Blantyre, Malawi.

The system uses a weighted graph to represent referral connections between healthcare facilities. Each facility is represented by a vertex, while connections are represented by weighted edges.

The edge weights represent assumed distances in kilometres.

## 2. Algorithm Used

The project implements **Dijkstra's Shortest Path Algorithm** to identify the shortest referral route between two healthcare facilities.

## 3. Technologies Used

- Python 3
- Visual Studio Code
- Git and GitHub

## 4. Facilities

The graph contains 20 healthcare facilities represented by vertices A to T.
| Vertex | Healthcare Facility |
|--------|---------------------|
| A | Queen Elizabeth Central Hospital |
| B | Bangwe Health Centre |
| C | Limbe Health Centre |
| D | Ndirande Health Centre |
| E | Chilomoni Health Centre |
| F | Zingwangwa Health Centre |
| G | Chitimba Health Centre |
| H | South Lunzu Health Centre |
| I | Mbatani Health Centre |
| J | Kachidi Health Centre |
| K | Makhetha Health Centre |
| L | Malabada Health Centre |
| M | Blantyre Adventist Hospital |
| N | Mwaiwathu Private Hospital |
| O | Beit Cure International Hospital |
| P | Shifa Hospital |
| Q | LMJ Hospital |
| R | Bean Medical Centre |
| S | Masm Medical Clinic |
| T | Atlas Medical Centre |

## 5. How to Run the Project

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run:

```powershell
python hospital_referral.py
```

5. Enter the starting facility and destination using their letters (A–T).

## 6. Example

Starting facility: A

Destination facility: C

Expected shortest route:

`A -> D -> B -> C`

Total distance: **14 km**

## 7. Project Purpose

This project demonstrates the application of graph data structures, weighted edges, Dijkstra's algorithm and shortest-path problem solving in a healthcare referral network.
