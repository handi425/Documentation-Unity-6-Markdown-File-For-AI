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

**Method group is Obsolete**  

#  [XRSettings](XR.XRSettings.html).LoadDeviceByName

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

**Obsolete** XRSettings.LoadDeviceByName is deprecated and should no longer be
used. Instead, use the SubsystemManager to load XR devices by querying
subsystem descriptors to create and start the subsystems of your choice.

## Declaration

public static void LoadDeviceByName(string deviceName);

**Obsolete** XRSettings.LoadDeviceByName is deprecated and should no longer be
used. Instead, use the SubsystemManager to load XR devices by querying
subsystem descriptors to create and start the subsystems of your choice.

## Declaration

public static void LoadDeviceByName(string[] prioritizedDeviceNameList);

### Parameters

deviceName | Name of the device from [XRSettings.supportedDevices](XR.XRSettings-supportedDevices.html).  
---|---  
prioritizedDeviceNameList | Prioritized list of device names from [XRSettings.supportedDevices](XR.XRSettings-supportedDevices.html).  
  
### Description

Loads the requested device at the beginning of the next frame.

A list of supported devices which can be passed into this method can be
obtained from [XRSettings.supportedDevices](XR.XRSettings-
supportedDevices.html).  
  
In order to check for success, check
[XRSettings.loadedDeviceName](XR.XRSettings-loadedDeviceName.html) on the next
frame.  
  
This function will try to initialize only the device(s) passed in, it will not
fall back to other devices in the [XRSettings.supportedDevices](XR.XRSettings-
supportedDevices.html) list. You can pass a list of values to fall back to
other devices on failure. If no device could be initialized, it will fall back
to [XRSettings.loadedDeviceName](XR.XRSettings-loadedDeviceName.html) as an
empty string and set [XRSettings.enabled](XR.XRSettings-enabled.html) to
false.  
  
You can disable XR by loading an empty string deviceName.  
  
After loading a device, you may want to enable it with
[XRSettings.enabled](XR.XRSettings-enabled.html).  
  
**Note:** Some VR Devices do not support reloading when already active. You
should make sure to check the currently loaded device and only load the new
device if it is different.

    
    
    // Run in split-screen mode
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;
    using UnityEngine;
    using UnityEngine.XR;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(LoadDevice("Split"));
        }  
      
        IEnumerator LoadDevice(string newDevice)
        {
            if (String.Compare([XRSettings.loadedDeviceName](XR.XRSettings-loadedDeviceName.html), newDevice, true) != 0)
            {
                XRSettings.LoadDeviceByName(newDevice);
                yield return null;
                [XRSettings.enabled](XR.XRSettings-enabled.html) = true;
            }
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

