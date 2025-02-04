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

#  [SystemInfo](SystemInfo.html).operatingSystem

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

public static string operatingSystem;

### Description

Operating system name with version (Read Only).

Returns detailed information about the operating system of the device,
including the version. For a simple platform detection, properties like
[Application.platform](Application-platform.html) or [deviceType](SystemInfo-
deviceType.html) might be more appropriate.  
  
**Note:** On Microsoft Store Apps, it's not easy to identify if you're running
32-bit or 64-bit version of Windows. However, you can query the CPU
architecture to find this information. If the CPU is 64-bit,
[SystemInfo.operatingSystem](SystemInfo-operatingSystem.html) returns
**Windows <version> 64 bit**, and if the CPU is 32-bit - **Windows
<version>**.

    
    
    using UnityEngine;  
      
    public class ExampleClass: [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Prints "Windows 11 (10.0.22621) 64bit" on 64 bit Windows 11
            // Prints "Mac OS X 13.4" on Mac OS Ventura
            // Prints "iPhone OS" with [iOS](PlayerSettings.iOS.html) 15.3.1
            // Prints "iPad OS" on iPad with [iOS](PlayerSettings.iOS.html) 16
            // Prints "[Android](TouchScreenKeyboard.Android.html) OS 13 / API-33 (TQ2A.230305.008.C1/9619669)"
            [Debug.Log](Debug.Log.html)([SystemInfo.operatingSystem](SystemInfo-operatingSystem.html));
        }
    }
    

Additional resources: [Application.platform](Application-platform.html),
[deviceType](SystemInfo-deviceType.html).

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

