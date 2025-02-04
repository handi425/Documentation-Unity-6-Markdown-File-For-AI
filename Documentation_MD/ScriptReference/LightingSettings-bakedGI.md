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

#  [LightingSettings](LightingSettings.html).bakedGI

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

public bool bakedGI;

### Description

Whether to enable the Baked Global Illumination system for this Scene.

When this is set to `true`, this Scene uses the Baked Global Illumination
system. This means that you are able to generate baked lightmaps, Light Probes
and Reflection Probes for this Scene.  
  
When this is set to `false`, this Scene does not use the Baked Global
Illumination system. This means that you are unable to generate baked
lightmaps and Light Probes for this Scene. At runtime, Unity will not load
precomputed lighting data for this Scene, and Baked Lights and Mixed Lights
will behave as real-time Lights.  
  
When Unity serializes this `LightingSettings` object as a [Lighting Settings
Asset](../Manual/class-LightingSettings.html), this property corresponds to
the **Baked GI** property in the Lighting Settings Asset Inspector.  
  
Additional resources: [Lighting Settings Asset](../Manual/class-
LightingSettings.html), [realtimeGI](LightingSettings-realtimeGI.html).

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

