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

# ReceiveGI

enumeration

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

This property only takes effect if you enable a global illumination setting
such as [Baked Global Illumination](../Manual/class-
LightingSettings.html#MixedLighting.html) or [Enlighten Realtime Global
Illumination](../Manual/class-LightingSettings.html#RealtimeLighting.html) for
the target Scene. When you enable ReceiveGI, you can determine whether
illumination data at runtime will come from [Light
Probes](../Manual/LightProbes.html) or Lightmaps. When you set ReceiveGI to
Lightmaps, the Mesh Renderer receives global illumination from lightmaps. That
means the Renderer is included in lightmap atlases, possibly increasing their
size, memory consumption and storage costs. Calculating global illumination
values for texels in this Renderer also adds to bake times. When you set
ReceiveGI to Light Probes, the Mesh Renderer is not assigned space in lightmap
atlases. Instead it receives global illumination stored by Light Probes in the
target Scene. This can reduce bake times by avoiding the memory consumption
and storage cost associated with lightmaps. ReceiveGI is only editable if you
enable [StaticEditorFlags.ContributeGI](StaticEditorFlags.ContributeGI.html)
for the GameObject associated with the target Mesh Renderer. Otherwise this
property defaults to the Light Probes setting.

### Properties

[Lightmaps](ReceiveGI.Lightmaps.html)| Makes the GameObject use lightmaps to
receive Global Illumination.  
---|---  
[LightProbes](ReceiveGI.LightProbes.html)| The object will have the option to
use Light Probes to receive Global Illumination. See LightProbeUsage.  
  
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

