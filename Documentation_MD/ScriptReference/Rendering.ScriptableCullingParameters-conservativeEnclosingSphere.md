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

#
[ScriptableCullingParameters](Rendering.ScriptableCullingParameters.html).conservativeEnclosingSphere

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

public bool conservativeEnclosingSphere;

### Description

This property enables a conservative method for calculating the size and
position of the minimal enclosing sphere around the frustum cascade corner
points for shadow culling.

The default value is `false` (disabled) to give control over enabling this
method to the render pipeline for compatibility.  
  
The high level shadow mapping algorithms require a culling sphere for each
frustum cascade slice which contains the entire individual cascade volume.  
  
When this property is set to `false`, the shadow culling implementation uses
spheres that are smaller than the cascade volume and also misaligned, which
causes shadow casters to be culled in the corners of the cascades erroneously.  
  
When this property is set to `true`, the shadow culling implementation uses
spheres which contain the entire cascade within the culling sphere. The
methods uses a conservative and iterative solution, and the number of
iterations can be set using
[ScriptableCullingParameters.numIterationsEnclosingSphere](Rendering.ScriptableCullingParameters-
numIterationsEnclosingSphere.html).  
  
Setting this property to `true` may slightly increase the culling sphere size,
which will cause the shadow map to cover a larger world space and increase
perspective aliasing.  
  
Additional resources:
[ShadowSplitData.cullingSphere](Rendering.ShadowSplitData-cullingSphere.html).

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

