from math import pi


def ddr_fk(L_rad, R_rad, L=0.7, r=0.15):
    """DDR inverse kinematics: calculate wheels speeds from desired velocity."""
    return (L_rad+R_rad)*r/2 , (R_rad-L_rad)*r/L

def ddr_ik(v_x, omega, L=0.7, r=0.15):
    """DDR inverse kinematics: calculate wheels speeds from desired velocity."""
    return (v_x - (L/2)*omega)/r, (v_x + (L/2)*omega)/r

phidot_L, phidot_R = ddr_ik(v_x=0.2, omega=0.3) #可以改動v 跟omega來檢驗角度(rad/s)是否正常
L_degs = phidot_L*180/pi
R_degs = phidot_R*180/pi
print(phidot_L,"rad/s", phidot_R,"rad/s")
print(L_degs,"deg/s", R_degs,"deg/s")

V_rad, Omega_rad = ddr_fk(L_rad = 0.6333333333333334 , R_rad = 2.033333333333333) #把Lrpm Rrpm 轉成rad/s 放進變數內
print("velocity: ",V_rad,"m/s","  omega: ",Omega_rad,"m/s")