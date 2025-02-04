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

class in UnityEngine.XR.Provider

/

Implemented in:[UnityEngine.XRModule](UnityEngine.XRModule.html)

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

Provides timing and other statistics from XR subsystems.

The XRStats class allows XR SDK providers to expose timing and other
statistics related to their XR subsystems. Such statistics can be used by XR
application developers for profiling and making dynamic performance
adjustments. For example, an application could dynamically adjust properties
like [XRSettings.eyeTextureResolutionScale](XR.XRSettings-
eyeTextureResolutionScale.html) or
[XRSettings.renderViewportScale](XR.XRSettings-renderViewportScale.html) at
run time to improve performance based on statistics provided by an XR
subsystem.  
  
`Note:` XR SDK providers can use this class to provide their own, device-
specific class for reporting statistics. XR application developers should not
need to use the XRStats class directly.

### Static Methods

[TryGetStat](XR.Provider.XRStats.TryGetStat.html)| Retrieve a statistic for an
XR subsystem.  
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

