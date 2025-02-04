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

# XRStats

class in UnityEngine.XR

/

Implemented in:[UnityEngine.VRModule](UnityEngine.VRModule.html)

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

Timing and other statistics from the XR subsystem.

Some XR SDKs provide access to additional timing and other statistics. These
can be used by games and applications for profiling and dynamic performance
adjustments. For example, modifying
[XRSettings.eyeTextureResolutionScale](XR.XRSettings-
eyeTextureResolutionScale.html) or
[XRSettings.renderViewportScale](XR.XRSettings-renderViewportScale.html)
during runtime can improve performance. This class exposes a set of
information that can be optionally reported by SDKs. Make sure to use the
return values of any methods to know whether the data is being reported by the
SDK or not.

### Static Methods

[TryGetDroppedFrameCount](XR.XRStats.TryGetDroppedFrameCount.html)| Retrieves
the number of dropped frames reported by the XR SDK.  
---|---  
[TryGetFramePresentCount](XR.XRStats.TryGetFramePresentCount.html)| Retrieves
the number of times the current frame has been drawn to the device as reported
by the XR SDK.  
[TryGetGPUTimeLastFrame](XR.XRStats.TryGetGPUTimeLastFrame.html)| Retrieves
the time spent by the GPU last frame, in seconds, as reported by the XR SDK.  
  
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

