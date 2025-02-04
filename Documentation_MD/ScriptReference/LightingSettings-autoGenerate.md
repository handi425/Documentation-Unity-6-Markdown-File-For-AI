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

**Method group is Obsolete**  

#  [LightingSettings](LightingSettings.html).autoGenerate

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

**Obsolete** LightingSettings.autoGenerate is obsolete. public bool
autoGenerate;

### Description

Deprecated as Auto Generate lighting is no longer supported. Whether the Unity
Editor automatically precomputes lighting data when the Scene data changes.
(Editor only).

When this is set to `true`, the Editor automatically bakes lightmaps, Light
Probes and Reflection Probes when you make changes to your Scene. When this is
set to `false`, Unity does not automatically bake this data. The default value
is `false`.  
  
When this is set to `false`, you can instruct Unity to perform the bake by
pressing the **Generate Lighting** button in the [Lighting
window](../Manual/lighting-window.html), or by using the
[Lightmapping.Bake](Lightmapping.Bake.html) or
[Lightmapping.BakeAsync](Lightmapping.BakeAsync.html) APIs.  
  
This setting applies to the Baked Global Illumination system and the Enlighten
Realtime Global Illumination system.  
  
When Unity serializes this `LightingSettings` object as a [Lighting Settings
Asset](../Manual/class-LightingSettings.html), this property corresponds to
the **Auto Generate** property in the Lighting Settings Asset Inspector.  
  
Additional resources: [Lighting Settings Asset](../Manual/class-
LightingSettings.html), [Lighting window](../Manual/lighting-window.html),
[Lightmapping.Bake](Lightmapping.Bake.html),
[Lightmapping.BakeAsync](Lightmapping.BakeAsync.html).

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

