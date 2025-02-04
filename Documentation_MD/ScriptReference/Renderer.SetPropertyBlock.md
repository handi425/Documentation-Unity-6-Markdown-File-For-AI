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

#  [Renderer](Renderer.html).SetPropertyBlock

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

public void
SetPropertyBlock([MaterialPropertyBlock](MaterialPropertyBlock.html)
properties);

## Declaration

public void
SetPropertyBlock([MaterialPropertyBlock](MaterialPropertyBlock.html)
properties, int materialIndex);

### Parameters

properties | Property block with values you want to override.  
---|---  
materialIndex | The index of the Material you want to override the parameters of. The index ranges from 0 to Renderer.sharedMaterials.Length-1.  
  
### Description

Lets you set or clear per-renderer or per-material parameter overrides.

This is recommended when only a few properties of a Material are different per
object. This is more memory efficient than having one complete distinct
Material per object.  
  
You can also provide a Material index (from 0 to Renderer.materials.Length-1).
In this case, only parameters of that Material are set. If there is both a
per-renderer and a per-material block, only the per-Material block is used.  
  
To disable any of per-Renderer or per-Material overrides, pass null as the
property’s argument.  
  
Additional resources: [MaterialPropertyBlock](MaterialPropertyBlock.html),
[GetPropertyBlock](Renderer.GetPropertyBlock.html).

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

