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

#  [GraphicsDevice](NVIDIA.GraphicsDevice.html).CreateGraphicsDevice

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

## Declaration

public static [NVIDIA.GraphicsDevice](NVIDIA.GraphicsDevice.html)
CreateGraphicsDevice();

## Declaration

public static [NVIDIA.GraphicsDevice](NVIDIA.GraphicsDevice.html)
CreateGraphicsDevice(string projectID);

## Declaration

public static [NVIDIA.GraphicsDevice](NVIDIA.GraphicsDevice.html)
CreateGraphicsDevice(string projectID, string appDir);

### Parameters

projectID | The projectID of the Unity project. Only the first call to this function uses this ID.  
---|---  
appDir | Specifies the directory in which the NVIDIA DLLS are located at. When not used, the system will locate the DLLs right next to the executable of the editor.  
  
### Returns

**GraphicsDevice** The Device API object to access NVIDIA features. If you
call this function again, the function returns the same device, regardless of
whether you pass in a different projectID.

### Description

Creates the main API object. Call this method only once in your application.

This function will instantiate the
[GraphicsDevice](NVIDIA.GraphicsDevice.html). It's safe to execute at any
point when the application is alive. Since the device is a direct
representation of the hardware graphics card, this method returns the same
device if you call it again. If you pass in an appDir or projectID, only the
first call to this method instantiates the device object using these
parameters.

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

