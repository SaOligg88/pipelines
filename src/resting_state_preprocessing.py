import nipype.pipeline.engine as pe
import nipype.interfaces.utility as util
import nipype.interfaces.fsl as fsl
import nipype.interfaces.nipy as nipy
import nipype.interfaces.freesurfer as fs

def create_resting_state_preprocessing_WF(name="preprocess"):
    wf = pe.Workflow(name=name)
    inputspec = pe.Node(util.IdentityInterface(fields=['resting', 'structural']), name="inputspec")
    
    skip = pe.Node(fsl.ExtractROI(), name="skip")
    skip.inputs.t_min = 4
    skip.inputs.t_size = -1
    
    wf.connect(inputspec, "resting", skip, "in_file")
    
    slice_time_realign = pe.Node(nipy.FmriRealign4d(), name="slice_time_realign")
    slice_time_realign.inputs.tr = 2.3
    slice_time_realign.inputs.slice_order = range(0,34,2) + range(1,34,2)
    slice_time_realign.inputs.time_interp = True
    
    wf.connect(skip, "roi_file", slice_time_realign, "in_file")
    
    recon_all = pe.Node(fs.ReconAll(), name="recon_all")
    wf.connect(inputspec, "structural", recon_all, "T1_files")
    
    mean_resting = pe.Node(fsl.MeanImage(), name="mean_resting")
    mean_resting.inputs.dimension = "T"
    
    wf.connect(slice_time_realign, "out_file", mean_resting, "in_file")
    
    register_funct_to_struct = pe.Node(fs.BBRegister(), name="register_func_to_struct")
    register_funct_to_struct.inputs.out_fsl_file = True
    
    wf.connect(mean_resting, "out_file", register_funct_to_struct, "source_file")
    wf.connect(recon_all, "subject_id", register_funct_to_struct, "subject_id")
    wf.connect(recon_all, "subjects_dir", register_funct_to_struct, "subjects_dir")
    
    
    return wf

if __name__ == '__main__':
    preprocess = create_resting_state_preprocessing_WF()
    preprocess.base_dir = "/Users/filo/workdir/rs_preprocessing"
    
    preprocess.inputs.inputspec.resting = "/Users/filo/data/rs_pipeline/GSDT/func/rest.nii"
    preprocess.inputs.inputspec.structural = "/Users/filo/data/rs_pipeline/GSDT/anat/mprage.nii"
    
    preprocess.run()