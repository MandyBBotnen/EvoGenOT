#######################################
### BEST Library build Purification ###
#######################################

## Description of procedure ##
#
#
# Things do before procedure
#
#	1. Ensure samples are room temperature and place libraries in magnetic module
# 	2. Ensure SPRI beads are room temperature
#   3. Make freshly made 80% Ethanol for purification
#   4. Distribute:
#                   SPRI beads to Column 1,
#                   Ethanol to Column 2 and 3
#                   Elution Buffer to Column 12
#
# Procedure
#
#		Purification
# 	1.	Distribute 1.5x beads to library and mixes
#	2.	Removes supernatant and adds ethanol for washing, washing will be processed twice
#   3.  Beads will air dry for 4 minutes and 35µl elution buffer will be added
#	4.	Elutes will incubate for 15 minutes at room temperature and be eluted to a new plate in slot 1
#
#	Good Luck!
#
######## IMPORT LIBRARIES ########
from opentrons import labware, instruments, modules, robot

#### METADATA ####

metadata = {
    'protocolName': 'BEST_Purification',
    'author': 'Jacob Agerbo Rasmussen <genomicsisawesome@gmail.com>',
    'version': '1.0',
    'date': '2019/07/04',
    'description': 'Purification procedure of Automated single tube library preperation after Carøe et al. 2017',
}
#### LOADING CUSTOM LABWARE ####

plate_name = 'One-Column-reservoir'
if plate_name not in labware.list():
    custom_plate = labware.create(
        plate_name,                    # name of you labware
        grid=(1, 1),                    # specify amount of (columns, rows)
        spacing=(0, 0),               # distances (mm) between each (column, row)
        diameter=81,                     # diameter (mm) of each well on the plate
        depth=35,                       # depth (mm) of each well on the plate
        volume=350000)

#### LABWARE SETUP ####
trough = labware.load('trough-12row', '10')
trash_box = labware.load('One-Column-reservoir', '8')
mag_deck = modules.load('magdeck', '7')
mag_plate = labware.load('biorad-hardshell-96-PCR', '7', share=True)
elution_plate = labware.load('biorad-hardshell-96-PCR','1')

tipracks_200_1 = labware.load('tiprack-200ul', '3', share=True)
tipracks_200_2 = labware.load('tiprack-200ul', '4', share=True)
tipracks_200_3 = labware.load('tiprack-200ul', '5', share=True)
tipracks_200_4 = labware.load('tiprack-200ul', '6', share=True)


#### PIPETTE SETUP ####

m300 = instruments.P300_Multi(
    mount='right',
    min_volume=30,
    max_volume=200,
    aspirate_flow_rate=100,
    dispense_flow_rate=200,
    tip_racks=[tipracks_200_1, tipracks_200_2, tipracks_200_3, tipracks_200_4])


## Purification reagents SETUP
SPRI_beads = trough.wells('A1')
EtOH1 = trough.wells('A2')
EtOH2 = trough.wells('A3')
Elution_buffer = trough.wells('A12')

Liquid_trash = trash_box.wells('A1')

## Plate SETUP

MA1 = mag_plate.wells('A1')
MA2 = mag_plate.wells('A2')
MA3 = mag_plate.wells('A3')
MA4 = mag_plate.wells('A4')
MA5 = mag_plate.wells('A5')
MA6 = mag_plate.wells('A6')
MA7 = mag_plate.wells('A7')
MA8 = mag_plate.wells('A8')
MA9 = mag_plate.wells('A9')
MA10 = mag_plate.wells('A10')
MA11 = mag_plate.wells('A11')
MA12 = mag_plate.wells('A12')

sample_number = 96
col_num = sample_number // 8 + (1 if sample_number % 8 > 0 else 0)
samples = [col for col in mag_plate.cols()[:col_num]]

#### VOLUME SETUP

sample_vol = 50
bead_vol = 1.5*sample_vol
EtOH_vol = 160
EtOH_vol2 = 150
Elution_vol = 35

#### PROTOCOL ####
### Beads addition
mag_deck.disengage()

#### Transfer beads to MA1
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA1.bottom(1))
m300.dispense(bead_vol, MA1.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA1.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA1.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

#### Transfer beads to MA2
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA2.bottom(1))
m300.dispense(bead_vol, MA2.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA2.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA2.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

#### Transfer beads to MA3
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA3.bottom(1))
m300.dispense(bead_vol, MA3.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA3.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA3.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

#### Transfer beads to MA4
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA4.bottom(1))
m300.dispense(bead_vol, MA4.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA4.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA4.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

#### Transfer beads to MA5
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA5.bottom(1))
m300.dispense(bead_vol, MA5.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA5.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA5.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

#### Transfer beads to MA6
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA6.bottom(1))
m300.dispense(bead_vol, MA6.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA6.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA6.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

#### Transfer beads to MA7
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA7.bottom(1))
m300.dispense(bead_vol, MA7.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA7.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA7.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

#### Transfer beads to MA8
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA8.bottom(1))
m300.dispense(bead_vol, MA8.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA8.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA8.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()


#### Transfer beads to MA9
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA9.bottom(1))
m300.dispense(bead_vol, MA9.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA9.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA9.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

#### Transfer beads to MA10
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA10.bottom(1))
m300.dispense(bead_vol, MA10.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA10.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA10.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

#### Transfer beads to MA11
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA11.bottom(1))
m300.dispense(bead_vol, MA11.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA11.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA11.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

#### Transfer beads to MA12
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(SPRI_beads.top(-30))
m300.mix(3, bead_vol, SPRI_beads.bottom(2))
max_speed_per_axis = {'x': (300), 'y': (300), 'z': (100), 'a': (50), 'b': (20), 'c': (20)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.set_flow_rate(aspirate=50, dispense=50)
m300.aspirate(bead_vol, SPRI_beads.bottom(2))
m300.move_to(MA12.bottom(1))
m300.dispense(bead_vol, MA12.bottom(4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, bead_vol, MA12.bottom(4))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=100, dispense=100)
m300.move_to(MA12.top(-4))
m300.blow_out()
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
m300.return_tip()

robot.comment("Incubating the beads and PCR products at room temperature \
for 5 minutes. Protocol will resume automatically.")
m300.delay(minutes=5)
mag_deck.engage(height=16)
m300.delay(minutes=2)

### Remove supernatant, by re-using tiprack 1
### remove supernatant from MA1
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A1'))
m300.aspirate(180, MA1.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA2
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A2'))
m300.aspirate(180, MA2.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA3
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A3'))
m300.aspirate(180, MA3.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA4
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A4'))
m300.aspirate(180, MA4.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA5
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A5'))
m300.aspirate(180, MA5.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA6
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A6'))
m300.aspirate(180, MA6.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA7
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A7'))
m300.aspirate(180, MA7.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA8
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A8'))
m300.aspirate(180, MA8.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA9
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A9'))
m300.aspirate(180, MA9.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA10
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A10'))
m300.aspirate(180, MA10.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA11
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A11'))
m300.aspirate(180, MA11.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### remove supernatant from MA12
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_1.wells('A12'))
m300.aspirate(180, MA12.bottom(1))
m300.dispense(180, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Wash 1 with Ethanol, using tiprack 2
### Transfer Wash 1 to MA1
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA1.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA1.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA1.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA2
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA2.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA2.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA2.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA3
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA3.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA3.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA3.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA4
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA4.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA4.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA4.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA5
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA5.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA5.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA5.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA6
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA6.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA6.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA6.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA7
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA7.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA7.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA7.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA8
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA8.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA8.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA8.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA9
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA9.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA9.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA9.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA10
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA10.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA10.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA10.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA11
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA11.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA11.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA11.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA12
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol, EtOH1.top(-12))
m300.dispense(EtOH_vol, MA12.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol, MA12.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA12.top(-10))
m300.blow_out()
m300.return_tip()

mag_deck.engage(height=16)
m300.delay(minutes=2)

### Remove supernatant, by re-using tiprack 2
### Remove supernatant from MA1
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A1'))
m300.aspirate(EtOH_vol, MA1.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA2
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A2'))
m300.aspirate(EtOH_vol, MA2.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA3
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A3'))
m300.aspirate(EtOH_vol, MA3.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA4
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A4'))
m300.aspirate(EtOH_vol, MA4.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA5
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A5'))
m300.aspirate(EtOH_vol, MA5.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA6
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A6'))
m300.aspirate(EtOH_vol, MA6.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA7
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A7'))
m300.aspirate(EtOH_vol, MA7.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA8
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A8'))
m300.aspirate(EtOH_vol, MA8.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA9
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A9'))
m300.aspirate(EtOH_vol, MA9.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA10
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A10'))
m300.aspirate(EtOH_vol, MA1.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA11
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A11'))
m300.aspirate(EtOH_vol, MA11.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA12
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_2.wells('A12'))
m300.aspirate(EtOH_vol, MA12.bottom(1))
m300.dispense(EtOH_vol, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Wash 2 with Ethanol, using tiprack 3
### Transfer Wash 2 to MA1
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH2.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA1.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA1.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA1.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 2 to MA2
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH2.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA2.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA2.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA2.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 2 to MA3
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH2.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA3.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA3.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA3.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 2 to MA4
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH2.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA4.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA4.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA4.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 2 to MA5
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH2.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA5.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA5.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA5.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 2 to MA6
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH2.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA6.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA6.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA6.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 2 to MA7
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH2.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA7.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA7.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA7.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 1 to MA8
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH2.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA8.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA8.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA8.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 2 to MA9
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH2.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA9.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA9.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA9.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 2 to MA10
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA10.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA10.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA10.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 2 to MA11
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH2.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA11.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA11.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA11.top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Wash 2 to MA12
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
m300.move_to(EtOH1.top(-16))
m300.aspirate(EtOH_vol2, EtOH2.top(-12))
m300.dispense(EtOH_vol2, MA12.top(-4))
m300.set_flow_rate(aspirate=100, dispense=100)
m300.mix(5, EtOH_vol2, MA12.bottom(5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(MA12.top(-10))
m300.blow_out()
m300.return_tip()

mag_deck.engage(height=16)
m300.delay(minutes=2)

### Remove supernatant, by re-using tiprack 3
### Remove supernatant from MA1
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A1'))
m300.aspirate(EtOH_vol2, MA1.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA2
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A2'))
m300.aspirate(EtOH_vol2, MA2.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA3
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A3'))
m300.aspirate(EtOH_vol2, MA3.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA4
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A4'))
m300.aspirate(EtOH_vol2, MA4.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA5
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A5'))
m300.aspirate(EtOH_vol2, MA5.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA6
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A6'))
m300.aspirate(EtOH_vol2, MA6.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA7
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A7'))
m300.aspirate(EtOH_vol2, MA7.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA8
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A8'))
m300.aspirate(EtOH_vol2, MA8.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA9
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A9'))
m300.aspirate(EtOH_vol2, MA9.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA10
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A10'))
m300.aspirate(EtOH_vol2, MA1.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA11
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A11'))
m300.aspirate(EtOH_vol2, MA11.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

### Remove supernatant from MA12
m300.set_flow_rate(aspirate=100, dispense=100)
m300.pick_up_tip(tipracks_200_3.wells('A12'))
m300.aspirate(EtOH_vol2, MA12.bottom(1))
m300.dispense(EtOH_vol2, trash_box.wells('A1').top(-5))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.blow_out(trash_box.wells('A1').top(-5))
m300.return_tip()

## Dry beads before elution
m300.delay(minutes=4)

## Elution of DNA

for target in samples:
    m300.set_flow_rate(aspirate=180, dispense=180)
    m300.pick_up_tip() # Slow down head speed 0.5X for bead handling
    max_speed_per_axis = {'x': (300), 'y': (300), 'z': (75), 'a': (75), 'b': (20), 'c': (20)}
    robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
    m300.set_flow_rate(aspirate=40, dispense=40)
    m300.transfer(Elution_vol, Elution_buffer, target.top(-2), air_gap=0, new_tip='never')
    m300.set_flow_rate(aspirate=50, dispense=50)
    m300.mix(3, 100, target.bottom(6))
    m300.delay(seconds=5)
    m300.move_to(target.top(-3))
    m300.blow_out()
    max_speed_per_axis = {'x': (600), 'y': (400), 'z': (100), 'a': (100), 'b': (40),'c': (40)}
    robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)
    m300.return_tip()

### Resets head speed for futher processing
max_speed_per_axis = {'x': (600), 'y': (400), 'z': (50), 'a': (50), 'b': (40),'c': (40)}
robot.head_speed(combined_speed=max(max_speed_per_axis.values()),**max_speed_per_axis)

### Incubate elutes for 15 minutes at room temperature
robot.pause("Please, incubate samples for 10 min at 37ºC and press resume after it")

### Transfer elutes to new plates.
### Transfer Elution buffer to elution_plate A1
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A1'))
m300.aspirate(Elution_vol, MA1.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A1').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A1').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A2
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A2'))
m300.aspirate(Elution_vol, MA2.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A2').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A2').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A3
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A3'))
m300.aspirate(Elution_vol, MA3.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A3').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A3').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A4
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A4'))
m300.aspirate(Elution_vol, MA4.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A4').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A4').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A5
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A5'))
m300.aspirate(Elution_vol, MA5.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A5').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A5').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A6
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A6'))
m300.aspirate(Elution_vol, MA6.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A6').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A6').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A7
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A7'))
m300.aspirate(Elution_vol, MA7.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A7').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A7').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A8
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A8'))
m300.aspirate(Elution_vol, MA8.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A8').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A8').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A9
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A9'))
m300.aspirate(Elution_vol, MA9.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A9').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A9').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A10
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A10'))
m300.aspirate(Elution_vol, MA10.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A10').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A10').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A11
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A11'))
m300.aspirate(Elution_vol, MA11.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A11').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A11').top(-10))
m300.blow_out()
m300.return_tip()

### Transfer Elution buffer to elution_plate A12
m300.set_flow_rate(aspirate=50, dispense=50)
m300.pick_up_tip(tipracks_200_4.wells('A12'))
m300.aspirate(Elution_vol, MA12.bottom(1))
m300.dispense(Elution_vol, elution_plate.wells('A12').bottom(2))
m300.delay(seconds=5)
m300.set_flow_rate(aspirate=130, dispense=130)
m300.move_to(elution_plate.wells('A12').top(-10))
m300.blow_out()
m300.return_tip()

mag_deck.disengage()

robot.pause("Yay! \ Purification has finished \ Please store purified libraries as -20°C \ Press resume when finished.")
