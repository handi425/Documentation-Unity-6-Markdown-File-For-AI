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

#  [Device](iOS.Device.html).generation

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

public static [iOS.DeviceGeneration](iOS.DeviceGeneration.html) generation;

### Description

The generation of the device. (Read Only)

For information on the possible values, see
[DeviceGeneration](iOS.DeviceGeneration.html).

    
    
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

