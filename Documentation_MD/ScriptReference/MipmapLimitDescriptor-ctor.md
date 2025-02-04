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

# MipmapLimitDescriptor Constructor

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

public MipmapLimitDescriptor(bool useMipmapLimit, string groupName);

### Parameters

useMipmapLimit | Enable or disable mipmap limit effects for a Texture.  
---|---  
groupName | The [TextureMipmapLimitGroup](TextureMipmapLimitGroups.html) to use the mipmap limit of.  
  
### Description

Creates a new MipmapLimitDescriptor.

Use a `MipmapLimitDescriptor` to determine whether a texture uses a mipmap
limit when you create the texture using a constructor. If you create a texture
using a script, the texture doesn't use mipmap limits by default. The texture
uses the mipmap limit of `groupName` if you set `useMipmapLimit` to `true`. If
the group is not defined (either `null` or an empty string), the texture falls
back to following the global mipmap limit.  
  
The texture also uses the global mipmap limit if the group is not known by the
Editor.  
  
Additional resources::
[TextureMipmapLimitGroups](TextureMipmapLimitGroups.html).

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

