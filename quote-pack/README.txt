"Quote pack" for SourceBots 2019 kit manufacture run
====================================================

# Organisation

Each folder `power`, `motor` and `servo` corresponds to a 
different board design. Within each of these, the following files 
and folders exist:

  * `BOARD.txt`: Overview of board and manufacturing specifications
  * `BOARD-bom.xlsx`: Bill of materials
  * `BOARD-coords.txt`: Text file containing coordinates of components, for pick-and-place
  * `BOARD-locations.png`: Reproduction of top silkscreen showing the location of each named component
  * `BOARD-polarities.png`: As above, but with markings for identifying orientation of polarised components
  * `BOARD-schematic.pdf`: Schematic diagram
  * `gerbers`: Gerber and drill files for the PCB
    * `BOARD.top.gbr`: Top copper
    * `BOARD.topmask.gbr`: Top soldermask
    * `BOARD.topsilk.gbr`: Top silkscreen
    * `BOARD.toppaste.gbr`: Top solder paste
    * `BOARD.bottom.gbr`: Bottom copper
    * `BOARD.bottommask.gbr`: Bottom soldermask
    * `BOARD.bottomsilk.gbr`: Bottom silkscreen
    * `BOARD.group2.gbr`: Inner copper
    * `BOARD.group3.gbr`: Inner copper
    * `BOARD.outline.gbr`: Outline
    * `BOARD.plated-drill.cnc`: Drill specification (plated holes only)
    * `BOARD.unplated-drill.cnc`: Drill specification (unplated holes only)
    * `BOARD.fab.gbr`: Human-readable drilling diagram
