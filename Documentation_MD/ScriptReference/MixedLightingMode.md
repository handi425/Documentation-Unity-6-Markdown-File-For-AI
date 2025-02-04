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

# MixedLightingMode

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

Enum describing what lighting mode to be used with Mixed lights.

Summary of the baked data associated with each mode:  
  
**IndirectOnly**  
Lightmaps

  * direct: no
  * occlusion: no

Light probes

  * direct: no
  * occlusion: no

**Shadowmask**  
Lightmaps

  * direct: no
  * occlusion: yes

Light probes

  * direct: no
  * occlusion: yes

**Subtractive**  
Light maps

  * direct: yes
  * occlusion: no

Light probes

  * direct: no
  * occlusion: yes

### Properties

[IndirectOnly](MixedLightingMode.IndirectOnly.html)| Mixed lights provide
real-time direct lighting while indirect light is baked into lightmaps and
light probes.  
---|---  
[Shadowmask](MixedLightingMode.Shadowmask.html)| Mixed lights provide real-
time direct lighting. Indirect lighting gets baked into lightmaps and light
probes. Shadowmasks and light probe occlusion get generated for baked shadows.
The Shadowmask Mode used at run time can be set in the Quality Settings panel.  
[Subtractive](MixedLightingMode.Subtractive.html)| Mixed lights provide baked
direct and indirect lighting for static objects. Dynamic objects receive real-
time direct lighting and cast shadows on static objects using the main
directional light in the Scene.  
  
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

