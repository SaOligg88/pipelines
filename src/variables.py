'''
Created on Oct 11, 2012

@author: gorgolewski
'''
#import os
#subjects = os.listdir("/scr/namibia1/baird/MPI_Project/Neuroimaging_Data/")

subjects = ['11065.70',
'07070.79',
'13061.30',
'18066.85',
'10576.44',
'11944.79',
'11111.28',
'13536.51',
'14102.d1',
'12522.80',
'06222.f4',
'13649.8d',
'13565.7c',
'14018.65',
'14388.48',
'14110.f4',
'15006.be',
'03796.a8',
'10080.62',
'10581.e8',
'06275.e0',
'15475.c7',
'09561.e0',
'10960.82',
'14390.d3',
'17421.31',
'15466.cb',
'14702.ea',
'15403.c5',
'14081.cb',
'15890.ea',
'13989.a7',
'02231.e3',
'16101.0d',
'16939.4f',
'12184.55',
'07296.ec',
'16758.c3',
'12961.f8',
'12315.9a',
'15070.25',
'15640.65',
'18015.4c',
'14446.fb',
'14075.bd',
'16090.c9',
'19417.87',
'18761.dc',
'18758.73',
'17845.a2',
'18579.10',
'13085.b0',
'18094.87',
'16056.3d',
'10363.85',
'12339.39',
'09169.c5',
'14074.a7',
'13261.8d',
'11109.5c',
'19091.a3',
'16105.7a',
'11960.6a',
'13630.5d',
'09440.22',
'10439.86',
'11059.75',
'07346.36']

exclude_subjects = ['02231.e3',
'03796.a8',
'10363.85',
'11065.70',
'12962.f2',
'13061.30',
'13649.8d',
'17815.6e',
'18015.4c',
'18066.85']
#subjects = ["14074.a7", "11111.28", "15640.65"]

short_seq_subjects = ['17815.6e', '12988.0e', '19032.10', '17765.54',
                      '17819.fa', '15189.fb', '11400.94']

subjects = list(set(subjects) - set(exclude_subjects))

workingdir = "/scr/adenauer1/workingdir"
resultsdir = "/scr/namibia1/baird/MPI_Project/results"
#resultsdir = "/scr/adenauer1/results"

freesurferdir = '/scr/namibia1/baird/MPI_Project/freesurfer/'

rois = [(26,58,0), (-26,58,0), (14,66,0), (-14,66,0), (6,58,0), (-6,58,0)]

#subjects = ["11111.28"]
