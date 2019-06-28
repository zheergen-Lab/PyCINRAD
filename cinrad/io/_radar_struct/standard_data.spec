#generic_header#
magic_number i4
major_version short
minor_version short
generic_type i4
product_type i4
res1 16c
#site_config#
site_code 8c
site_name 32c
Latitude f4
Longitude f4
antenna_height i4
ground_height i4
frequency f4
beam_width_hori f4
beam_width_vert f4
RDA_version i4
radar_type short
antenna_gain short
trans_loss short
recv_loss short
other_loss short
res2 46c
#task_config#
task_name 32c
task_dsc 128c
polar_type i4
scan_type i4
pulse_width i4
scan_start_time i4
cut_number i4
hori_noise f4
vert_noise f4
hori_cali f4
vert_cali f4
hori_tmp f4
vert_tmp f4
ZDR_cali f4
PHIDP_cali f4
LDR_cali f4
res3 40c
#cut_config#
process_mode i4
wave_form i4
PRF1 f4
PRF2 f4
dealias_mode i4
azimuth f4
elev f4
start_angle f4
end_angle f4
angular_reso f4
scan_spd f4
log_reso i4
dop_reso i4
max_range1 i4
max_range2 i4
start_range i4
sample1 i4
sample2 i4
phase_mode i4
atmos_loss f4
nyquist_spd f4
moments_mask i8
moments_size_mask i8
misc_filter_mask i4
SQI_thres f4
SIG_thres f4
CSR_thres f4
LOG_thres f4
CPA_thres f4
PMI_thres f4
DPLOG_thres f4
res_thres 4V
dBT_mask i4
dBZ_mask i4
vel_mask i4
sw_mask i4
DP_mask i4
res_mask 12V
scan_sync i4
direction i4
ground_clutter_classifier_type short
ground_clutter_filter_type short
ground_clutter_filter_notch_width short
ground_clutter_filter_window short
res4 72V
#radial_header#
radial_state i4
spot_blank i4
seq_number i4
radial_number i4
elevation_number i4
azimuth f4
elevation f4
seconds i4
microseconds i4
data_length i4
moment_number i4
res5 short
hori_est_noise short
vert_est_noise short
zip_type c
res6 13c
#moment_header#
data_type i4
scale i4
offset i4
bin_length short
flags short
block_length i4
res 12c