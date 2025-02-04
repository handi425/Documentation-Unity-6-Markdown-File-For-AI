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

# InputExtraction

class in UnityEngine.LightTransport

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

Class used when extracting
[BakeInput](LightTransport.InputExtraction.BakeInput.html) from the set of
open scenes.

The [BakeInput](LightTransport.InputExtraction.BakeInput.html) class can be
used to populate the world space data structures used by integrators. Related
content: [IWorld](LightTransport.IWorld.html).

### Static Methods

[ComputeOcclusionLightIndicesFromBakeInput](LightTransport.InputExtraction.ComputeOcclusionLightIndicesFromBakeInput.html)|
For each probe position, computes the indices of the brightest lights from the
probe position's point of view. The function uses the information about lights
stored in an existing BakeInput. This function is intended to be used with
IProbeIntegrator.IntegrateOcclusion.  
---|---  
[ExtractFromScene](LightTransport.InputExtraction.ExtractFromScene.html)|
Extract BakeInput from the set of open scenes.  
[GetShadowmaskChannelsFromLightIndices](LightTransport.InputExtraction.GetShadowmaskChannelsFromLightIndices.html)|
Get's the associated baked shadowmask channels of the mixed lights with the
specified indices. Use this together with
InputExtraction.ComputeOcclusionLightIndicesFromBakeInput.  
[PopulateWorld](LightTransport.InputExtraction.PopulateWorld.html)| Populate
the given world from a bake input.  
  
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

