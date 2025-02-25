import SimpleITK as sitk

asl_path = r'./asl.nii.gz'
rai_path = r'./rai.nii.gz'

asl = sitk.ReadImage(asl_path)
rai = sitk.ReadImage(rai_path)
asl_ = sitk.PermuteAxes(asl, [2, 0, 1])
asl_ = sitk.Flip(asl_, (True, False, True))
asl_.SetDirection(rai.GetDirection())

asl_origin = asl.GetOrigin()
asl_spacing = asl.GetSpacing()
asl_size = asl.GetSize()
rai_origin = rai.GetOrigin()
new_origin = (rai_origin[0], rai_origin[1], asl_origin[2] - asl_spacing[2] * (asl_size[2]-1))
asl_.SetOrigin(rai.GetOrigin())

sitk.WriteImage(asl_, 'asl2rai.nii.gz')

