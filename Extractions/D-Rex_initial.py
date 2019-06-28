## Description of procedure ##
#
#
# Things do before procedure
#
#	1. Bead beat samples at maximum speed for 5 minutes (If needed do Proteinase K for digestion of tissue)
# 	2. Spin down samples 10.000 rpm for 1 minute
#	3. Transfer 200µl lysed sample to a deep well plate

### Procedure ###


######## IMPORT LIBRARIES ########
from opentrons import labware, instruments, modules, robot

#### METADATA ####



metadata = {
    'protocolName': 'D-Rex Inital Extraction',
    'author': 'Jacob Agerbo Rasmussen <genomicsisawesome@gmail.com>',
    'version': '1.0',
    'date': '2019/03/28',
    'description': 'Automation of D-Rex RNA and DNA seperation for extraction protocol of stool samples in SHIELD',
}


#### LABWARE SETUP ####
trough = labware.load('trough-12row', '2')
RNA_plate = labware.load('96-deep-well', '1')
mag_deck = modules.load('magdeck', '7')
sample_plate = labware.load('96-deep-well', '7', share=True)

tipracks_200 = [labware.load('tiprack-200ul', slot)
               for slot in ['4','5','6','11']]



#### PIPETTE SETUP ####
p50 = instruments.P50_Single(
    mount='right',
    tip_racks=tipracks_200)

m300 = instruments.P300_Multi(
    mount='left',
    tip_racks=tipracks_200)

#### REAGENT SETUP

Binding_buffer = trough.wells('A1')			# Buffer B

EtOH_Bind1 = trough.wells('A2')
EtOH_Bind2 = trough.wells('A3')

Liquid_trash = trash_box.wells('A1')

#### VOLUME SETUP


Sample_vol = 200
Binding_buffer_vol = Sample_vol
EtOH_buffer_vol = 350


#### PROTOCOL ####
## add beads and sample binding buffer to DNA plate
mag_deck.disengage()
m300.distribute(Binding_buffer_vol, Binding_buffer, [well.top() for well in sample_plate.wells()],mix_after=(8,200) , new_tip='once',  blow_out =True)
m300.delay(minutes=10)

## add beads and EtOH binding buffer to RNA plate
mag_deck.disengage()
m300.distribute(EtOH_buffer_vol, EtOH_Bind1, [well.bottom() for well in RNA_plate.wells()], new_tip='once',  blow_out =True)


## Transfer supernatant
mag_deck.engage()
m300.delay(minutes=5)
m300.transfer(350, [well.top() for well in sample_plate.wells()], RNA_plate,mix_after=(8,200), new_tip='always',  blow_out =True)
robot.pause("Transfer DNA plate to fridge with cover-foil")
