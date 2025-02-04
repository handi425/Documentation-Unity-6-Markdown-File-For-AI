[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# DeviceGeneration

enumeration

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

iOS device generation.

    
    
    using UnityEngine;
    using UnityEngine.iOS;  
      
    public class DeviceGenerationExample : [MonoBehaviour](MonoBehaviour.html)
    {
        string m_DeviceGeneration = "Undefined";  
      
        void Start()
        {
            // Check if the device running this is an "iPhone 14 Pro Max"
            if ([Device.generation](iOS.Device-generation.html) == [DeviceGeneration.iPhone14ProMax](iOS.DeviceGeneration-iPhone14ProMax.html))
            {
                m_DeviceGeneration = "iPhone 14 Pro Max";
            }
            
            // Check if the device running this is an 'iPad Mini (6th generation)"
            if ([Device.generation](iOS.Device-generation.html) == [DeviceGeneration.iPadMini6Gen](iOS.DeviceGeneration-iPadMini6Gen.html))
            {
                m_DeviceGeneration = "iPad Mini (6th generation)";
            }
            
            // Check if the device running this is an "iPod [Touch](Touch.html) (7th generation)"
            if ([Device.generation](iOS.Device-generation.html) == [DeviceGeneration.iPodTouch7Gen](iOS.DeviceGeneration-iPodTouch7Gen.html))
            {
                m_DeviceGeneration = "iPod [Touch](Touch.html) (7th generation)";
            }  
      
            // Check if the device running this is an unknown iPhone
            if ([Device.generation](iOS.Device-generation.html) == [DeviceGeneration.iPhoneUnknown](iOS.DeviceGeneration-iPhoneUnknown.html))
            {
                m_DeviceGeneration = "Unknown iPhone";
            }
            
            // Check if the device running this is an unknown iPad
            if ([Device.generation](iOS.Device-generation.html) == [DeviceGeneration.iPadUnknown](iOS.DeviceGeneration-iPadUnknown.html))
            {
                m_DeviceGeneration = "Unknown iPad";
            }
            
            // Check if the device running this is an unknown iPod [Touch](Touch.html)
            if ([Device.generation](iOS.Device-generation.html) == [DeviceGeneration.iPodTouchUnknown](iOS.DeviceGeneration-iPodTouchUnknown.html))
            {
                m_DeviceGeneration = "Unknown iPod [Touch](Touch.html)";
            }
            
            // Output the device generation to the console/device log
            [Debug.Log](Debug.Log.html)("[Device](iOS.Device.html) generation: " + m_DeviceGeneration);
        }
    }
    

### Properties

[iPhone](iOS.DeviceGeneration-iPhone.html)| iPhone, first generation.  
---|---  
[iPhone3G](iOS.DeviceGeneration-iPhone3G.html)| iPhone, second generation.  
[iPhone3GS](iOS.DeviceGeneration-iPhone3GS.html)| iPhone, third generation.  
[iPodTouch1Gen](iOS.DeviceGeneration-iPodTouch1Gen.html)| iPod Touch, first
generation.  
[iPodTouch2Gen](iOS.DeviceGeneration-iPodTouch2Gen.html)| iPod Touch, second
generation.  
[iPodTouch3Gen](iOS.DeviceGeneration-iPodTouch3Gen.html)| iPod Touch, third
generation.  
[iPad1Gen](iOS.DeviceGeneration-iPad1Gen.html)| iPad, first generation.  
[iPhone4](iOS.DeviceGeneration-iPhone4.html)| iPhone, fourth generation.  
[iPodTouch4Gen](iOS.DeviceGeneration-iPodTouch4Gen.html)| iPod Touch, fourth
generation.  
[iPad2Gen](iOS.DeviceGeneration-iPad2Gen.html)| iPad, second generation.  
[iPhone4S](iOS.DeviceGeneration-iPhone4S.html)| iPhone, fifth generation.  
[iPad3Gen](iOS.DeviceGeneration-iPad3Gen.html)| iPad, third generation.  
[iPhone5](iOS.DeviceGeneration-iPhone5.html)| iPhone5.  
[iPodTouch5Gen](iOS.DeviceGeneration-iPodTouch5Gen.html)| iPod Touch, fifth
generation.  
[iPadMini1Gen](iOS.DeviceGeneration-iPadMini1Gen.html)| iPad Mini, first
generation.  
[iPad4Gen](iOS.DeviceGeneration-iPad4Gen.html)| iPad, fourth generation.  
[iPhone5C](iOS.DeviceGeneration-iPhone5C.html)| iPhone 5C.  
[iPhone5S](iOS.DeviceGeneration-iPhone5S.html)| iPhone 5S.  
[iPadAir1](iOS.DeviceGeneration-iPadAir1.html)| iPad Air.  
[iPadMini2Gen](iOS.DeviceGeneration-iPadMini2Gen.html)| iPad Mini, second
generation.  
[iPhone6](iOS.DeviceGeneration-iPhone6.html)| iPhone 6.  
[iPhone6Plus](iOS.DeviceGeneration-iPhone6Plus.html)| iPhone 6 plus.  
[iPadMini3Gen](iOS.DeviceGeneration-iPadMini3Gen.html)| iPad Mini, third
generation.  
[iPadAir2](iOS.DeviceGeneration-iPadAir2.html)| iPad Air 2.  
[iPhone6S](iOS.DeviceGeneration-iPhone6S.html)| iPhone 6S.  
[iPhone6SPlus](iOS.DeviceGeneration-iPhone6SPlus.html)| iPhone 6S Plus.  
[iPadPro1Gen](iOS.DeviceGeneration-iPadPro1Gen.html)| iPad Pro 12.9", first
generation.  
[iPadMini4Gen](iOS.DeviceGeneration-iPadMini4Gen.html)| iPad Mini, fourth
generation.  
[iPhoneSE1Gen](iOS.DeviceGeneration-iPhoneSE1Gen.html)| iPhone SE, first
generation.  
[iPadPro10Inch1Gen](iOS.DeviceGeneration-iPadPro10Inch1Gen.html)| iPad Pro
9.7", first generation.  
[iPhone7](iOS.DeviceGeneration-iPhone7.html)| iPhone 7.  
[iPhone7Plus](iOS.DeviceGeneration-iPhone7Plus.html)| iPhone 7 Plus.  
[iPodTouch6Gen](iOS.DeviceGeneration-iPodTouch6Gen.html)| iPod Touch, sixth
generation.  
[iPad5Gen](iOS.DeviceGeneration-iPad5Gen.html)| iPad, fifth generation.  
[iPadPro2Gen](iOS.DeviceGeneration-iPadPro2Gen.html)| iPad Pro 12.9", second
generation.  
[iPadPro10Inch2Gen](iOS.DeviceGeneration-iPadPro10Inch2Gen.html)| iPad Pro
10.5", second generation 10" iPad.  
[iPhone8](iOS.DeviceGeneration-iPhone8.html)| iPhone 8.  
[iPhone8Plus](iOS.DeviceGeneration-iPhone8Plus.html)| iPhone 8 Plus.  
[iPhoneX](iOS.DeviceGeneration-iPhoneX.html)| iPhone X.  
[iPhoneXS](iOS.DeviceGeneration-iPhoneXS.html)| iPhone XS.  
[iPhoneXSMax](iOS.DeviceGeneration-iPhoneXSMax.html)| iPhone XSMax.  
[iPhoneXR](iOS.DeviceGeneration-iPhoneXR.html)| iPhone XR.  
[iPadPro11Inch](iOS.DeviceGeneration-iPadPro11Inch.html)| iPad Pro 11", first
generation.  
[iPadPro3Gen](iOS.DeviceGeneration-iPadPro3Gen.html)| iPad Pro 12.9", third
generation.  
[iPad6Gen](iOS.DeviceGeneration-iPad6Gen.html)| iPad, sixth generation.  
[iPadAir3Gen](iOS.DeviceGeneration-iPadAir3Gen.html)| iPad Air, third
generation.  
[iPadMini5Gen](iOS.DeviceGeneration-iPadMini5Gen.html)| iPad Mini, fifth
generation.  
[iPhone11](iOS.DeviceGeneration-iPhone11.html)| iPhone 11.  
[iPhone11Pro](iOS.DeviceGeneration-iPhone11Pro.html)| iPhone 11 Pro.  
[iPhone11ProMax](iOS.DeviceGeneration-iPhone11ProMax.html)| iPhone 11 Pro Max.  
[iPodTouch7Gen](iOS.DeviceGeneration-iPodTouch7Gen.html)| iPod Touch, seventh
generation.  
[iPad7Gen](iOS.DeviceGeneration-iPad7Gen.html)| iPad, seventh generation.  
[iPhoneSE2Gen](iOS.DeviceGeneration-iPhoneSE2Gen.html)| iPhone SE, second
generation.  
[iPadPro11Inch2Gen](iOS.DeviceGeneration-iPadPro11Inch2Gen.html)| iPad Pro
11", second generation.  
[iPadPro4Gen](iOS.DeviceGeneration-iPadPro4Gen.html)| iPad Pro 12.9", fourth
generation.  
[iPhone12Mini](iOS.DeviceGeneration-iPhone12Mini.html)| iPhone 12 Mini.  
[iPhone12](iOS.DeviceGeneration-iPhone12.html)| iPhone 12.  
[iPhone12Pro](iOS.DeviceGeneration-iPhone12Pro.html)| iPhone 12 Pro.  
[iPhone12ProMax](iOS.DeviceGeneration-iPhone12ProMax.html)| iPhone 12 Pro Max.  
[iPad8Gen](iOS.DeviceGeneration-iPad8Gen.html)| iPad, eighth generation.  
[iPadAir4Gen](iOS.DeviceGeneration-iPadAir4Gen.html)| iPad Air, fourth
generation.  
[iPad9Gen](iOS.DeviceGeneration-iPad9Gen.html)| iPad, ninth generation.  
[iPadMini6Gen](iOS.DeviceGeneration-iPadMini6Gen.html)| iPad Mini, sixth
generation.  
[iPhone13](iOS.DeviceGeneration-iPhone13.html)| iPhone 13.  
[iPhone13Mini](iOS.DeviceGeneration-iPhone13Mini.html)| iPhone 13 Mini.  
[iPhone13Pro](iOS.DeviceGeneration-iPhone13Pro.html)| iPhone 13 Pro.  
[iPhone13ProMax](iOS.DeviceGeneration-iPhone13ProMax.html)| iPhone 13 Pro Max.  
[iPadPro5Gen](iOS.DeviceGeneration-iPadPro5Gen.html)| iPad Pro 12.9", fifth
generation.  
[iPadPro11Inch3Gen](iOS.DeviceGeneration-iPadPro11Inch3Gen.html)| iPad Pro
11", third generation.  
[iPhoneSE3Gen](iOS.DeviceGeneration-iPhoneSE3Gen.html)| iPhone SE, third
generation.  
[iPadAir5Gen](iOS.DeviceGeneration-iPadAir5Gen.html)| iPad Air, fifth
generation.  
[iPhone14](iOS.DeviceGeneration-iPhone14.html)| iPhone 14.  
[iPhone14Plus](iOS.DeviceGeneration-iPhone14Plus.html)| iPhone 14 Plus.  
[iPhone14Pro](iOS.DeviceGeneration-iPhone14Pro.html)| iPhone 14 Pro.  
[iPhone14ProMax](iOS.DeviceGeneration-iPhone14ProMax.html)| iPhone 14 Pro Max.  
[iPadPro6Gen](iOS.DeviceGeneration-iPadPro6Gen.html)| iPad Pro 12.9", sixth
generation.  
[iPadPro11Inch4Gen](iOS.DeviceGeneration-iPadPro11Inch4Gen.html)| iPad Pro
11", fourth generation.  
[iPad10Gen](iOS.DeviceGeneration-iPad10Gen.html)| iPad, tenth generation.  
[iPhone15](iOS.DeviceGeneration-iPhone15.html)| iPhone 15.  
[iPhone15Plus](iOS.DeviceGeneration-iPhone15Plus.html)| iPhone 15 Plus.  
[iPhone15Pro](iOS.DeviceGeneration-iPhone15Pro.html)| iPhone 15 Pro.  
[iPhone15ProMax](iOS.DeviceGeneration-iPhone15ProMax.html)| iPhone 15 Pro Max.  
[iPhone16](iOS.DeviceGeneration-iPhone16.html)| iPhone 16.  
[iPhone16Plus](iOS.DeviceGeneration-iPhone16Plus.html)| iPhone 16 Plus.  
[iPhone16Pro](iOS.DeviceGeneration-iPhone16Pro.html)| iPhone 16 Pro.  
[iPhone16ProMax](iOS.DeviceGeneration-iPhone16ProMax.html)| iPhone 16 Pro Max.  
[iPhoneUnknown](iOS.DeviceGeneration-iPhoneUnknown.html)| Yet unknown iPhone.  
[iPadUnknown](iOS.DeviceGeneration-iPadUnknown.html)| Yet unknown iPad.  
[iPodTouchUnknown](iOS.DeviceGeneration-iPodTouchUnknown.html)| Yet unknown
iPod Touch.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

