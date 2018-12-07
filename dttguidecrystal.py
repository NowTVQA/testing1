# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:22:00 2017

@author: 1549245
"""


import stormtest.ClientAPI as StormTest
# Global return value definitions
import TestEnvironment


logParam = [57600, 8, "none", 1, "none", "TestName"]



def doTest():
    i = 0

    for i in range (5):
        
        '''1st step: Go to DTT ch.031'''
        step_name = "Step"+str(5*i+1)+": Go to DTT ch.031"
        StormTest.BeginTestStep(step_name)
        
        StormTest.PressButton('Stop')
        StormTest.PressDigits(031, waitSec=0.5)
        
        ret_motion = StormTest.DetectMotionEx((559, 179, 655, 301), 5)
        if ret_motion[0][1]:
            step_comment = "Go to DTT ch.31 is success"
            print ret_motion
            StormTest.EndTestStep(step_name,StormTest.TM.PASS,step_comment)
        else:
            step_comment = "Go to DTT ch.31 is failed"
            StormTest.EndTestStep(step_name,StormTest.TM.FAIL,step_comment)
        
        print step_comment
        StormTest.CaptureImageEx(None, "Step1.png")

        
        '''2st step: Go to DTT Duide'''
        step_name = "Step "+str(5*i+2)+": Go to DTT Duide"
        StormTest.BeginTestStep(step_name)
        StormTest.PressButton('TV_Guide')
        StormTest.WaitSec(5)
           
        ret = [83, 34, 230, 58]
        ocr_result = StormTest.OCRSlot(ret)
        print ocr_result
        if ocr_result[4][0][1].strip() == 'DTT GUIDE':
            step_comment = "Go to DTT Guide success"
            print ocr_result
            StormTest.EndTestStep(step_name,StormTest.TM.PASS,step_comment)
        else:
            step_comment = "Go to DTT Guide is failed"
            StormTest.EndTestStep(step_name,StormTest.TM.FAIL,step_comment)
        
        print step_comment    
        StormTest.CaptureImageEx(None, "Step2.png")
        
        
        '''3rd step: Check program name'''
        step_name = "Step"+str(5*i+3)+": Check program name"
        StormTest.BeginTestStep(step_name)
        
        ret_name = [420, 643, 414, 37]
        ocr_result_name = StormTest.OCRSlot(ret_name)
        print ocr_result_name
        if ocr_result_name [4][0][1] != '':
            step_comment = "Program name is correct"
            print ocr_result_name
            StormTest.EndTestStep(step_name,StormTest.TM.PASS,step_comment)
        else:
            step_comment = "Program name is incorrect"
            StormTest.EndTestStep(step_name,StormTest.TM.FAIL,step_comment)
        
        print step_comment
        StormTest.CaptureImageEx(None, "Step3.png")
        
        
        '''4th step: Exit to Live'''
        step_name = "Step "+str(5*i+4)+": Exit to Live"
        StormTest.BeginTestStep(step_name)
        
        StormTest.PressButton('Ok')
        ret_motion_live = StormTest.DetectMotionEx((359, 163, 1135, 371), 5)
        if ret_motion_live[0][1]:
            step_comment = "Exit to Live success"
            print ret_motion_live
            StormTest.EndTestStep(step_name,StormTest.TM.PASS,step_comment)
        else:
            step_comment = "Exit to Live is failed"
            StormTest.EndTestStep(step_name,StormTest.TM.FAIL,step_comment)
        
        print step_comment
        StormTest.CaptureImageEx(None, "Step4.png")
        
        
        '''5th step: Check program name on Mini-Guide'''
        step_name = "Step "+str(5*i+5)+": Check program name on Mini-Guide"
        StormTest.BeginTestStep(step_name)
        
        ret_name = [222, 678, 448, 41]
        ocr_result_name_step_5 = StormTest.OCRSlot(ret_name)
        print ocr_result_name_step_5
        if ocr_result [4][0][1].strip() == ocr_result_name[4][0][1]:
            step_comment = "Program name is correct"
            print ocr_result_name
            StormTest.EndTestStep(step_name,StormTest.TM.PASS,step_comment)
        else:
            step_comment = "Program name is incorrect"
            StormTest.EndTestStep(step_name,StormTest.TM.FAIL,step_comment)
        
        print step_comment
        StormTest.CaptureImageEx(None, "Step5.png")
        
        StormTest.PressButton('Channel+')
           
    return StormTest.TM.PASS


def setup():
    try:
        # Connect to the StormTest server, e.g. "jack", or "123.123.123.123",
        # and send a comment to help others to identify the purpose of the test
        StormTest.ConnectToServer(TestEnvironment.ServerName, "Hello World Test")
    
        # Reserves a slot on the server and start serial logging
        slot_resa_result = StormTest.ReserveSlot(5, TestEnvironment.RC_KeySet, logParam, False )
    
        if slot_resa_result == 1:
            StormTest.ShowVideo()
            #StormTest.StartVideoLog()
            test_result = doTest()
            StormTest.CloseVideo()
            #StormTest.StopVideoLog()
        else:
            test_result = StormTest.TM.NOT_RUN    

    
    except:
        import traceback
        traceback.print_exc()
        test_result = StormTest.TM.FAIL
    # End of test - release ports back to the server
    finally:
        StormTest.ReleaseServerConnection()
        # Return test result
        return test_result   
        
        
# So that this module can be used as reusable module, or as standalone program
if __name__ == '__main__':

    result = setup()
    StormTest.ReturnTestResult(result)
    
    
    
    
    