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

# GraphicsDevice

class in UnityEngine.NVIDIA

/

Implemented in:[UnityEngine.NVIDIAModule](UnityEngine.NVIDIAModule.html)

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

Provides the main entry point for the NVIDIA Module. Use this to interact with
specific NVIDIA graphics card features.

### Static Properties

[device](NVIDIA.GraphicsDevice-device.html)| Gets the device created by
GraphicsDevice.CreateGraphicsDevice. If the device hasn't been created this
property evaluates to null.  
---|---  
[version](NVIDIA.GraphicsDevice-version.html)| Gets the version that
corresponds to Unity's host plugin that manages the NVIDIA.NVUnityPlugin
official library.  
  
### Public Methods

[CreateDebugView](NVIDIA.GraphicsDevice.CreateDebugView.html)| Creates an
object containing debug information of the device.  
---|---  
[CreateFeature](NVIDIA.GraphicsDevice.CreateFeature.html)| Creates a specific
NVIDIA feature.  
[DeleteDebugView](NVIDIA.GraphicsDevice.DeleteDebugView.html)| Deletes a debug
view created with GraphicsDevice.CreateDebugView.  
[DestroyFeature](NVIDIA.GraphicsDevice.DestroyFeature.html)| Destroys a
specific feature created with GraphicsDevice.CreateFeature.  
[ExecuteDLSS](NVIDIA.GraphicsDevice.ExecuteDLSS.html)| Records the execution
of DLSS into a rendering command buffer. This call does not execute the
command buffer, it only appends custom commands into it.  
[GetOptimalSettings](NVIDIA.GraphicsDevice.GetOptimalSettings.html)| Returns a
structure containing the optimal settings for a specific target resolution and
quality.  
[IsFeatureAvailable](NVIDIA.GraphicsDevice.IsFeatureAvailable.html)| Checks if
the current NVIDIA graphics card supports the feature you specify using the
GraphicsDeviceFeature enum.  
[UpdateDebugView](NVIDIA.GraphicsDevice.UpdateDebugView.html)| Updates a
snapshpot of the debug information for the view object passed.  
  
### Static Methods

[CreateGraphicsDevice](NVIDIA.GraphicsDevice.CreateGraphicsDevice.html)|
Creates the main API object. Call this method only once in your application.  
---|---  
  
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

