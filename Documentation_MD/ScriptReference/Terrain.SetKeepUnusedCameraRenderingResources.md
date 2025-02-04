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

#  [Terrain](Terrain.html).SetKeepUnusedCameraRenderingResources

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

public void SetKeepUnusedCameraRenderingResources(int cameraInstanceID, bool
keepUnused);

### Parameters

cameraInstanceID | The InstanceID of the camera for which freeUnusedRenderingResources is being set. See [Object.GetInstanceID](Object.GetInstanceID.html).  
---|---  
freeUnusedRenderingResources | The value to set to this camera's freeUnusedRenderingResources flag.  
  
### Description

Defines whether Unity cleans up rendering resources for a given Camera during
garbage collection.

Each Camera has its own `KeepUnusedRenderingResources` setting, which is
`false` by default. Unity uses this per-Camera setting in combination with the
Terrain's overall `KeepUnusedRenderingResources` setting. If either setting is
`true`, Unity preserves all rendering resources regardless of how long they've
remained unused.  
  
Additional resources:
[Terrain.GetKeepUnusedCameraRenderingResources](Terrain.GetKeepUnusedCameraRenderingResources.html),
[Terrain.keepUnusedRenderingResources](Terrain-
keepUnusedRenderingResources.html).

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

