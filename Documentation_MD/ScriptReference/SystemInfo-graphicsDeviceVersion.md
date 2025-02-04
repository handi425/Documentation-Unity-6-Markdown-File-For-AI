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

#  [SystemInfo](SystemInfo.html).graphicsDeviceVersion

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

public static string graphicsDeviceVersion;

### Description

The graphics API type and driver version used by the graphics device (Read
Only).

Returns a string identifying low-level graphics API kind and driver version.
In most cases when you need to detect which graphics API is being used it is
much easier to use [SystemInfo.graphicsDeviceType](SystemInfo-
graphicsDeviceType.html).  
  
In case of OpenGL API, the returned string will contain "`OpenGL`" followed by
version in "`major.minor`" format, followed by full version string in square
brackets.  
  
In case of Direct3D9 API, the returned string will contain "`Direct3D 9.0c`"
followed by driver name and version in square brackets.  
  
In case of Direct3D11 API, the returned string will contain "`Direct3D 11.0`"
followed by feature level in square brackets.  
  
Additional resources: [SystemInfo.graphicsDeviceType](SystemInfo-
graphicsDeviceType.html), [SystemInfo.graphicsDeviceName](SystemInfo-
graphicsDeviceName.html), [SystemInfo.graphicsDeviceVendor](SystemInfo-
graphicsDeviceVendor.html).

    
    
    using UnityEngine;
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Prints "OpenGL 2.0 [2.0 ATI-1.4.40]" on MacBook Pro running Mac OS X 10.4.8
            // Prints "Direct3D 9.0c [atiumdag.dll 7.14.10.471]" on MacBook Pro running Windows Vista
            print([SystemInfo.graphicsDeviceVersion](SystemInfo-graphicsDeviceVersion.html));
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

