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

#  [LightingSettings](LightingSettings.html).lightProbeSampleCountMultiplier

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

[Switch to Manual](../Manual/class-LightingSettings.html "Go to
LightingSettings Component in the Manual")

public float lightProbeSampleCountMultiplier;

### Description

Specifies the number of samples to use for Light Probes relative to the number
of samples for lightmap texels. (Editor only).

The default value is 4.  
  
This value is a multiplier of [directSampleCount](LightingSettings-
directSampleCount.html), [indirectSampleCount](LightingSettings-
indirectSampleCount.html) and [environmentSampleCount](LightingSettings-
environmentSampleCount.html). This multiplier is used to account for the fact
that Light Probes have to sample a larger area and therefore require more
samples than a lightmap texel. If you increase this value, the quality of your
Light Probes might improve, but baking takes more time. This can help in cases
where Light Probes appear inconsistent with other baked lighting in the Scene.  
  
When Unity serializes this `LightingSettings` object as a [Lighting Settings
Asset](../Manual/class-LightingSettings.html), this property corresponds to
the **Light Probe Sample Multiplier** property in the Lighting Settings Asset
Inspector.  
  
Additional resources: [Lighting Settings Asset](../Manual/class-
LightingSettings.html).

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

