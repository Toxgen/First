package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.util.ElapsedTime;

public class BlankLinearOpMode extends LinearOpMode {

private DcMotor fL;
private DcMotor fR;
private DcMotor bL;
private DcMotor	bR; 

    @Override
    public void runOpMode() {
		
      	fL = hardwareMap.get(DcMotor.class, "frontLeft");
        fR = hardwareMap.get(DcMotor.class, "frontRight");
        bL = hardwareMap.get(DcMotor.class, "backLeft");
        bR = hardwareMap.get(DcMotor.class, "backRight");
        telemetry.update();
      	waitForStart();

        while (opModeIsActive()) {
          	fR.setPower(-1); // idunno it worked like with 2 motors but now it doesnt work for 4 motors?
          	fL.setPower(1);	
          	bR.setPower(1);
          	bL.setPower(-1);
          	program.sleep(1000);
            fR.setPower(0);
          	fL.setPower(0);	
          	bR.setPower(0);
          	bL.setPower(0);
          	program.sleep(1000);
          	telemetry.update(); 

        }
    }
}
