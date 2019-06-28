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

tipracks_200 = [labware.load('tiprack-200ul', slot, share=True)
               for slot in ['4','5','6']]



#### PIPETTE SETUP ####
m300 = instruments.P300_Multi(
    mount='right',
    tip_racks=tipracks_200)

#### REAGENT SETUP

Binding_buffer = trough.wells('A1')			# Buffer B

EtOH_Bind1 = trough.wells('A2')
EtOH_Bind2 = trough.wells('A3')


#### VOLUME SETUP


Sample_vol = 200
Binding_buffer_vol = Sample_vol*1
EtOH_buffer_vol = 350


#### PROTOCOL ####
## add beads and sample binding buffer to DNA/sample plate
mag_deck.disengage()
m300.distribute(Binding_buffer_vol, Binding_buffer, sample_plate.cols(), new_tip='once',  blow_out =True)


## add beads and EtOH binding buffer to RNA plate
mag_deck.disengage()
m300.distribute(EtOH_buffer_vol, EtOH_Bind1, RNA_plate.cols('1','2','3','4','5','6'), new_tip='once', blow_out =True)
m300.distribute(EtOH_buffer_vol, EtOH_Bind2, RNA_plate.cols('7','8','9','10','11','12'), new_tip='never', blow_out =True)

## Incubate beads
m300.delay(minutes=6)

## Transfer supernatant
mag_deck.engage(height=12)
m300.delay(minutes=5)
m300.transfer(175, sample_plate.cols('1'), RNA_plate.cols('1'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('1'), RNA_plate.cols('1'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('2'), RNA_plate.cols('2'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('2'), RNA_plate.cols('2'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('3'), RNA_plate.cols('3'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('3'), RNA_plate.cols('3'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('4'), RNA_plate.cols('4'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('4'), RNA_plate.cols('4'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('5'), RNA_plate.cols('5'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('5'), RNA_plate.cols('5'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('6'), RNA_plate.cols('6'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('6'), RNA_plate.cols('6'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('7'), RNA_plate.cols('7'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('7'), RNA_plate.cols('7'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('8'), RNA_plate.cols('8'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('8'), RNA_plate.cols('8'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('9'), RNA_plate.cols('9'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('9'), RNA_plate.cols('9'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('10'), RNA_plate.cols('10'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('10'), RNA_plate.cols('10'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('11'), RNA_plate.cols('11'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('11'), RNA_plate.cols('11'), mix_after=(8,200), new_tip='once',  blow_out =True)

m300.transfer(175, sample_plate.cols('12'), RNA_plate.cols('12'), new_tip='once',  blow_out =True)
m300.transfer(175, sample_plate.cols('12'), RNA_plate.cols('12'), mix_after=(8,200), new_tip='once',  blow_out =True)

robot.pause("Transfer DNA plate to fridge with cover-foil")
