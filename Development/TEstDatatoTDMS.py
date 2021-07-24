#Script for Test_Data_File_v2 to TDMS test file

import pandas as pd
from nptdms import TdmsFile
import numpy as np
from nptdms import TdmsWriter, GroupObject, ChannelObject

df = pd.read_pickle("/Users/Lillie/Downloads/DSFM_Test_Data/DSFM_test_data_v3.pkl")

def write_NMR(index, dataframe):
    ProbeName = "NMR"
    ProbeID = "Metrolab Technology SA,PT2026,25,elC2D1B2-arm1.21-dsp2.8-cpld1.9-pa3.7-opt00000000\n"
    Status = "OK"
    Timestamp = dataframe['TIMESTAMP'].loc[index]
    Fluxdensity = dataframe['B_NMR'].loc[index]
    NMR_array = np.array([f'ProbeName:{ProbeName}', f"ProbeID:{ProbeID}",f"FluxDensity:{Fluxdensity}", f"Status:{Status}", f"Timestamp:{Timestamp}" ])
    NMRchannel = ChannelObject(f'{step}','NMRProbe', NMR_array)
    return NMRchannel


def write_Hall(index, dataframe):
    SP1address = ''
    SP1temp = dataframe['HP_SP1_Temperature'].loc[index]
    SP1_Z_field = dataframe['HP_SP1_Bz_Meas'].loc[index]
    SP1_Y_field = dataframe['HP_SP1_By_Meas'].loc[index]
    SP1_X_field = dataframe['HP_SP1_Bx_Meas'].loc[index]
    SP1_Z_volt = dataframe['HP_SP1_Vz'].loc[index]
    SP1_Y_volt = dataframe['HP_SP1_Vy'].loc[index]
    SP1_X_volt = dataframe['HP_SP1_Vx'].loc[index]
    SP1_status = 'OK'
    SP1_Sensorname = 'SP1'
    SP1_SensorID = dataframe['HP_SP1_ID'].loc[index]
    SP1_Timestamp = dataframe['TIMESTAMP'].loc[index]

    SP2address = ''
    SP2temp = dataframe['HP_SP2_Temperature'].loc[index]
    SP2_Z_field = dataframe['HP_SP2_Bz_Meas'].loc[index]
    SP2_Y_field = dataframe['HP_SP2_By_Meas'].loc[index]
    SP2_X_field = dataframe['HP_SP2_Bx_Meas'].loc[index]
    SP2_Z_volt = dataframe['HP_SP2_Vz'].loc[index]
    SP2_Y_volt = dataframe['HP_SP2_Vy'].loc[index]
    SP2_X_volt = dataframe['HP_SP2_Vx'].loc[index]
    SP2_status = 'OK'
    SP2_Sensorname = 'SP2'
    SP2_SensorID = dataframe['HP_SP2_ID'].loc[index]
    SP2_Timestamp = dataframe['TIMESTAMP'].loc[index]

    SP3address = ''
    SP3temp = dataframe['HP_SP3_Temperature'].loc[index]
    SP3_Z_field = dataframe['HP_SP3_Bz_Meas'].loc[index]
    SP3_Y_field = dataframe['HP_SP3_By_Meas'].loc[index]
    SP3_X_field = dataframe['HP_SP3_Bx_Meas'].loc[index]
    SP3_Z_volt = dataframe['HP_SP3_Vz'].loc[index]
    SP3_Y_volt = dataframe['HP_SP3_Vy'].loc[index]
    SP3_X_volt = dataframe['HP_SP3_Vx'].loc[index]
    SP3_status = 'OK'
    SP3_Sensorname = 'SP3'
    SP3_SensorID = dataframe['HP_SP3_ID'].loc[index]
    SP3_Timestamp = dataframe['TIMESTAMP'].loc[index]

    BP1address = ''
    BP1temp = dataframe['HP_BP1_Temperature'].loc[index]
    BP1_Z_field = dataframe['HP_BP1_Bz_Meas'].loc[index]
    BP1_Y_field = dataframe['HP_BP1_By_Meas'].loc[index]
    BP1_X_field = dataframe['HP_BP1_Bx_Meas'].loc[index]
    BP1_Z_volt = dataframe['HP_BP1_Vz'].loc[index]
    BP1_Y_volt = dataframe['HP_BP1_Vy'].loc[index]
    BP1_X_volt = dataframe['HP_BP1_Vx'].loc[index]
    BP1_status = 'OK'
    BP1_Sensorname = 'BP1'
    BP1_SensorID = dataframe['HP_BP1_ID'].loc[index]
    BP1_Timestamp = dataframe['TIMESTAMP'].loc[index]

    BP2address = ''
    BP2temp = dataframe['HP_BP2_Temperature'].loc[index]
    BP2_Z_field = dataframe['HP_BP2_Bz_Meas'].loc[index]
    BP2_Y_field = dataframe['HP_BP2_By_Meas'].loc[index]
    BP2_X_field = dataframe['HP_BP2_Bx_Meas'].loc[index]
    BP2_Z_volt = dataframe['HP_BP2_Vz'].loc[index]
    BP2_Y_volt = dataframe['HP_BP2_Vy'].loc[index]
    BP2_X_volt = dataframe['HP_BP2_Vx'].loc[index]
    BP2_status = 'OK'
    BP2_Sensorname = 'BP2'
    BP2_SensorID = dataframe['HP_BP2_ID'].loc[index]
    BP2_Timestamp = dataframe['TIMESTAMP'].loc[index]

    BP3address = ''
    BP3temp = dataframe['HP_BP3_Temperature'].loc[index]
    BP3_Z_field = dataframe['HP_BP3_Bz_Meas'].loc[index]
    BP3_Y_field = dataframe['HP_BP3_By_Meas'].loc[index]
    BP3_X_field = dataframe['HP_BP3_Bx_Meas'].loc[index]
    BP3_Z_volt = dataframe['HP_BP3_Vz'].loc[index]
    BP3_Y_volt = dataframe['HP_BP3_Vy'].loc[index]
    BP3_X_volt = dataframe['HP_BP3_Vx'].loc[index]
    BP3_status = 'OK'
    BP3_Sensorname = 'BP3'
    BP3_SensorID = dataframe['HP_BP3_ID'].loc[index]
    BP3_Timestamp = dataframe['TIMESTAMP'].loc[index]

    BP4address = ''
    BP4temp = dataframe['HP_BP4_Temperature'].loc[index]
    BP4_Z_field = dataframe['HP_BP4_Bz_Meas'].loc[index]
    BP4_Y_field = dataframe['HP_BP4_By_Meas'].loc[index]
    BP4_X_field = dataframe['HP_BP4_Bx_Meas'].loc[index]
    BP4_Z_volt = dataframe['HP_BP4_Vz'].loc[index]
    BP4_Y_volt = dataframe['HP_BP4_Vy'].loc[index]
    BP4_X_volt = dataframe['HP_BP4_Vx'].loc[index]
    BP4_status = 'OK'
    BP4_Sensorname = 'BP4'
    BP4_SensorID = dataframe['HP_BP4_ID'].loc[index]
    BP4_Timestamp = dataframe['TIMESTAMP'].loc[index]

    BP5address = ''
    BP5temp = dataframe['HP_BP5_Temperature'].loc[index]
    BP5_Z_field = dataframe['HP_BP5_Bz_Meas'].loc[index]
    BP5_Y_field = dataframe['HP_BP5_By_Meas'].loc[index]
    BP5_X_field = dataframe['HP_BP5_Bx_Meas'].loc[index]
    BP5_Z_volt = dataframe['HP_BP5_Vz'].loc[index]
    BP5_Y_volt = dataframe['HP_BP5_Vy'].loc[index]
    BP5_X_volt = dataframe['HP_BP5_Vx'].loc[index]
    BP5_status = 'OK'
    BP5_Sensorname = 'BP5'
    BP5_SensorID = dataframe['HP_BP5_ID'].loc[index]
    BP5_Timestamp = dataframe['TIMESTAMP'].loc[index]

    Hall_array = np.array([f'Address:{SP1address}', f'Temperature:{SP1temp}', f'Z.field:{SP1_Z_field}', f'Y.field:{SP1_Y_field}', f'X.field:{SP1_X_field}', f'Z.zolt:{SP1_Z_volt}',f'Y.volt:{SP1_Y_volt}', f'X.volt:{SP1_X_volt}', f'Status:{SP1_status}', f'Sensor.name:{SP1_Sensorname}', f'Sensor.ID:{SP1_SensorID}', f'Timestamp:{SP1_Timestamp}',
                          f'Address:{SP2address}', f'Temperature:{SP2temp}', f'Z.field:{SP2_Z_field}', f'Y.field:{SP2_Y_field}', f'X.field:{SP2_X_field}', f'Z.zolt:{SP2_Z_volt}',f'Y.volt:{SP2_Y_volt}', f'X.volt:{SP2_X_volt}', f'Status:{SP2_status}', f'Sensor.name:{SP2_Sensorname}', f'Sensor.ID:{SP2_SensorID}', f'Timestamp:{SP2_Timestamp}',
                          f'Address:{SP3address}', f'Temperature:{SP3temp}', f'Z.field:{SP3_Z_field}', f'Y.field:{SP3_Y_field}', f'X.field:{SP3_X_field}', f'Z.zolt:{SP3_Z_volt}',f'Y.volt:{SP3_Y_volt}', f'X.volt:{SP3_X_volt}', f'Status:{SP3_status}', f'Sensor.name:{SP3_Sensorname}', f'Sensor.ID:{SP3_SensorID}', f'Timestamp:{SP3_Timestamp}',
                          f'Address:{BP1address}', f'Temperature:{BP1temp}', f'Z.field:{BP1_Z_field}', f'Y.field:{BP1_Y_field}', f'X.field:{BP1_X_field}', f'Z.zolt:{BP1_Z_volt}',f'Y.volt:{BP1_Y_volt}', f'X.volt:{BP1_X_volt}', f'Status:{BP1_status}', f'Sensor.name:{BP1_Sensorname}', f'Sensor.ID:{BP1_SensorID}', f'Timestamp:{BP1_Timestamp}',
                          f'Address:{BP2address}', f'Temperature:{BP2temp}', f'Z.field:{BP2_Z_field}', f'Y.field:{BP2_Y_field}', f'X.field:{BP2_X_field}', f'Z.zolt:{BP2_Z_volt}',f'Y.volt:{BP2_Y_volt}', f'X.volt:{BP2_X_volt}', f'Status:{BP2_status}', f'Sensor.name:{BP2_Sensorname}', f'Sensor.ID:{BP2_SensorID}', f'Timestamp:{BP2_Timestamp}',
                          f'Address:{BP3address}', f'Temperature:{BP3temp}', f'Z.field:{BP3_Z_field}', f'Y.field:{BP3_Y_field}', f'X.field:{BP3_X_field}', f'Z.zolt:{BP3_Z_volt}',f'Y.volt:{BP3_Y_volt}', f'X.volt:{BP3_X_volt}', f'Status:{BP3_status}', f'Sensor.name:{BP3_Sensorname}', f'Sensor.ID:{BP3_SensorID}', f'Timestamp:{BP3_Timestamp}',
                          f'Address:{BP4address}', f'Temperature:{BP4temp}', f'Z.field:{BP4_Z_field}', f'Y.field:{BP4_Y_field}', f'X.field:{BP4_X_field}', f'Z.zolt:{BP4_Z_volt}',f'Y.volt:{BP4_Y_volt}', f'X.volt:{BP4_X_volt}', f'Status:{BP4_status}', f'Sensor.name:{BP4_Sensorname}', f'Sensor.ID:{BP4_SensorID}', f'Timestamp:{BP4_Timestamp}',
                          f'Address:{BP5address}', f'Temperature:{BP5temp}', f'Z.field:{BP5_Z_field}', f'Y.field:{BP5_Y_field}', f'X.field:{BP5_X_field}', f'Z.zolt:{BP5_Z_volt}',f'Y.volt:{BP5_Y_volt}', f'X.volt:{BP5_X_volt}', f'Status:{BP5_status}', f'Sensor.name:{BP5_Sensorname}', f'Sensor.ID:{BP5_SensorID}', f'Timestamp:{BP5_Timestamp}'])
    HALLchannel = ChannelObject(f'{step}', 'HallProbes', Hall_array)
    return HALLchannel

def write_Timestamp(index, dataframe):
    timestamp = dataframe['TIMESTAMP'].loc[index]
    Timestamp_array = np.array([f'Timestamp:{timestamp}'])
    Timestampchannel = ChannelObject(f'{step}', 'Timestamp', Timestamp_array)
    return Timestampchannel

def write_Mapper(index,dataframe):
    timestamp = dataframe['TIMESTAMP'].loc[index]
    requestedangle = ''
    home = ''
    angle = dataframe['Mapper_Angle'].loc[index]
    mapperposition = dataframe['X_NMR'].loc[index]
    Mapper_array = np.array([f'Timestamp:{timestamp}', f'RequestedAngle:{requestedangle}', f'Home:{home}', f'Angle:{angle}', f'Position:{mapperposition}'])
    Mapperchannel = ChannelObject(f'{step}','Mapper',Mapper_array)
    return Mapperchannel

def write_Current(index, dataframe):
    timestamp = ''
    requestedcurrent = '0.000000'
    current ='0.000000'
    Current_array = np.array([f'Timestamp:{timestamp}', f'RequestedCurrent:{requestedcurrent}', f'Current:{current}'])
    Currentchannel = ChannelObject(f'{step}', 'Current', Current_array)
    return Currentchannel

def write_QC(index, dataframe):
    item1 = ''
    item2 = ''
    QC_array = np.array([f'{item1}', f'{item2}'])
    QCchannel = ChannelObject(f'{step}', 'QC', QC_array)
    return QCchannel

def write_stepID(index, dataframe):
    Step_array = np.array([f"{step}"])
    StepIDchannel = ChannelObject(f'{step}', 'StepID', Step_array)
    return StepIDchannel

def write_group(index, dataframe):
    timestamp = dataframe['TIMESTAMP'].loc[index]
    group = GroupObject(f"{step}", properties={
        "name": "FMSSystemTest_v2",
        "Time": f"{timestamp}", })
    wholegroup = tdms_writer.write_segment(
        [group, write_stepID(index, dataframe), write_Timestamp(index, dataframe), write_Mapper(index, dataframe),
         write_NMR(index, dataframe), write_Hall(index, dataframe),
         write_QC(index, dataframe), write_Current(index, dataframe)])
    return wholegroup

def write_ID(dataframe):
    id = 'R_2021'
    id_array = np.array([f'{id}'])
    IDchannel = ChannelObject('run:R_2021', 'ID', id_array)
    return IDchannel

def write_Time(dataframe):
    timestamp = dataframe['TIMESTAMP'].loc[0]
    time_array = np.array([f'{timestamp}'])
    Timechannel = ChannelObject('run:R_2021', 'Time',time_array)
    return Timechannel

def write_magnet(dataframe):
    magnet = 'Argonne'
    magnet_array = np.array([f'{magnet}'])
    Magnetchannel = ChannelObject('run:R_2021', 'magnet', magnet_array)
    return Magnetchannel

def write_measurement(dataframe):
    meas = 'FMS'
    measurement_array = np.array([f'{meas}'])
    Measurementchannel = ChannelObject('run:R_2021', 'measurement', measurement_array)
    return Measurementchannel

def write_configuration(dataframe):
    config = 'C:\\Users\\fms-local\\Development\\FMS\\emma_daq\\Property\\Config\\Devel\\FMS_SystemTestNorthwestern2021.ini'
    config_array = np.array([f'{config}'])
    Configchannel = ChannelObject('run:R_2021', 'configuration', config_array)
    return Configchannel

def write_user(dataframe):
    user = 'Northwestern'
    user_array = np.array([f'{user}'])
    Userchannel = ChannelObject('run:R_2021', 'user', user_array)
    return Userchannel

def write_script(dataframe):
    script = 'FMS_SystemTestNorthwestern2021.py'
    script_array = np.array([f'{script}'])
    scriptchannel = ChannelObject('run:R_2021', 'script', script_array)
    return scriptchannel

def write_scriptparameters(dataframe):
    sp = 'FMS.dat'
    sp_array = np.array([f'{sp}'])
    spchannel = ChannelObject('run:R_2021', 'scriptParameters', sp_array)
    return spchannel

def write_scriptfolder(dataframe):
    sf = 'C:\\Users\\fms-local\\Development\\FMS\\emma_daq\\Script\\Scripts'
    sf_array = np.array([f'{sf}'])
    sfchannel = ChannelObject('run:R_2021', 'scriptFolder', sf_array)
    return sfchannel

def write_file(dataframe):
    file = 'C:\\FMS\\data\\Northwestern\\FMSSystemTest_R_2021.tdms'
    file_array = np.array([f'{file}'])
    filechannel = ChannelObject('run:R_2021', 'File', file_array)
    return filechannel

def write_system(dataframe):
    system = 'FMS'
    system_array = np.array([f'{system}'])
    systemchannel = ChannelObject('run:R_2021', 'system', system_array)
    return systemchannel

def write_initalilizationgroup(dataframe):
    group = GroupObject("run:R_2021", properties={
       })
    wholegroup = tdms_writer.write_segment([group, write_ID(dataframe), write_Time(dataframe), write_magnet(dataframe),
                                            write_measurement(dataframe), write_configuration(dataframe), write_user(dataframe),
                                            write_script(dataframe), write_scriptparameters(dataframe), write_scriptfolder(dataframe),
                                            write_file(dataframe), write_system(dataframe)])
    return wholegroup


######## Write file


with TdmsWriter("TestDataV2.tdms") as tdms_writer:
    dataframe = df
    dataframe["digit_one"]=0
    dataframe["digit_two"]=0
    dataframe["GroupID"]= 'Step:0.0.0' # Step.digittwo.digitone
    write_initalilizationgroup(dataframe)

    for index, row in df.iterrows():
        #create the stepID, stored in new column GroupID
        if index == 0:
            idlastrow = 0
        else:
            idlastrow = df.loc[index-1, "digit_one"]
        if index == 0:
            df.loc[index, "digit_two"] = 1
        if idlastrow == 16:
            df.loc[index,"digit_one"] = number = 1
            df.loc[index, "digit_two"] = df.loc[index-1, "digit_two"] + 1
        else:
            df.loc[index, "digit_one"] = number = idlastrow+1
        if index != 0 and idlastrow != 16:
            df.loc[index, "digit_two"] = df.loc[index-1, "digit_two"]
        seconddigit = df["digit_two"].loc[index]
        df.loc[index,"GroupID"] = f'Step:1.{seconddigit}.{number}'
        #write the group for the GroupID
        step = df["GroupID"].loc[index]
        write_group(index, df)

